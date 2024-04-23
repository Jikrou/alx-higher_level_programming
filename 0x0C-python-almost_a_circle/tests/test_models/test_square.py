import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    """
    Test cases for the Square class.
    """

    def test_area(self):
        """
        Test the area method of the Square class.
        """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update(self):
        """
        Test the update method of the Square class.
        """
        s = Square(3, 2)
        s.update(4, 6)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 6)

    def test_str(self):
        """
        Test the str method of the Square class.
        """
        s = Square(2)
        expected_str = "[Square] (8) 0/0 - 2"
        self.assertEqual(str(s), expected_str)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """
        s = Square(4, 1, 2, 5)
        expected_dict = {'id': 5, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
