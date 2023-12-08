import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a new instance of BaseModel for each test"""
        self.my_model = BaseModel()

    def test_attributes(self):
        """Test the initial attributes of BaseModel"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str_representation(self):
        """Test the __str__ method"""
        str_representation = str(self.my_model)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn(str(self.my_model.id), str_representation)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)

    def test_to_dict_isoformat(self):
        """Test if created_at and updated_at are in ISO format"""
        my_model_dict = self.my_model.to_dict()
        created_at = datetime.strptime(my_model_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(my_model_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_json_representation(self):
        """Test if the to_dict representation can be converted to JSON"""
        my_model_dict = self.my_model.to_dict()
        my_model_json = json.dumps(my_model_dict)
        self.assertIsInstance(my_model_json, str)

    """New tests """
    def test_init_with_kwargs(self):
        """Test __init__ when instantiated with kwargs"""
        """ Example kwargs representing attributes loaded from a JSON file"""
        kwargs_example = {
            'id': 'some_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T13:30:00.000000',
            'other_attribute': 'some_value'
        }

        """ Create an instance of BaseModel using kwargs"""
        my_model = BaseModel(**kwargs_example)

        """ Verify that attributes from kwargs are correctly set in the instance"""
        self.assertEqual(my_model.id, kwargs_example['id'])
        self.assertEqual(my_model.created_at, datetime.strptime(kwargs_example['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(my_model.updated_at, datetime.strptime(kwargs_example['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(getattr(my_model, 'other_attribute', None), 'some_value')

    def test_init_with_kwargs_convert_isoformat(self):
        """Test __init__ when instantiated with kwargs and converting isoformat"""
        """Example kwargs with ISO format strings for created_at and updated_at"""
        kwargs_isoformat = {
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T13:30:00.000000',
        }

        """ Create an instance of BaseModel using kwargs with ISO format strings"""
        my_model = BaseModel(**kwargs_isoformat)

        """ Verify that attributes are correctly set and converted to datetime objects """
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
