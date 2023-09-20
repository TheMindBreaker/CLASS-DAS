from flask import Blueprint, jsonify, request
from grocery.repository import data

blueprint = Blueprint('my_blueprint', __name__)


@blueprint.route('/item', methods=['GET'])
def get_items():
    return jsonify(data.load_data())

@blueprint.route('/item/<sku>', methods=['GET'])
def get_item(sku):
    return jsonify(data.load_sku(sku=sku))

@blueprint.route('/item', methods=['POST'])
def add_item():
    item = request.json
    if data.add_item(item):
        return jsonify({"message": "Agregado"}), 201
    else:
        return jsonify({"message": "El Sku ya existe"}), 400

@blueprint.route('/item/<sku>', methods=['DELETE'])
def delete_item(sku):
    if data.delete_item_by_sku(sku):
        return jsonify({"message": f"Producto {sku} borrado"})
    else:
        return jsonify({"message": f"Producto {sku} no encontrado"}), 404