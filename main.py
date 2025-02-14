# TASK: Write a function that asks for a valid age input and handles invalid inputs.

# Define a function that takes one string parameter
def get_age(promt: str)->int:
# Create a loop that keeps asking for input until a valid age is entered
    while True:
        try:
            age=int(input("enter age "))# Try to convert the input to an integer
            if age>0:# If successful, check if the number is positive
                return age# If valid, return the number
                break
            else:
                print("enter a proper age please")
        except ValueError:
            print("please, enter a number ")# If not valid, show an error message and prompt again


# Call the function and store the result
user_age=get_age("enter your age: ")
# Display the valid age
print("your valid age is: ",user_age) 
