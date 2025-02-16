# Problem 1028

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1028.jpg)

Richard and Vicent are crazy about football collectable cards. In their spare time, they arrange a way of playing some game involving such cards. Both also have the habit of exchanging the repeated cards with their friends, and one day they thought about a different game. They called all their friends and proposed the following: with the cards in hand, each one tried to make an exchange with his closest friend following this simple rule: each one must count how many cards he owned. After this, they had to split these cards into stacks, all of it with the same size, as large as it was possible for both players. Then, each one choose one of the friend's card stacks to receive. For example, if Richard and Vincent would change the cards with respectively 8 and 12 cards each, both must put his cards in stacks of four cards (Richard would have two stacks and Vincent had three stacks), and both choose a stack from his friend to receive it.

Input
-----

The first input line contains a single integer **N** (1 â¤ **N** â¤ 3000), indicating the number of test cases. Each test case contains two integer numbers **F1** (1 â¤ **F1** â¤ 1000) and **F2** (1 â¤ **F2** â¤ 1000)  indicating, respectly, the among of collectable cards that Richard and Vicent have to change.

Output
------

For each test case there will be an integer number at the output, representing the maximum size of the stack of cards which can be exchanged between two players.


| Input Sample | Output Sample |
| --- | --- |
| 3 8 12 9 27 259 111 | 4 9 37 |


# Problem 1093

Descrição
----------

Felipinho is thrilled with his new RPG game, about wars between clans of vampires. In this game he plays a vampire that repeatedly comes into combat against vampires from other clans. Such battles are won or lost based on some characteristics of the opponents, with the help of a standard six-faced dice. For simplicity, we will consider only the fight between two vampires, Vampire 1 and Vampire 2. Each vampire has a vital energy (denoted respectively by *EV1* and *EV2*). Besides, an attack force *AT* and a damage capacity *D* are also given.

The combat is fought in turns, in the following way. At each turn, the dice is rolled; if the result value is less than or equal to ***AT***, Vampire 1 wins the turn, otherwise Vampire 2 wins. The winner then sucks the value ***D*** from the loser\'s vital energy. That is, ***D*** points are subtracted from the loser's vital energy and added to the winner's vital energy. The combat continues until one of the fighters has ***EV*** less than or equal to zero.

For example, suppose
***EV1**=7*,***EV2**=5*, ***AT**=2* and***D**=4*. The dice is rolled and the result value is *3*. Then, Vampire 2 wins the turn, and therefore *4* points are subtracted from
***EV1*** and added to
***EV2***. The new values for the vital energies would be
***EV1**=3*
and
***EV2**=9*. Notice that, if in the next turn Vampire 2 wins again, the combat ends. The values of ***AT*** and ***D*** are constant throughout the combat; only
***EV1*** and
***EV2*** vary.

Despite loving the game, Felipinho thinks that the combats are too long, and suspects that, given the initial values of
***EV1***,
***EV2***, ***AT*** and ***D***, it is possible to determine the probability of one of the players winning the combat, and that could help shorten the combat time. Felipinho has asked your help to verify his suspicion.

Input
-----

The input contains several test cases. Each test case is given in one single line, containing four integers
***EV1***,
***EV2***, ***AT*** and ***D*** separated by spaces (*1 â¤ **EV1**, **EV2** â¤ 10*, *1 â¤ **AT** â¤ 5* and *1 â¤ **D** â¤ 10*). The end of input is indicated by one line containing only four zeros, separated by spaces.

Output
------

For each test case in the input, your program must print a single line. The line must contain a real number representing, in terms of percentages, the probability that Vampire 1 wins the combat. The result must be printed as a real number with exactly one decimal figure.


| Input Sample | Output Sample |
| --- | --- |
| 1 1 3 1 1 2 1 1 8 5 3 1 7 5 2 4 0 0 0 0 | 50.0 3.2 61.5 20.0 |

Maratona de ProgramaÃ§Ã£o da SBC 2008.


# Problem 1138

Descrição
----------

