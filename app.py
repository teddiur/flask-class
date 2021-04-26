from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': "my first store",
        'items': [
            {
                'name': 'simple item',
                'price': 10.5
            }
        ]
    }
]
# POST /store {name:}


@app.route('/store', methods=["POST"])
def create_store():
    pass

# GET /store/<string:name>


@app.route('/store/<string:name>', methods=["GET"])
def get_store(name):
    pass

# GET /store


@app.route('/store', methods=["GET"])
def get_all_stores():
    pass


# POST /store/<string:name>/item {name: , price:}


@app.route('/store/<string:name>/item', methods=["POST"])
def create_item(name):
    pass

# GET /store/<string:name>/item


@app.route('/store', methods=["GET"])
def get_items_in_store(name):
    pass


app.run(port=19000)
