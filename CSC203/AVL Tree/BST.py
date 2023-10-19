from typing import cast, TypeVar

T = TypeVar('T')

from BinTree import BinTree

class BST(BinTree[T]):
    """Class to implement a binary search tree for values of type T."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = super()._invariant()
        if self.hasLeftChild():
            valid = (valid and self.value() > self.getLeftChild().value()  # type: ignore
                    and self.getLeftChild()._invariant())
        if self.hasRightChild():
            valid = (valid and self.value() < self.getRightChild().value() # type: ignore
                    and self.getRightChild()._invariant())
        if not self.isRoot():
            parent: BST[T] = cast(BST(T), self.getParent())
            if self.value() < parent.value():
                valid = (valid and parent.hasLeftChild() and self is parent.getLeftChild())
        return valid
    
    def __init__(self, value: T):
        """Construct a one-node BST with data VALUE."""
        super().__init__(value)
        # Post:
        assert self._invariant()

    # --------------- QUERY METHODS ----------------------
    
    def __contains__(self, value: T) -> bool:
        """Returns True if VALUE is in the tree, otherwise False."""
        return (self.get(value) is not None)

    def get(self, value: T, default: T | None = None) -> T | None:
        """If VALUE is in the tree, return it.  Otherwise, return None."""
        result = None
        if value == self.value():
            result = value
        # Look in the left subtree
        elif value < self.value() and self.hasLeftChild():   # type: ignore
            result = cast(BST[T], self.getLeftChild()).get(value)
        # Look in the right subtree
        elif value > self.value() and self.hasRightChild():  # type: ignore
            result = cast(BST[T], self.getRightChild()).get(value)
        return result

    def findMinVal(self) -> T:
        """Find the minimum value (not node) in the subtree rooted
          at the current node."""
        if not self.hasLeftChild():
            return self.value()
        else:
            return cast(BST[T], self.getLeftChild()).findMinVal()
        
    def findSuccessor(self) -> T | None:
        """Find the successor value (not node) for the current node
          in an inorder traversal."""
        successor: T | None = None
        if self.hasRightChild():
            successor = cast(BST[T], self.getRightChild()).findMinVal()
        elif not self.isRoot():
            parent: BST[T] = cast(BST[T], self.getParent())
            if parent.hasLeftChild() and parent.getLeftChild() is self:
                # self is the left child of its parent
                successor = parent.value()
            else: # self is the right child of its parent
                parent.setRightChild(None) # Temporary!
                successor = parent.findSuccessor()
                parent.setRightChild(self) # Put things back when we're done
                # Verify we got it back correctly
                assert self.getParent() is parent and parent.getRightChild() is self
        return successor

    # --------------- MUTATOR METHODS ---------------------

    def put(self, value: T) -> None:
        """Put a value VALUE into the tree.  Does nothing
           if VALUE is already in the tree."""
        if value < self.value(): # type: ignore
            if self.hasLeftChild():
                cast(BST[T], self.getLeftChild()).put(value)
            else:
                self.setLeftChild(BST[T](value))
        elif value > self.value(): # type: ignore
            if self.hasRightChild():
                cast(BST[T], self.getRightChild()).put(value)
            else:
                self.setRightChild(BST[T](value))
        # Post:.
        assert self._invariant()

    def delete(self, value: T) -> 'BST[T] | None':
        """Delete item with value VALUE from the tree.
           Raise a KeyError if VALUE is not in the tree.
           Returns the tree with the node removed."""
        result: BST[T] | None = self
        if self._data == value: # This is the victim node
            if not self.hasLeftChild() and not self.hasRightChild():
                # No children, just return None
                result = None
            elif not self.hasLeftChild(): # Right child only
                result = cast(BST[T], self.getRightChild())
            elif not self.hasRightChild(): # Left child only
                result = cast(BST[T], self.getLeftChild())
            else: # Two children
                successor: T = cast(BST[T], self.getRightChild()).findMinVal()
                self._data = successor
                self.setRightChild(cast(BST[T], self.getRightChild()).delete(successor))
                # return self (happens by default)
        
        elif value < self.value(): # type: ignore 
            # Look in the left subtree
            if self.hasLeftChild():
                self.setLeftChild(cast(BST[T], self.getLeftChild()).delete(value))
            else:
                raise KeyError('Value to be deleted not in tree')
        elif value > self.value():  # type: ignore
            # Look in the right subtree
            if self.hasRightChild():
                self.setRightChild(cast(BST[T], self.getRightChild()).delete(value))
            else:
                raise KeyError('Value to be deleted not in tree')
        
        # Post
        assert (result is None) or (result._invariant())
        return result

    def __delitem__(self, value: T) -> None:
        self.delete(value)