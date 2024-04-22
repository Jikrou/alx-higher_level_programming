import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """
    def test_initialization(self):
        """
        Test the initialization of the Rectangle class.
        """
        r = Rectangle(2, 3, 4, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """
        r = Rectangle(3, 2)
        r.display()
        expected_display = r.display()
        self.assertEqual(r.display(), expected_display)

    def test_str(self):
        """
        Test the str method of the Rectangle class.
        """
        r = Rectangle(3, 2, 1, 4, 5)
        expected_str = "[Rectangle] (5) 1/4 - 3/2"
        self.assertEqual(str(r), expected_str)

    def test_update(self):
        """
        Test the update method of the Rectangle class.
        """
        r = Rectangle(3, 2, 1, 4, 5)
        r.update(7)
        self.assertEqual(r.id, 7)
        r.update(7, 10)
        self.assertEqual(r.width, 10)
        r.update(7, 10, 8)
        self.assertEqual(r.height, 8)
        r.update(7, 10, 8, 5)
        self.assertEqual(r.x, 5)
        r.update(7, 10, 8, 5, 6)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary methode of the class rectangle."""
        r = Rectangle(3, 2, 1, 4, 5)
        expected_dict = {'id': 5, 'width': 3, 'height': 2, 'x': 1, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
