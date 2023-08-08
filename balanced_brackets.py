def is_balanced(str):
    stack = []
    for char in str:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    print(is_balanced("{[()]}"))
    print(is_balanced("{[(])}"))
    print(is_balanced("{{[[(())]]}}"))