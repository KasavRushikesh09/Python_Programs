def longest_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        i = 0
        while i<len(prefix) and i<len(word) and word[i] == prefix[i]:
            i+=1
        prefix = prefix[:i]
    return prefix
print(longest_prefix(["flower","flight","flow"]))