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
    'Щ': '---..',
    'Ь': '-..-',
    'Ы': '-.--',
    'Ъ': '--.--',
    'Я': '---'
    }   
    new_string = ''
    
    for i in string:
        try:
            if i == " ":
                new_string += '/'
                continue
            
            new_string += morse_code_dict[i.upper()]
            new_string += " "
        except KeyError:
            continue
    return new_string

