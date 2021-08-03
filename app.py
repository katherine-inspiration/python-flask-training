from flask import Flask
from routes import initialize_routes

app = Flask(__name__)


initialize_routes(app)


if __name__ == "__main__":
    app.run(debug=True)