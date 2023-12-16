def check_character(char):
    if char.isalpha():
        if char.islower():
            print("The character '{}' is a lowercase letter.".format(char))
        else:
            print("The character '{}' is an uppercase letter.".format(char))
    elif char.isdigit():
        num_words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        print("The character '{}' is a numeric digit ({}).".format(char, num_words[int(char)]))
    else:
        print("The character '{}' is a special character.".format(char))

l = True
while l:
    char = input("Enter a character: ")

    if len(char) != 1:
        print("Please enter a single character.")
    else:
        check_character(char)
    
    l = input("Do you want to run the program again? (y/n): ").lower()
    if l != "y":
        break
