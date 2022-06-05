"""
Coding practice -- Module 3
1. Line
Write a function called line that returns a string that consists of 50
copies of the x character.
"""


def line(string):
    copy = ""
    for i in range(len(string)):
        if string[i] == "x":
           return string[i] * 50


def main():
    print(line("xie"))


if __name__ == "__main__":
    main()
