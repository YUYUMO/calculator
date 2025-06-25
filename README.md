After climbing the steps, you've all reached the treasure! Now, Karel is trying to share the treasure with you and the rest of the crew. However, there’s one tiny problem: Karel can't count! To help share, Karel needs your help to build a simple calculator to perform arithmetic in order to do the math to properly split the treasure.



Karel will ask the user what type of operation they want to perform (addition, subtraction, multiplication, or division). Then, they’ll ask for two piles of the treasure as input. Once the math is complete, Karel will display the result and ask if the user wants to perform another calculation.



Below is an example of what the program output should look like when ran:

Welcome to Karel's Calculator!
------------------------------
Help Karel with arithmetic!

1. Addition
2. Subtraction
3. Multiplication
4. Division

Which operation do you want to help Karel with?: 1
Enter your first number: 17
Enter your second number: 18
17 + 18 results in 35.

Do you want to perform another operation? (y/n): y

1. Addition
2. Subtraction
3. Multiplication
4. Division

Which operation do you want to help Karel with?: 4
Enter your first number: 88
Enter your second number: 35
88 // 35 results in 2.

Do you want to perform another operation? (y/n): n



Things to keep in mind:





Input Validation is not required, not expected. Assume the user will always input a valid response.



For Division, please print only the nearest floor of the division using the // integer division operator.