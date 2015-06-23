import sys
 
def usage():
	print("Usage: %s <text_file> <words_file> <out_file>" % sys.argv[0])


def read_words_file(words_file):
	words = []
	with open(words_file) as f:
		for line in f:
			for word in line.rstrip().split():
				words.append(word)
	return set(words)


def write_in_file(word, words, out, string):
	if word in words:
		out.write('<b>'+ word + '</b>' + string)
	else:
		out.write(word + string)		


if __name__ == '__main__':
	if len(sys.argv) != 4:
		usage()
		exit(1)

	text_file  = sys.argv[1]
	words_file = sys.argv[2]
	out_file   = sys.argv[3]

	words = read_words_file(words_file)
	with open(text_file) as current_file, open(out_file, 'w') as out:
		for line in current_file:
			for word in line.rstrip().split():			
				last_letter = word[-1]
				if last_letter.isalpha():
					write_in_file(word, words, out, ' ')
				else:	
					new_word = ''
					for letter in word:
						if letter != last_letter:
							new_word += letter
					write_in_file(new_word, words, out, '')
					out.write(last_letter + ' ')
		
							