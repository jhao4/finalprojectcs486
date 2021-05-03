# https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application

from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
	return 'This is a test button'

class app():
	def hello():
		return 1234

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')