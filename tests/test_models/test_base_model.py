""" This is the test file for the BaseModel class. """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ A class to test the BaseModel class. """

    def setUp(self):
        """ Code to be added at the beginning of each test case. """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def TearDown(self):
        """ Code to be added at the end of each test case. """
        pass
# ===============================
    # Testing __init__ function
# ===============================

    def test_kwargs_setattr_and_hasattr(self):
        """ Testing kwargs with setatrr() and hasattr(). """

        self.b1 = BaseModel(
            name="My_First_Model",
            age=89,
            created_at="2024-05-05T17:20:07.031849")

        self.b2 = BaseModel(
            name="My_Second_Model",
            age=30,
            updated_at="2024-05-05T17:20:07.031849"
            )

        self.assertIsNot(self.b1, self.b2)
        self.assertIsNot(self.b1.id, self.b2.id)
        self.assertIsNot(self.b1.created_at, self.b2.created_at)
        self.assertIsNot(self.b1.updated_at, self.b2.updated_at)
        self.assertEqual(type(self.b1.created_at), type(self.b2.updated_at))

    def test_models_with_no_kwargs(self):
        """ Testing models with no keyworded arguments. """

        self.assertIsNot(self.b1, self.b2)
        self.assertIsNot(self.b1.id, self.b2.id)
        self.assertIsNot(self.b1.created_at, self.b2.created_at)
        self.assertIsNot(self.b1.updated_at, self.b2.updated_at)

    def test_created_and_updated_equalityand_types(self):
        """ Testing id, created_at, updated_at types. """

        self.assertEqual(self.b1.created_at, self.b1.updated_at)
        self.assertEqual(type(self.b1.id), str)
        self.assertEqual(type(self.b1.created_at), datetime)
        self.assertEqual(type(self.b1.updated_at), datetime)

# ===============================
    # Testing Save function
# ===============================

    def test_save_func(self):
        """Testing save method."""

        self.assertNotEqual(self.b1.save(), self.b1.created_at)
        self.assertEqual(self.b1.save(), self.b1.updated_at)

# ===============================
    # Testing to_dict function
# ===============================

    def test_to_dict(self):
        """Testing the to_dict method."""

        self.assertEqual(self.b1.to_dict(), self.b1.__dict__)
        self.assertEqual(type(self.b1.to_dict()), dict)

# ===============================
    # Testing __str__ function
# ===============================

    def test_str(self):
        """Testing the __str__ method."""

        str1 = self.b1.__str__()

        self.assertEqual(self.b1.__class__.__name__, "BaseModel")
        self.assertIn(self.b1.id, self.b1.__str__())
        # self.assertIn(self.b1.created_at, self.b1.__str__())
        self.assertIn(str(self.b1.__dict__), self.b1.__str__())

    def test_str_with_kwrgs(self):
        """Testing the __str__ method."""

        base = BaseModel(name="Yassin", num=3)
        str1 = base.__str__()

        self.assertIn(base.name, str1)


if __name__ == "__main__":
    unittest.main()
