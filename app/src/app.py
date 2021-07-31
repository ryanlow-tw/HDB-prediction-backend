from flask import Flask
from model import PredModel

app = Flask(__name__)
model = PredModel("model.pkl")
model.load_model()


@app.route('/')
def index():
    return "Index Page"


@app.route('/prediction')
def prediction():
    result = ''

    default_prediction = PredModel.get_default_prediction()

    for pred in default_prediction:
        result += str(pred) + ' '
    return result
