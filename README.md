# Assignment-3-Repeated-execution
## 1. Description

This submission contains two Python programs.

The first program calculates the **GCF or **LCM ** of two positive numbers. The user can choose between GCF mode and LCM mode(1 for GCF and 2 for LCM. 
The GCF is calculated using repeated subtraction,the program runs until both diffrences are equal.
repeated subtraction to get GCF example: 
let diff1=num1=18 diff2=num2=5
18>5 so diff1=18-5=13
13>5 so diff1= 13-5=8
8>5 so diff1=  8-5=3
5>3 so diff2=  5-3=2
3>2 so diff2=  3-2=1
2>1 so diff2=  2-1=1
diff1== diff2
the loop ends and the GCF is 1 
the LCM is calculated using the GCF.
  lcm=(num1*num2)//gcf 
then the user is asked whether  they want to stop or continue. the program will repeat( chosing the mode, the numbers) until the user enters "stop"



The second program creates a **Pascal pyramid**. The user enters the number of rows, and the program uses loops to calculate and display the numbers in the shape of a pyramid.

The program first asks the user to enter a positive number of rows.
The for loop then creates each row of the Pascal pyramid. 
num_spaces controls the spaces at the beginning of each row to create the pyramid shape. 
coef = 1 starts each row with 1.
The inner for loop calculates how many numbers are needed in each row.
The formula coef = coef * (i-j) // (j+1) calculates the next number in the row. 
After each row, num_spaces -= 1 decreases the spaces because the next row is wider.
Finally, print(row) displays the completed row.
