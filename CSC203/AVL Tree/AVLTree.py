from typing import cast, TypeVar

T = TypeVar('T')

from BST import BST
from BinTree import BinTree

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
        valid = valid and (self._balance == (leftHeight - rightHeight))
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
    def _rotateLeft(self) -> 'AVLTree[T]':
        """Perform a left rotation on the subtree rooted at self."""
        assert self.hasRightChild()

        newRoot = cast(AVLTree[T], self.getRightChild())
        if not self.isRoot():
            # Set up...
            allParent = cast(AVLTree[T], self._parent)
            # Promote the new root.
            newRoot = cast(AVLTree[T], self.getRightChild())
            newRoot._parent = allParent
            if self is allParent.getLeftChild():
                allParent._leftChild = newRoot
            else:
                allParent._rightChild = newRoot
        if newRoot.hasLeftChild():
            self._right = newRoot.getLeftChild()
            self._right._parent = self
        newRoot._leftChild = self
        self._parent = newRoot
        # Update the balance factors.
        self._balance = self.balance() + 1 - min(newRoot.balance(), 0)
        newRoot._balance = self.balance() + 1 + max(self.balance(), 0)
        
        # In case self *was* a root before, return newRoot anyways.
        return newRoot
    
    def _rotateLeft(self) -> 'AVLTree[T]':
        """Perform a left rotation on the subtree rooted at self."""
        assert self.hasLeftChild()

        newRoot = cast(AVLTree[T], self.getLeftChild())
        if not self.isRoot():
            # Set up...
            allParent = cast(AVLTree[T], self._parent)
            # Promote the new root.
            newRoot = cast(AVLTree[T], self.getLeftChild())
            newRoot._parent = allParent
            if self is allParent.getRightChild():
                allParent._rightChild = newRoot
            else:
                allParent._leftChild = newRoot
        if newRoot.hasRightChild():
            self._right = newRoot.getRightChild()
            self._right._parent = self
        newRoot._rightChild = self
        self._parent = newRoot
        # Update the balance factors.
        self._balance = self.balance() + 1 - max(newRoot.balance(), 0)
        newRoot._balance = self.balance() + 1 + min(self.balance(), 0)
        
        # In case self *was* a root before, return newRoot anyways.
        return newRoot

    def _updateBalance(self) -> None:
        """Update the balance factor, running up the tree to do so."""
        if not self.isRoot():
            parent = cast(AVLTree[T], self.getParent())
            if parent.hasLeftChild() and self is parent.getLeftChild():
                parent._balance += 1
            else: # self is parent's right child
                assert parent.hasRightChild() and self is parent.getRightChild()
                parent._balance -= 1
            if parent.balance() != 0:
                parent._updateBalance()

    def put(self, value: T) -> None:
        """Put a value VALUE into the tree.  Does nothing
           if VALUE is already in the tree."""
        if value < self.value(): # type: ignore
            if self.hasLeftChild():
                cast(AVLTree[T], self.getLeftChild()).put(value)
            else:
                newNode = AVLTree[T](value)
                self._leftChild = newNode
                newNode._parent = self
                newNode._updateBalance()
        elif value > self.value(): # type: ignore
            if self.hasRightChild():
                cast(AVLTree[T], self.getRightChild()).put(value)
            else:
                newNode = AVLTree[T](value)
                self._rightChild = newNode
                newNode._parent = self
                newNode._updateBalance()
        # else: value == self.value(), in which case we don't re-insert

        # Post, but only once all the rebalancing is done, so don't call it here
        # assert self._invariant()

    # def setLeftChild(self, newChild: BinTree[T] | None) -> None:
    #     """Add the node newChild as the left child of this node."""
    #     try:
    #         super().setLeftChild(newChild)
    #     except AssertionError as e:
    #         self._updateBalance(cast(AVLTree[T], newChild))
    #     finally:
    #         assert self._invariant()