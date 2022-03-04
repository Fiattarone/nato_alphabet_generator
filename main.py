import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alpha_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

natoize = input("What word do you need NATOized?").upper()

print([nato_alpha_dict[letter] for letter in natoize if letter in nato_alpha_dict])
