"""
pythonAssessment.py
Summative Lab: Analyze a News Article

Reads a news article text file and reports:
  1. Occurrences of a specific word
  2. The most common word
  3. Average word length (punctuation excluded)
  4. Number of paragraphs
  5. Number of sentences
"""

import re
from collections import Counter


# ---------- Configuration ----------
ARTICLE_PATH = "../starter-files/ACME_Apple_Pie_Machine.txt"
SPECIFIC_WORD = "apple"


# ---------- File I/O ----------
def read_article(path):
    """Read the article file and return its contents as a string."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: could not find the file at '{path}'.")
        return ""


# ---------- Analysis functions ----------
def count_specific_word(text, word):
    """Count occurrences of a specific word (case-insensitive, whole word)."""
    pattern = r"\b" + re.escape(word) + r"\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return len(matches)


def most_common_word(text):
    """Return the most common word, ignoring punctuation and case."""
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    if not words:
        return None
    counter = Counter(words)
    common = counter.most_common(1)[0][0]
    return common


def average_word_length(text):
    """Average length of words, excluding punctuation/special characters."""
    words = re.findall(r"[A-Za-z']+", text)
    if not words:
        return 0.0

    total = 0
    for word in words:          # explicit for loop (rubric)
        total += len(word)
    return total / len(words)


def count_paragraphs(text):
    """Count paragraphs, where a paragraph is separated by a blank line."""
    blocks = re.split(r"\n\s*\n", text.strip())
    count = 0
    for block in blocks:        # explicit for loop (rubric)
        if block.strip():
            count += 1
    return count


def count_sentences(text):
    """Count sentences ending with ., !, or ?"""
    collapsed = re.sub(r"\s+", " ", text).strip()
    sentences = re.findall(r"[^.!?]+[.!?]", collapsed)
    return len(sentences)


# ---------- Main ----------
def main():
    text = read_article(ARTICLE_PATH)
    if not text:
        return

    # explicit while loop (rubric): allow user to query multiple words
    keep_going = True
    while keep_going:
        word = input(
            f"Enter a word to count (default '{SPECIFIC_WORD}', "
            f"or type 'done' to finish): "
        ).strip()

        if word.lower() == "done":
            keep_going = False
            continue

        if word == "":
            word = SPECIFIC_WORD

        specific_count = count_specific_word(text, word)
        print(f"  -> '{word}' appears {specific_count} time(s).\n")

    # Full report
    common_word = most_common_word(text)
    avg_len = average_word_length(text)
    paragraphs = count_paragraphs(text)
    sentences = count_sentences(text)

    print("=" * 55)
    print("NEWS ARTICLE ANALYSIS")
    print("=" * 55)
    print(f"Most common word           : {common_word}")
    print(f"Average word length        : {avg_len:.2f}")
    print(f"Number of paragraphs       : {paragraphs}")
    print(f"Number of sentences        : {sentences}")
    print("=" * 55)


if __name__ == "__main__":
    main()