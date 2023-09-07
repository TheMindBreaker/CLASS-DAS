from flask import Flask, request, jsonify
from grocery.controller import routes, data

app = Flask(__name__)
app.register_blueprint(routes.blueprint)
app.register_blueprint(data.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)