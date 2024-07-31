def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provided a valid input"  # If no input is provided, the program terminates here
    formatted_fname=f_name.title()
    formatted_lname=l_name.title()
    # print(f"{formatted_fname} {formatted_lname}")
    return f"Result: {formatted_fname} {formatted_lname}"    # return tells its the end of the function ,should now exit the function
    print("hello")  # This line won't executes 

# format_name("chandan", "GOWDA")
formated_string = format_name("chandan", "GOWDA")
print(formated_string)
    