Diana is going to write a list of all positive integers between **A** and **B**, inclusive, in base 10 and without any leading zeros. She wants to know how many times each digit is going to be used.

Input
-----

Each test case is given in a single line that contains two integers **A** and **B** (1 â¤ **A**â¤ **B**â¤ 108). The last test case is followed by a line containing two zeros.

Output
------

For each test case print a single line with 10 integers representing the number of times each digit is used when writing all integers between **A** and **B**, inclusive, in base 10 and without leading zeros. Write the counter for each digit in increasing order from 0 to 9.


| Input Sample | Output Sample |
| --- | --- |
| 1 9 12 321 5987 6123 12345678 12345679 0 0 | 0 1 1 1 1 1 1 1 1 1 61 169 163 83 61 61 61 61 61 61 134 58 28 24 23 36 147 24 27 47 0 2 2 2 2 2 2 2 1 1 |

ACM/ICPC South America Contest 2010.


# Problem 1161

Descrição
----------

Read two numbers M and N indefinitely. Calculate and write the sum of their factorial. Be carefull, because the result can have more than 15 digits.

Input
-----

The input file contains many test cases. Each test case contains two integer numbers M (0 â¤ M â¤ 20) and N (0 â¤ N â¤ 20). The end of file is determined by eof.

Output
------

For each test case in the input your program must print a single line, containing a number that is the sum of the both factorial (M and N).


| Input Sample | Output Sample |
| --- | --- |
| 4 4  0 0  0 2 | 48 2 3 |


# Problem 1163

Descrição
----------

In a far away land there are two cities, Nlogony, home of the Nlogonies, and Ducklogony, home of their neighbors, the Ducknese. These two cities have been at war for some time and now, in a try to win the war, the Ducknese intend to attack Nlogony with a slingshot that fires ducks. However, to avoid mistakes, they asked you to build a program that, given the values of the slingshot's height (**h**), the points where the Nlogony city begins (**p1**) and ends (**p2**), the shooting angle (**Î±**) and the launching speed, calculates if the projectile will hit the target.

  

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1163.jpg)

  

For the calculations, assume that the gravity's acceleration is g=9,80665 and that Ï = 3,14159.

Input
-----

There are various test cases, where each one starts with 1 floating point value **h**( 1 â¤ **h** â¤ 150) indicating the slingshot's height, containing, in the next line, 2 integer values **p1** and **p2**( 1 â¤ **p1, p2** â¤ 9999) indicating where Nlogony begins and ends, the next line containing 1 integer **n**(1 â¤ **n** â¤ 100) indicating the number of tries that will be made to hit the Nlogony and the **n** following lines containing 2 floating point values indicating the values of the launching's angle **Î±**(1 â¤ **Î±** â¤ 180) and speed **V**(1 â¤ **V** â¤ 150).  

  

The end of the input file is determined by EOF.

Output
------

For each shoot, your program must print a single line in the following format: âX -> DUCKâ for when the duck hits Nlogony or âX -> NUCKâ where the duck doesn't hit Nlogony, where **X** is the maximum distance that the projectile reached until reaching the ground (y = 0). X must be printed with an accuracy of 5 decimal places.


| Input Sample | Output Sample |
| --- | --- |
| 2.1 368 380 3 42.3 60 30 55 44 60.876842 | 367.76208 -> NUCK 270.72675 -> NUCK 379.83781 -> DUCK |

Acknowledgments to Ãber JessÃ© da Silva Peretto by the translation.



# Problem 1169

Descrição
----------

A queen requested the services of a monk and told him she would pay any price. The monk, needing food, asked the queen if the payment could be made in wheat grains arranged in a chessboard, so that in the first square it would be put only one grain, and in the subsequent squares twice as much as its previous square. The queen considered it a bargain and asked to the service be done. However, one of the riders who was present was good in math and warned that it would be impossible to execute the payment, because the amount of grain needed would be very high. The Queen then asked this gentleman who was good in calculation to develop a program that receives as input the number of squares to be used in a checkerboard and informs the amount of corresponding kg of wheat, knowing that 12 grains of the cereal correspond to one gram. Finally, the calculated amount should fit into an unsigned 64-bit integer number.

