def numchar(val):
    string = ''
    number = 0
    end = 0
    val += ' '
    for space in val:
        end += 1
        if space == " ":
            try:
                string += chr(int(val[number:end]))
            except Exception:
                print(
                    "Please Enter a Valid Numeric Value Like This \"72 101 108 108 111 32 87 111 114 108 100\" "
                    "without commas")
                break
            else:
                number = end
    print(string)


def charnum(val):
    string = ''
    for alphabet in val:
        string += str(ord(alphabet)) + ' '
    print(string)


def userinput(choice):
    userinpt = str(input("Enter AnyThing Want: "))
    if choice == 'NC':
        numchar(userinpt)
    elif choice == 'CN':
        charnum(userinpt)


while True:
    choice = str(input("Enter 'NC' to convert numbers to character\nEnter 'CN' to convert string to numbers\nEnter 'X' To Exit: ")).upper()
    if choice == 'NC' or choice == 'CN':
        UI = str(input("Enter 'I' For Input\nEnter 'X' to exit: ")).upper()
        if UI == 'I':
            userinput(choice)
        elif UI == 'X':
            break
        else:
            print('Not a Valid Choice')
            continue
    elif choice == 'X':
        break
    else:
        print(f'"{choice}" is not a valid input')
        continue
