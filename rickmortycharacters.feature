Feature: Rick and Morty Characters
	I would like to know the species, status and location of some rick and morty characters

	Scenario: Rick and Morty character: Jerry Smith
		When Rick and Morty character id 5
		Then the response shows name is jerry smith
		Then the response shows species is human
		Then the response shows status is Alive
		Then the response shows location is Earth (Replacement Dimension)