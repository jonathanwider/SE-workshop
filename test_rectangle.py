from rectangle import Rectangle
import pytest as pt

class Test_Rectangle:
    mock_rectangle = Rectangle(width=2.5, height=3)

    def test_area_and_perimeter_updates_to_new_length(self):
        self.mock_rectangle.width = 5
        assert self.mock_rectangle.area == 15
        assert self.mock_rectangle.perimeter == 16

    def test_area(self):
        assert self.mock_rectangle.area == 7.5

    def test_perimeter(self):
        assert self.mock_rectangle.perimeter == 11
