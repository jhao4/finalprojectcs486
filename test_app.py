import app

def test_add():
	assert app.add_test(4, 5) == 9

def test_find_information_id_244():
	assert app.find_information(244, 'name') == 'Mr. Poopybutthole'

def test_find_information_id_4():
	assert app.find_information(4, 'species') == 'Human'

def test_find_information_id_10():
	assert app.find_information(10, 'status') == 'Dead'