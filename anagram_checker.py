def are_anagrams(a: str, b: str) -> bool:
    a = a.lower()
    b = b.lower()

    if len(a) != len(b):
        return False

    count = {}

    for char in a:
        count[char] = count.get(char, 0) + 1

    for char in b:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("hello", "world"))
