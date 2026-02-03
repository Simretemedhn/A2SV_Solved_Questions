def swap_case(s):
    word = ""
    for char in s:
        if char.islower():
            word += char.upper()
        elif char.isupper():
            word += char.lower()
        else:
            word += char
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
