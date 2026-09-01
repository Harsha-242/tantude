text = "apple banana apple cherry banana apple"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word counts:", word_count)
