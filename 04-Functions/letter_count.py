def letter_count(text : str, letter):
    result = 0
    for l in text:
        if l == letter:
            result+=1
    return result
if __name__ == "__main__":
    text = "You never get a second chance to make a first impression"
    print(letter_count(text, "e"))