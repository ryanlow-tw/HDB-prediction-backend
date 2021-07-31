import pickle


class PredModel:
    __instance = None

    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):

        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)

    @staticmethod
    def get_default_prediction():

        avg_storey_range = 1
        avg_floor_area_sqm = 98.313419
        avg_remaining_lease = 75.0

        default_prediction = [avg_storey_range,
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

        default_prediction.extend(1 if col == 'town_PUNGGOL' else 0 for col in remaining_column_names)

        return default_prediction
