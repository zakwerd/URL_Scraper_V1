from collections import Counter
import re

def count_word_frequencies(text):
    # Remove punctuation and make lowercase
    text = re.sub(r'\W+', ' ', text.lower())
    words = text.split()
    word_counts = Counter(words)
    return word_counts

def read_scraped_text(filename="scraped_text.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_word_frequencies_to_file(word_counts, filename="url_data.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in word_counts.most_common():
            file.write(f"{word}: {count}\n")
