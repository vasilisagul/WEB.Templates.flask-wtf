from flask import Flask, render_template

app = Flask(__name__)


@app.route('/trainding/<prof>')
def index(prof):
    return render_template('traiding.html', title=prof.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')