# CS-313-E-Data-Structures

All the mini projects for CS 313E at UT Austin at display different Data Structures: 
  Each project file contains a larger overview on what the project needed. 
  For a brief description w/ the DSA used scroll down

## Table of Contents
- P1 Spiral
- P2 Employee Salaries
- P3 Working Hard
- P4 Josephus Problem
- P5 Expression Tree
- P6 BST Cipher
- P7 BST and AVL Tree


## P1 Spiral

#### Summary
Reads the input size for the spiral matrix, adjusting it to be odd if it's even.
Generats the spiral matrix by populating a 2D list with decreasing numbers from the matrix's size squared, spiraling inward.
Reads additional inputs, which are numbers for which the script calculates the sum of all adjacent numbers within the spiral matrix.
Outputting these sums or error messages for invalid inputs.
The main function reads the input, creates the spiral, and calculates the adjacent sums.

#### Data Strucure and Algorithms
2D List/Array: It's used to store the spiral numbers and to perform lookups and manipulations.
Simple iterative and conditional constructs are used for creating the spiral pattern and for finding the sums of adjacent numbers.

## P2 Employee Salaries

#### Summary
This script defines an employee class hierarchy for a company's payroll system. 
It includes a base Employee class and subclasses for 
Permanent_Employee, Manager, Temporary_Employee, Consultant, and Consultant_Manager, 
each with role-specific salary calculations. 

#### Data Strucure and Algorithms
#### Class Inheritance:
- A fundamental OOP concept, a method of structuring objects.
#### Encapsulation:
- Utilizing private attributes and public getter/setter methods.
#### Polymorphism: 
- Overriding the __str__ and cal_salary methods in derived classes.

## P3 Working Hard

#### Summary
This script calculates how many lines of code a programmer can write before needing coffee 
and eventually falling asleep due to decreased productivity. 

#### Data Strucure and Algorithms
#### Recursion: 
- To compute the total lines of code before sleep due to productivity drop after each coffee.
#### Linear Search: 
- To find the initial count of lines to write before the first coffee break through sequential checking.
#### Binary Search: 
- To determine the initial line count more efficiently by dividing the search range in half each time.

## P4 Josephus Problem

#### Summary
The code implements the Josephus problem using a circular linked list data structure. This problem is a theoretical puzzle where soldiers are standing in a circle and every k-th soldier is eliminated until one remains. 

#### Data Strucure and Algorithms
#### Circular Linked List: 
The data structure used is a circular linked list where each node (Link) represents a soldier. This list has no end as the last node points back to the first, creating a circular structure.

## P5 Expression Tree

#### Summary
This code is designed to parse, construct, and evaluate expressions in a binary tree structure, 
known as an expression tree. 
It includes functionality to print the expressions in prefix and postfix notation.

#### Data Strucure and Algorithms
#### Stack:
A traditional stack is used for keeping track of nodes when building the expression tree from an infix expression.

#### Binary Tree: 
The expression tree is a binary tree with nodes that represent either operators or operands. Each node can have up to two children, which can themselves be operators or operands.

## P6 BST Cipher

#### Summary
This script defines a binary search tree (BST) cipher for encrypting and decrypting messages using a key.

#### Data Strucure and Algorithms
#### Binary Search Tree (BST):
Algos: BST Insertion, BST Search, Traversal, String Manipulation, Recursion, Tree-based Encryption, Tree-based Decryption. Input Sanitization, Command Parsing, Debugging, Conditional Logic

## P7 BST and AVL Tree

#### Summary
This code defines the implementation of a binary search tree (BST) 
and can be extended to support an AVL tree (a self-balancing binary search tree).

#### Data Strucure and Algorithms
#### Binary Search Tree (BST):
Represents both BST and AVL
Algos: insert, rightRotate, leftRotate, rebalance, height, range, levelOrderTraversal, leftSideView, leafNodeSum, printTree, printTreeInfo

