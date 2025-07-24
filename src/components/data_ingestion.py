# ================================
# 📥 Data Ingestion Script
# ================================

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# import custom exception handling and logging
from src.exception import CustomException
from src.logger import logging

# import the transformer
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# 🛠️ Configuration Class for Data Ingestion

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts',"train.csv")  # Path where the training data will be saved
    test_data_path:str = os.path.join('artifacts',"test.csv")  # Path where the test data will be saved
    raw_data_path:str = os.path.join('artifacts',"data.csv")  # Path where the raw data will be saved

# 📦 Data Ingestion Component

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Load the config containing all required paths

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            # ✅ Step 1: Load the dataset
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as DataFrame')

            # ✅ Step 2: Create the artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # ✅ Step 3: Save raw data for backup or reference
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)

            # ✅ Step 4: Perform train-test-split
            logging.info("train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # ✅ Step 5: Save the split datasets to disk
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of the data is completed")

            # ✅ Step 6: Return Paths for train and test data

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # ⚠️ Handle and raise custom exception for better debugging
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    # Instantiate the DataIngestion class
    obj = DataIngestion()

    # call the ingestion method
    train_data, test_data = obj.initiate_data_ingestion()

    # perform the transformers
    data_transformation = DataTransformation()
    train_arr, test_arr,preprocessor_path  = data_transformation.initiate_data_transformation(train_data, test_data)


    # print the output file paths 

    print(f"✅ Data ingestion completed.\nTrain data saved to: {train_data}\nTest data saved to: {test_data}")
