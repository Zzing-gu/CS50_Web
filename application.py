import os

from flask import Flask, session , render_template , request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template("login_register.html")
    else:
        return render_template("search.html")
    


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    print( name , email , username , password)

    session["user_id"] = username

    db.execute("INSERT INTO users (name , email, username , password) VALUES (:name, :email, :username, :password)" ,
        {"name":name, "email":email, "username":username, "password":password})
    db.commit()
    return render_template("login_register.html")



@app.route("/login" , methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = db.execute("SELECT * FROM users WHERE username = :username AND password = :password", {"username": username , "password":password})
    if user is None:
        return render_template("error.html", message="No such user or wrong password.")

    
    session['logged_in'] = True
    session['user_id'] = username
        
    return index()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['user_id'] = None

    return index()


@app.route("/search" , methods=["GET" , "POST"])
def search():
    search = request.form.get("search")
    print(search)
    newsearch = '%' + search + '%'
    books = db.execute("SELECT * FROM books WHERE isbn::text LIKE :search OR  title::text LIKE :search OR  author::text LIKE :search " , {"search" : newsearch})
    print(books)
    #books= [1,2,3]
    return render_template('search.html', books=books)



@app.route("/book")
def book():

    return "book!"