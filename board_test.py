from board import Board
from cell import Cell
import pytest

@pytest.fixture
def subject():
	return Board(5)

@pytest.fixture
def mockcell(mocker):
	return mocker.Mock(spec=Cell)


def test_update_preps_cells(subject, mocker):
	mocker.spy(subject.cells[0][0],'prep')
	subject.update()
	assert subject.cells[0][0].prep.call_count == 1

def test_update_updates_cells(subject, mocker):
	mocker.spy(subject.cells[0][0],'update')
	subject.update()
	assert subject.cells[0][0].update.call_count == 1

def test_initialises_cells_with_their_neighbours(mockcell):
	def cell_double():
		return mockcell

	Board(5,cell_double)
	mockcell.set_surrounders.assert_called_with([mockcell,mockcell,mockcell])
	
