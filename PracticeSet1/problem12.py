import re
text = input("Enter the text: ")
regex = r"[aeiou]"
matches = (re.findall(regex,text,re.IGNORECASE))
print(len(matches))
