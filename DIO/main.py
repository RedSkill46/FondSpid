from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopstend.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Colum(db.Iteger, primary_key=True)
    title = db.Colum(db.String(100), nullable=False)
    price = db.Colum(db.Iteger, nullable=False)
    isActive = db.Colum(db.Boolean, default=True)
    text = db.Colum(db.Text, nullable=False)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__== "__main__":
    app.run(debug=True)