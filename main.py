#   Text to Morse Code Converter
#   by VelvetFingers ©️

from data import MORSE_CODES, LOGO

is_on = True
print(f"{LOGO}\n-- --- .-. ... ./-.-. --- -.. ./-.-. --- -. ...- . .-. - . .-.\nThis program converts a message into morse code!")


while is_on:
    print("\nPlease note: this program only accepts alphanumerical characters, do not use any symbols.")
    message = input("Enter your message:\n")

    try:
        # [1] Split the message into a space-separated list
        # [2] Add each letter (morse code converted) into a new list
        # [3] Convert to a string, each morse-code letter separated by a space
        # [4] Convert to a string, each morse-code word separated by a forward-slash
        output = "/".join(
            [" ".join(MORSE_CODES[letter.upper()] for letter in word)
            for word in message.split()]
        )
    except KeyError:
        message = input("\nYour message included an illegal character. Please enter a new message using only letters or numbers:\n")
        output = "/".join(
            [" ".join(MORSE_CODES[letter.upper()] for letter in word)
             for word in message.split()]
        )
    else:
        # Print output to console
        print(f"\nYour converted message:\n{output}")

    # Ask to convert another message, or end program
    should_continue = input("\nWould you like to convert another message? 'Y' for yes, 'N' for no:\n=> ")
    if should_continue.lower() != "y": is_on = False
