#!/usr/bin/python3
"""
This module contains tests for the FileStorage class
"""
import unittest
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up environment for each test"""
        self.storage = FileStorage()
        self.file_path = FileStorage.__file_path

    def tearDown(self):
        """Clean environment after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_and_save(self):
        """Test adding new object and saving"""
        user = User(id="1", email="test@example.com")
        self.storage.new(user)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        self.assertIn("User.1", data)

    def test_reload(self):
        """Test reloading from save"""
        user = User(id="1", email="test@example.com")
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        loaded_user = self.storage.all().get("User.1")
        self.assertIsInstance(loaded_user, User)
        self.assertEqual(loaded_user.email, "test@example.com")

if __name__ == '__main__':
    unittest.main()
