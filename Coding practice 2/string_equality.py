"""
String Equality
Write a program that reads in a word from the keyboard and prints
"Hi, how are you" and "Done" if someone enters the word "Hi"
(capitalization matters). Otherwise it just prints "Done"
"""
greeting = input("")


def main():
    if greeting == "Hi":
        print("Hi, how are you?")
    else:
        print("Bye")
    print("Done")


if __name__ == "__main__":
    main()
