from cmath import log
import pickle
from text_operations import clean_text
from logging_tools import logger
from flask import Flask

def abuse_detector(comment)->int:   
    with open("models/vectorization_model_banned_wrds.sav",'rb') as file:
        vector = pickle.load(file)  #load the vectorization model we saved earlier
    with open("models/abuse_classifier_banned_wrds.sav",'rb') as file:
        model = pickle.load(file)  #load the classification model we saved earlier
    
    abuse_detector_logger = logger() #create a logging object
    filtered_comment = [clean_text(comment)] #cleaning the comment and removing stop words
    
    abuse_detector_logger.log_info(f'filtered_comment: {filtered_comment}')

    vectorized_comment = vector.transform(filtered_comment) 
    prediction = model.predict(vectorized_comment)
    
    return prediction