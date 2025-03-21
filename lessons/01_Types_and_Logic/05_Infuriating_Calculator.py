"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk   # Import the required modules

window = Tk()  # Create a window object

window.withdraw() # Hide the window, hint: use the withdraw method

number = simpledialog.askinteger("Number", "Pick a number")    # Ask the user for the first number   

hello = simpledialog.askinteger("Number", "Pick another number")    # Ask the user for the second number

operation = simpledialog.askstring("Number", "Pick an operation")  # Ask the user for the math operation

if operation == 'add':# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
   hi = number + hello
   messagebox.showinfo('Sum', hi)
   
elif operation == 'subtract': # If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
   paper = number - hello
   messagebox.showinfo('Difference', paper)

elif operation == 'multiply': # Keep the window open
   pen = number * hello
   messagebox.showinfo('Product', pen)

elif operation == 'divide':
   car = number / hello
   messagebox.showinfo('Quotient', car)

else:
   messagebox.showerror()

