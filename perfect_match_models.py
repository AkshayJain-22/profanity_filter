from logging_tools import logger

def profanity_filter(comment):
    profanity_filter_logger = logger(name='profanity_filter')
    banned_words=[]
    try:
        with open("files/Words_to_be_Deleted_sk.csv") as file: #read from file with profane words
            banned_words=file.readlines()
    except Exception as e:
        profanity_filter_logger.log_error(f'Could not open file: {e}')
    else:
        lower_comment = str(comment).lower()
        original_words=comment.split()
        for word in banned_words:
            word = word.replace("\n","")
            if word in lower_comment.split():             #check each word inside comment
                print('1: ',word)
                try:
                    lower_comment = lower_comment.replace(word,f"{word[0]}{'*'*(len(word)-1)}") #if match found replace the comment with **
                    print('2: ',word)
                except Exception as e:
                    profanity_filter_logger.log_error(f'Error in word {word}: {e}')
        lower_words = lower_comment.split()

        for word in range(len(lower_words)):             #iterating through starred comment to replace with original letters where required
            try:
                if "*" not in lower_words[word]:
                    lower_words[word] = original_words[word]
                else:
                    lower_words[word]= f"{original_words[word][0]}{'*'*(len(lower_words[word])-1)}"
            except Exception as e:
                profanity_filter_logger.log_error(f"Error in '{lower_words[word]}': {e}")
        comment = " ".join(lower_words)
    return(comment)                                  #return the filtered comment

def profanity_filter_inner(comment):
    lower_comment = str(comment).lower()
    original_words=comment.split()
    banned_words=[]
    profanity_filter_inner_logger = logger(name='profanity_filter_inner')
    try:
        with open("files/Words_to_be_Deleted_sk.csv") as file: #read from file with profane words
            banned_words=file.readlines()
    except Exception as e:
        profanity_filter_inner_logger.log_error(f'Could not load the file: {e}')
    else:
        for word in banned_words:
            word = word.replace("\n","")
            for i in range(len(lower_comment)):
                try:
                    if word == lower_comment[i:i+len(word)]:                  #check each word inside comment
                        print(word)
                        lower_comment = lower_comment.replace(word,f"{word[0]}{'*'*(len(word)-1)}") #if match found replace the comment with *
                except Exception as e:
                    profanity_filter_inner_logger.log_error('Error in word {word}')
        lower_words = lower_comment.split()

        for word in range(len(lower_words)):             #iterating through starred comment to replace with original letters where required
            try:
                if "*" not in lower_words[word]:
                    lower_words[word] = original_words[word]
                else:
                    lower_words[word]= f"{original_words[word][0]}{'*'*(len(lower_words[word])-1)}"
            except Exception as e:
                profanity_filter_inner_logger.log_error(f"Error in '{lower_words[word]}': {e}")
        comment = " ".join(lower_words)
    return(comment)