#!/usr/bin/python3
"""
This module contains tests for the FileStorage class
"""
import unittest
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
        # Set up the FileStorage instance for each test
        self.storage = FileStorage()
        # Define the User object
        self.user = User(email="john@example.com", password="password123",
                         first_name="John", last_name="Doe")
        self.user.id = str(uuid.uuid4())

    def test_all_empty(self):
        # Test that all returns an empty dictionary
        self.assertEqual(self.storage.all(), {})

    def test_new_object(self):
        # Test adding a new object to storage correctly
        self.storage.new(self.user)
        self.assertIn('User.' + self.user.id, self.storage.all())

    def test_save_load(self):
        # Test saving to file and reloading from file
        user2 = User(email="jane@example.com", password="password456",
                     first_name="Jane", last_name="Doe")
        user2.id = str(uuid.uuid4())
        self.storage.new(self.user)
        self.storage.new(user2)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()),   2)
        self.assertIn('User.' + self.user.id, self.storage.all())
        self.assertIn('User.' + user2.id, self.storage.all())

if __name__ == '__main__':
    unittest.main()
