import befunge
import sys

if len(sys.argv) != 2:
    print("Invalid number of arguments.")
    print("Usage: run.py <code>")
    exit(1)

code = open(sys.argv[1], "r")

befunge.run(code.read())