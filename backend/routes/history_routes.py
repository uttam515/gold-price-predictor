from flask import Blueprint, jsonify

history_bp = Blueprint("history", __name__)

@history_bp.route("/gold/history", methods=["GET"])
def get_history():

    history = [
        {"date": "2024-01-01", "price": 6200},
        {"date": "2024-02-01", "price": 6300},
        {"date": "2024-03-01", "price": 6450},
        {"date": "2024-04-01", "price": 6600},
        {"date": "2024-05-01", "price": 6700}
    ]

    return jsonify(history)