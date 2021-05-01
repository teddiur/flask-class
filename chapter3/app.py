from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "my first store",
        "items": [
            {
                "name": "simple item",
                "price": 10.5
            }
        ]
    }
]
# POST /store {name:}


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    name = request_data.get("name")
    new_store = {
        "name": request_data["name"],
        "items": []}
    if any(name == store["name"] for store in stores):
        return jsonify(
            {"error": 409, "message": "this store already exists"})
    else:
        stores.append(new_store)
        return jsonify({"status": 200, "store": new_store})

# GET /store/<string:name>


@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"status": "success", "store": store})
    return jsonify({"error": 404, "message": "Store not found"})

# GET /store


@app.route("/store", methods=["GET"])
def get_all_stores():
    return jsonify({"stores": stores})


def get_store(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store
# POST /store/<string:name>/item {name: , price:}


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item(name):
    request_data = request.get_json()
    store_to_add = get_store(name)
    try:
        item = {"name": request_data["name"],
                "price": request_data["price"]}
        store_to_add["items"].append(item)
        return jsonify({"item": item, "status": "success"})
    except NameError:
        return jsonify({"error": 404, "message": "store doesn't exist"})

# GET /store/<string:name>/item


@app.route("/store/<string:name>/item", methods=["GET"])
def get_items_in_store(name):
    searched_store = get_store(name)
    if (searched_store):
        return jsonify({"items": searched_store["items"]})
    return jsonify({"error": 404, 'message': 'store not found'})
