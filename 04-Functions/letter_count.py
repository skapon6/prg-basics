def letter_count(text, letter):
    result = 0
    for l in text:
        if l == letter:
            result += 1
    return result
