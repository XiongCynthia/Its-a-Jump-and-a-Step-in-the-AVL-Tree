# It's a Jump and a Step in the AVL Tree

[Binary_Search_Tree.py](https://github.com/XiongCynthia/Its-a-Jump-and-a-Step-in-the-AVL-Tree/blob/main/Binary_Search_Tree.py) is an implementation of a self-balancing binary search tree, an AVL tree, that can store and process any object that uses the built-in comparison methods, as well as return the in-fix, pre-fix, and post-fix expression of the tree. 

---

## Performance Analysis

Both the **insert_element** and **remove_element** methods each have a recursion method: **\_\_recursive_insert** and **\_\_recursive_remove**, respectively, which are for traversing through the BST. A larger tree entails more values to traverse through for reaching specific values or locations, and thus longer runtimes. However, since the tree would always be balanced, every complete traversal involve passing though some values instead of all of them, thus operating in logarithmic time. The methods may traverse to some location, be it at the bottom of the tree or somewhere halfway down, then work back upwards to complete some constant time operations (which are explained later), resulting in logarithmic time (i.e., O(log n) + O(log n) => O(log n)).

The \_\_recursive_remove method can have two additional traversals in cases where the node of the specified value to remove has two children. To maintain proper structure, the method locates the minimum value in the right child to replace the removing value. To accomplish this, **\_\_find_min** is called to get the node of the minimum value by traversing left from the right child for as many times as possible, operating in logarithmic time. And then another \_\_recursive_remove is called to remove the node from the original location, which also operates in logarithmic time. The result is still a logarithmic time operation.

After inserting or removing a value, the \_\_recursive_insert and \_\_recursive_remove methods work backwards through the values they pass through to complete some constant time operations. One of them is the **update_height** method for adjusting set values for height, which only consists of assignment, if-elif statements, and comparisons.

There is also the **\_\_balance** method, used to check balance factors and perform rotations to preserve the balance of the tree. Balance factors are calculated with the **\_\_find_balance** method, which consists of assignment, if statements, comparisons, and arithmetic, thus operating in constant time. When a subtree is deemed unbalanced by the balance factor, the \_\_balance method performs rotations using the **\_\_rotate_left** and **\_\_rotate_right** methods, which are only comprised of assignment and the update_height method, which are also all constant time operations.

Since the \_\_balance method and all its operations are in constant time, it does not affect the runtime of the \_\_recursive_insert and \_\_recursive_remove methods in any significant way, and so logarithmic time is maintained. By extension, insert_element and remove_element also operate logarithmic time since they only use those methods and some constant time operations (i.e., assignments, if statement, comparison, \_\_balance, and update_height).