Input
-----

The first line of the input contains a single integer **N** (1 â¤ **N** â¤ 100), indicating the number of test cases. Each test case contains a single integer **X** (1 â¤ **X** â¤ 64), indicating the number of possible squares to be used.

Output
------

For each test case, print the quantity expected to be received by the monk, according to the following example.


| Input Sample | Output Sample |
| --- | --- |
| 3 7 19 14 | 0 kg 43 kg 1 kg |

Thanks to Cassio F.


# Problem 1170

Descrição
----------

On the planet Alpha lives the creature Blobs, that eats just half of its supply of food available all day. Write an algorithm that reads the initial capacity of the food supply (in Kg), and calculate how many days will pass before Blobs eat all this supply until left a kg or less.

Input
-----

The first line of the input contains a single integer **N** (1 â¤ **N** â¤ 1000), indicating the number of test cases. Each test case contains a single floating-point number **X** (1 â¤ **X** â¤ 1000), indicating the amount of food available for Blobs.

Output
------

For each test case, print one line containing the number of days that blobs will take to eat all their food supply, followed by the word "dias" that means days in portuguese.


| Input Sample | Output Sample |
| --- | --- |
| 3 40.0 200.0 300.0 | 6 dias 8 dias 9 dias |

Thanks to Cassio F.


# Problem 1193

Descrição
----------

The Julian math teacher has marked a test whose content will be on converting between decimal, hexadecimal and binary numbers. For Julian, this kind of convertion is one of the most complex things to be done. Regardless of the time spent for studying these contents, he simple doesn't understand. So, as you understand about computing and being a friend of Julian, he asked for your help to make a program that checks if the conversions made ââby him are correct.

Input
-----

The input contains many test cases. The first line of input contains an integer N indicating the number of test cases that follow, one by line. Each test case contains a number X (X > 0) followed by a Y text with three characters, indicating if the X number is in binary, decimal or hexadecimal. Regardless of the format, any of the numbers must fit into a 32-bit integer.

Output
------

For each test case, Julian wants you to print the number of the test case followed by two lines, that contains the original number converted for each one of the other two bases. The sequence of the bases of output is always: decimal, hexadecimal (lowercase) and binary, ie must respect this order obviously excluding the input format.

  

Note: should print a blank line after each test case, even after the last test case.


| Input Sample | Output Sample |
| --- | --- |
| 3 101 bin 101 dec 8f hex | Case 1: 5 dec 5 hex  Case 2: 65 hex 1100101 bin  Case 3: 143 dec 10001111 bin |


# Problem 1197

Descrição
----------

A particle has initial velocity and constant acceleration. If its velocity after certain time is v then what will its displacement be in twice of that time?

Input
-----

The input will contain two integers in each line. Each line makes one set of input. These two integers denote the value of **v** (-100 â¤ **v** â¤ 100) and t(0 â¤ **t** â¤ 200) ( **t** means at the time the particle gains that velocity). The end of the input is determined by EOF.

Output
------

For each line of input print a single integer in one line denoting the displacement in double of that time.


| Input Sample | Output Sample |
| --- | --- |
| 0 0 5 12 | 0 120 |

Thanks to Rezaul Alam Chowdhury


# Problem 1198

Descrição
----------

Hashmat is a brave warrior who with his group of young soldiers moves from one place to another to fight against his opponents. Before fighting he just calculates one thing, the difference between his soldier number and the opponent's soldier number. From this difference he decides whether to fight or not. Sometimes Hashmat's soldier number is greater than his opponent.

Input
-----

The input contains two integer numbers in every line. These two numbers in each line denotes the number of soldiers in Hashmat's army and his opponent's army or vice versa. The input numbers are not greater than 232. Input is terminated by End of File.

Output
------

For each line of input, print the difference of number of soldiers between Hashmat's army and his opponent's army. Each output should be in seperate line.


