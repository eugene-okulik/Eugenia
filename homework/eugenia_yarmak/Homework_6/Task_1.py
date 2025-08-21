text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

sep_words = text.split()
fin_words = []

for word in sep_words:
    if word.endswith((",", ".")):
        words = word[:-1] + "ing" + word[-1]
    else:
        words = word + "ing"
    fin_words.append(words)

print(" ".join(fin_words))
