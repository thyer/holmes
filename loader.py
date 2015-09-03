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
                self.prev = None
                self.current = None
                for word in line.split():
                    if not self.dictionary.__contains__(word):
                        self.current = Node(word)
                        value = []
                        self.dictionary[re.sub(r'\W+', '', word.upper())] = value
                        value.append(self.current)
                    else:
                        self.current = Node(word)
                        self.dictionary[word.upper()].append(self.current)

                    if self.prev:
                        self.prev.next = self.current
                        self.prev = self.current

    def search(self, token):
        output = []
        output.append("Search Results: ")
        linked_list = self.dictionary[token.upper()]
        if not linked_list:
            output.append("\tWORD NOT FOUND")
            return output
        for item in linked_list:
            print(item.next)
            output.append(self.get_KWIC(item))
        return output

    def get_KWIC(self, item):
        output = ""
        output += item.text.upper()


class Node:
    def __init__(self, word):
        self.text = word
        self.prev = None
        self.next = None


count = 0
corpus = Corpus("holmes")
print(corpus.search("AMUSING"))
print(str(corpus.dictionary))