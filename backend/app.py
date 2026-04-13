from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from routes.prediction_routes import prediction_bp
from routes.health_routes import health_bp
from routes.history_routes import history_bp


app = Flask(__name__)
CORS(app)

swagger = Swagger(app)

app.register_blueprint(prediction_bp)
app.register_blueprint(health_bp)
app.register_blueprint(history_bp)

@app.route("/")
def home():
    return {"message": "Gold Price Predictor API running"}

if __name__ == "__main__":
    app.run(debug=True)