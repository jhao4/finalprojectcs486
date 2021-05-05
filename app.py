# https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application
# https://github.com/alexanderdamiani/test_repo_pylinter_v2/blob/main/.github/workflows/python-app.yml
from flask import Flask
import random, requests

app = Flask(__name__)

RICKMORTY_API = 'https://rickandmortyapi.com/api/character/'

@app.route('/')
def index():
	randomNum = random.randint(1,400)
	params = {'format': 'json'}
	response = requests.get(RICKMORTY_API + str(randomNum), params=params)
	name = response.json()['name']
	img = response.json()['image']
	species = response.json()['species']
	location = response.json()['location']['name']
	status = response.json()['status']
	return page_layout(name, img, species, location, status)

def page_layout(name, img, species, location, status):
	return f'<h1>Hello my name is {name}<br>' + img_layout(img) + '<br>' + info_layout(species, location, status)

def img_layout(img):
	return f'<img src={img} width=\'500\' height=\'600\'>'

def info_layout(species, location, status):
	if status == 'Alive':
		status = '<h2>Against all the odds, I\'m still alive!</h2>'
	else:
		status = '<h2>Unfortunately I\'m dead, more than likely cause of either Rick or Morty, or both of them</h2>'
	return f'<h2>I\'m a {species} and was last seen on {location}</h2>' + status


@app.route('/<name>')
def user(name):
	return f"Hello {name}!!!"

def hello():
	return 1234

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')