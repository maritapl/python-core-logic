def is_palindrome(text: str) -> bool:
    cleaned = ""

    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("Racecar"))
    print(is_palindrome("Hello"))
