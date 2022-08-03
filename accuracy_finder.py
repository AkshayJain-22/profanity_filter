import pandas as pd

def accuracy_record():
    records = pd.read_csv(filepath_or_buffer='records.csv',names=['comment','updated_comment','prediction_output','score'])

    accuracy =(len(records['score'][records['score']==1])/len(records))*100
    accuracy = ("%.2f" % accuracy)
    return(accuracy)