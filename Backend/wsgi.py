from flask_app.run import app 

if __name__=="__main__":
    app.run('0.0.0.0', debug=True)
    #app.run('127.0.0.1, debug=True) is our debugging webserver

    #'0.0.0.0' production webserver