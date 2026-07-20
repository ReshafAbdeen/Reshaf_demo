# Word Frequency Counter

import string
def count_words(text):
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
print("--- Word Frequency Counter ---")
while True:
    print("\nEnter a sentence/paragraph (or type 'quit' to exit):")
    user_input = input("> ")
    if user_input.lower().strip() == 'quit':
        break
    if not user_input.strip():
        print("Please enter some text!")
        continue
    frequencies = count_words(user_input)
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    print("\nWord Frequencies:")
    for word, count in sorted_freq:
        print(f"'{word}': {count} times")
print("Exiting Word Counter...")
# Word counter session closed.
print("Goodbye!")