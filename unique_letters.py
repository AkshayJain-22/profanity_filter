from auto_correct import autocorrect
from perfect_match_models import profanity_filter_inner
from ml_models import abuse_detector

import nltk
stemmer = nltk.SnowballStemmer("english")
#from nltk.corpus import stopwords
#stopword=set(stopwords.words('english'))
stopword=["i", "br", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    

def unique_letters_profanity(comment): 
    comment = str(comment).lower()
    new_word=[]
    for word in [word for word in comment.split(' ') if word not in stopword]: #iterating through each word in original comment
        print('words:',word)
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