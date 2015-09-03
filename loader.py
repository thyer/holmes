__author__ = 'trent'

import re

class Corpus:

    def __init__(self, path):
        self.dictionary = dict()
        self.load(path)
        self.prev = None
        self.current = None

    def load(self, path):
        with open(path) as text_file:
            for line in text_file:
                self.prev_word = None
                self.current = None
                for word in line.split():
                    word_cleaned = re.sub(r'\W+', '', word.upper())
                    if not self.dictionary.__contains__(word_cleaned):
                        self.current = Node(word)
                        self.current.prev = self.prev_word
                        value = []
                        self.dictionary[word_cleaned] = value
                        value.append(self.current)
                    else:
                        self.current = Node(word)
                        self.current.prev = self.prev_word
                        self.dictionary[word_cleaned].append(self.current)

                    if self.prev_word:
                        self.prev_word.next = self.current
                    self.prev_word = self.current

    def search(self, token):
        output = "Search Results: "
        token = re.sub(r'\W+', '', token.upper())
        if not self.dictionary.__contains__(token):
            output += ("\n\tWORD NOT FOUND")
            return output
        linked_list = self.dictionary[re.sub(r'\W+', '', token.upper())]
        for item in linked_list:
            output += "\n\t" + (self.get_KWIC(item))
        return output

    def get_KWIC(self, item):
        output = ""
        temp = item
        
        # Add up to five words before key word
        for i in range(4):
            if temp.prev:
                output = temp.prev.text + " " + output
                temp = temp.prev
                
        # Add key word
        output += item.text.upper()
        
        # Add up to five words following key word
        for i in range(4):
            if item.next:
                output += " " + item.next.text
                item = item.next

        return output


class Node:
    def __init__(self, word):
        self.text = word
        self.prev = None
        self.next = None


print("Welcome to HOLMES")
corpus = Corpus("holmes")
input = ""
while not input == "QUIT":
    if not input == "":
        print(corpus.search(input) + "\n\n\n\n\n")
    print("Enter a search term. Type \'QUIT\' to end the program")
    input = raw_input('--> ')
