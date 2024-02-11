import matplotlib.pyplot as plt

def graph_word_frequency (word_frequencies):
    # Assuming `word_frequencies` is your dictionary of word frequencies
    word_counts = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    words, frequencies = zip(*word_counts[:50])

    plt.figure(figsize=(10, 8))  # Optional: Adjusts the size of the graph
    plt.bar(words, frequencies)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)  # Rotate the words on the x-axis to prevent overlap
    plt.title('Top Word Frequencies')
    plt.show()
