import pandas as pd
from db_operations import read_data
def accuracy_record():
    records = read_data(table_name='records')
    accuracy =(len(records['score'][records['score']==1])/len(records))*100
    accuracy = ("%.2f" % accuracy)
    return(accuracy)