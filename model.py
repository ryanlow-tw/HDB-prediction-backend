import pickle


class PredModel:
    storey_range_mapping = {
        "low": 0,
        "mid": 1,
        "high": 2
    }
    avg_storey_range = storey_range_mapping["mid"]
    avg_floor_area_sqm = 98.313419
    avg_remaining_lease = 75.0

    column_names = ["storey-range",
                    "floor-area-sqm",
                    "remaining-lease"]

    default_parameters = [avg_storey_range,
                          avg_floor_area_sqm,
                          avg_remaining_lease]

    remaining_column_names = ['town_ANG MO KIO',
                              'town_BEDOK', 'town_BISHAN', 'town_BUKIT BATOK', 'town_BUKIT MERAH',
                              'town_BUKIT PANJANG', 'town_BUKIT TIMAH', 'town_CENTRAL AREA',
                              'town_CHOA CHU KANG', 'town_CLEMENTI', 'town_GEYLANG', 'town_HOUGANG',
                              'town_JURONG EAST', 'town_JURONG WEST', 'town_KALLANG/WHAMPOA',
                              'town_MARINE PARADE', 'town_PASIR RIS', 'town_PUNGGOL',
                              'town_QUEENSTOWN', 'town_SEMBAWANG', 'town_SENGKANG', 'town_SERANGOON',
                              'town_TAMPINES', 'town_TOA PAYOH', 'town_WOODLANDS', 'town_YISHUN'
                              ]

    default_parameters.extend([1 if col == 'town_PUNGGOL' else 0 for col in remaining_column_names])

    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)

    @staticmethod
    def get_default_parameters():

        return PredModel.default_parameters

    def get_default_prediction(self):

        model_results = self.model.predict([PredModel.default_parameters])

        model_result = model_results[0]

        return model_result

    @staticmethod
    def _get_town_col_number(town):
        print(town)
        if f"town_{town}" not in PredModel.remaining_column_names:
            raise ValueError(f"{town} is not a valid town name!")

        return PredModel.remaining_column_names.index(f"town_{town}") + len(PredModel.column_names)

    @staticmethod
    def get_prediction_params(flat_details):

        valid_args = PredModel.process_query_strings(flat_details)

        prediction_params = [PredModel.get_floor_mapping(valid_args)]

        prediction_params.extend([valid_args["floor-area-sqm"], valid_args["remaining-lease"]])

        prediction_params.extend([0] * len(PredModel.remaining_column_names))

        town_col = PredModel._get_town_col_number(valid_args["town"])

        prediction_params[town_col] = 1

        return prediction_params

    @staticmethod
    def get_floor_mapping(flat_details):

        if flat_details["storey-range"] < 0:
            raise ValueError("Storey-range cannot be less than 1!")
        elif 7 > flat_details["storey-range"] > 0:
            return 0
        elif 6 < flat_details["storey-range"] < 13:
            return 1
        return 2

    @staticmethod
    def process_query_strings(query_strings):

        valid_args = {
            "storey-range": "",
            "floor-area-sqm": "",
            "remaining-lease": "",
            "town": ""
        }

        for key, value in query_strings.items():

            if key in valid_args:
                if key != "town":
                    valid_args[key] = int(value)
                else:
                    valid_args[key] = value

        return valid_args

    def make_prediction(self, prediction_params):

        return self.model.predict([prediction_params])[0]