| Input Sample | Output Sample |
| --- | --- |
| 10 12 10 14 100 200 | 2 4 100 |


# Problem 1199

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1199.gif)

In this problem you are asked to write a simple base conversion program. It will be given a hexadecimal or decimal integer number as input. You have to output the corresponding decimal or hexadecimal number. Hexadecimal numbers always starts with a `0x' and all other numbers are to be considered as decimal numbers. There will be no invalid numbers in the input.

Input
-----

The input file contains several lines of input. Each line contains a single non-negative number, which may be a decimal or hexadecimal number as explained in the problem statement. The decimal value of this number will be equal or less than 231. A line containing a negative decimal number terminates the input. This number should not be processed. Input numbers will contain no space within them.

Output
------

For each line of input (Except the last one) produce one line of output. This line should contain the decimal or hexadecimal representation of the corresponding hexadecimal or decimal number. Like the input, the hexadecimal numbers in the output should be preceded by a "0x".


| Input Sample | Output Sample |
| --- | --- |
| 4 7 44 0x80685 -1 | 0x4 0x7 0x2C 525957 |


# Problem 1202

Descrição
----------

Every year, at the time of the so-called "white nights" when the sun does not set over the city of St. Petersburg is the "festival of arts of White Nights", which consists of a series of musical performances, concerts, ballets, and attracting more artists around the world.

  

It is considered one of the greatest demonstrations of all Russia, since the height of the white nights, the festival usually has up to one million participants roaming the city streets. The Mariinsky Theatre hosts some of the best shows and, since no tickets enough for everyone who wants to watch 'performances, often using a system curious and fun raffle for those who may enter the theater.

  

Each person entering the theater, interested in attending a presentation chooses a row in which I would sit and receives a card with a number from 000 to 999 written on it. This number is the code of the draw that person. Arriving `entry clerk verifies the situation queue in which the person sit. The line is described by a sequence of '1 's and '0' s, where 1 indicates free chair seat and 0 indicates busy. This sequence is then interpreted as a binary representation of the number *n*. The person enters with his entourage if the *n*th number of the Fibonacci sequence ends exactly with the number written on your card. Thus, for example, if the description of row 100 is not enter if the person owning the card with the number 003.

Input
-----

The input is composed of several instances. The first line of input contains an integer T indicating the number of instances. Each instance consists of a line containing a description of row with up to 10000 digits. The description of a row is a sequence of  '1' s and '0' s, never starting with '0' (the first chair of all ranks are reserved).

Output
------

For each instance print the 3 digits that must be written in the permission card that the person uses to entering the theater.


| Sample Input | Sample Output |
| --- | --- |
| 3 1 10 1010 | 001 001 055 |

Note: be a positive integer written in decimal base. The n-th number, f (n) of the Fibonacci sequence is defined as follows:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1202_en.png)

XVI Maratona de ProgramaÃ§Ã£o IME-USP, 2012. Thanks to Carlos E. Ferreira, USP.


# Problem 1212

Descrição
----------

Children are taught to add multi-digit numbers from right-to-left one digit at a time. Many find the "carry" operation - in which a 1 is carried from one digit position to be added to the next - to be a significant challenge. Your job is to count the number of carry operations for each of a set of addition problems so that educators may assess their difficulty.

Input
-----

Each line of input contains two unsigned integers less than 10 digits. The last line of input contains 0 0.

Output
------

For each line of input except the last you should compute and print the number of carry operations that would result from adding the two numbers, in the format shown below.

| Sample Input | Sample Output |
| --- | --- |
| 123 456 555 555 123 594 0 0 | No carry operation. 3 carry operations. 1 carry operation. |


# Problem 1213

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1213_a.gif)Given any integer **n** (1 â¤ **n** â¤ 10000) not divisible by 2 ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1213_c.gif)or 5, some multiple of **n** is a number which in decimal notation is a sequence of 1\'s. How many digits are in the smallest such a multiple of n?

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1213_b.gif)

Input
-----

The input consists in many test cases and ends with EOF. Each test case contains one integer **n** (1 â¤ **n** â¤ 10000) not divisible by 2 or 5.

