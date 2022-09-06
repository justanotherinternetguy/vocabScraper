end = False

# Load input text
with open('file.txt', 'r') as word_list:
    file = word_list.read().split(' ')

words = open('file.txt', 'r')

# len parameter
length = int(input("length : "))


# Filtered list of vocab words
filtered = []


# filtering process

# by length

for i in file:
    if len(i) >= length and i.isalpha() == True:
        filtered.append(str(i))


unique = list(set(filtered))

# list of unique words

print(unique)
print(len(unique))


# write to output.txt
with open("output.txt", 'w') as f:
    f.truncate(0)
    f.write(str(unique))


