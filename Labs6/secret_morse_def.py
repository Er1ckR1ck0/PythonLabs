import re
def secret_string(string):
    
    morse_code_dict = {
    'А': '.-',
    'Б': '-...',
    'В': '.--',
    'Г': '--.',
    'Д': '-..',
    'Е': '.',
    'Ж': '...-',
    'З': '--..',
    'И': '..',
    'Й': '.---',
    'К': '-.-',
    'Л': '.-..',
    'М': '--',
    'Н': '-.',
    'О': '---',
    'П': '.--.',
    'Р': '.-.',
    'С': '...',
    'Т': '-',
    'У': '..-',
    'Ф': '..-.',
    'Х': '....',
    'Ц': '-.-.',
    'Ч': '--..',
    'Ш': '----',
    'Щ': '--.-',
    'Ь': '-..-',
    'Ы': '-.--',
    'Ъ': '--.--',
    'Я': '.-.-'
    }   
    new_string = ''
    

    if not re.compile('[А-Яа-я]').search(string):
        string = string.split(' ')
        print(string)
        for i in string:
            try:
                for key, val in morse_code_dict.items():
                    if i == '/':
                        new_string += " "
                        continue
                    if val == i:
                        new_string += key
            except KeyError:
                continue
        return new_string
    else:
        for i in string:
            try:
                if i == " ":
                    new_string += '/ '
                    continue
                
                new_string += morse_code_dict[i.upper()]
                new_string += " "
            except KeyError:
                continue
        return new_string


