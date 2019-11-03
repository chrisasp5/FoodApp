from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cq4z!qeu*a65et^c75c&w$@an-eg5=hbgy59yzg17c17h__2$-'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/home/codejoy/Desktop/WebTemps/Django/Django/db.sqlite3.db'

db = SQLAlchemy(app)


class NewFood(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
    rating = db.Column(db.Integer())
	comments = db.Column(db.String(500))
    date_added = db.Column(db.DateTimeField(default=timezone.now))

@app.route('/')
def past():
	result = NewFood.query.all()

    return render_template('past.html', result=result)

@app.route('/past')
def past():
	result = NewFood.query.all()

	return render_template('past.html', result=result)

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	rating = request.form['rating']
	comments = request.form['comments']

	signature = NewFood(name=name, rating=rating, comments=comments)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('past'))

@app.route('/home', methods=['GET', 'POST'])
	return render_template('home.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
