import pickle
from text_operations import clean_text
import logging
from flask import Flask

def abuse_detector(comment)->int:   
    with open("models/vectorization_model_banned_wrds.sav",'rb') as file:
        vector = pickle.load(file)  #load the vectorization model we saved earlier
    with open("models/abuse_classifier_banned_wrds.sav",'rb') as file:
        model = pickle.load(file)  #load the classification model we saved earlier
    #with open("clean_text_func.sav",'rb') as file:
        #clean_text = pickle.load(file)  #load the text cleaning fucntion
    module = Flask(__name__)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    module.logger.handlers = gunicorn_logger.handlers
    module.logger.setLevel(gunicorn_logger.level)
    filtered_comment = [clean_text(comment)] #cleaning the comment and removing stop words
    
    module.logger.info(f'filtered_comment: {filtered_comment}')

    vectorized_comment = vector.transform(filtered_comment) 
    prediction = model.predict(vectorized_comment)
    
    return prediction