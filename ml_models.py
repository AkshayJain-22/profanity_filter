from cmath import log
import pickle
from text_operations import clean_text
from logging_tools import logger

def abuse_detector(comment)->int:
    abuse_detector_logger = logger(__name__) #create a logging object
    try:   
        with open("models/vectorization_model_ngram2.sav",'rb') as file:
            vector = pickle.load(file)  #load the vectorization model we saved earlier
        with open("models/abuse_classifier_ngram2.sav",'rb') as file:
            model = pickle.load(file)  #load the classification model we saved earlier
    except Exception as e:
        abuse_detector_logger.log_error(f"Could not load the model: {e}")
        prediction = 0
    else:
        filtered_comment = [clean_text(comment)] #cleaning the comment and removing stop words
        vectorized_comment = vector.transform(filtered_comment) 
        prediction = model.predict(vectorized_comment)
        abuse_detector_logger.log_info(f'Returning Prediction without error.')
    
    return prediction