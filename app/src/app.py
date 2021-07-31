from flask import Flask, request
from model import PredModel


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

model = PredModel("model.pkl")
model.load_model()

random_forest_model = model.model


@app.route('/')
def index():
    return "Index Page"


@app.route('/default-prediction')
def prediction():
    default_prediction = model.get_default_prediction()
    return f"$ {default_prediction:.2f}"


@app.route('/make-prediction')
def make_prediction():

    valid_args = {
        "storey-range": "",
        "floor-area-sqm": "",
        "remaining-lease": "",
        "town": ""
    }

    query_strings = request.args.to_dict()

    for key, value in query_strings.items():

        if key in valid_args:
            valid_args[key] = value

    return valid_args
