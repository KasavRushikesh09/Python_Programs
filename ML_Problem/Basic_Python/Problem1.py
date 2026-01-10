import re
text = "Rushikesh kasav"
regex = r"(\w+)\s+(\w+)"
matches = re.sub(regex,r"\2 \1" ,text)
print(matches)