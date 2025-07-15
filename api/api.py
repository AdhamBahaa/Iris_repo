import pickle
import flask
from flask import request
from sklearn.linear_model import LogisticRegression

app = flask.Flask(__name__)

# Load our trained model from a file we created earlier 
with open("iris_model.pkl", 'rb') as file:  
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # grabbing a set of wine features from the request's body
    feature_array = request.get_json()['feature_array']

    # our model rates the wine based on the input array
    prediction = model.predict([feature_array]).tolist()
    
    # preparing a response object and storing the model's predictions
    response = {}
    response['prediction'] = prediction
    
    # sending our response object back as json
    return flask.jsonify(response)

@app.route('/is_run', methods=['GET'])
def is_run():
    return flask.jsonify({"status": "API is running"})

@app.route('/model_info', methods=['GET'])
def model_info():
    params = model.get_params()
    return flask.jsonify({"model_params": params})


# script initialization
if __name__ == '__main__':
    app.run(debug=True, port ='5000',host='0.0.0.0')
