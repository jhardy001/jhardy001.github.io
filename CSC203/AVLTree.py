from typing import cast, TypeVar

T = TypeVar('T')

from BST import BST

class AVLTree(BST[T]):
    """Class to implement an AVL tree for values of type T.
    The balance factor is the height of the right subtree
    minus the height of the left subtree.  It should always
    be in the interval [-1, 1]."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = super()._invariant()
        # Balance factor is not too out of balance
        valid = valid and (-1 <= self._balance <= 1)
        # Is the balance factor correct?
        leftHeight = 0
        rightHeight = 0
        if self.hasLeftChild():
            leftHeight = self.getLeftChild().height()
        if self.hasRightChild():
            rightHeight = self.getRightChild().height()
        valid = valid and (self._balance == (rightHeight - leftHeight))
        return valid

    def __init__(self, value: T):
        """Construct a one-node AVLTree with data VALUE."""
        self._balance = 0 # No children yet
        super().__init__(value)
        

    # ---------------- QUERY METHODS -----------------------------

    def balance(self) -> int:
        return self._balance
    
    def __str__(self) -> str:
        """Return a string representation of the current node."""
        result: str = '['
        if self.hasLeftChild():
            result += str(self.getLeftChild()) + " "
        result += str(self._data) + ':' + str(self._balance)
        if self.hasRightChild():
            result += " " + str(self.getRightChild())
        result += ']'
        return result
    
    # --------------- MUTATOR METHODS ---------------------

    def put(self, value: T) -> None:
        """Put a value VALUE into the tree.  Does nothing
           if VALUE is already in the tree."""
        if value < self.value(): # type: ignore
            if self.hasLeftChild():
                cast(AVLTree[T], self.getLeftChild()).put(value)
            else:
                self.setLeftChild(AVLTree[T](value))
        elif value > self.value(): # type: ignore
            if self.hasRightChild():
                cast(AVLTree[T], self.getRightChild()).put(value)
            else:
                self.setRightChild(AVLTree[T](value))
        # Post:.
        assert self._invariant()