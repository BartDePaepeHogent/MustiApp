import joblib


class MustiModel:

    def __init__(self):
        self.model = joblib.load("models/my_model.pkl")

