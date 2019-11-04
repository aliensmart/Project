from flask import jsonify, request
from .run import app
from kpass import Account, util, Passwords
import bcrypt
import re
import cryptography
from cryptography.fernet import Fernet


#--------------------------------Main Route-------------------------------------------
@app.route('/', methods=["GET"])
def root():
    return jsonify({"name":"Welcom to Kpass API"})


#--------------------------------Account creation Route-------------------------------------------
@app.route('/api/create', methods=['POST'])
def create_account():
    data = request.get_json()
    api_key = util.random_api_key()
    account = Account()
    def validate_email():
        email = data["email"]
        #validate email with these characters
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
        if(re.search(regex, email)):
            return email
        
        
    account.email = validate_email()
    print(account.email)
    account.username = data["username"]

    #Getting password from the post request
    password = data["password"]
    salt = bcrypt.gensalt()
    account.salt = salt
    account.set_key()
    confirm_password = data["password_confirmation"]
    #check if email password and username are not empty
    if account.username=="" or password=='' or account.email==None:
        return jsonify({"error": "All field must be filled or review your email"})
    else:
        if len(password) < 8:
            return jsonify({"error":"password must be at least 8 charactere"})
        else:
            #character for the passwords
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            #compiling regex
            pat = re.compile(reg)
            #searching regex
            mat = re.search(pat, password)
            print(mat)
            if mat:
                if confirm_password == password:
                    hashed_pass = util.hash_password(password, salt)
                    account.password_hash = hashed_pass
                    account.api_key = api_key
                    account.save()
                    return jsonify({"api_key":account.api_key})
                else:
                    return jsonify({"error": "password not matched"})
            else:
                return jsonify({"error": "password must have at least one number, one uppercase and one lowercase"})


#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------Login Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
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
        return jsonify({"error":"account not found, please check email or password"})


#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------Retrieve passwords Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
@app.route('/api/<api_key>/passwords', methods=["GET"])
def get_pass(api_key):
    account = Account.api_authenticate(api_key)
    key = account.get_key()
    f = Fernet(key)
    
    passwords = account.get_passwords()
    data_list = []
    count = 1
    for passw in passwords:
        decrypted = f.decrypt(passw.password_hash)
        data_dict = {}
        data_dict['pk'] = passw.pk
        data_dict['id'] = count
        data_dict["email"] = passw.email
        data_dict["username"] = passw.username
        data_dict["password_hash"] = decrypted.decode("utf8")
        data_dict["site_name"] = passw.site_name
        data_dict["url"] = passw.url
        data_dict["account_pk"] = passw.account_pk
        data_list.append(data_dict)
        count +=1
    
    return jsonify({"passwords": data_list})


#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------Posting passwords to the database Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
@app.route('/api/<api_key>/passwords_post', methods=["POST"])
def post_passwords(api_key):
    data = request.get_json()
    print(data)
    #account of the user by the api
    account = Account.api_authenticate(api_key)
    key = account.get_key()
    #intialized the passwords class
    passwords = Passwords()
    passwords.email = data['email']
    #created the salt and the password
    salt = bcrypt.gensalt()
    passwords.salt = salt
    password = data['password']
    password = password.encode()
    f = Fernet(key)
    hashed_pass = f.encrypt(password)
    passwords.password_hash = hashed_pass
    passwords.site_name = data["site_name"]
    passwords.url = data["url"]
    passwords.account_pk = account.pk
    passwords.username = data['username']

    passwords.save()

    return jsonify({"Added":"worked"})


#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------Delete Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
@app.route('/api/<api_key>/delete', methods=["POST"])
def delet(api_key):
    account = Account().api_authenticate(api_key)
    data = request.get_json()
    pk = data['pk']
    password = Passwords(pk=pk)
    password.delete()
    account.save()
    return jsonify({"deleted":True})


#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------get site passwords Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
@app.route('/api/<api_key>/<site>', methods=["GET"])
def get_site(api_key, site):
    account = Account.api_authenticate(api_key)
    password = account.search(site)
    print(password)

    if password:
        for passw in password:
            data = {}
            data['pk'] = passw.pk
            data["email"] = passw.email
            data["username"] = passw.username
            data["password_hash"] = str(passw.password_hash)
            data["site_name"] = passw.site_name
            data["url"] = passw.url
            data["account_pk"] = passw.account_pk
            return jsonify({"your_pass":data})
    else:
        return jsonify({"erro":"not"})



#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------404 ERROR Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
@app.errorhandler(404)
def err_404(e):
    return jsonify({"error": "Not found"}), 404


#------------------------------------------------------------------------------------------------------------------------------
#--------------------------------405 ERROR Route-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
@app.errorhandler(405)
def err_405(e):
    return jsonify({"error":"method not allowed"})



