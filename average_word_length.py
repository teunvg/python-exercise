# Script settings
file_name = 'beyond_good_and_evil.txt'
interpunction = ['.', ',', ':', ';', '?']

# Open file
with open(file_name) as file:
    text = file.read()

# Clean the text, remove interpunction
for character in interpunction:
    text = text.replace(character, '')

# Create a list of individual word lengths  
word_lengths = []
for word in text.split():
    word_lengths.append(len(word))

# Print the answer
print(f'Average word length: {sum(word_lengths) / len(word_lengths)}')
