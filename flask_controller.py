from flask import Flask, render_template, request, jsonify, make_response
from read_config import ReadConfig
from es_operations import ElasticHandlers

handler = ElasticHandlers()

config_file = "config_file.conf"
config = ReadConfig(config_file)
host_name = config.get_config("config", "hostname")
port = config.get_config("config", "port")
index_name = config.get_config("config", "index_name")

app = Flask(__name__)
@app.route('/users', methods = ["POST"])
def user_create():
    first_name = request.json.get('fname')
    last_name = request.json.get('lname')
    age = request.json.get('age')
    user_obj = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    result = handler.es_post(index_name, user_obj)
    return jsonify(result)


@app.route('/users', methods = ["DELETE"])
def user_delete():
    user_id = request.json.get('id')
    result = handler.es_delete(index_name, user_id)
    return jsonify(result)

@app.route('/users', methods = ["GET"])
def user_get():
    user_id = request.json.get('id')
    result = handler.es_get(index_name, user_id)
    return jsonify(result)


@app.route('/users', methods = ["PUT"])
def user_update():
    user_id = request.json.get('id')
    # user_get_id = request.args.get('id')
    first_name = request.json.get('fname')
    last_name = request.json.get('lname')
    age = request.json.get('age')
    user_obj = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }

    result = handler.es_update(index_name, user_id, user_obj)
    return jsonify(result)

@app.route('/search', methods = ["POST"])
def user_search():
    age = request.json.get('age')
    user_id = request.json.get('id')
    result = handler.es_search(index_name, user_id, age)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=port)