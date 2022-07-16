# MarkleTrees
Cyber Security project of Shandong University (holder:Jin Cuifu)

# Task_List
• Implement Merkle Tree as of RFC 6962 in any programming language that you prefer.  
• Construct a merkle tree with 100k leaf nodes.  
• Construct the existence (inclusion) proof for randomly chosen leaf node & verify the proof.  

# Implementation_Process
1. Implement Merkle Tree as of RFC 6962 in any programming language that you prefer  
For the implementation of this process, first of all, the following explanations are made:  
(1) The Merkle tree is stored in the form of a two-dimensional list:  
1）. Write the hash value of the same layer into a list according to the sequence of data  
2）. Record the Hash list of each layer and write it into the general list in depth order. And take this general list as the form of storing Merkle tree.  
(2) In the implementation process, we determine the parent-child node relationship of data through the subscript of the list.  

## Implement the process
(1) Declare a two-dimensional list and calculate the tree depth and the number of leaf nodes:  
(2) Calculate the data hash value and write it to the leaf node.  
(3) For every two child nodes, the hash value after the addition is calculated and written to the list of the parent node. And for the nodes in the same layer, continue this process to generate the nodes of the next layer (parent node layer) Merkle tree.  
(4) For the last node in the layer with odd number of nodes, it is written directly to the next layer (parent node layer).  
(5) Continue the process of steps (3) and (4) and cycle the depth of the tree calculated in step (1) to complete the generation process of Merkle tree.  
(6) Carry out the experimental test: input the test data, call the createtree() function, and print. Then the Merkle tree will be printed, and the same layer is in the same list.  

## Construct a merkle tree with 100k leaf nodes
(1) Generate 100k data;  
(2) Call implementation 1 The createtree() function in is OK;  
(3) Test, generate the data, generate the tree, and then print the tree.  

## Construct the existence proof for randomly chosen leaf node & verify the proof.
(1) Introduction:
To prove that a node is in the tree, you only need to give the adjacent siblings of the node and its parent node. The verification idea is to verify whether the given nodes form a tree according to the given form, and whether the root node is the same as the root node of the tree to be verified. For the form of proof given, because it is also a Merkle tree (there are at most two nodes in each layer), implementation 1 is adopted The same storage form in (two-dimensional list storage).
(2) For the node to be proved, find out whether its hash value is in the tree and its position in the tree (find its subscript n).
(3) Then, its subscript determines whether it is the even node or the odd node. If it is the odd number: first check whether it is the last node. If so, do not operate and enter the next cycle (that is, there is no brother node of this node in this layer. In other words, in the logic diagram of Merkle tree, this node is not located in this layer, but on a higher layer.) On the no side, write its right node (the node with subscript +1) into a list together with this node. If it is the even number: write its left node (the node with subscript -1) into a list together with this node.
(4) Call the program in (3) continuously, and finally put the root node into the tree.
(5) When proving, first check the hash value of the node to be proved and whether the root node of the tree is in the given evidence;
(6) Then check whether the hash value of the sum of child nodes in each layer of the tree given as evidence is its parent node (that is, check whether it is a Merkle tree). Finally, whether the child nodes of the root node can generate the root node is tested separately: if it can pass all the tests, it indicates that the detection node is indeed in the tree of the given root node.

# Done...
