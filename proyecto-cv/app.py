from flask import Flask, render_template, url_for
from data import data_informacion


app = Flask(__name__)
@app.route('/')

def index():
    
    """ return 'Hello, World!' """
    return render_template('index.html', data = data_informacion)


if __name__ == '__main__':
    app.run(debug=True)