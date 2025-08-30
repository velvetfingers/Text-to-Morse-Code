#   Text to Morse Code Converter
#   by VelvetFingers - a python student ©️

from data import MORSE_CODES, LOGO

is_on = True
print(f"{LOGO}\n-- --- .-. ... ./-.-. --- -.. ./-.-. --- -. ...- . .-. - . .-.\nThis program converts a message to and from morse code!")


while is_on:
    output = ""
    morse_char_to_letter = dict((v, k) for k,v in MORSE_CODES.items())

    direction = int(input("\nChoose a direction:\n[1] From text to morse code\n[2] From morse code to text\nEnter a choice (e.g. 1) => "))
    print("\nPlease note: this program only accepts alphanumerical characters, do not use any symbols.")
    message = input("Enter your message:\n" if direction == 1 else "Paste the morse code:\n")

    try:
        # plaintext --> morse-code
        if direction == 1:
            output = "/".join(
                [" ".join(MORSE_CODES[letter.upper()] for letter in word)
                for word in message.split()]
            )

        # morse-code --> plaintext
        elif direction == 2:
            output = (
                " ".join(
                    ["".join(
                        [morse_char_to_letter[letter] for letter in word.split()]
                    ) for word in message.split("/")]
                )
            ).capitalize()
    except KeyError:
        message = input("\nYour message included an illegal character. Please try again using only letters or numbers.\n")
        break
    else:
        # Print output to console
        print(f"\nYour converted message:\n{output}")

    # Ask to convert another message, or end program
    should_continue = input("\nWould you like to convert another message? 'Y' for yes, 'N' for no:\n=> ")
    if should_continue.lower() != "y": is_on = False
