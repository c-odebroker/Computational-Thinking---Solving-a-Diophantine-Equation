# importing math module to access functions like sqrt() and pow()
import math

# sentinel is assigned with a value to be modified later in the loop by user action
sentinel = "y"

# loop allows program to run continuously unless user interacts with sentinel value in their terminal
while sentinel == "y":

    # unicode will enable mathematical expressions visible in the terminal
    superscript_two = "\u00B2"

    # this nested loop verifies if the user entering a number
    while True:
        # try-except is to test out the input from user until user enters a number and breaks the loop
        try:
            # Assign the users input to variable called x_value as integer type (Steps 1, 2, 3)
            x_value = int(input(f"~ Enter an integer number for x value to solve for y: x{superscript_two} + y{superscript_two} = 25 ~"))
            break
        # we don't want the program to be interrupted by raising errors
        # instead we want user to realize what is needed from them in order to continue
        except ValueError:
            print("Please enter a number.")


    # this nested loop checks out if the user entered a valid number
    # and asks user to try again with required domain mentioned
    # this method skips the possible ValueError
    while x_value < -5 or x_value > 5:
        print("Please enter a whole number between -5 and 5")
        x_value = int(input(f"~ Enter an integer number for x value to solve for y: x{superscript_two} + y{superscript_two} = 25 ~"))


    # Assign the evaluated equation for y to a variable called y_value (Step 4)
    # Now it is time to put the math module imported earlier in use
    # pow function raises the value to given power, power two in this case
    # sqrt function returns the value's square root value
    y_value = math.sqrt(25 - math.pow(x_value,2))

    # Here program finds the difference between the y and rounded y values to 3 decimal points (Step 5)
    subtract_y_rounded = y_value - round(y_value,3)

    # conditional if-else statement helps to convert floating numbers
    # to integers if they are whole numbers(if no difference between the original value and the rounded one)
    # otherwise leaves y values as they are and assigns the difference value with its 15th decimal point
    # because terminal prints out scientific(exponential) notation after the 15th, we want it to look simple
    if subtract_y_rounded == 0:
        y_value = int(y_value)
        subtract_y_rounded = int(subtract_y_rounded)
    else:
        y_value = y_value
        subtract_y_rounded = f"{subtract_y_rounded:.15f}"

    # Output stated with explanations for the equation and its components (Step 6)
    # I wanted to use one print function for all three outputs, so I wrote them with backspaces inside the same function
    # each line starts with a bulletin triangles
    # first statement tells the x and y pairs and there is a unicode(of positive or negative sign) for y pairs
    # because program gives all the solutions for y except negative ones, this is logically incorrect
    # second line we have the line starting with \n, without \n we cannot go to a next line in the same print function
    # and this would be hard to read extended sentences in a single line for users screen
    # this line has a clear output for what user reads
    # third line has the same escape sequence(\n) to jump to new line
    # here we have the answer for the difference in the line before
    print(
          f" ∆ (x,y) : ({x_value},\u00B1 {y_value})"
          f"\n ∆ Calculated and rounded(3 decimal) values for y are \u00B1 {y_value} , \u00B1 {y_value:.3f} respectively, where x is {x_value} "
          f"\n ∆ Difference between y and its rounded value to 3 decimal digits is {subtract_y_rounded} "
          )

    # Program will check if the user wants to do more with it or not
    # since this is another loop user will not be able to process without entering the required input
    sentinel = input("Do you wish to continue(y/n)?: ")
    while sentinel not in ("y", "n"):
        sentinel = input("Do you wish to continue(y/n)?: ")
   


# Program shut down message printed
print("Bye")