Output
------

For each test case, print how many digits have the multiple of n that attends the above requisites.


| Sample Input | Sample Output |
| --- | --- |
| 3 7 9901 | 3 6 12 |


# Problem 1214

Descrição
----------

It is said that 90% of frosh expect to be above average in their class. You are to provide a reality check.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1214.jpg)

Input
-----

The input contains many test cases. The first line of standard input contains an integer **C**, the number of test cases. C data sets follow. Each data set begins with an integer, **N**, the number of people in the class (1 â¤ **N** â¤ 1000). N integers follow, separated by spaces or newlines, each giving the final grade (an integer between 0 and 100) of a student in the class.

Output
------

For each case you are to output a line giving the percentage of students whose grade is above average, rounded to 3 decimal places.


| Sample Input | Sample Output |
| --- | --- |
| 5 5 50 50 70 80 100 7 100 95 90 80 70 60 50 3 70 90 80 3 70 90 81 9 100 99 98 97 96 95 94 93 91 | 40.000% 57.143% 33.333% 66.667% 55.556% |


# Problem 1219

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1219_a.jpg)"Roses are red, violets are blue..."  

  

Millionaire Mr Smith is well-known -- not for his wealth, but for his odd sense of "art"... Mr Smith has got a circular garden. On the boundary he picks three points and gets a triangle. He then finds the largest circle in that triangular region. So he gets something like this (Please click here for a black-and-white version of the figure):

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1219_b.png)

Mr Smith then plants yellow sunflowers, blue violets and red roses in the way shown in the figure. (Nice combination, eh? :-) Given the lengths of the three sides of the triangle, you are to find the areas of the regions with each kind of flowers respectively.

Input
-----

Each line of input contains three integers **a**, **b**, **c**, the lengths of the three sides of the triangular region, with 0 < **a** â¤ **b** â¤ **c** â¤ 1000. The input is terminated by end of file (EOF).

Output
------

For each case, your program should output the areas of the regions with sunflowers, with violets and with roses respectively. Print your answers correct to 4 decimal places.


| Sample Input | Sample Output |
| --- | --- |
| 3 4 5 4 30 32 | 13.6350 2.8584 3.1416 954.8794 45.2993 8.2824 |

Tip 1: use for PI: 3.1415926535897 or the constant M\_PI of math library  
  

Tip 2: nbsp;https://www.mathopenref.com/heronsformula.html.  

  

A method for calculating the area of a triangle when you know the lengths of all three sides. Let a,b,c be the lengths of the sides of a triangle. The area is given by:  

  

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1219_c.gif) where p is half the perimeter, or (a + b + c) / 2


# Problem 1220

Descrição
----------

Some students are members of a club that travels annually to exotic locations. Their destinations in the past have included Indianapolis, Phoenix, Nashville, Philadelphia, San Jose, and Atlanta. This spring they are planning a trip to Eindhoven. The group agrees in advance to share expenses equally, but it is not practical to have them share every expense as it occurs. So individuals in the group pay for particular things, like meals, hotels, taxi rides, plane tickets, etc. After the trip, each student's expenses are tallied and money is exchanged so that the net cost to each is the same, to within one cent. In the past, this money exchange has been tedious and time consuming. Your job is to compute, from a list of expenses, the minimum amount of money that must change hands in order to equalize (within a cent) all the students' costs.

Input
-----

The input will contain the information for several trips. The information for each trip consists of a line containing a positive integer **n** (1 â¤ **n** â¤ 1000) indicating the number of students on the trip, followed by **n** lines of input, each containing the amount, in dollars and cents spent by a student. No student spent more than $10,000.00.  

  

A single line containing 0 follows the information for the last trip.

Output
------

For each trip, output a line stating the total amount of money, in dollars and cents, that must be exchanged to equalize the students' costs.


| Sample Input | Sample Output |
| --- | --- |
| 3 10.00 20.00 30.00 4 15.00 15.01 3.00 3.01 0 | $10.00 $11.99 |


