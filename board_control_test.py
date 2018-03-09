from board_control import BoardControl
from graphics import GraphWin, Rectangle
import pytest

@pytest.fixture
def window(mocker):
	return mocker.Mock(spec=GraphWin)

@pytest.fixture
def rectangle(mocker):
	return mocker.Mock(spec=Rectangle)

@pytest.fixture
def rectangle_class(mocker,rectangle):
	rc = mocker.Mock()
	rc.return_value = rectangle
	return rc

@pytest.fixture
def cell(mocker):
	cell = mocker.Mock()
	cell.alive.return_value = True
	return cell

@pytest.fixture
def board(mocker,cell):
	board = mocker.Mock()
	board.cells = [[cell,cell],[cell,cell]]
	board.size = 2
	return board
	
@pytest.fixture
def subject( board, rectangle_class):
	return BoardControl(board, image_class=rectangle_class)

def test_draw_draws_cells(subject, rectangle, window):
	subject.draw(window)
	assert rectangle.draw.call_count == 4

