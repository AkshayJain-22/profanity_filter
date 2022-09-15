import pandas as pd

def autocorrect(trimmed_sentence):
    trimmed_dictionary = pd.read_csv('files/banned_words_final.csv',encoding='unicode_escape')
    
    for index in range(len(trimmed_dictionary['trimmed'])):
        word = trimmed_dictionary['trimmed'][index]
        for trimmed_word in trimmed_sentence.split():
            if word == trimmed_word:
                correct_word = trimmed_dictionary['tweet'][index]
                trimmed_sentence=trimmed_sentence.replace(word,correct_word)
                
    return(trimmed_sentence)