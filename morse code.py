while True:
    morse = input("Enter Text To Convert: ")
    print('\n\nTranslation;\n')
    def encode_morse(morse):

        encoded_text = ''
        char_to_dots = {
            # Letters
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            # Numbers
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            # Punctuation
            '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
            ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
            '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.',
            ' ': ' ',
        }

        for letter in morse.upper():
            for dictionary in char_to_dots:
                if dictionary == letter:
                    encoded_text = (encoded_text+' '+char_to_dots[letter])



        morse = encoded_text

        Print = morse.replace('   ','  ')
        print('Encoded Message: ',Print)
        morse = morse.replace(
            '   ',
            ' £̡҉͏(͏̶̧(҉̸(̕͝0̀҉̀0̢͜2̧̢5̢̡҉2̸0hj̀a͜s͢͡d̶͡f͠b̢͘e͡a̸̛͡l͘̕d͞f̨j́a̕͞h́e0͝҉̡8̸̡͏3͏2̸͞?̀͠͞>́͘͝,̵͢.̢͞$̡ ')


        decode_morse(morse, 'Retanslated Message:')



    def decode_morse(morse, description):
        decoded_text = ''
        dots_to_char = {
            # Letters
            ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f",
            "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
            "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
            "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
            "-.--": "y", "--..": "z",
            # Numbers
            "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
            ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
            # Punctuation
            ".-...": "&", ".----.": "'", ".--.-.": "@", "-.--.-": ")", "-.--.": "(",
            "---...": ":", "--..--": ",", "-...-": "=", "-.-.--": "!", ".-.-.-": ".",
            "-....-": "-", ".-.-.": "+", ".-..-.": '"', "..--..": "?", "-..-.": "/",
            ' ': ' ',
        }
        morse = morse.replace(
            '  ',
            ' £̡҉͏(͏̶̧(҉̸(̕͝0̀҉̀0̢͜2̧̢5̢̡҉2̸0hj̀a͜s͢͡d̶͡f͠b̢͘e͡a̸̛͡l͘̕d͞f̨j́a̕͞h́e0͝҉̡8̸̡͏3͏2̸͞?̀͠͞>́͘͝,̵͢.̢͞$̡ ')

        morse = morse.split(' ')
        temp = []
        for format in morse:
            temp_ = format.replace(
                '£̡҉͏(͏̶̧(҉̸(̕͝0̀҉̀0̢͜2̧̢5̢̡҉2̸0hj̀a͜s͢͡d̶͡f͠b̢͘e͡a̸̛͡l͘̕d͞f̨j́a̕͞h́e0͝҉̡8̸̡͏3͏2̸͞?̀͠͞>́͘͝,̵͢.̢͞$̡',
                ' ')
            temp.append(temp_)

        morse = temp

        for letter in morse:
            for dictionary in dots_to_char:
                #print('TEST__ ',morse)
                if dictionary == letter.upper():
                    decoded_text = (decoded_text+dots_to_char[letter])

        morse = decoded_text
        print(description,morse)

    encode_morse(morse)
    decode_morse(morse, 'Decoded Message:')