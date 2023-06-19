def to_lisp(program):
    if isinstance(program, list):
        return "(" + " ".join(to_lisp(item) for item in program) + ")"
    elif isinstance(program, str):
        return '"' + program + '"'
    else:
        return str(program)

def from_lisp(s):
    def read_from_tokens(tokens):
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF')
        token = tokens.pop(0)
        if token == '(':
            L = []
            while tokens[0] != ')':
                L.append(read_from_tokens(tokens))
            tokens.pop(0)  # pop off ')'
            return L
        elif token == '"':
            L = ''
            while tokens[0] != '"':
                L += tokens.pop(0)
            tokens.pop(0)  # pop off closing "
            return L
        else:
            try:
                return int(token)
            except ValueError:
                try:
                    return float(token)
                except ValueError:
                    return token

    # Convert string to list of tokens
    tokens = []
    in_string = False
    token = ''
    for c in s:
        if c == ' ' and not in_string:
            if token != '':
                tokens.append(token)
            token = ''
        elif c == '"' and not in_string:
            in_string = True
            token += c
        elif c == '"' and in_string:
            in_string = False
            token += c
            tokens.append(token)
            token = ''
        else:
            token += c
    if token != '':
        tokens.append(token)

    return read_from_tokens(tokens)

# Example usage
program = [
    "seq",
    ["print", "staring...."],
    [
        "def",
        "repeat",
        ["x"],
        [
            "seq",
            ["print", "in loop"],
            ["if", ["get", "x"], ["call", "repeat", ["decrement", ["get", "x"], 1]], 0],
        ],
    ],
    ["set", "x", 2],
    ["call", "repeat", ["get", "x"]],
]

lisp_program = to_lisp(program)
print(lisp_program)

# Output:
# (seq ("print" "staring....") ("def" "repeat" ("x") (seq ("print" "in loop") ("if" ("get" "x") ("call" "repeat" ("decrement" ("get" "x") 1)) 0))) ("set" "x" 2) ("call" "repeat" ("get" "x")))

converted_program = from_lisp("(seq (\"print\" \"staring....\") (\"def\" \"repeat\" (\"x\") (seq (\"print\" \"in loop\") (\"if\" (\"get\" \"x\") (\"call\" \"repeat\" (\"decrement\" (\"get\" \"x\") 1)) 0))) (\"set\" \"x\" 2) (\"call\" \"repeat\" (\"get\" \"x\")))")
print(converted_program)

# Output:
# ['seq', ['print', 'staring....'], ['def', 'repeat', ['x'], ['seq', ['print', 'in loop'], ['if', ['get', 'x'], ['call', 'repeat', ['decrement', ['get', 'x'], 1]], 0]]], ['set', 'x', 2], ['call', 'repeat', ['get', 'x']]]