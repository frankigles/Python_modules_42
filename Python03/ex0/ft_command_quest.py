import sys

arg_len: int = len(sys.argv)
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if arg_len == 1:
    print("No argument provided!")
else:
    print(f"Arguments received: {arg_len -1}")
    i = 0
    for argv in sys.argv:
        if argv != sys.argv[0]:
            i += 1
            print(f"Argument {i}: {argv}")
print(f"Total arguments: {arg_len}")
