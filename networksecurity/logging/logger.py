import logging
import os
from datetime import datetime


log_file =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_PATH = os.path.join(os.getcwd(),"logs", log_file)

os.makedirs(LOG_PATH,exist_ok=True)

log_file_path = os.path.join(LOG_PATH, log_file)

logging.basicConfig(
    filename=log_file_path,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


