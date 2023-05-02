#########################################################################################################################################################

###############                SAMUEL GETNET                              ########################################
#
#
#
###############                 ID 0127/12                                 ########################################


from tkinter import *
#########################                                                #######################################
#######                    Function to convert Roman numbers to decimal                          ##############

def roman_to_decimal(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i-1]]:
            decimal += roman_dict[roman[i]] - 2 * roman_dict[roman[i-1]]
        else:
            decimal += roman_dict[roman[i]]
    return decimal

# Function to convert decimal to Roman numbers
def decimal_to_roman(decimal):
    roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman = ''
    for key in sorted(roman_dict.keys(), reverse=True):
        while decimal >= key:
            roman += roman_dict[key]
            decimal -= key
    return roman
# ##############               Function to handle the button click                             ###############
def convert():
    input_value = input_field.get()
    output_value = ''
    if input_type.get() == 'Roman':
        output_value = roman_to_decimal(input_value.upper())
        output_type.set('Decimal')
    else:
        output_value = decimal_to_roman(int(input_value))
        output_type.set('Roman')
    output_field.delete(0, END)
    output_field.insert(0, output_value)

# Create the main window
window = Tk()

window.title('SAMUEL GETNET ID 0127/12')
window.geometry('700x500')
window.config(bg='light blue')

# Create the input field
input_frame = Frame(window)
input_frame.pack(pady=10)
input_label = Label(input_frame, text='Enter a value:')
input_label.pack(side=LEFT)
input_field = Entry(input_frame)
input_field.pack(side=LEFT)
########################################################################################################################################
# ##################################Create the input type radio buttons####################################################################
input_type = StringVar()
input_type.set('Roman')
input_roman_radio = Radiobutton(window, text='Roman', variable=input_type, value='Roman')
input_roman_radio.pack()
input_decimal_radio = Radiobutton(window, text='Decimal', variable=input_type, value='Decimal')
input_decimal_radio.pack()
#########################################################################################################################################################
# ###################################################Create the output field ####################################################################
output_frame = Frame(window)
output_frame.pack(pady=10)
output_label = Label(output_frame, text='Converted value:')
output_label.pack(side=LEFT)
output_field = Entry(output_frame)
output_field.pack(side=LEFT)

# ##################################Create the output type label
output_type = StringVar()
output_type.set('Decimal')
output_type_label = Label(window, textvariable=output_type)
output_type_label.pack()

# ##################################Create the convert button
convert_button = Button(window, text='Convert', command=convert)
convert_button.pack(pady=10)

info = Frame(window)
info.pack(pady=10)
info_label = Label(info, text=
                              'SAMUEL GETNET'
                              '  ==> ID: 0127/12')
info_label.pack(side=LEFT)

# ###################################################Start the main loop
window.mainloop()
