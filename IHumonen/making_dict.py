import sys
 
def usage():
	print("Usage: %s <text_file> <words_file> <out_file>" % sys.argv[0])


def read_words_file(words_file):
	words = []
	with open(words_file) as f:
		for line in f:
			for word in line.rstrip().split():
				words.append(word)
	return words


def add_to_dictionary(word, dictionary):
	part = word[0: len(word)-2]
	if part in dictionary_parts.values() :
		dictionary[word] += 1
#	else:
#		dictionary[word] = 0


if __name__ == '__main__':
	if len(sys.argv) != 4:
		usage()
		exit(1)

	text_file  = sys.argv[1]
	words_file = sys.argv[2]
	out_file   = sys.argv[3]

	dictionary_popularity = dict.fromkeys(read_words_file(words_file), 0)
	dictionary_parts = dict.fromkeys(read_words_file(words_file), 0)
	for x in dictionary_parts:
		dictionary_parts[x] = x[0: len(x)-2]

	words = read_words_file(words_file)
	with open(text_file) as current_file, open(out_file, 'w') as out_file:
		for line in current_file:
			for word in line.rstrip().split():			
				last_letter = word[-1]
				if last_letter.isalpha():
					add_to_dictionary(word, dictionary_popularity)
				else:	
					new_word = ''
					for letter in word:
						if letter != last_letter:
							new_word += letter
					add_to_dictionary(new_word, dictionary_popularity)
		for x in dictionary_popularity:
			out_file.write(x + ' . ' + str(dictionary_popularity[x]) + '\n')			