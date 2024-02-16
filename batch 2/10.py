class PyWords:
    def __init__(self, process_words):
        self.process_words = process_words

    def words_with_length(self, val):
        return [word for word in self.process_words if len(word) == val]

    def starts_with(self, val):
        return [word for word in self.process_words if word.startswith(val)]

    def palindromes(self):
        return [word for word in self.process_words if word == word[::-1]]

st = input("Enter a list of words").split()
ob = PyWords(st)
print(ob.words_with_length(3))
print(ob.starts_with('a'))
print(ob.palindromes()) if len(ob.palindromes()) > 0 else print("No palindrome")
    
