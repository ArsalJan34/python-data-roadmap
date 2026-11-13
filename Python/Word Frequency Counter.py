import string

def count_words(text):
    trans_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = text.translate(trans_table).lower()
    words = cleaned_text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_n(counts, n):
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:n]

def print_table(top_words):
    """Prints the results as a neat aligned table."""
    print(f"{'Word':<15} | {'Count':<5}")
    print("-" * 25)
    for word, count in top_words:
        print(f"{word:<15} | {count:<5}")

if __name__ == "__main__":
    sample_text = (
        "Hello, world! Hello everyone. Welcome to the world of Python, "
        "python programming. Data science and data analysis are fun."
    )
    word_counts = count_words(sample_text)
    top_5_words = top_n(word_counts, 5)
    print_table(top_5_words)
