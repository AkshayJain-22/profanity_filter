import pandas as pd


def file_entry(record):
    record_df = pd.DataFrame([record])
    
    with open('records.csv','a') as file:
        record_df.to_csv(file, header=False, index=False)