# Constants must be changed to fit users file path. Default setting were chossen to fit my file system!
INVITED_FILE_PATH = "./Input/Names/invited_names.txt"
TEMPLATE_FILE_PATH = "./Input/Letters/starting_letter.txt"
REPLACE = "[name]"
# Final destination must be edited to users choice on line 21.

with open(INVITED_FILE_PATH) as names_file:
    # Readlines returns a list of every line in invited file
    names = names_file.readlines()

with open(TEMPLATE_FILE_PATH) as letter_file:
    # copy letter template into string
    letter = letter_file.read()

    for name in names:
        # readlines() gives '\n' to every entry by default. strip() removes whitespace. i.e. the '\n'
        ws_name = name.strip()
        # Replace the name variable from template with stripped white space name
        new_letter = letter.replace(REPLACE, ws_name)
        # Write out edited template with correct name into a folder named accordingly.
        with open(f"./Output/ReadyToSend/letter_for_{ws_name}.txt", 'w') as final_file:
            final_file.write(new_letter)

