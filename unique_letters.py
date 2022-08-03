from auto_correct import autocorrect
from perfect_match_models import profanity_filter_inner
from ml_models import abuse_detector

import nltk
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
stopword=set(stopwords.words('english'))

def unique_letters_profanity(comment): 
    comment = str(comment).lower()
    new_word=[]
    for word in [word for word in comment.split(' ') if word not in stopword]: #iterating through each word in original comment
        l=[]
        for letter in word:
            l.append(letter)
            if (len(word)<=3):                     #3-letter words are straightforward (un-fiddled)
                unique_letters = l
            else:
                unique_letters = dict.fromkeys(l).keys() #creating words from unique letters
        new_word.append("".join(unique_letters))
    
    trimmed_sentence = " ".join(new_word)
    
    new_comment = autocorrect(trimmed_sentence)
    
    prediction = abuse_detector(new_comment)       #calling our detector function for new comment using unique words

    original_words = comment.split()               #what were the words in the actual comment
    profane_return = profanity_filter_inner(new_comment).split() # get the starred comment using unique letter words
    
    for word in range(len(profane_return)):        #iterating through starred comment using unique words
        if "*" not in profane_return[word]:
            profane_return[word] = original_words[word] #replace the allowed words with original words
    
    if prediction==0:                              #if ML model says not abusive
        if ('*') in profanity_filter_inner(new_comment): #if profanity filter caught some curse words
            return(1," ".join(profane_return))
        else:                                      #both said not abusive
            return(0," ".join(profane_return)) 
    else:                                          #if ML model says its abusive
        return(1," ".join(profane_return))    