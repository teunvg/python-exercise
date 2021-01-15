# Script settings
file_names = ['beyond_good_and_evil.txt', 'jenseits_von_gut_und_boese.txt', 'hamlet.txt']
interpunction = ['.', ',', ':', ';', '?']


# Loop over all specified files
for file_name in file_names:
    # Open file
    with open(file_name, encoding='utf-8') as file:
        text = file.read()

    # Clean the text, remove interpunction
    for character in interpunction:
        text = text.replace(character, '')

    # Create a list of individual word lengths
    word_lengths = []
    for word in text.split():
        word_lengths.append(len(word))

    # Print the answer
    print(f'Average word length in {file_name}: {sum(word_lengths) / len(word_lengths)}')
