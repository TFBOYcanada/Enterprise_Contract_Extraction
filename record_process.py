import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename='RecordP.log',filemode='a')
# debug info warning error critical
logging.debug('this is debug message demo ')
logging.info('this is info message demo')
logging.warning('this is warning message demo')

import EnterprisePdfreader as EPR
import pandas as pd
import os
import numpy as np
import  CarDecoding as CD
filePath = '/Users/gaominhao/Documents/Enterprise'
Rental_data_all=[]
os.listdir(filePath)
for i in os.listdir(filePath):
    if 'pdf'  in i:   # no other files
        path='/Users/gaominhao/Documents/Enterprise/'+i
        logging.info('parsing %s',i)
        with open(path, "rb") as my_pdf:
            Rental_data = EPR.pdf_parse(path)
            if len(Rental_data)!=12:
                logging.error('errors happen in file  %s', i)
            else:
                Rental_data_all.append(Rental_data) ### collect all records


for i in Rental_data_all:
    logging.info('start reading pdf text record')
    logging.info('Records: %s', i)



colname = ['Start', 'End', 'Class', 'Drive', 'Charge', 'Make', 'Total', 'Day', 'Model', 'Plate', 'Location',
                'Agreement']

df = pd.DataFrame(Rental_data_all, columns=colname)

df['Model'] = df['Model'].map(lambda x: x.strip('License'))  #  whole column
logging.debug('Records: %s', df['Model'])

df['Plate'] = df['Plate'].map(lambda x: x.strip('RENTER'))
logging.debug('Records: %s', df['Plate'])

df['Class'] = df['Class'].map(lambda x: x.strip('Class'))
logging.debug('Records: %s',df['Class'])

df['Charge'] = df['Charge'].map(lambda x: x.strip('Make'))
logging.debug('Records: %s', df['Charge'])

df['Total'] = df['Total'].map(lambda x: x.strip('Name'))
logging.debug('Records: %s', df['Total'])

df=df[['Agreement','Make','Model','Class','Charge','Day','Total','Plate','Drive','Start','End','Location']]




df['Class']=df['Class'].map(lambda x: CD.decode(x))


df.to_csv('rentaldata.csv')

logging.debug('Records: %s', df['Class'])