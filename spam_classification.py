import pickle
from text_operations import clean_text_scam
from logging_tools import logger

def check_spam(comment)->int:
    spam_logger = logger(__name__)
    try:
        with open("models/vectorization_model_spam_ngram2.sav",'rb') as file:
            vector = pickle.load(file)  #load the vectorization model we saved earlier
        with open("models/spam_classifier.sav",'rb') as file:
            model = pickle.load(file)  #load the vectorization model we saved earlier
    except Exception as e:
        logger.log_error('Could not load models: {e}')
        prediction=0
    else:    
        filtered_comment = [clean_text_scam(comment)] #cleaning the comment and removing stop words
        
        vectorized_comment = vector.transform(filtered_comment) 
        prediction = model.predict(vectorized_comment)
    
    if(prediction==1):
        prediction=2
        
    return prediction