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
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD", "Auth123")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB", "auth")
app.config["MYSQL_PORT"] = int(os.environ.get("MYSQL_PORT", 3306))

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handle the login request 
    """
    #retrieve the username and password
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")    

    #check for missing credentials
        if not email or not password:
            return "Please provide both email address and password.", 400
    #query the database
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT email, password FROM user WHERE email = %s", (email,)
        )
        user_data = cursor.fetchone()
    #verifies the credentials
        if user_data:
            if email != user_data[0] or password != user_data[1]:
                return "Invalid credentials", 401
            else:
                return "Login successful", 200
    #generates jwt token            
                #return createJWT(email, os.environ.get("JWT_SECTRET"), True)
        else:
            return "Invalid credentials", 401
    else:
        return render_template("login.html"), 200
                        
@app.route("/validate", methods=["POST"])
def validate():
    """
    """
    pass

@app.route("/logout", methods=["POST"])
def logout():
    """
    """
    pass

def createJWT(username, secret, authz):
    """
    """
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


    
