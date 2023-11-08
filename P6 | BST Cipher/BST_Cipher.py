#  File: BST_Cipher.py
#  Name: Patrick Pichardo
#  UT EID: pjp953

import sys

# One node in the BST Cipher Tree
class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None

# The BST Cipher Tree
class Tree:
    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        self.root = Node(None)
        clean_key = self.clean(key)
        for ch in clean_key.lower():   # a) make all characters from file lowercase before creating tree b) ignore all invalid characters (not a letter or space)
            self.insert(ch)            # True condition between a - z lowercased / True condition if a space | # if you are seeing this it took me 1.5 hours to realize there were helper functions
        return

    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        node = Node(ch)             # node lol 
        if self.root.ch == None:    # base case, empty tree
            self.root = node

        temp = self.root
        parent = self.root
        while temp != None:         # Tree traversal till we find a valid location
            parent = temp           # update parent to get the last location before a valid locatoin
            if ch == ' ' and temp.ch != ' ':    
                temp = temp.left    # ch is space & temp node's ch is not space, move to the left
            elif temp.ch > ch:                  
                temp = temp.left    # temp node's ch > the ch to be inserted, move to the left
            elif temp.ch < ch:                  
                temp = temp.right   # temp node's ch < the ch to be inserted, move to the right
            else:                  
                return              # character is in the tree, return
        if ch < parent.ch:          
            parent.left = node      # Insert ch to left of parent
        elif ch > parent.ch:        
            parent.right = node     # insert ch to right of parent
        else:
            return

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        encryptedMessage = ""
        i = 0
        while i < len(message):
            if self.isValidCh(message[i]):
                encryptedMessage += self.encrypt_ch(message[i]) + "!"
            i += 1
        return encryptedMessage[:-1]       # removes trailing "!"

    # Encrypts a single character
    def encrypt_ch(self, ch):
        code = ""
        temp = self.root
        if ch == temp.ch:       # Originally had this in the loop, was messing up my code, realized it'd work better as a base case
            code += "*"
        while temp != None:        # Traverse tree until None
            if ch == temp.ch:       # I thinking of making this the while loop break but this code worked so im not touching it. 
                break
            elif ch < temp.ch:      
                code += "<"
                temp = temp.left
            elif ch > temp.ch:
                code += ">"
                temp = temp.right
        else:
            code = ch           # Character not found in the tree, return the character itself
        return code

    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):
        decryptedMessage = ""
        substrng = ""
        i = 0
        while i < len(codes_string):
            cd = codes_string[i]
            if cd == "!":
                decryptedMessage += self.decrypt_code(substrng)
                substrng = ""
            else:
                substrng += cd
            i += 1
        if substrng:
            decryptedMessage += self.decrypt_code(substrng)
        return decryptedMessage

    # Decrypts a single code
    def decrypt_code(self, code):
        if not code:            # if empty or what ever
            return ""
        temp = self.root

        if code == "*":         # Base case if the first thang is *
            return temp.ch
        
        for char in code:       # just traversal loop till we get to end
            if char == "<" and temp.left != None:       # those pesky edge cases
                temp = temp.left
            elif char == ">" and temp.right != None:      # those pesky edge cases
                temp = temp.right
            else:
                return ""
        return temp.ch          # return that character

    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False

def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
