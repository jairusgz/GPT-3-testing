# Functions fully generated by Github Copilot using the name of the function as prompt.

def CYK(grammar, sentence):
    """
    CYK algorithm for parsing a sentence.
    """
    # Create a table of size (len(sentence) + 1) x (len(sentence) + 1)
    table = [[[None for _ in range(len(sentence) + 1)] for _ in range(len(sentence) + 1)] for _ in
             range(len(sentence) + 1)]
    # Fill the table with the terminals
    for i in range(len(sentence)):
        table[i][i][0] = sentence[i]
    # Fill the table with the non-terminals
    for i in range(len(sentence)):
        for j in range(i + 1, len(sentence) + 1):
            for k in range(i, j):
                for rule in grammar:
                    if table[i][k][0] == rule[0] and table[k][j][0] == rule[2]:
                        table[i][j][0] = rule[1]
                        break
    # Fill the table with the productions
    for i in range(len(sentence)):
        for j in range(i + 1, len(sentence) + 1):
            for k in range(i, j):
                for rule in grammar:
                    if table[i][k][0] == rule[0] and table[k][j][0] == rule[2]:
                        table[i][j][0] = rule[1]
                        break
    # Check if the sentence is in the language
    if table[0][len(sentence)][0] is None:
        return False
    else:
        return True


def fibonacci(n):
    """
    Returns the nth fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
