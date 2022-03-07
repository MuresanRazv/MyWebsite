from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days = 5)

db = SQLAlchemy(app)

class info(db.Model):
	_id = db.Column("id", db.Integer, primary_key = True)
	name = db.Column("name", db.String(100))
	email = db.Column("email",db.String(100))
	country = db.Column("country",db.String(50))
	message = db.Column("message",db.String(500))
	def __init__(self, name, email, country, message):
		self.name = name
		self.email = email
		self.country = country
		self.message = message


@app.route('/')
@app.route('/home')
def home():
	return render_template('RO/home_RO.html')

@app.route('/home_EN')
def home_EN():
	return render_template('EN/home_EN.html')

@app.route('/home_GER')
def home_GER():
	return render_template('GER/home_GER.html')

@app.route('/photos')
def photos():
	return render_template('RO/gallery_RO.html')

@app.route('/photos_EN')
def photos_EN():
	return render_template('EN/gallery_EN.html')

@app.route('/photos_GER')
def photos_GER():
	return render_template('GER/gallery_GER.html')

@app.route('/contact', methods=["POST","GET"])
def contact():
	if request.method == "POST":
		session.permanent = True
		name  = request.form["name"]
		email = request.form["email"]
		country = request.form["country"]
		message = request.form["message"]
		usr = info(name, email, country, message)
		db.session.add(usr)
		db.session.commit()
	return render_template('RO/contact_RO.html')

@app.route('/contact_EN', methods=["POST","GET"])
def contact_EN():
	if request.method == "POST":
		session.permanent = True
		name  = request.form["name"]
		email = request.form["email"]
		country = request.form["country"]
		message = request.form["message"]
		usr = info(name, email, country, message)
		db.session.add(usr)
		db.session.commit()
	return render_template('EN/contact_EN.html')

@app.route('/contact_GER', methods=["POST","GET"])
def contact_GER():
	if request.method == "POST":
		session.permanent = True
		name  = request.form["name"]
		email = request.form["email"]
		country = request.form["country"]
		message = request.form["message"]
		usr = info(name, email, country, message)
		db.session.add(usr)
		db.session.commit()
	return render_template('GER/contact_GER.html')

@app.route("/view")
def view():
	return render_template("view.html", values = info.query.all())

if __name__=="__main__":
	db.create_all()
	app.run(debug = True)
	