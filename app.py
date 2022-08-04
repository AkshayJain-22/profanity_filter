from flask import Flask, request, render_template, Response
from flask_cors import CORS, cross_origin
from ml_models import abuse_detector
from perfect_match_models import profanity_filter
from unique_letters import unique_letters_profanity
from file_operations import file_entry
from accuracy_finder import accuracy_record
import os

comment=''
prediction_output=''
updated_comment=''

app=Flask(__name__)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

@app.route("/",methods=['GET','POST'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/begin',methods=['GET','POST'])
def begin():
    global comment
    global prediction_output
    global updated_comment

    if request.method == 'POST':
        raw_comment = request.form['content'] # obtaining the comment entered in the form
    elif request.method == 'GET':
        raw_comment = request.args.getlist('content')

    comment=raw_comment[0]
    if len(comment) == 0:
        return render_template('index.html')
    
    prediction = abuse_detector(comment)         #calling our detector function (ML model)
    filtered_comment = profanity_filter(comment) #profanity filter model returns *ed comment

    if prediction==0:                            #if Ml model says not abusive in the first attempt
        if ('**') in filtered_comment:           #check the prediction of profanity filter
            prediction_output='Abusive' 
            updated_comment = filtered_comment
        else:                                    #both said not abusive so go for second step verification
            second_prediction, filtered_comment = unique_letters_profanity(comment) #prediction returned by unique letters method
            if second_prediction==0:             #if ML model again says not abusive
                filtered_comment = profanity_filter(comment)
                if ('*') in filtered_comment:    #if profanity filter says abusive
                    prediction_output='Abusive'
                    updated_comment= filtered_comment
                else:                            #if both models says not abusive
                    prediction_output='Not Abusive'
                    updated_comment=comment
            else:                                #if ML model says abusive on the second attempt
                prediction_output='Abusive' 
                updated_comment=filtered_comment
    else:                                        #if ML model says abusive in the first attempt
        prediction_output='Abusive'
        updated_comment=filtered_comment

    result={'prediction_output':prediction_output,'updated_comment':updated_comment}
    return render_template('index.html', result=result) # showing the result to the user


@app.route("/user_review")
def store_data():
    if request.method == 'GET':
        review = request.args.getlist('drone')[0]

    print(review)
    if(review=='Y'):
        score = 1
    else:
       score = 0

    record = {'comment':comment, 'updated_comment':updated_comment,'prediction_output':prediction_output,'score':score}
    
    file_entry(record)
    accuracy = {'accuracy':accuracy_record()}

    return render_template('index.html', accuracy=accuracy) # showing the result to the user)


if __name__=="__main__":
    app.run(debug=True)