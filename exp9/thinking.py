import re


def count_word_occurrences(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  # Read the file and convert to lowercase
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    words = re.findall(r'\b\w+\b', text)  # Find all words in the text

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    filename = 'text.txt'
    with open(filename, 'w') as f:
        f.write("This is a test. This is only a test.")

    count_word_occurrences(filename)
