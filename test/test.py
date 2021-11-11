from src.model import PredModel
from src.make_json import MakeJson
from unittest import TestCase


class TestModel(TestCase):

    def setUp(self):
        self.pred_model = PredModel('model.pkl')

    def test_model_should_be_random_forest_regressor(self):
        result = str(type(self.pred_model.model))
        expected = "<class 'sklearn.ensemble._forest.RandomForestRegressor'>"

        self.assertEqual(result, expected)

    def test_for_correct_default_parameters(self):
        result = PredModel.get_default_parameters()
        expected = [1, 98.313419, 75.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(result, expected)

    def test_that_model_returns_default_prediction(self):
        result = round(self.pred_model.get_default_prediction(), 2) >= 400000
        expected = True
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

    def test_that_storey_range_is_correct_for_1_to_6_floors(self):

        prediction_params = {
            "storey-range": "1",
            "floor-area-sqm": "75",
            "remaining-lease": "64",
            "town": "PUNGGOL"
        }

        valid_args = PredModel.process_query_strings(prediction_params)

        result = PredModel.get_floor_mapping(valid_args)
        expected = 0

        self.assertEqual(result, expected)

    def test_that_storey_range_is_correct_for_7_floors(self):

        prediction_params = {
            "storey-range": "7",
            "floor-area-sqm": "75",
            "remaining-lease": "64",
            "town": "PUNGGOL"
        }

        valid_args = PredModel.process_query_strings(prediction_params)

        result = PredModel.get_floor_mapping(valid_args)
        expected = 1

        self.assertEqual(result, expected)

    def test_that_storey_range_is_correct_for_12_floors(self):

        prediction_params = {
            "storey-range": "12",
            "floor-area-sqm": "75",
            "remaining-lease": "64",
            "town": "PUNGGOL"
        }

        valid_args = PredModel.process_query_strings(prediction_params)

        result = PredModel.get_floor_mapping(valid_args)
        expected = 1

        self.assertEqual(result, expected)

    def test_that_storey_range_is_correct_for_13_floors(self):

        prediction_params = {
            "storey-range": "13",
            "floor-area-sqm": "75",
            "remaining-lease": "64",
            "town": "PUNGGOL"
        }

        valid_args = PredModel.process_query_strings(prediction_params)

        result = PredModel.get_floor_mapping(valid_args)
        expected = 2

        self.assertEqual(result, expected)

    def test_that_error_is_raised_if_floor_is_negative(self):

        prediction_params = {
            "storey-range": "-1",
            "floor-area-sqm": "75",
            "remaining-lease": "64",
            "town": "PUNGGOL"
        }

        valid_args = PredModel.process_query_strings(prediction_params)

        with self.assertRaises(ValueError) as error:
            PredModel.get_floor_mapping(valid_args)

        exception = error.exception
        self.assertEqual(f"{exception}","Storey-range cannot be less than 1!")

    def test_number_of_prediction_parameters_is_29(self):

        prediction_params = {
            "storey-range": "13",
            "floor-area-sqm": "75",
            "remaining-lease": "64",
            "town": "PUNGGOL"
        }

        valid_args = PredModel.process_query_strings(prediction_params)

        result = len(PredModel.get_prediction_params(valid_args))
        expected = 29

        self.assertEqual(result, expected)