# Problem 1221

Descrição
----------

Mary knows that a Prime Number is a number that is divisible only by 1 (one) and by itself. For example the number 7 is Prime, because it can be divided only by 1 and by 7. So she asked you to write a program that reads many numbers ââand inform if each one of these numbers are prime or not. But Patience is not one of the virtues of Mariazinha, so she wants that the execution of all test cases (instances) created by herself happen at the maximum in one second, because she hates waiting :>).

Input
-----

The first input line contains an integer **N** (1 â¤ **N** â¤ 200), corresponding to the number of test cases. Follow **N**  lines, each one containig one integer number **X** (1 < **X** < 231) that can be or not a prime number

Output
------

For each test case output the message âPrimeâ or âNot Primeâ according to the to following example.


| Sample Input | Sample Output |
| --- | --- |
| 3 123321 123 103 | Not Prime Not Prime Prime |


# Problem 1230

Descrição
----------

Given a positive integer *n*, denote by [*n*] the real interval {*x* : 0 â¤ *x* â¤ *n*}. A function *f* : [*n*] â R. Values of *f* are provided on a subset *S* of [*n*], thereby partially specifying *f*.

The set *S* satisï¬es the following properties:

1. The points in S are all integers.

2. The extremes 0 and *n* of [*n*] are both in *S*.

The function *f* satisï¬es the following properties:

1. The values of *f* in the integral points of [n] are integers.

2. For every integral point *x* in [*n*] \ *S* (ie, the integral points of [n] are not in S), the function f is monotonic in the interval [x â 1, x + 1]. In other words, at least one of the inequalities *f*(*x* â 1) â¤ *f*(*x*) â¤ *f*(*x* + 1) and *f*(*x* â 1) â¥ *f*(*x*) â¥ *f*(*x* + 1) is satisï¬ed.

3. For each non-integral point *x* in [*n*], the value of *f*(*x*) is given by the linear interpolation of *f*(â*x*â) and f(â*x*â), ie, *f*(*x*) = (*x* â â*x*â)*f*(â*x*â) + (â*x*â â *x*)*f*(â*x*â).

We still have the freedom of specifying the values of f in the integral points of [*n*] \ *S* (note however that *S* can contain all the integral points of [*n*]). We would like to use this ï¬exibility to make ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1230.png)*f*(*x*)dx = *y*, i.e., the area under *f*(x) between the extremes 0 and *n* equal to *y*, a given value. Your problem then is to decide whether this is possible or not.

Input
-----

The input contains several test cases. The ï¬rst line of a test case contains three integers, **N** (1 â¤ **N** â¤ 106), **M** and **Y** (0 â¤ **Y** â¤ 109), respectively the amplitude of the interval, the size of *S* and the value of **y**. Each of the following **M** lines describes function *f* at a point of *S*, containing two integers **X** (0 â¤ **X** â¤ **N**, â**X** â **S**) and **F** (0 â¤ **F** â¤ 106), representing *f**(X)* = **F**. The values of **X** are not necessarily in ascending order.

Note.:  ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1230.png) *f(x)dx* â¤ 109 for any assignment of values to *f*(*x*) para *x* â [*n*] \ **S** satisfying the stated constraints.

Output
------

For each test case, determine whether there is a value assignment to *f**(x)* for each integral point x â [n] \ *S* such that ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1230.png)*f*(*x*)*dx* = *y*, i.e. the area under *f**(x)* between the ends 0 and *n* is equal to *y*. If not, your program should print a line containing only the character âNâ. If the assignments are possible, your program should print a line containing the character âSâ, followed by values of *f**(x)* for the integral points *x* in [n] \ *S*, in increasing order of the values of x. The initial character and following values, if any, should be separated by a blank space. If more than one solution is possible, then print the lexicographically smallest solution.


| Sample Input | Sample Output |
| --- | --- |
| 5 6 10 0 2 1 2 5 2 2 2 3 2 4 2 5 2 10 0 0 5 10 2 2 5 0 1 2 2 10 3 18 0 2 6 4 10 0 2 2 1 0 0 2 1 | S S 0 0 0 5 N S 2 2 2 2 2 1 1 1 N |

