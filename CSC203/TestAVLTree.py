# Empty unit-testing class
# Made with Peter Brown, 9/28/23

import unittest
from typing import cast
from AVLTree import AVLTree

# --------------------- TESTING BEGINS HERE!!!!!!!!!!!  --------------------------#

class TestAVLTree(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def setUp(self) -> None:
        self._single = AVLTree[str]('coffee needed')

        self._tree2 = AVLTree[int](5)
        self._tree2.put(1)
        self._tree2.put(11)
        self._tree2.put(-24)
        self._tree2.put(4)
        self._tree2.put(7)
        self._tree2.put(16)
        self._tree2.put(23)

    def testBalance(self) -> None:
        self.assertEqual(self._single.balance(), 0)

        self.assertEqual(self._tree2.balance(), -1)
        self.assertEqual(cast(AVLTree[int], self._tree2.getLeftChild()).balance(), 0)
        self.assertEqual(cast(AVLTree[int], self._tree2.getLeftChild().getLeftChild()).balance(), 0)
        self.assertEqual(cast(AVLTree[int], self._tree2.getLeftChild().getRightChild()).balance(), 0)
        self.assertEqual(cast(AVLTree[int], self._tree2.getRightChild()).balance(), -1)
        self.assertEqual(cast(AVLTree[int], self._tree2.getRightChild().getLeftChild()).balance(), 0)
        self.assertEqual(cast(AVLTree[int], self._tree2.getRightChild().getRightChild()).balance(), -1)
        self.assertEqual(cast(AVLTree[int], self._tree2.getRightChild().getRightChild().getRightChild()).balance(), 0)


if __name__ == '__main__':
    unittest.main()