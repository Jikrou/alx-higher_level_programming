import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_constructor_with_id(self):
        """Test the constructor with an ID parameter."""
        base_obj = Base(1)
        self.assertEqual(base_obj.id, 1)

    def test_constructor_without_id(self):
        """Test the constructor without an ID parameter."""
        base_obj1 = Base()
        base_obj2 = Base()
        self.assertEqual(base_obj1.id, 1)
        self.assertEqual(base_obj2.id, 2)

    def test_to_json_string(self):
        """Test the to_json_string method."""
        base_obj = Base(1)
        expected_json = '[{"id": 1}]'
        self.assertEqual(base_obj.to_json_string([{'id': 1}]), expected_json)

    def test_from_json_string(self):
        """Test the from_json_string method."""
        json_string = '[{"id": 1}, {"id": 2}]'
        expected_list = [{'id': 1}, {'id': 2}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    def test_save_to_file(self):
        """Test the save_to_file method."""
        obj1 = Square(1, 2, 3, 4)
        obj2 = Square(5, 6, 7, 8)
        list_objs = [obj1, obj2]
        Base.save_to_file(list_objs)

    def test_create_with_dictionary(self):
        """Test the create method."""
        dict_obj = {'width': 10, 'height': 20, 'x': 1, 'y': 2, 'id': 10}
        instance = Rectangle.create(**dict_obj)

        self.assertEqual(instance.width, 10)
        self.assertEqual(instance.height, 20)
        self.assertEqual(instance.x, 1)
        self.assertEqual(instance.y, 2)
        self.assertEqual(instance.id, 10)

   
if __name__ == '__main__':
    unittest.main()