Maratona de ProgramaÃ§Ã£o da SBC 2012


# Problem 1232

Descrição
----------

Probably everyone in this competition knows the Rubikâs Cube, a challenging 3-D puzzle. Each of it six sides is covered with nine labels, each label of a color (blue, yellow, orange, white, green and red). In its initial state, all nine labels on one face have the same color. One ingenious mechanism enables each face to be independently rotated, causing the colors of the labels on the sides to be mixed.  

  

Each of the faces of the Rubikâs Cube is denoted by a letter: F, B, U, D, L, and R, as illustrated in the figure below.

  

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1232.png)

  

U F D R L B The rotation of a face is called a movement. We describe the movements using the letters that identify the faces:

* a capital letter represents a 90o clockwise turn of the corresponding face;
* a lowercase letter represents a 90o counterclockwise turn of the corresponding face.

  

For example, F represents a 90o clockwise turn of face F; r represents a 90o counterclockwise turn of face R. A sequence of movements is denoted by a sequence of letters identifying faces. Thus, rDF represents a 90o counterclockwise turn of face R, followed by a 90o clockwise turn of face D, followed by a 90o clockwise turn of face F.  

  

An interesting property of the Rubikâs Cube is that any sequence of movements, if applied repeat- edly, causes the cube to return to its original state (the state it had before the first application of the sequence). For example, after four applications of the sequence B the cube returns to its original state.  

  

You must write a program that, given a sequence of movements, determines the minimum number of complete applications of that sequence to make the cube return to its original state.

Input
-----

The input contains several test cases. Each test case is described in a single line, which contains the sequence of movements. Note: Each sequence has at least one and at most 80 characters.

Output
------

For each test case your program must print a single line, containing a single integer, indicating the minimum number of complete applications of the given sequence to make the hub return to its original state.


| Sample Input | Sample Output |
| --- | --- |
| Rr LLL dl RUUdBd | 1 4 105 1260 |

Maratona de ProgramaÃ§Ã£o da SBC 2012


# Problem 1233

Descrição
----------

Fernando won a compass for his birthday, and now his favorite hobby is drawing stars: ï¬rst, he marks **N** points on a circumference, dividing it into **N** equal arcs; then, he connects each point to the *k-th* next point, until returning to the ï¬rst point.  

  

Depending on the value of *k*, Fernando may or may not reach all points marked on the circumference; when that happens, the star is called complete. For example, when **N** = 8, the possible stars are shown in the ï¬gure below. Stars (a) and (c) are complete, while stars (b) and (d) are not.

  

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1233.png)

  

Depending on the value of **N**, it may be possible to draw many diï¬erent stars; Fernando asked you to write a program that, given **N**, determines the number of complete stars he can draw.

Input
-----

The input contains several test cases. Each test case contains a single line, containing a single integer **N** (3 â¤ **N** < 231), indicating the number of arcs in which the circumference was divided.

Output
------

For each test case, your program must print a single line containing a single integer, indicating the number of complete stars that can be drawn.


| Sample Input | Sample Output |
| --- | --- |
| 3 4 5 18 36 360 2147483647 | 1 1 2 3 6 48 1073741823 |

Maratona de ProgramaÃ§Ã£o da SBC 2012


# Problem 1240

Descrição
----------

Paulinho have in your hands a little problem. The teacher asked him to make a program to verify from two integer numbers A and B, if B  corresponds to the last digit of A.

Input
-----

The input consists of several test cases. The first line of input contains an integer **N** that indicates the number of test cases. Each test case consists of two integers **A** (1 â¤ **A** < 231 ) e **B** (1 â¤ **B** < 231) positives.

Output
------

For each test case, print a message informing if the second number fit ("encaixa" in portuguese) or didn't fit ("nao encaixa") in the first number.


| Sample Input | Sample Output |
| --- | --- |
| 4 5678690 78690 5434554 543 1243 1243 54 654 | encaixa nao encaixa encaixa nao encaixa |


