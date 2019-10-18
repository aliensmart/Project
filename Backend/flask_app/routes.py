from flask import jsonify, request
from .run import app
from kpass import Account, util
import bcrypt

@app.route('/', methods=["GET"])
def root():
    return jsonify({"name":"Welcom to Kpass API"})


@app.route('/api/create', methods=['POST'])
def create_account():
    data = request.get_json()
    api_key = util.random_api_key()
    account = Account()
    account.email = data["email"]
    account.username = data["username"]
    password = data["password"]
    salt = bcrypt.gensalt()
    account.salt = salt
    confirm_password = data["password_confirmation"]

    if confirm_password == password:
        hashed_pass = util.hash_password(password, salt)
        account.password_hash = hashed_pass
        account.api_key = api_key
        account.save()
        return jsonify({"api_key":account.api_key})
    else:
        return jsonify({"error": "password not matched"})

@app.route('/api/get_api_key', methods=['POST'])
def get_api_key():
    if not request.json:
        return jsonify({"error":'bad request'})
    if 'username' not in request.json or 'password' not in request.json:
        return jsonify({'error' : 'check username or password'})
    data = request.get_json()
    account = Account.login(username=data["username"], password=data["password"])
    if account != None:
        api = account.get_api()
        return jsonify({"api":api})
    else:
        return jsonify({"error":"account not found"})


@app.errorhandler(404)
def err_404(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(405)
def err_405(e):
    return jsonify({"error":"method not allowed"})



