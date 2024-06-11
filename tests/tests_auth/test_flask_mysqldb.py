from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_USER"] = "auth_user"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "auth"
app.config["MYSQL_HOST"] = "localhost"

mysql = MySQL(app)

@app.route("/")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM user""")
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run(debug=True)
