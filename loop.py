from datetime import datetime
import time
import logging

while True:
    now = datetime.now()
    print(f'Looping: {now}')
    logging.error('err')
    logging.critical('crit')
    logging.debug('debug')
    logging.info('info') 
    logging.warning('warn')
    time.sleep(10)