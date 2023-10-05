from collections.abc import Sized
from typing import Generic, TypeVar

T = TypeVar('T')

class BinTree(Generic[T], Sized):
    """Class to represent a binary tree, using the
       node-and-references approach.  This tree representation
       adds an upward link to the node's parent to the classic
       node-and-references representation."""
    
    def _invariant(self) -> bool:
        # Check whether the parent link is valid
        valid: bool = True
        if not self.isRoot():
            parent: BinTree[T] = self.getParent()
            valid = valid and \
                ((parent.hasLeftChild() and parent.getLeftChild() is self) or \
                    (parent.hasRightChild() and parent.getRightChild() is self))
        if self.hasLeftChild():
            valid = valid and (self.getLeftChild().getParent() is self)
        if self.hasRightChild():
            valid = valid and (self.getRightChild().getParent() is self)
        return valid


    def __init__(self, data: T, parent: 'BinTree[T] | None' = None):
        """Create a childless node."""
        self._data: T = data
        self._parent: BinTree[T] | None = parent
        self._leftChild: BinTree[T] | None = None
        self._rightChild: BinTree[T] | None = None
        assert self._invariant()

    # -------- QUERY METHODS -----------------------------------

    def value(self) -> T:
        """Returns the data in the current node."""
        return self._data

    def isRoot(self) -> bool:
        """Return True is the current node is the root of the tree (has no parent)."""
        return self._parent is None

    def hasLeftChild(self) -> bool:
        """Return True if the current node has a left child."""
        return self._leftChild is not None
    
    def hasRightChild(self) -> bool:
        """Return True if the current node has a right child."""
        return self._rightChild is not None

    def getParent(self) -> 'BinTree[T]':
        """Return the parent of the current node."""
        # Pre:
        assert self._parent is not None
        return self._parent

    def getLeftChild(self) -> 'BinTree[T]':
        """Return the left child of the current node."""
        # Pre:
        assert self._leftChild is not None
        return self._leftChild

    def getRightChild(self) -> 'BinTree[T]':
        """Return the right child of the current node."""
        # Pre:
        assert self._rightChild is not None
        return self._rightChild
    
    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        result: int = 1
        if self.hasLeftChild():
            result += len(self.getLeftChild())
        if self.hasRightChild():
            result += len(self.getRightChild())
        return result
    
    def size(self) -> int:
        """Return the number of nodes in the tree."""
        return len(self)
    
    def height(self) -> int:
        """Return the height of the tree rooted at
        the current node."""
        leftHeight: int = 0  # Height of the left subtree
        rightHeight: int = 0 # Height of the right subtree

        if self.hasLeftChild():
            leftHeight = self.getLeftChild().height()
        if self.hasRightChild():
            rightHeight = self.getRightChild().height()
        return 1 + max(leftHeight,rightHeight)

    def __str__(self) -> str:
        """Return a string representation of the current node."""
        result: str = '['
        if self.hasLeftChild():
            result += str(self.getLeftChild()) + " "
        result += str(self._data)
        if self.hasRightChild():
            result += " " + str(self.getRightChild())
        result += ']'
        return result