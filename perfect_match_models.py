

def profanity_filter(comment):
    banned_words=[]
    with open("files/Words_to_be_Deleted_sk.csv") as file: #read from file with profane words
        banned_words=file.readlines()
    for word in banned_words:
        word = word.replace("\n","")
        if word in comment.split():                  #check each word inside comment
            comment = comment.replace(word,f"{word[0]}{'*'*(len(word)-1)}") #if match found replace the comment with **
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