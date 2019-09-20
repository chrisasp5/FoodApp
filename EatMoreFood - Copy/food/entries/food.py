from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class NewFood(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
    rating = db.Column(db.Integer())
	comment = db.Column(db.String(500))
    date_added = db.Column(db.DateTimeField(default=timezone.now))

@app.route('/')
def past():
	result = NewFood.query.all()

	return render_template('past.html', result=result)

@app.route('/new')
def new():
	return render_template('new.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = NewFood(name=name, comment=comments)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('past'))

@app.route('/home', methods=['GET', 'POST'])
	return render_template('past.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)
