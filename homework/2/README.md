Homework 2: A Django calculator

1. User Interface

The calculator contain 15 clickable buttons: a button for each digit 0 to 9, and ​+​, ​-​, ×, ÷, and ​=​.

Buttons have round corners.

Digit buttons and operator buttons have different colors.

The calculator displays a single integer value that the user may not directly edit.

When the user hovers over a button, its color must change.

2. Calculator's Behavior

An integer number is displayed in the block and will change after clicking buttons. At the beginning, the number is set to 0.

The calculator performs integer math (e.g. 9 ÷ 4 = 2).

If the user attempts to divide by 0 or send malformed input, reset the state and display an error message until the next button is clicked.

There is no operator precedence. Execute the operations in the order they are encountered.

If several operator buttons are clicked continuously, the operator of the last clicked button will be used.

If operator button '=' is clicked and then click other operator buttons, the calculator will use the displayed number, rather than 0, to do next calculation
