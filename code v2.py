# i = selection of tool
# r = result
# t = text to be tool'ed

err1 = "Invalid character!"
err2 = "Text must be bigger than 1 (one) character."

title = "Welcome to Text Tools!"

print(title)

selection ="""
Please type the letter corresponding to your process of choice.

Count length in characters (C)
Count length in words (W)
Transform all in lowercase (L)
Transform all in uppercase (U)
"""

print(selection)

print()
i = input("Selection:");

print()
print("Ok, now the content.")
print()

t = input("Paste your text here:")

if i == "C":
    r = len(t);
elif i == "W":
    r = len(t.split());
elif i == "L":
    r = t.lower();
elif i == "U":
    r = t.upper();
else:
    print (err1);

print("""
Processing...
.
.
.
""")

print ("Here is your final product:")
print()
print(r)
