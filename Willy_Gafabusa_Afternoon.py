# #Handling handling
try:
    # Code block where an exception might occur
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend / divisor
    print("Result:", result)

except ValueError:
    # Exception handler for ValueError
    print("Invalid input. Please enter a valid integer.")

except ZeroDivisionError:
    # Exception handler for ZeroDivisionError
    print("Cannot divide by zero.")

except Exception as e:
    # Generic exception handler
    print("An error occurred:", str(e))

finally:
    # Code block that always executes, regardless of whether an exception occurred or not
    print("End of program.")


#File Handling
my_file = "WillyTech.txt"


file = open(my_file, "w")


file.write("Hello, World!\n")
file.write("Adam comes from Masaka City.\n")


file.close()


file = open(my_file, "r")

content = file.read()

print(content)
file.close()
