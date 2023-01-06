class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
      
    def update_height(self):
      lchild = self.left
      rchild = self.right
      if lchild == None and rchild == None:
        self.height = 1
      elif lchild == None: # From here, lh and rh cannot both be None
        self.height = rchild.height + 1
      elif rchild == None:
        self.height = lchild.height + 1
      elif lchild.height > rchild.height: # From here, neither lh nor rh are None
        self.height = lchild.height + 1
      else: # lchild.height <= rchild.height
        self.height = rchild.height + 1

  def __init__(self):
    self.__root = None
  
  def __find_balance(self, root):
    hleft = 0
    hright = 0
    if root.left != None:
      hleft = root.left.height
    if root.right != None:
      hright = root.right.height
    return hright - hleft
  
  def __rotate_left(self, old_root):
    new_root = old_root.right
    floater = new_root.left
    new_root.left = old_root
    old_root.right = floater
    old_root.update_height()
    return new_root
  
  def __rotate_right(self, old_root):
    new_root = old_root.left
    floater = new_root.right
    new_root.right = old_root
    old_root.left = floater
    old_root.update_height()
    return new_root

  def __balance(self, root):
    balance = self.__find_balance(root)
    if balance < -1: # Left child height is greater than the right child height by 2
      subtree_bal = self.__find_balance(root.left)
      if subtree_bal > 0: # Left child is right-heavy
        root.left = self.__rotate_left(root.left)
        root.left.update_height()
        root = self.__rotate_right(root)
      else: # subtree_bal <= 0, left child is left-heavy or balanced
        root = self.__rotate_right(root)
    elif balance > 1: # Right child height is greater than the left child height by 2
      subtree_bal = self.__find_balance(root.right)
      if subtree_bal < 0: # Right child is left-heavy
        root.right = self.__rotate_right(root.right)
        root.right.update_height()
        root = self.__rotate_left(root)
      else: # subtree_bal >= 0, right child is right-heavy or balanced
        root = self.__rotate_left(root)
    return root # No changes to the specified subtree if balanced

  def __recursive_insert(self, root, value):
    if root == None: # Base case
      return Binary_Search_Tree.__BST_Node(value)
    else: # Recursive case
      if value < root.value:
        root.left = self.__recursive_insert(root.left, value) # Traverse into the left child
      elif value > root.value:
        root.right = self.__recursive_insert(root.right, value) # Traverse into the right child
      else: # value == root.value
        raise ValueError('{} already contained in tree'.format(value))
      root = self.__balance(root)
      root.update_height()
      return root

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError.
    self.__root = self.__recursive_insert(self.__root, value)

  def __find_min(self, root):
    while root.left != None:
      root = root.left
    return root

  def __recursive_remove(self, root, value):
    if root == None:
      raise ValueError('{} not contained in tree'.format(value))
    if root.value == value: # Base case
      if root.right == None:
        return root.left # Replace the specified value with the left child (or None)
      elif root.left == None:
        return root.right # Replace the specified value with the right child
      else: # If the specified value has two children
        min_node = self.__find_min(root.right) # Find the minimum value of the right subtree
        root.right = self.__recursive_remove(root.right, min_node.value) # Remove the minimum value
        root.value = min_node.value # Replace the specified value with the minimum value
        root.update_height()
        return root
    else: # Recursive case
      if value < root.value:
        root.left = self.__recursive_remove(root.left, value) # Traverse into the left child
      else: # value > root.value
        root.right = self.__recursive_remove(root.right, value) # Traverse into the right child
      if root != None: # For cases when the specified value is a leaf node
        root = self.__balance(root)
        root.update_height()
      return root

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead.
    self.__root = self.__recursive_remove(self.__root, value)
    if self.__root != None:
      self.__root = self.__balance(self.__root)
      self.__root.update_height()
      
  def __in_order_list(self, root):
    values = []
    if root.left != None: # Left child
      values.extend(self.__in_order_list(root.left))
    values.append(root.value) # Parent
    if root.right != None: # Right child
      values.extend(self.__in_order_list(root.right))
    return values

  def to_list(self):
    if self.__root == None: # Check whether tree is empty
      return []
    else:
      return self.__in_order_list(self.__root)

  def __in_order_traversal(self, root):
    output = ''
    if root.left != None:
      output = output + str(self.__in_order_traversal(root.left))
    output = output + str(root.value) + ', '
    if root.right != None:
      output = output + str(self.__in_order_traversal(root.right))
    return output
  
  def __pre_order_traversal(self, root):
    output = ''
    output = output + str(root.value) + ', '
    if root.left != None:
      output = output + str(self.__pre_order_traversal(root.left))
    if root.right != None:
      output = output + str(self.__pre_order_traversal(root.right))
    return output
    
  def __post_order_traversal(self, root):
    output = ''
    if root.left != None:
      output = output + str(self.__post_order_traversal(root.left))
    if root.right != None:
      output = output + str(self.__post_order_traversal(root.right))    
    output = output + str(root.value) + ', '
    return output

  def __order_output(self, order):
    if self.__root == None: # Check whether tree is empty
      return '[ ]'
    else:
      output = order(self.__root)
      return '[ ' + output[:len(output)-2] + ' ]'

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ].
    return self.__order_output(self.__in_order_traversal)

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ].
    return self.__order_output(self.__pre_order_traversal)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ].
    return self.__order_output(self.__post_order_traversal)
    
  def get_height(self):
    # Return an integer that represents the height of the tree.
    # Assume that an empty tree has height 0 and a tree with one
    # node has height 1.
    if self.__root == None: return 0 # If tree is empty
    else: return self.__root.height # If tree not empty

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass

