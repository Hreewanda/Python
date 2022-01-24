
def translate(phrase):
    translatation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translatation = translatation + "g"
        else:
            translatation = translatation + letter
    return translatation


print(translate(input("Enter a Phase: ")))
