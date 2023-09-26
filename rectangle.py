class Rectangle(object):
        def __init__(self, width: float, height: float):
            """

            :param width: The rectangle's width
            :param height: The rectangle's height
            """
            self.width = width
            self.height = height
            self._area = width * height
            self._perimeter = 2 * width + 2 * height

        @property
        def area(self):
            """

            :return: The area of the rectangle
            """
            return self._area

        @property
        def perimeter(self):
            """

            :return: The perimeter of the rectangle
            """
            return self._perimeter