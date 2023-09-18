########################################################
### Algorithm for valid parentheses problem 
########################################################
def valid_parentheses(s):
    key_dictionary = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    stack = []

    for bracket in s:
        if bracket in key_dictionary.keys():
            stack.append(key_dictionary[bracket])
        
        else:
            if stack == []:
                return False
            if stack.pop() != bracket:
                return False
        
    if stack != []:
        return False
    
    return True

