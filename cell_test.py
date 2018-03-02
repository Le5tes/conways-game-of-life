from cell import Cell

def test_starts_dead():
	cell = Cell([])
	assert cell.is_alive == False