from text_op import Textfile

# input a valid filename
# if exists the file is printed (supports txt, csv, json)
# else prints menu again
# loops to start or closes once a file is printed
def menu():
    file_name = input("Input file name: ")
    try:
        new_file = Textfile(file_name)
        new_file.printlines()
        if not type(new_file) is Textfile:
            raise TypeError
    except TypeError:
        print("Not Textfile type. Check Textfile reading")
        return menu()
    else:
        x = input("A = Repease. Else close\n")
        if x == 'A':
            menu()

"""
# Goals
- convert numpy array into a viewable image
- open and show files (txt, csv, json, jpg, png, pdf, )
"""

menu_file = Textfile("menu.txt")
menu_file.printlines()

menu()