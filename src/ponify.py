

list_of_finds = eval(open("list.txt", "r").read())

def replace(text, replacements=list_of_finds):
	for number in range(len(replacements)):
		find = replacements[number][0]
		text = text.replace(find, replacements[number][1])
			
	return str(text)

def undo_replace(text, replacements=list_of_finds):
        for number in range(len(replacements)):
                find = replacements[number][1]
                text = text.replace(find, replacements[number][0])

        return text

