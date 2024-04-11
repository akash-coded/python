def filter_stop_words(text):
    stopwords = set(["the", "am", "is", "to",
                    "are", "and", "with", "of"])

    text = text.lower()

    word_list = set(text.split(" "))
    print(word_list)

    filtered_words = [
        word for word in word_list if word not in stopwords]
    print(filtered_words)
    print()


def main():
    documents = [
        "John likes to play the football",
        "The quick brown fox jumps over the lazy dog",
        "I am the third document",
        "Harry! Harry! Did you put your name in the goblet of fire?",
        "And I am Iron Man"
    ]

    for document in documents:
        filter_stop_words(document)


if __name__ == "__main__":
    main()
