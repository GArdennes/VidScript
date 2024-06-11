#!/usr/bin/env python3
"""
Script for authentication service
"""
import jwt, datetime, os
from flask import Flask, request, render_template, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

#configuration
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST", "localhost")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER", "auth_user")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD", "")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB", "auth")
app.config["MYSQL_PORT"] = int(os.environ.get("MYSQL_PORT", 3306))

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handle the login request 
    """
    #retrieve the username and password
    if request.method == "POST":
        auth = request.authorization 

    #check for missing credentials
        if not auth:
            return "Please provide both email address and password.", 400
    #query the database
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT email, password FROM user WHERE email = %s", (auth.username,)
        )
        user_data = cursor.fetchone()
    #verifies the credentials
        if user_data:
            if auth.username != user_data[0] or auth.password != user_data[1]:
                return "Incorrect credentials", 401
            else:
                #return "Login successful", 200
    #generates jwt token            
                return createJWT(auth.username, os.environ.get("JWT_SECRET", 'FortKnox'), True)
        else:
            return "Invalid credentials", 401
    else:
        return render_template("login.html"), 200


@app.route("/validate", methods=["POST", "GET"])
def validate():
    """
    Authorize and authenticate Jason Web Token
    """
    #extract the token
    if request.method == "POST":
        encodedjwt = request.headers["Authorization"]
    #check for missing parameters
        if not encodedjwt:
            return "Missing token", 401
    #decode the token
        encodedjwt = encodedjwt.split(" ")[1]
        try:
    #return decoded jwt 
            decoded = jwt.decode(
                encodedjwt, os.environ.get("JWT_SECRET", 'FortKnox'), algorithms=["HS256"]
            )
        except Exception as error:
            print(error)
            return "\n Not authorized", 403  
        return decoded, 200
    else:
        return render_template("validate.html"), 200
    

@app.route("/register", methods=["POST"])
def logout():
    """
    """
    pass

def createJWT(username, secret, authz):
    """
    Generate JWT token as string
    """
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


    
