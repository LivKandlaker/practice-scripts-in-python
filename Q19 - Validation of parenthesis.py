def isValid(s):
    # 1) First we check if the string include only parenthesis. we use an allowed chars list and all function
    allow_chars = "()[]{}"
    bool_answer = all(char in allow_chars for char in s)

    # 2) Second we check if for open char exist a close char.
    for i in range(len(s)):
        if s[i] == "(" :
            if i == len(s)-1:
                return False
            elif s[i + 1] != ")":
                return False
        elif s[i] == "[":
            if i == len(s)-1:
                return False
            elif s[i + 1] != "]":
                return False
        elif s[i] == "{" :
            if i == len(s)-1:
                return False
            elif s[i + 1] != "}":
                return False
        elif s[0] == "]" or s[0] == ")" or s[0] == "}":
            return False
        elif s[i] == "]" and i != 0:
            if s[i - 1] != "[":
                return False
        elif s[i] == "}" and i != 0:
            if s[i - 1] != "{":
                return False
        elif s[i] == ")" and i != 0:
            if s[i - 1] != "(":
                return False

    return bool_answer


string_parenthesis = "[](){}"
answer = isValid(string_parenthesis)
print(answer)
