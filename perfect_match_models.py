import re

def profanity_filter(comment):
    banned_words=[]
    with open("files/Words_to_be_Deleted_sk.csv") as file: #read from file with profane words
        banned_words=file.readlines()
    lower_comment = str(comment).lower()
    original_words=comment.split()

    for word in banned_words:
        word = word.replace("\n","")
        if word in lower_comment.split():             #check each word inside comment
            lower_comment = lower_comment.replace(word,f"{word[0]}{'*'*(len(word)-1)}") #if match found replace the comment with **
    lower_words = lower_comment.split()
    for word in range(len(lower_words)):             #iterating through starred comment using unique words
        if "*" not in lower_words[word]:
            lower_words[word] = original_words[word]
        else:
            lower_words[word]= f"{original_words[word][0]}{'*'*(len(lower_words[word])-1)}"
    comment = " ".join(lower_words)
    return(comment)                                  #return the filtered comment

def profanity_filter_inner(comment):
    banned_words=[]
    with open("files/Words_to_be_Deleted_sk.csv") as file: #read from file with profane words
        banned_words=file.readlines()
    for word in banned_words:
        word = word.replace("\n","")
        for i in range(len(comment)):
            if word == comment[i:i+len(word)]:                  #check each word inside comment
                comment = comment.replace(word,f"{word[0]}{'*'*(len(word)-1)}") #if match found replace the comment with **
    return(comment)