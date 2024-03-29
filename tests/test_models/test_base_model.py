#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def value(self, **kwargs):
        if 'Name' not in kwargs:
            raise KeyError("'Name' key is missing")
        return BaseModel()

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        except Exception as e:
            print(f"An error occured: {e}")

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """  """
        instance = self.value()
        instance.save()
        key = "{}.{}".format(type(instance).__name__, instance.id)
        with open('file.json', 'r') as file:
            json_data = json.load(file)
        self.assertIn(key, json_data)
        self.assertEqual(json_data[key], instance.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def save(self):
        """ """
        self.updated_at = datetime.now()
        models.storage.save()

    def test_updated_at(self):
        """ """
        new = self.value()
        old_updated_at = new.updated_at
        new.some_attribute = "some_value"
        new.save()
        self.assertNotEqual(old_updated_at, new.updated_at)
