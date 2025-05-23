import os
import sys
import dill

import pandas as pd
import numpy as np  

from src.logger import logging
from src.exception import CustomException



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            logging.info("Object saved successfully")
    except Exception as e:
        logging.error("Error occurred while saving object")
        raise CustomException(e, sys)
