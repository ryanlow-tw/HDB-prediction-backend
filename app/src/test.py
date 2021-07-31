from model import PredModel
from make_json import MakeJson
from unittest import TestCase, skip


class TestModel(TestCase):

    def setUp(self):
        self.pred_model = PredModel('model.pkl')
        self.pred_model.load_model()

    def test_model_should_be_random_forest_regressor(self):
        result = str(type(self.pred_model.model))
        expected = "<class 'sklearn.ensemble._forest.RandomForestRegressor'>"

        self.assertEqual(result, expected)

    def test_for_correct_default_parameters(self):
        result = PredModel.get_default_parameters()
        expected = [1, 98.313419, 75.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(result, expected)

    def test_that_model_returns_default_prediction(self):
        result = round(self.pred_model.get_default_prediction(), 2)
        expected = 455699.59

        self.assertEqual(result, expected)

    def test_that_formatter_returns_correct_format(self):
        result_to_be_formatted = 24.0
        expected = {
            "results": "24.00"
        }
        result = MakeJson.format_results(result_to_be_formatted)

        self.assertEqual(result, expected)

    def test_that_town_col_number_is_returned_correctly(self):
        result = PredModel._get_town_col_number("BISHAN")
        expected = 5

        self.assertEqual(result, expected)

    def test_that_error_is_raised_if_wrong_town_is_called(self):
        town = "WHEEEEEe"
        with self.assertRaises(ValueError) as error:
            PredModel._get_town_col_number(town)

        exception = error.exception
        self.assertEqual(f"{exception}", f"{town} is not a valid town name!")


