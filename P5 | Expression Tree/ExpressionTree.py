#  File: ExpressionTree.py
#  Name: Patrick Pichardo

import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Stack Class - DO NOT CHANGE
# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
# You do not need to make changes to this class.
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
# You need to make a lot f changes to this class!
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
        current = self.root     # root 4 base case
        stack = Stack()         # create stack ig
        for token in expr.split():
            if token == '(':                # If the token is an opening parenthesis
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            elif token in operators:        # If the token is an operator
                current.data = token
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
            elif token == ')':              # If the token is a closing parenthesis
                if not stack.is_empty():
                    current = stack.pop()
            else:
                current.data = token    # if its a number we add the token to current data
                current = stack.pop()
                
    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):
        if current is None:          # base case
            return None              # return none if current is none
        
        l = self.evaluate(current.lChild)   # eval left of sub tree
        r = self.evaluate(current.rChild)   # eval right of sub tree
        if current.data in operators:
            return float(operation(current.data, l, r)) # Calls operation funcitno on the operators 
        else:
            return current.data

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        if current is None:         # return none if current is none
            return None             # base case

        l = self.pre_order(current.lChild)  # recurse eval o right of sub tree
        r = self.pre_order(current.rChild)  # recurse eval o left of sub tree
        if l is None or r is None:
            return current.data             # either subtree is None, return the current node's data
        else:
            return current.data + " " + l + " " + r # Combine the current node's data w left N right subtree results

    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        if current is None:         # base case
            return None             # return none if current is none
        
        l = self.post_order(current.lChild)  # recurse eval o left of sub tree
        r = self.post_order(current.rChild)  # recurse eval o right of sub tree
        if l is None or r is None:
            return current.data + " "
        else:
            return l + r + current.data + " "   # Combine left and right subtree results with the current node's data

def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()
    
    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
