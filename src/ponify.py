

list_of_words = eval(open("list.txt", "r").read())

def replace(text, replacements=list_of_words):
	print "given:", text
	#text.split()
	for number in range(len(replacements)):
		word = replacements[number][0]
		print word, "tried"
		if word in text:
			print word, "found"
			text.replace(word, replacements[number][1])
			
	return str(text)

def undo_replace(text, replacements=list_of_words):
        for number in range(len(replacements)):
                word = replacements[number][1]
                if word in text:
                        text.replace(word, replacements[number][0])

        return text

