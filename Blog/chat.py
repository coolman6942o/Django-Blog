from collections import Counter
import nltk
nltk.download('punkt')

# Load Text
with open('document.txt', 'r') as file:
    text = file.read()

# Tokenize
words = nltk.word_tokenize(text)
sentences = nltk.sent_tokenize(text)

# Analyze
word_count = len(words)
sentence_count = len(sentences)
unique_words = len(set(words))
lexical_diversity = unique_words / word_count

# Output
print(f"Word Count: {word_count}")
print(f"Sentence Count: {sentence_count}")
print(f"Unique Words: {unique_words}")
print(f"Lexical Diversity: {lexical_diversity:.2f}")

# Top Words
top_words = Counter(words).most_common(10)
print("Top Words:", top_words)
