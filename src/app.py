import sys
sys.path.append(".")

from flask import Flask, request
from model import PredModel
from make_json import MakeJson



app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

random_forest = PredModel("model.pkl")


@app.route('/')
def index():
    return "Index Page"


@app.route('/default-prediction')
def prediction():
    default_prediction = random_forest.get_default_prediction()
    return f"$ {default_prediction:.2f}"


@app.route('/make-prediction')
def make_prediction():

    query_strings = request.args.to_dict()

    prediction_params = PredModel.get_prediction_params(query_strings)

    result = random_forest.make_prediction(prediction_params)

    display_results = MakeJson.format_results(result)

    return display_results
