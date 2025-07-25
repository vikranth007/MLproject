from fastapi import FastAPI, Request, Form,requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import os


import uvicorn

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = FastAPI()

app = application

templates = Jinja2Templates(directory="templates")



@app.get("/",response_class=HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/predictdata",response_class=HTMLResponse)
async def form_get(request : Request):
    return templates.TemplateResponse("home.html",{"request": request})

@app.post("/predictdata",name="predict_datapoint")
async def predict_data(
    request : Request,
    gender : str = Form(...),
    race_ethnicity : str = Form(...),
    parental_level_education : str = Form(...),
    lunch : str = Form(...),
    test_preparation_course : str = Form(...),
    reading_score : float = Form(...),
    writing_score : float = Form(...)
):
    
    try:
        data = CustomData(
            gender = gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        Predict_Pipeline = PredictPipeline()
        results = Predict_Pipeline.predict(pred_df)

        return templates.TemplateResponse("home.html", {
            "request": request,
            "results": results[0]
})
    
    except Exception as e:
        return templates.TemplateResponse("home.html",{
            "request" : request,
            "results" : f"Error occurred : {str(e)}" 
        })
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 locally
    uvicorn.run(app, host="0.0.0.0", port=port)



