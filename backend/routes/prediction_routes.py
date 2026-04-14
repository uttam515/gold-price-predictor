from flask import Blueprint, request, jsonify
from services.prediction_service import predict_price

prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body must be JSON"
        }), 400

    if "year" not in data or "usd_to_inr" not in data:
        return jsonify({
            "error": "Missing required fields: year and usd_to_inr"
        }), 400

    try:
        result = predict_price(data)

        return jsonify({
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500