# Braille Translator in Python

# Braille to English and English to Braille dictionary
braille_dict = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..',
    'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.', 'P': 'OOO.O.',
    'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO',
    'Y': 'OO.OOO', 'Z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ',': '..O...', ';': '..OO..', ':': '...O..', '.': '...OO.',
    '!': '..OO.O', '?': '..O.O.', '(': '...O.O', ')': '...O.O', '-': '...OO.', ' ': '......', 'capital': '.....O', 'number': '.O.OO.'
}

# Reverse dictionary for translating Braille to English
english_dict = {v: k for k, v in braille_dict.items()}

def detect_language(input_string):
    """Detect if the input string is English or Braille based on its characters."""
    if set(input_string).issubset({'O', '.'}):
        return 'braille'
    return 'english'

def translate_to_braille(text):
    """Translate English text to Braille."""
    result = []
    for char in text:
        if char.isupper():
            result.append(braille_dict['capital'])
            char = char.lower()
        if char.isdigit():
            result.append(braille_dict['number'])
        result.append(braille_dict.get(char.upper(), '......'))
    return ''.join(result)

def translate_to_english(braille):
    """Translate Braille to English text."""
    result = []
    i = 0
    length = len(braille)
    capitalize_next = False
    number_mode = False
    while i < length:
        symbol = braille[i:i+6]
        if symbol == braille_dict['capital']:
            capitalize_next = True
            i += 6
            continue
        elif symbol == braille_dict['number']:
            number_mode = True
            i += 6
            continue
        char = english_dict.get(symbol, '?')
        if number_mode:
            char = str(english_dict.get(symbol, '?'))
            number_mode = False
        if capitalize_next:
            char = char.upper()
            capitalize_next = False
        result.append(char)
        i += 6
    return ''.join(result)

def translate(input_string):
    """Main function to translate based on detected language."""
    language = detect_language(input_string)
    if language == 'english':
        return translate_to_braille(input_string)
    elif language == 'braille':
        return translate_to_english(input_string)
    else:
        return "Invalid input"

# Example usage
if __name__ == "__main__":
    input_string = input("Enter text to translate (English or Braille): ")
    output = translate(input_string)
    print(f"Translated output: {output}")
