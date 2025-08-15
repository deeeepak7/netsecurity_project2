from networksecurity.exception.exception import customException
import os
import sys
from networksecurity.constant.training_pipeline import saved_model_dir,model_file_name
from networksecurity.logging.logger import logging


class networkmodel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise customException(e,sys)

    def predict(self,x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise customException(e.sys)
