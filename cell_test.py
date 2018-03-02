from cell import Cell

def setup_cell(is_alive,num_of_surrounding_alive):
	living_cell = Cell([])
	living_cell.is_alive = True
	surrounders= [living_cell] * num_of_surrounding_alive
	cell = Cell(surrounders)
	cell.is_alive = is_alive
	return cell 

def test_starts_dead():
	cell = Cell([])
	assert cell.is_alive == False

def test_becomes_alive_if_3_living_cells_nearby():
	cell = setup_cell(False,3)
	cell.prep()
	cell.update()
	assert cell.is_alive == True

def test_stays_alive_with_2_or_3_living_cells_nearby():
	cell = setup_cell(True,2)
	cell.prep()
	cell.update()
	assert cell.is_alive == True
	cell = setup_cell(True,3)
	cell.prep()
	cell.update()
	assert cell.is_alive == True

def test_dies_with_fewer_living_cells_nearby():
	cell = setup_cell(True,1)
	cell.prep()
	cell.update()
	assert cell.is_alive == False

def test_dies_with_too_many_living_cells_nearby():
	cell = setup_cell(True,4)
	cell.prep()
	cell.update()
	assert cell.is_alive == False