import sys

if len(sys.argv) < 2:
    print("Usage: python greet.py <your_name>")

else:
    name = sys.argv[1]
    print(f"hello, {name}! Welcome to section!")
    sys.exit("nah i'm just playing gtfo")