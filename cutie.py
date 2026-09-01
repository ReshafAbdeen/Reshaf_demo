import collections
import re


class TextAnalyzer:

    def __init__(self, text):
        self.text = text
        self.words = re.findall(r"\b\w+\b", text.lower())

    def word_count(self):
        return len(self.words)

    def char_count(self, ignore_spaces=True):
        if ignore_spaces:
            return len(self.text.replace(" ", ""))
        return len(self.text)

    def top_words(self, n=5):
        counts = collections.Counter(self.words)
        return counts.most_common(n)

    def average_word_length(self):
        if not self.words:
            return 0
        total_chars = sum(len(word) for word in self.words)
        return round(total_chars / len(self.words), 2)


sample_text = "Python is powerful, readable, and fun. Python makes coding clear and intuitive!"
analyzer = TextAnalyzer(sample_text)

print(f"Total Words: {analyzer.word_count()}")
print(f"Total Chars (no spaces): {analyzer.char_count()}")
print(f"Average Word Length: {analyzer.average_word_length()}")
print(f"Top 3 Most Frequent Words: {analyzer.top_words(3)}")