def word_frequency(text: str) -> dict:
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    text = "Python is great and Python is powerful"
    print(word_frequency(text))