# Problem 1247

Descrição
----------

"Stop thief! Stop thief!" Stole the purse of an innocent lady who was walking on the beach and Nlogonia thief fled toward the sea. His plan seems obvious: he intends to take a boat and escape!  

  

The fugitive, who by now is aboard their vessel leakage, intends to follow the coast perpendicularly toward the limit of international waters, which is 12 nautical miles away, where will be saved from local authorities. Your boat can travel that distance at a constant speed of VF us.  

  

The Coast Guard intends to intercept him, and your boat has a constant speed of VG us. Assuming both boats departing the coast at exactly the same instant, with a distance of D nautical miles between them, can be possible that the Coast Guard reach the thief before the limit of international waters?  

  

Assume the coast of Nlogonia is perfectly straight and the sea calm enough, to allow a trajectory so as retilÃ­Ä±nea the coast.

Input
-----

The input consists of several test cases. Each test case is described in a line containing three integers,
**D** (1 â¤ **D** â¤ 100), **VF** (1 â¤ **VF** â¤ 100) and **VG** (1 â¤ **VG** â¤ 100), indicating the initial distance between the fugitive and the Coast Guard, the runaway boat speed and the Coast Guard boat speed.

Output
------

For each test case print a line containing 'S' if the Coast Guard can reach the fugitive before he exceeds the limit of international waters or 'N' otherwise.


| Sample Input | Sample Output |
| --- | --- |
| 5 1 12 12 10 7 12 9 10 10 5 5 9 12 15 | S N N N S |

Maratona de ProgramaÃ§Ã£o da SBC 2011


# Problem 1264

Descrição
----------

Have you heard the fact âThe base of every normal number system is 10â ? Of course, I am not talking about number systems like Stern Brockot Number System. This problem has nothing to do with this fact but may have some similarity.

You will be given an **N** based integer number **R** and you are given the guaranty that **R** is divisible by (**N**-1). You will have to print the smallest possible value for N. The range for N is (2 â¤ **N** â¤ 62) and the digit symbols for 62 based number is (0..9 and A..Z and a..z). Similarly, the digit symbols for 61 based number system is (0..9 and A..Z and a..y) and so on.

Input
-----

Each line in the input file will contain an integer number **N** of any integer base (2..62) with up to 1024 digits. You will have to determine what is the smallest possible base of that number for the given conditions. No invalid number will be given as input.

Output
------

If number with such condition is not possible output the line âsuch number is impossible!â For each line of input there will be only a single line of output. The output will always be in decimal number system.


| Sample Input | Sample Output |
| --- | --- |
| 3 5 A -45678901234567890ABC -nnnnnnnnnnnnnnnnnnnn -oooooooooooooooooooooooooooo ggggggggggggggggggggggggggg | 4 6 11 14 50 51 43 |


# Problem 1279

Descrição
----------

The ancient race of Gulamatu is very advanced in their year calculation scheme. They understand what leap year is (A year that is divisible by 4 and not divisible by 100 with the exception that years that are divisible by 400 are also leap year.) and they have also similar festival years. One is the Huluculu festival (happens on years divisible by 15) and the Bulukulu festival (Happens on years divisible by 55 provided that is also a leap year). Given an year you will have to state what properties these years have. If the year is not leap year nor festival year, then print the line 'This is an ordinary year.' The order of printing (if present) the properties is leap year-->huluculu-->bulukulu.

Input
-----

Input will contain several years as input. Each year will be in separate lines. Input is terminated by end of file. All the years will not be less than 2000 (to avoid the earlier different rules for leap years) but can have more than 1000 digits.

Output
------

For each input, output the different properties of the years in different lines according to previous description and sample output. A blank line should separate the output for each line of input. Note that there are four different properties.


| Sample Input | Sample Output |
| --- | --- |
| 2000 3600 4515 2001 | This is leap year.  This is leap year. This is huluculu festival year.  This is huluculu festival year.  This is an ordinary year. |

Adapted by Neilor.


