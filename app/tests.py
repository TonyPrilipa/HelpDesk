from models import User
import unittest


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        user = User(password='cat')
        self.assertTrue(user.password_hash is not None)


    def test_no_password_getter(self):
        user = User(password='dog')
        with self.assertRaises(AttributeError):
            user.password


    def test_password_verification(self):
        user = User(password='mouse')
        self.assertTrue(user.verify_password('mouse'))
        self.assertFalse(user.verify_password('elephant'))

    def test_password_salts_are_random(self):
        user = User(password='tiger')
        user2 = User(password='tiger')
        self.assertTrue(user.password_hash != user2.password_hash)

