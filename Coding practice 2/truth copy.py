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


def main():
    # A = (p and q) or not r
    # B = not(p and (q or not r))
    p = str(input("Enter T or F for p: "))
    q = str(input("Enter T or F for q: "))
    r = str(input("Enter T or F for r: "))
    var = ""
    mpd = ""
    amp = ""
    abc = ""
    ssd = ""
    if r == "T":
        var = "F" # when r = T, -r = F
    else:
        var = "T" # when r = F, -r = T
    if (p == "T") and (q == "T"):
        mpd = "T"
    else:
        mpd = "F"
    if (mpd == "F") and (var == "F"):
        amp = "F"
        print("A = (p and q) or not r is F")
    else:
        amp = "T"
        print("A = (p and q) or not r is T")
    if (q == "T") or (var == "T"):
        abc = "T"
    else:
        abc = "F"
    if (p == "T") and (abc == "T"):
        ssd = "T"
    else:
        ssd = "F"
    if ssd == "T":
        print("B = not(p and(q or not r)) is F")
    else:
        print("B = not(p and(q or not r)) is T")


if __name__ == "__main__":
    main()
