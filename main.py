from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) 
auth = HTTPBasicAuth()
@auth.verify_password
def VerifyPassword(username, password):
    pass

@app.route("/test")
@auth.login_required
def Test():
    return "Hello world"

app.run(debug=True)