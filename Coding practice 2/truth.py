"""
Truth
Write a program that completes and prints out the following truth table.
Recall from this module that a truth table contains all of the possible
combination of p, q, and r. You should use the |, -, and + to build the
lines in the table.

p	q	r	A	B
F	F	F	?	?
F	F	T	?	?
F	T	F	?	?
F	T	T	?	?
T	F	F	?	?
T	F	T	?	?
T	T	F	?	?
T	T	T	?	?
"""


def truthTable(expression,inputs=2):
    print("Boolean Expression:")
    print("  X = " + expression.upper())
    expression = expression.lower()
    expression = expression.replace("and","&")
    expression = expression.replace("xor","^")
    expression = expression.replace("or","|")
    expression = expression.replace("not","~")
    print("\nTruth Table:")
    if inputs==2:
        print("  -------------")
        print("  | p | q | r |")
        print("  -------------")

        for a in range(0,2):
            for b in range(0,2):
                x = eval(expression)
                print("  | " + str(a) + " | " + str(b) + " | "
                      + str(x) + " |" )
                print("  -------------")

    elif inputs==3:
        print("  -----------------")
        print("  | p | q | r | X |")
        print("  -----------------")

        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    x = eval(expression)
                    print("  | " + str(a) + " | " + str(b) + " | "
                          + str(c) + " | " + str(x) + " |" )
                    print("  -----------------")

    elif inputs==4:
        print("  ---------------------")
        print("  | p | q | r | D | X |")
        print("  ---------------------")

        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    for d in range(0,2):
                        x = eval(expression)
                        print("  | " + str(a) + " | " + str(b) + " | "
                              + str(c) + " | " + str(d) + " | "
                              + str(x) + " |" )
                        print("  ---------------------")

expression = "A AND NOT (B XOR C)"
truthTable(expression,3)

if __name__ == "___main__":
    main()

# not(p and (q or not r))['(p and q) or not r',
# 'not(p and (q or not r))']
