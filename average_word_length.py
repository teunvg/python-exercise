# Open file
file_name = 'beyond_good_and_evil.txt'

with open(file_name) as file:
    text = file.read()

# Create a list of individual word lengths
word_lengths = []
for word in text.split():
    word_lengths.append(len(word))

# Print the answer
print(f'Average word length: {sum(word_lengths) / len(word_lengths)}')
