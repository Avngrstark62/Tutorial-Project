import os
import sys
from src.TutorialProject.logger import logging
from src.TutorialProject.exception import CustomException
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')

def read_sql_data():
    logging.info('Reading SQL Database Started')
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info('connection established', mydb)
        df = pd.read_sql_query('SELECT * FROM Students', mydb)
        return df
    except Exception as e:
        raise CustomException(e, sys)