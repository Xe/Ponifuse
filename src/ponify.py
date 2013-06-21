import re
import json

list_of_finds = json.load(open("list.json", "r"))

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

if __name__ == "__main__":
    
    test_string = [x[0] for x in list_of_finds]
    
    print test_string
    
    print replace(str(test_string))
