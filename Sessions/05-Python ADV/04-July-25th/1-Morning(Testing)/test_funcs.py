# import unittest
# from .funcs import add
#
#
# class TestFunctions(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(10, 2), 12)
#         self.assertEqual(add(4, 2), 6)
#         self.assertNotEqual(add(4, 2), 8)
#
#     def test_add2(self):
#         self.assertEqual(add(10, 2), 12)
#         self.assertEqual(add(4, 2), 6)
#         self.assertNotEqual(add(4, 2), 8)
#
#
# if __name__ == "__main__":
#     unittest.main()

# Python -m unittest test_func.TestFuncts.test_Add
# Python -m unittest -v

# ------------------------
# pip install pytest
# You should start your files name with test_

from funcs import add


def test_add():
    assert add(10, 2) == 12
    assert add(4, 2) == 6
    assert add(4, 2) != 6

