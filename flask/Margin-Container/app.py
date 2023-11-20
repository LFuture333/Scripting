from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Log_in():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)