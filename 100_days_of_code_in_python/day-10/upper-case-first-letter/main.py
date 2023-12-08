#define a function to format the names
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


#print welcome message
print("Transform the first letter in each word upper case.")

#ask user for inputs
f_name = input("What's your first name?\n")
l_name = input("What's your last name?\n")

#print the ouput result
print(f"Result: \n{format_name(f_name, l_name)}")
