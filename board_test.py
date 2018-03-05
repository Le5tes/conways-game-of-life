from board import Board
import pytest

@pytest.fixture
def subject():
	return Board(5)

def test_update_preps_cells(subject, mocker):
	mocker.spy(subject.cells[0],'prep')
	subject.update()
	assert subject.cells[0].prep.call_count == 1

def test_update_updates_cells(subject, mocker):
	mocker.spy(subject.cells[0],'update')
	subject.update()
	assert subject.cells[0].update.call_count == 1

