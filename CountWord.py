text = "hello world hello python"

def count_word(text):
    count = {}
    for word in text.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(count_word(text))