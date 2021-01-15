# Open file
file_name = 'hamlet.txt'

with open(file_name) as file:
    text = file.read()

total_characters = 0
word_count = 0
for word in text.split():
    total_characters += len(word)
    word_count += 1

# print(f'total_characters = {total_characters}, word_count = {word_count}')
print(f'{total_characters=}, {word_count=}')

print(f'Average word length: {total_characters/word_count}')