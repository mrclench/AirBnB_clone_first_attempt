import unittest
import os
from models.engine.file_storage import FileStorage

class TestFileStorageReload(unittest.TestCase):
    def setUp(self):
        """Set up a new instance of FileStorage for each test"""
        self.file_storage = FileStorage()

    def test_reload_file_exists(self):
        """Test reloading when the file exists"""
        # Create a temporary JSON file with some data
        with open(self.file_storage._FileStorage__file_path, 'w', encoding='utf-8') as file:
            file.write('{"example_key": "example_value"}')

        # Reload the FileStorage
        self.file_storage.reload()

        # Check if the content is loaded correctly
        self.assertIn("example_key", self.file_storage._FileStorage__objects)
        self.assertEqual(self.file_storage._FileStorage__objects["example_key"], "example_value")

        # Clean up: delete the temporary file
        os.remove(self.file_storage._FileStorage__file_path)

    def test_reload_file_not_exists(self):
        """Test reloading when the file doesn't exist"""
        # Ensure the file doesn't exist
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

        # Reload the FileStorage
        self.file_storage.reload()

        # Check if __objects is empty
        self.assertEqual(len(self.file_storage._FileStorage__objects), 0)

if __name__ == '__main__':
    unittest.main()
