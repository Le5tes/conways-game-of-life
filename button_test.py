from button import Button
import pytest

class XY:
	def __init__(self,x,y):
		self.x = x
		self.y = y




@pytest.fixture
def subject(mocker): 
	mock_method = mocker.stub(name='my_method')
	return Button(XY(5,5),XY(10,10),'MAH BUTTON', mock_method)

def test_if_click_is_within_bounds_calls_function(subject):
	subject.click(XY(10,10))
	subject.function.assert_called_with()

def test_if_not_within_bounds_do_nothing(subject):
	subject.click(XY(4,4))
	subject.click(XY(16,16))

	subject.function.assert_not_called()


class MyObj:
	def __init__(self):
		self.value = 0
		self.button = Button(XY(5,5),XY(10,10), 'Button', self.method)

	def click(self, point):
		self.button.click(point)

	def method(self):
		self.value +=1


def test_interaction():
	foo = MyObj()
	foo.click(XY(10,10))
	assert foo.value == 1
