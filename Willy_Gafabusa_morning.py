#Day 3
#Basic operators and expressions(Input and Output operators)
'''
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
//Division
== Equal to
!= Not equal to !==
>Greater than, < less than, >= greater than or equal to, <= less than or equal to

-Logical operators
Logical AND 'and', Logical OR 'or' Logical NOT 'not'
'''
#Addition
x=45+10
print(x)
#Subtraction
y=45-10
print(y)
#Multiplication
z=45*10
print(z)
#Division
w=45/10
print(w)
#Modulus
v=45%10
print(v)
#Exponentiation
e=45**10
print(e)

#Comparison operators
a=15
b=9
#Greater than
if a>b:
    print("a is greater than b")
    print(a>b)
    #Less than
    if a<b:
     print("a is less than b")
    print(a<b)

    #Greater than or equal to
    if a>=b:
     print("a is greater than or equal to b")
    print(a>=b)

    #Less than or equal to
    if a<=b:
     print("a is less than or equal to b")
    print(a<=b)

    #Equal to
    if a==b:
     print("a is equal to b")
    print(a==b)

    #Not equal to
    if a!=b:
     print("a is not equal to b")
    print(a!=b)

    #Logical operators
    a=True
    b=False

    #Logical AND
    print(a and b)

    #Logical OR
    print(a or b)

    #Logical NOT
    print(not a)
    print(not b)

#Assignment operators
#Compound assignment operators
a=5
#Add and assign
a+=5
print(a)

#Subtract and assign
b=19
b-=5
print(b)

#Multiply and assign
c=19
c*=5
print(c)

#Divide and assign
d=19
d/=5
print(d)

#Modulus and assign
e=19
e%=5
print(e)

#Exponentiation and assign
f=19
f**=5
print(f)

#Mmembership assignment operators
cars=['Jeep','Mercedes','Raum']
if 'Jeep' in cars:
  print("Jeep is in the list")
  print('Toyota is' in cars)

  #Identity operators
  x=10
  y=10
  #is operator
  print(x is y)
  print(x is not y)
  print(x==y)
  print(x!=y)
  print(x<y)

  #List
  #Is not operator
  w=[1,2,3,4,5]
  z=[1,2,3,4,5]
  print(w is not z)

  #Bitwise operators
  '''
  Bitwise operators are used to perform operations on individual bits in binary numbers
  Bitwise AND ('&'): Performs a Bitwise AND operation betweeen the corresponding bits
  '''
  #Examples of Bitwise operators
  a=10
  b=20

  #Bitwise AND
  result_and=a&b
  print(result_and)

  #Bitwise OR
  result_or=a|b
  print(result_or)

  #Bitwise XOR
  result_xor=a^b
  print(result_xor)

  #Bitwise left shift operation
  result_left_shift=a<<2
  print(result_left_shift)

  #Bitwise right shift operation
  result_right_shift=a>>2
  print(result_right_shift)

  #Example And operation
  #Create a simple calculator
  #CALCULATOR SOLUTION
  import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget for displaying the result
entry = tk.Entry(window, width=30, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(window, text="1", padx=10, pady=5, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=10, pady=5, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=10, pady=5, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=10, pady=5, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=10, pady=5, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=10, pady=5, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=10, pady=5, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=10, pady=5, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=10, pady=5, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=10, pady=5, command=lambda: button_click(0))

# Create operator buttons
button_add = tk.Button(window, text="+", padx=10, pady=5, command=lambda: button_click('+'))
button_subtract = tk.Button(window, text="-", padx=10, pady=5, command=lambda: button_click('-'))
button_multiply = tk.Button(window, text="*", padx=10, pady=5, command=lambda: button_click('*'))
button_divide = tk.Button(window, text="/", padx=10, pady=5, command=lambda: button_click('/'))

button_equal = tk.Button(window, text="=", padx=10, pady=5, command=button_equal)
button_clear = tk.Button(window, text="C", padx=10, pady=5, command=button_clear)

# Arrange buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4,column=1)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Start the GUI event loop
window.mainloop()
  