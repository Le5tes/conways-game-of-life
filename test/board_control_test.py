from lib.board_control import BoardControl
from lib.graphics import GraphWin, Rectangle
from lib.xy import XY
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
def board(mocker):
	board = mocker.Mock()
	board.cells = [[mocker.Mock(name='cell'),mocker.Mock(name='cell')],
				   [mocker.Mock(name='cell'),mocker.Mock(name='cell')]]
	board.size = 2
	return board
	
@pytest.fixture
def subject( board, rectangle_class):
	return BoardControl(board, image_class=rectangle_class)

def test_draw_draws_cells(subject, rectangle, window):
	subject.draw(window)
	assert rectangle.draw.call_count == 4

def test_update_updates_board(subject, board):
	subject.update()
	board.update.assert_called()

def test_click_tells_board_to_toggle_cell(subject, board):
	subject.click(XY(8,6))
	board.toggle.assert_called_with(XY(1,1))

