from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'To są małe zmiany w pliku Wojtek Test'


if __name__ == '__main__':
    app.run()
