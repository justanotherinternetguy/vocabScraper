with open('file.txt', "r") as word_list:
	words = word_list.read().split(' ')

filtered = []


for i in words:
	if len(i) >= 15 and i.isalpha() == True:
		filtered.append(str(i))
		
print(filtered)
print(len(filtered))

filter = open('output.txt', 'w')
filter.write(str(filtered))
filter.close()
#any(i.isdigit() for i in filtered)
