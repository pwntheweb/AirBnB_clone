#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    testing file storage
    """

    @classmethod
    def setUpClass(cls):
        cls.usr = User()
        cls.usr.first_name = "Andrew"
        cls.usr.last_name = "Suh"
        cls.usr.email = "andrew@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        del cls.usr

    def teardown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        except Exception as e:
            print(f"An error occured: {e}")

    def test_pep8_filestorage(self):
        """
        tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all_filestorage(self):
        """
        tests for all
        """
        new = FileStorage()
        instances_dic = new.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, new._FileStorage__objects)

    def test_new_filestorage(self):
        """
        tests for new
        """
        altsotrage = FileStorage()
        dic = altsotrage.all()
        rev = User()
        rev.id = 69
        rev.first_name = "Meep"
        altsotrage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_reload_filestorage(self):
        """ tests reload """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []

        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        except Exception as e:
            print(f"An error occured: {e}")

        self.storage.save()

        try:
            with open(path, 'r') as f:
                lines2 = f.readlines()
        except FileNotFoundError:
            lines2 = []

        self.assertEqual(lines, lines2)

        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"An error occured: {e}")

        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
