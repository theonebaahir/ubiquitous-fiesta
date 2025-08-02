class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Split the string into words, reverse the list, then join back
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
s = StringReverser("Python is a powerful language")
print("Original:", s.text)
print("Reversed:", s.reverse_words())
