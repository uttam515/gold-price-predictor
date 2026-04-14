import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../ml"))
sys.path.append(BASE_DIR)

from predict import predict_gold_price


def predict_price(data):

    year = int(data["year"])
    usd_to_inr = float(data["usd_to_inr"])

    prediction = predict_gold_price(year, usd_to_inr)

    return prediction