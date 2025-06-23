from utils.logger import Logger
from datetime import datetime

import threading
import time

instances = []


def some_function(number):
    time.sleep(3)
    app_logger = Logger()
    instances.append(app_logger)
    app_logger.logger.info("Thread #%d finished at %s",number,str(datetime.now()))

threads = [threading.Thread(target=some_function, args=[i]) for i in range(10)]

for t in threads:
    t.start()


for t in threads:
    t.join()

unique_loggers = set(instances)
print(f'Finished with {len(unique_loggers)} loggers')