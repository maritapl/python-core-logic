def is_balanced(expression: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    test_cases = ["()[]{}", "([{}])", "(]", "((()))", "("]

    for case in test_cases:
        print(case, "->", is_balanced(case))
