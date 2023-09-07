from flask import Blueprint, request, jsonify
from grocery.repository import data

blueprint = Blueprint("grocery_print", __name__)

@blueprint.route("/grocery",methods=["GET"])
def load_data():
    return jsonify(data.load_data())
    
@blueprint.route("/grocery",methods=["POST"])
def new_record():
    return "Hola"