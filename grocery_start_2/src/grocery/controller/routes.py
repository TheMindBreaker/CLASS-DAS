from flask import Blueprint, request, jsonify

blueprint = Blueprint("default_print",__name__)


# http://localhost:8081/hello
@blueprint.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


# http://localhost:8081/params?test=Mario
@blueprint.route("/params", methods=["GET"])
def params():
    test = request.args.get("test", default="World", type=str)
    return f"Hello {test}"


# http://localhost:8081/mario
@blueprint.route("/name/<name>", methods=["GET"])
def root(name: str):
    return f"Hello {name}"


@blueprint.route('/test', methods=['POST'])
def my_view_func():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Hello {email}"


@blueprint.route('/json', methods=["POST"])
def json():
    data = request.get_json()
    return jsonify(data)