from flask import Flask, request, jsonify
from flask.logging import create_logger
import pandas as pd
import logging
import joblib

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

#root of the flask server
@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Root</h3>"
    return html.format(format)

#prediction happens.
@app.route("/predict", methods=['POST'])
def predict():
    """
        Document:
            Performs an sklearn prediction

            input looks like:
            {
                "filename":"test.csv"
            }
            result looks like:
            { "prediction": [ 1 ] }
    """

    # load pre trained model(.joblib) file
    try:
        print("try to load joblib")
        clf = joblib.load("binary_clf.joblib")
    except:
        LOG.info("Model not loaded")
        return "Model not loaded"

    #get file name from user request
    filename = request.json["filename"]
    LOG.info("JSON payload: filename %s" % filename)

    #read test csv data and classify input data
    test_df = pd.read_csv(filename)
    X_test = test_df.drop("label", axis=1)

    prediction = clf.predict(X_test)

    #the way http, json works is that python data types cannot be embeded to json
    #need to conver each prediction result from "int","double","long" data types into string before sending
    strResult = "["    
    for x in prediction:
        strResult = strResult + str(x) + ","
    strResult = strResult[:-1]
    strResult += "]"
    
    # make result as json and return to client
    return jsonify({'prediction': strResult})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
