# https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'This is a test'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')