import nltk
stemmer = nltk.SnowballStemmer("english")
#from nltk.corpus import stopwords
import string
#stopword=set(stopwords.words('english'))
stopword=["i", "br", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
import re 

def clean_text(text)->str: # this function will clean the text and return it.
    text = str(text).lower()
    text = re.sub('-'," ",text)
    text = re.sub('[%s]' % re.escape('@'),"a",text)
    text = re.sub('[%s]' % re.escape('$'),'s',text)
    text = re.sub('[%s]' % re.escape('&'),'s',text)
    text = re.sub('0','o',text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape('!"#$%&\'()+,-./:;<=>?@[\\]^_`{|}~'), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text

def clean_text_scam(text)->str: # this function will clean the text and return it.
    text = str(text).lower()
    text = re.sub('&amp;','',text)
    text = re.sub('&amp;rsquo;',"'",text)
    text = re.sub('ï»¿','',text)
    text = re.sub('â','',text)
    text = re.sub('ð','',text)
    text = re.sub('Ÿ','',text)
    text = re.sub('&quot;','"',text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape('!"#$%&\'()+,-./:;<=>?@[\\]^_`{|}~'), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text