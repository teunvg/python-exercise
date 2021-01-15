# Open file
file_name = 'hamlet.txt'

with open(file_name) as file:
    text = file.read()

unwanted_character_replacements = {
    92: '', # \
    47: '', # /
    34: '', # "
    39: '', # '
    96: '', # `
    44: '', # ,
    46: '', # .
    59: '', # ;
    58: '', # :
    40: '', # (
    41: '', # )
    33: '', # !
    63: '', # ?
}

# Create a list of individual word lengths
word_lengths = []
for word in text.split():
    word_lengths.append(len(word.translate(unwanted_character_replacements)))

# Print the answer
print(f'Average word length: {sum(word_lengths) / len(word_lengths)}')
