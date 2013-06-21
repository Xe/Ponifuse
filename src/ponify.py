import re
import json

list_of_finds = json.load(open("list.json"))
list_of_finds = list(map(lambda x: [bytes(s) for s in x[:2]], list_of_finds))
print list_of_finds
def map_each(replacements, f):
    return list(list(map(f, entry)) for entry in replacements)

# add titles and ALL CAPS
list_of_finds += map_each(list_of_finds, str.title) + map_each(list_of_finds, str.upper)


def replace(text, replacements=list_of_finds):
	for number in range(len(replacements)):
		find = replacements[number][0]
		text = text.replace(find, replacements[number][1])

	return str(text)


#TODO: performance?
def fast_replace(text, replacements=list_of_finds):
    LOOKUP = {x[0]:x[1] for x in list_of_finds}
    match_re = "|".join([re.escape(key) for key in LOOKUP.keys()] + ["."])

    #TODO: use finditer
    parts = re.findall(match_re, text, re.DOTALL | re.MULTILINE)
    parts = map((lambda s:LOOKUP.get(s, s)), parts)
    return ''.join(parts)

def undo_replace(text, replacements=list_of_finds):
        for number in range(len(replacements)):
                find = replacements[number][1]
                text = text.replace(find, replacements[number][0])

        return text

if __name__ == "__main__":

    test_string = [x[0] for x in list_of_finds]

    print test_string

    print replace(str(test_string))

    test_string_b = 'human\nman\nHUMAN\n\nman\nHUMAN'
    test_replacements = [['human', 'pony', '\n'], ['man', 'stallion', '\n']]
    test = fast_replace(test_string_b, test_replacements)
    assert test == 'pony\nstallion\nPONY\n\nstallion\nPONY'
    assert undo_replace(test, test_replacements) == test_string_b
