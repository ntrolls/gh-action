from triangle import triangle

def test_invalid():
	assert triangle(-2, 3, 4) == -1
	assert triangle(2, -3, 4) == -1
	assert triangle(2, 3, -4) == -1

def test_equilateral():
	assert triangle(2, 2, 2) == 2