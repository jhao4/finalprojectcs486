import pytest
import requests
import app

from pytest_bdd import scenarios, when, then, parsers

scenarios('rickmortycharacters.feature')

@pytest.fixture
@when('Rick and Morty character id 5')
def character_response():
	return app.parse_information(5)

@then('the response shows name is jerry smith')
def character_response_name(character_response):
	assert character_response[0] == 'Jerry Smith'

@then('the response shows species is human')
def character_response_species(character_response):
	assert character_response[2] == 'Human'

@then('the response shows status is Alive')
def character_response_status(character_response):
	assert character_response[4] == 'Alive'

@then('the response shows location is Earth (Replacement Dimension)')
def character_response_status(character_response):
	assert character_response[3] == 'Earth (Replacement Dimension)'
