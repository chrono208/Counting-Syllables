def count(word):
    count = 1
    for letter in  word:
        if letter == "-":
            count += 1
    return count