class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, wlist):
        new_array = []
        for words in wlist:
           if sorted([letter for letter in self.word]) == sorted([letter for letter in words]):
                new_array.append(words)
        return new_array
            

seth = Anagram("listen")
print(seth.match(['enlists', 'google', 'inlets', 'silent', 'banana']))

