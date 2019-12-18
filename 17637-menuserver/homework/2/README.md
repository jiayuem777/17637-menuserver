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

If operator button '=' is clicked and then click other operator buttons, the calculator will use the displayed number, rather than 0, to do next calculation.

If an error message is displayed and then click digit buttons, the displayed number will show the digit.

If an error message is displayed and then click operator button '=', the displayed number will be 0, or click other operator buttons subsequently, the number used to calculate before operator will set to be 0.

3. Validation

If the inputs do not have demanded hidden inputs like "cur_val", "cur_opt", "pre_val", "pre_opt", the displayed area will show error massage.

If the button inputs names are not "num" or "opt", the displayed area will show error massage.

If the value of "cur_val", "pre_val" and "num" are not integers, the displayed area will show error massage.

If the value of "pre_opt" and "opt" is not in the list of [&add, &minus, &times, &divide, &equals], or the value of "cur_opt" is not in the list and not equals to '', the displayed area will show error massage.

4. GET and POST request

To transfer the data from client to server, use "method=POST" int the <form> element since:

1) When the method is GET, all form data is encoded in the URL, appended to the action URL in the <form> element as query string parameters. With POST, form data appears within the message body of the HTTP request. Variables are not displayed in the URL.

2) Parameters are not saved in the browser history with POST method.

3）When form is submitted, app will generate POST method.

4) In the initial state of app, browser will generate GET method to the server. Use "if request.method == 'GET' to initialy set up a zero state. Then if request.method == 'POST', form message is submitted and judge request.POST massage to gain next operations.
