from model import PredModel
from unittest import TestCase, skip


class TestModel(TestCase):

    def setUp(self):
        self.pred_model = PredModel('model.pkl')
        self.pred_model.load_model()

    def test_model_should_be_random_forest_regressor(self):
        result = str(type(self.pred_model.model))
        expected = "<class 'sklearn.ensemble._forest.RandomForestRegressor'>"

        self.assertEqual(result, expected)

    def test_for_correct_default_prediction(self):
        result = PredModel.get_default_prediction()
        expected = [1, 98.313419, 75.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(result, expected)
