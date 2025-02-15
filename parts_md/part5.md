# Problem 1729

Descrição
----------

A relay is a race for two or more teams of runners. Each member of a team runs one section of the race. Your task is to help to evaluate the results of a relay race.   

You have to process several teams. For each team you are given a list with the running times for every section of the race. You are to compute the average time per kilometer over the whole distance. That's easy, isn't it?

So if you like the fun and challenge competing at this contest, perhaps you like a relay race, too. Students from Ulm participated e.g. at the "SOLA" relay in Zurich, Switzerland. For more information visit http://www.sola.asvz.ethz.ch/ after the contest is over.

Input
-----

The first line of the input specifies the number of sections **N** followed by the total distance of the relay **D** in kilometers. You may safely assume that 1<=**N**<=20 and 0.0<**D**<200.0. Every following line gives information about one team: the team number **T** (an integer, right-justified in a field of width 3) is followed by the n results for each section, separated by a single space. These running times are given in the format "h:mm:ss" with integer numbers for the hours, minutes and seconds, respectively. In the special case of a runner being disqualified, the running time will be denoted by "-:--:--". Finally, the data on every line is terminated by a newline character. Input is terminated by EOF.

Output
------

For each team output exactly one line giving the team's number t right aligned in a field of width 3, and the average time for this team rounded to whole seconds in the format "m:ss". If at least one of the team's runners has been disqualified, output "-" instead. Adhere to the sample output for the exact format of presentation.


| Sample Input | Sample Output |
| --- | --- |
| 2 12.5   5 0:23:21 0:25:01  42 0:23:32 -:--:--   7 0:33:20 0:41:35 | 5: 3:52 min/km  42: -   7: 6:00 min/km |

University of Ulm local Contest 2001/2002.


# Problem 1734

Descrição
----------

Signals of most probably extra-terrestrial origin have been received and digitized by The Aeronautic and Space Administration (that must be going through a defiant phase: "But I want to use feet, not meters!"). Each signal seems to come in two parts: a sequence of n integer values and a non-negative integer t. We'll not go into details, but researchers found out that a signal encodes two integer values. These can be found as the lower and upper bound of a subrange of the sequence whose absolute value of its sum is closest to t.

You are given the sequence of n integers and the non-negative target t. You are to find a non-empty range of the sequence (i.e. a continuous subsequence) and output its lower index l and its upper index u. The absolute value of the sum of the values of the sequence from the lth to the uth element (inclusive) must be at least as close to t as the absolute value of the sum of any other non-empty range.

Input
-----

The input file contains several test cases. Each test case starts with two numbers **n** (1 â¤ **n** â¤ 105) and **k**. Input is terminated by **n** = **k** = 0. Otherwise, follows **n** integers with absolute values lower than 104 which constitute the sequence. Then follows **k** queries for this sequence. Each query is a target **t** (0 â¤ **t** â¤ 109).

Output
------

For each query output 3 numbers on a line: some closest absolute sum and the lower and upper indices of some range where this absolute sum is achieved. Possible indices start with 1 and go up to **n**.


| Sample Input | Sample Output |
| --- | --- |
| 5 1  -10 -5 0 5 10  3  10 2  -9 8 -7 6 -5 4 -3 2 -1 0  5 11  15 2  -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  15 100  0 0 | 5 4 4  5 2 8  9 1 1  15 1 15  15 1 15 |

University of Ulm local Contest 2001/2002.


# Problem 1735

Descrição
----------

A tree (i.e. a connected graph without cycles) with vertices numbered by the integers 1, 2, ..., n is given. The "Prufer" code of such a tree is built as follows: the leaf (a vertex that is incident to only one edge) with the minimal number is taken. This leaf, together with its incident edge is removed from the graph, while the number of the vertex that was adjacent to the leaf is written down. In the obtained graph, this procedure is repeated, until there is only one vertex left (which, by the way, always has number n). The written down sequence of n-1 numbers is called the Prufer code of the tree.

Your task is, given a tree, to compute its Prufer code. The tree is denoted by a word of the language specified by the following grammar:

T ::= "(" N S ")"

S ::= " " T S

| empty

N ::= number

That is, trees have parentheses around them, and a number denoting the identifier of the root vertex, followed by arbitrarily many (maybe none) subtrees separated by a single space character. As an example, take a look at the tree in the figure below which is denoted in the first line of the sample input.

Note that, according to the definition given above, the root of a tree may be a leaf as well. It is only for the ease of denotation that we designate some vertex to be the root. Usually, what we are dealing here with is called an "unrooted tree".

![](https://resources.beecrowd.com/gallery/images/promocao/code%20de%20tree.gif)

Input
-----

The input contains several test cases. Each test case specifies a tree as described above on one line of the input file. Input is terminated by EOF. You may assume that 1 â¤ **n** â¤ 50.

Output
------

For each test case generate a single line containing the Prufer code of the specified tree. Separate numbers by a single space. Do not print any spaces at the end of the line.


| Sample Input | Sample Output |
| --- | --- |
| (2 (6 (7)) (3) (5 (1) (4)) (8)) (1 (2 (3))) (6 (1 (4)) (2 (3) (5))) | 5 2 5 2 6 2 8 2 3 2 1 6 2 6 |

University of Ulm local Contest 2001/2002.


# Problem 1736

Descrição
----------

A tree (i.e. a connected graph without cycles) with vertices numbered by the integers 1, 2, ..., **n** is given. The "PrÃ¼fer" code of such a tree is built as follows: the leaf (a vertex that is incident to only one edge) with the minimal number is taken. This leaf, together with its incident edge is removed from the graph, while the number of the vertex that was adjacent to the leaf is written down. In the obtained graph, this procedure is repeated, until there is only one vertex left (which, by the way, always has number **n**). The written down sequence of **n-1** numbers is called the PrÃ¼fer code of the tree.

Your task is, to reconstruct a tree, given its PrÃ¼fer code. The tree should be denoted by a word of the language specified by the following grammar:

T ::= "(" N S ")"  

S ::= " " T S  

    | empty  

N ::= number

That is, trees have parentheses around them, and a number denoting the identifier of the root vertex, followed by arbitrarily many (maybe none) subtrees separated by a single space character. As an example, take a look at the tree in the figure below which is denoted in the first line of the sample output.

Note that, according to the definition given above, the root of a tree may be a leaf as well. It is only for the ease of denotation that we designate some vertex to be the root. Usually, what we are dealing here with is called an "unrooted tree".

![](https://resources.beecrowd.com/gallery/images/promocao/decode%20the%20tree.gif)

Input
-----

The input contains several test cases. Each test case specifies the PrÃ¼fer code of a tree on one line. You will find **n-1** numbers separated by a single space. Input is terminated by EOF. You may assume that 1 â¤ **n** â¤ 50.

Output
------

For each test case generate a single line containing the corresponding tree, denoted as described above. Note that, in general, there are many ways to denote such a tree: choose your favorite one.


| Sample Input | Sample Output |
| --- | --- |
| 5 2 5 2 6 2 8 2 3 2 1 6 2 6 | (8 (2 (3) (5 (1) (4)) (6 (7)))) (3 (2 (1))) (6 (1 (4)) (2 (3) (5))) |

University of Ulm local Contest 2001/2002.


# Problem 1745

Descrição
----------

Substrings are strings formed by choosing a subset of contiguous characters from a string. This is well known. A little more obscure is the definition of substhreengs. A substhreeng is a substring which complies to the following additional requirements:

1. It is non-empty, and composed entirely of base 10 digits.

2. Interpreted in base 10 (allowing extra leading zeros), the resulting integer is a multiple of 3.

For instance, the string â130a303â contains 9 substhreengs: the substhreeng â3â three times, the substhreengs â30â and â0â twice each, and the substhreengs â303â and â03â once each. The substring â30a3â is not a substhreeng because it is not composed entirely of base 10 digits, while the substring â13â is not a substhreeng because 13 is not a multiple of 3.

Notice that two substhreengs are considered different if they are different in length or start at a different position, even if the selected characters are the same.

Given a string, you are asked to count the number of substhreengs it contains.

Input
-----

The input consists of a single line that contains a non-empty string **S** of at most 10 6 characters. Each character of **S** is either a digit or a lowercase letter.

Output
------

Output a line with an integer representing the number of substhreengs contained in **S**.


| Input Samples | Output Samples |
| --- | --- |
| 130a303 | 9 |

| 0000000000 | 55 |

| icpc2014regional | 2 |

ACM/ICPC Latin America Contest 2014.


# Problem 1754

Descrição
----------

In an attempt to stop Super Buu, Goten and Trunks entered the Time Room to train. Time passes faster inside this room (1 second outside the room might be equivalent to seconds, minutes, hours or even days inside the room). Goten and Trunks need X seconds to finish training, however Super Buu has become impatient and ordered Mr. Picollo to take him to his opponents immediately.

Mr. Picollo used his telephatic powers to alert the boys (who had done nothing so far but playing around the room) and they started training immediately.

Mr. Picollo did his best to delay the path to the Time Room, taking Y to do so.

Let K be the number of seconds that passes inside the room during 1 second outside it. Find the smallest value for K that'll give the boys enough time to finish their training before Super Buu's arrival. Consider that the boys have plenty Senzu Beans therefore they will never need to stop training to rest and the training ends when Super Buu get through the entrance door.

Input
-----

The first input line contains an integer **T** (1 â¤ **T** â¤ 100), the number of test cases. The following **T** lines contain 2 integers each: **X** (1 â¤ **X** â¤ 1015) e **Y** (1 â¤ **Y** â¤ 105), the time needed to finish the training and Super Buu's path time, respectively.

Output
------

For each test case output a single line containing the integer **K**.


| Input Sample | Output Sample |
| --- | --- |
| 2  7 4  8 4 | 2  2 |

Contest Peixoto 2014


# Problem 1756

Descrição
----------

Some computer science courses are too much theorical and sometimes boring. In an attempt to raise the students' interest in some topics, the Artificial Intelligence professor, always when possible, propose a challenging contemplating the topics seen in class that day.

Today's lecture was about genetic algorithms and the professor explained the following procedure:

From 2 individuals (two sequences of N bits: x0x1...xN-1) A and B, we choose a cut position Y ( 1 â¤ Y < N) and the crossover process happens, creating 2 new individuals: the first one is the concatenation of bits x0...xY-1 from individual A followed by bits xY..xN-1 from individual B, the second one is the concatenation of bits x0...xY-1 from individual B followed by bits xY..xN-1 from individual A.

The following image shows the result of a crossover with Y = 5.

![](https://resources.beecrowd.com/gallery/images/contests/C_01.png)

After the crossover, each bit from the brand-new individuals may suffer mutation (change its value) according to a specified mutation probability **P**.

The challenge's statement left by the professor was the following:

"Write a program that takes as input 3 individuals, the cutting position and the mutation probability. The program must calculate the probability of obtaining the third individual as a result of a crossover between the other two."

Input
-----

The first line of input contains an integer **T** (1 â¤ **T** â¤ 50), the number of test cases.

Each test case takes 5 lines.

The first line contains an integer **N** (2 â¤ **N** â¤ 8), the number of bits in each individual.

The second line contains an integer **Y** (1 â¤ **Y** < **N**) followed by a floating-point number **P** (0 â¤ **P** â¤ 1), the cut position and the mutation probability, respectively.

The third line contains the first individual to be crossedover.

The fourth line contains the second individual to be crossedover.

The fifth line contains the individual that will be compared to the possible crossover results.

Output
------

For each test case output a single line containing the answer with 7 digits after the decimal point.


| Input Sample | Output Sample |
| --- | --- |
| 4 3 2 0 111 111 111 2 1 0.5 11 11 10 4 2 0.1 1010 0001 1111 2 1 0.1 11 11 11 | 1.0000000 0.4375000 0.0089927 0.9639000 |

Contest Peixoto 2014


# Problem 1760

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1760.gif)

Lapland is a quiet and very cold place. There is not much to do there after Christmas (where the elves work diligently in Santa's toy factory). The marasmus has made the elf Tod review research about the only thing that could be seen in Lapland: Snow.

In their studies, Tod found very interesting things about the snowflakes. How did incessant search the sites for information about snowflakes, eventually finding links that talk about a theory called Koch Snowflake.

Tod found the very interesting theory because the Koch snowflake is a fractal that is obtained from an equilateral triangle. Then divide each of its sides into three equal parts and added, from each middle section, a new equilateral triangle of side equal to 1/3 of the measure on the side of the initial triangle.

At each iteration fractal perimeter and after n iterations increases, it tends to infinity but remains smaller area than the area of the circle surrounding the original triangle. Thus, an infinitely long line is surrounded by a finite area.

Based on this information and knowing that the area of a triangle is equal to l2 â3 /4 (where *l* is equal to measure the length of a side of the equilateral triangle) your task is to help Tod find the area of a Koch snowflake based on the measurement of the length of side of the equilateral triangle given.

Input
-----

The input has several test cases and consists of an integer **l** (1mm â¤ *l* â¤ 1000mm) that represents a measure of the length of one side of the equilateral triangle. The end of input is determined by EOF.

Output
------

The output should show the value Koch Snowflake area with two decimal places.


| Input Sample | Output Sample |
| --- | --- |
| 2  3  4 | 2.77  6.24  11.09 |

Contest de Natal 2014


# Problem 1761

Descrição
----------

This Christmas, Santa Claus appointed some of his most dedicated elves to decorate the yard in the present manufacturing at the North Pole. The yard has several pine trees of various sizes. Santa Claus instructed the elves to decorate a tree with string of lights, their size should be 5 times the size of the tree.

To find the height of each tree, Santa Claus gave them an old theodolite (instrument used to measure angles) and ordered them to use trigonometric concepts to find the height of each tree.

Your task is to help the elves to find a way to calculate the amount of string of lights needed for each tree.

Consider for this challenge that the theodolite is positioned at the height of each elf and that this point needs to be computed. The theodolite inform values in degrees. In this problem consider PI as 3.141592654.

Input
-----

The input is composed by several test cases. Each test case consists of a double value **A** that is the angle calculated by the theodolite (1.00 < **A** < 90.00), a value double **B** (1 â¤ **B** â¤ 100) corresponding to the distance between the theodolite and the tree and a value double **C** (0.50 â¤ **C** â¤ 1.50) which is the height in metres of the elf who is measuring the angle. The end of input is determined by EOF.

Output
------

You should show the amount string of lights needed to adorn each tree. Note: Decimal values should be rounded to 2 decimal places.


| Input Sample | Output Sample |
| --- | --- |
| 57.25 57.34 0.98  54.83 46.49 1.47  36.23 19.29 1.46 | 450.63  337.24  77.97 |

Contest de Natal 2014


# Problem 1776

Descrição
----------

The class of Computer Science of CIn-UFPE 2025.1 is graduating! It is a very special graduation, not only because all major projects of students in this class have become multinational corporations, but also because the number 2025 is a perfect square! Therefore, the students decided to make all numbers of the ceremony a perfect square: dates, number of guests, hash of the name of the class, the amount of students graduating, etc.

The party organizers were able to meet this requirement until the time comes to buy the snacks. They came into boxes with N snacks at a time. If N is not a perfect square, they will have to buy more than one box. Help the party organizers by making a program to calculate the minimum number of snacks they should buy to meet the eccentric requirements of the students.

Input
-----

The first line contains an integer **T** (1 â¤ **T** â¤ 1000), the number of test cases. Each of the next **T** lines contains an integer **N** (1 â¤ **N** â¤ 10â¹), the number of snacks that comes in a single box.

Output
------

For each test case print a line with "Caso #**X**: **Y**", where **X** is he number of the current case, starting with 1, and **Y** is the minimum number of snacks that the party organizers should buy.


| Input Sample | Output Sample |
| --- | --- |
| 5 5 9 10 12 13 | Caso #1: 25 Caso #2: 9 Caso #3: 100 Caso #4: 36 Caso #5: 169 |

AdaptaÃ§Ã£o da Prova Final da Seletiva UFPE - 2014


# Problem 1785

Descrição
----------

The number 6174 is known as Krapekarâs constant after the Indian mathematician Dattathreya Ramachandra Kaprekar. This number is interesting because of the following fact: let X be any 4-digit number (leading 0âs are allowed) in which not all of them are the same, then Krapekarâs routine starting at this number always converge to 6174. That is, Krapekarâs routine converges to 6174 if, and only if, X is a 4-digit number and at least two of them are pairwise different. Krapekarâs routine is defined as follows:

  

int krapekar(int X) {

   int cnt = 0;

   while (X != 6174) {

       int hi = highest\_number\_with\_digits\_of(X);

       int lo = lowest\_number\_with\_digits\_of(X);

       X = hi - lo;

       cnt = cnt + 1;

   }

   return cnt;

}

  

highest\_number\_with\_digits\_of(X) is the highest number that can be made using Xâs digits.

lowest\_number\_with\_digits\_of(X) is the lowest number that can be made using Xâs digits.

  

For example:

highest\_number\_with\_digits\_of(3524) = 5432

lowest\_number\_with\_digits\_of(3524) = 2345

highest\_number\_with\_digits\_of(10) = 1000 //because 10 = 0010 with four digits.

lowest\_number\_with\_digits\_of(10) = 1

Input
-----

The first line contains an integer **T** (1 â¤ **T** â¤ 10â´), the number of test cases. Each test case consists of a line containing an integer **X** (0 â¤ **X** â¤ 9999).

Output
------

For each test case print âCaso #**X**: **Y**â, where **X** is the number of the current case, starting at 1, and **Y** is the return of Krapekarâs routine or -1 in case it stays in an infinite loop.


| Input Sample | Output Sample |
| --- | --- |
| 3 3524 0 10 | Caso #1: 3 Caso #2: -1 Caso #3: 5 |

AdaptaÃ§Ã£o da Prova Final da Seletiva UFPE - 2014


# Problem 1795

Descrição
----------

The trinomial triangle is a number triangle of trinomial coefficients. It can be obtained by starting with a row containing a single "1" and the next row containing three 1s and then letting subsequent row elements be computed by summing the elements above to the left, directly above, and above to the right:

![](https://resources.beecrowd.com/gallery/images/contests/tritri.png)

The first row of the trinomial triangle is numbered as zero, the second row is numbered as one and so on.

Given the row number *R*, you are asked to write a program that prints the sum of its elements. For instance, the sum of elements at row 2 is 9 = 1 + 2 + 3 + 2 + 1.

Input
-----

The input is the row number *R* (0 â¤ *R* â¤ 20).

Output
------

The output is the sum of all elements at row *R*. Don't forget the end-of-line character after printing the sum.


| Input Samples | Output Samples |
| --- | --- |
| 0 | 1 |

| 1 | 3 |

| 2 | 9 |

Contest Oficial de Aquecimento da OlimpÃ­ada Brasileira de InformÃ¡tica 2015


# Problem 1801

Descrição
----------

Prof. Cedrado-Cueta likes to play with numbers, and he is particularly fond of perfect squares. A natural number *n* is said to be a perfect square if there exists a natural number *m* such that *n* = *m*2. For example, 9 and 36 are perfect squares because 9 = 32 and 36 = 62, whereas 5 and 12 are not perfect squares.

The Prof. recently found a number *x*, and he would like to create a perfect square using it. In order to do so, he will reorder the digits of *x* to form some number *y*, and then calculate *n* = *x* + *y*. In how many ways is it possible for him to obtain a perfect square as the value of *n*? For example, if *x* = 29 the Prof. can take *y* = 92, so that *n* = 29 + 92 = 121 = 112.

Note that when reordering the digits of *x* the Prof. should use all its digits and obtain a correct expression for the number *y*, i.e. there can be no leading 0's in *y*. Also note that he may choose to keep the digits of *x* in the same order, effectively getting for *y* the same value as *x*.

Input
-----

The input consists of a single line containing one positive integer number *x* with at most 12 digits.

Output
------

The output consists of a single line containing one integer number representing the number of ways in which the Prof. can obtain a perfect square as the value of *n*. Two ways are considered different if they differ in the value of *n* obtained.


| Input Samples | Output Samples |
| --- | --- |
| 2 | 1 |

| 511 | 0 |

| 1234567890 | 67 |

Contest Oficial de Aquecimento da OlimpÃ­ada Brasileira de InformÃ¡tica 2015


# Problem 1805

Descrição
----------

One natural number is a non-negative integer (0, 1, 2, 3, 4, 5,...). Your task in this problem is to calculate the sum of the natural numbers that are present in a given interval [**A**, **B**] including.

For instance, the sum of the natural numbers in the range [2, 5] is 14 = (2 + 3 + 4 + 5).

Input
-----

The test case contains two integers **A** e **B** (1 â¤ **A** â¤ **B** â¤ 109), representing the lower limit and the upper respectively.

Output
------

For each test, the output consists of one line containing the sum of natural numbers in the range.


| Input Sample | Output Sample |
| --- | --- |
| 1 5 | 15 |

| 1 1000 | 500500 |
| --- | --- |

| 10 20 | 165 |
| --- | --- |

Contest Oficial de Aquecimento da OlimpÃ­ada Brasileira de InformÃ¡tica 2015


# Problem 1807

Descrição
----------

The trinomial triangle is a number triangle of trinomial coefficients. It can be obtained by starting with a row containing a single "1" and the next row containing three 1s and then letting subsequent row elements be computed by summing the elements above to the left, directly above, and above to the right:

![](https://resources.beecrowd.com/gallery/images/contests/tritri.png)

The first row of the trinomial triangle is numbered as zero, the second row is numbered as one and so on.

Given the row number *R*, you are asked to write a program that prints the sum of its elements. For instance, the sum of elements at row 2 is 9 = 1 + 2 + 3 + 2 + 1.

But this time the row number *R* can be much bigger! Thereby the sum of elements at row *R* must be printed modulo (231 - 1). For instance, the sum of elements at row 20 is 3486784401 but the expected answer is 1339300754, which is congruent to 3486784401 modulo (231 - 1).

Input
-----

The input is the row number **R** (0 â¤ **R** â¤ 999999999).

Output
------

The output is the sum modulo (231 - 1) of all elements at row **R**. Don't forget the end-of-line character after printing the sum.


| Input Samples | Output Samples |
| --- | --- |
| 0 | 1 |

| 2 | 9 |

| 20 | 1339300754 |

Contest Oficial de Aquecimento da OlimpÃ­ada Brasileira de InformÃ¡tica 2015


# Problem 1812

Descrição
----------

The Science Academy of Czech Republic, worried about the summer floods in Prague, is fostering the development of a new computational cluster, it has, among other tasks, to make a more accurate weather forecast. This new cluster is composed by m equally machines working in parallel. Because of budget reasons, each machine may process only a task at once, and each task can not be processed in more than one machine simultaneously. The cluster allows, however, pre-emption. In other words, it is possible to interrupt the execution of a task and return it posteriorly, in other machine if necessary.

You've been invited to an Computer Science related event to develop a preliminary version of task scheduler of the cluster, since you were in Prague. In this version, it's provided a set of tasks T, in which one task t â T has:

* A process requirement pt that denotes the number of time units needed to accomplish the task;
* A release moment rt, that represents the time unit from which the task is available to processing (it could be waiting data, for example);
* A value dt â¥ pt + rt, that indicates the first moment, in time units, in which the task shall, imperatively, be done. In other words, the task t must be held in range [rt , dt).

Your scheduler must receive that data, accordingly with the format described below and it must tell if there is or not a viable scheduling, or in other words, a scheduling that completes every task in the time interval allowed.

Input
-----

Your scheduler must be prepared to work with various instances of input. Each instance follows this format. On the first line are provided the number of machines, 0 â¤ **m** â¤ 100, and tasks, 0 â¤ **n** â¤ 1000, respectively. On the next **n** lines are provided the values **p****t** â¥0, **r****t** â¥ 0 and **d****t** â¥ 0 (one triple per line) for the tasks **t** â T. The instants **rt** and **dt** are integers, and **pt** is decimal. Values **m** = 0 and **n** = 0 indicates that the instances processing is finished and there's nothing more to process. All the input values of the same line are separated by any number of empty spaces.

Output
------

For each solved instance, you must print an identifier Instance h, in which **h** is an integer number, sequential and crescent starting from 1. On the next line it must be printed Viable or Not Viable, depending of the scheduling for the instance if it's viable or not, respectively. An empty line must separate each instance output.


| Sample Input | Sample Output |
| --- | --- |
| 3 4  1.5 3 5  1.25 1 3  2.1 3 7  3.6 5 9  3 1  3 1 2  0 0 | Instance 1  Viable  Instance 2  Not Viable |

VII Maratona de ProgramaÃ§Ã£o IME-USP 2003.


# Problem 1815

Descrição
----------

In the winters of Praga the cold is unbearable. To keep the body warm, many locals use warm drinks (like coffee or tea for example) or alcoholic drinks. Sometimes, Mr. TÅeboÅ frequents a small bar from his neighborhood. However, after several hours, some end up exaggerating on the doses. In this moment, Mr. TÅeboÅ needs to return to his house. The problem is that he's not feeling well (actually he's drunk :-) and he doesn't remember where he lives. So he begins ringing the houses' bells to ask if he lives there. He does that until he finds his house. Due to his state, Mr. TÅeboÅ won't follow any logical order to ring the houses' bells. After ringing a bell and verifying that that house isn't his, he will keep searching. Also he can't memorize which bells he already rang. The way he chooses the houses to have their bells rang follows a distribution of probability conditioned only to the last house visited. Consider that someone always answers the door and responds to Mr. TÅeboÅ if he lives
there or not. We want to know his chances of not getting home to sleep, knowing that after ringing a ceirtain number of bells he won't be able to carry on and he'll end up staying there.

Input
-----

The input file has the following composition for each instance: the first line contain the integers 0 â¤ **n** â¤ 100, 0 < **t** â¤ **n**, 0 < **k** â¤ **n**, 0 < **m** â¤ 100, representing the number of houses, the initial house, Mr. TÅeboÅ's house and the quantity of houses that he can visit to try to get home, respectively. Then **n** lines are gaven. The **i**-th line represents the house **i** and contain the numbers **ai1**, ... , **aij**, ... , **ain**, separated by whitespaces, representing the probability of Mr. TÅeboÅ to go from **i** to **j**. The input ends with **n** = 0.

Output
------

The output file must contain, for each input instance, an indentifier **Instancia h** (Instance h), where **h** is an integer, sequential and ascending starting from 1. In the following line, a number (rounded to 6 decimals) indicating the probability of Mr. TÅeboÅ not have found his house after m bells rang. A blank line must separate the output of each instance, including the last.


| Sample Input | Sample Output |
| --- | --- |
| 2 1 2 1 0.5 0.5 0.5 0.5 3 1 2 2 0.25 0.25 0.5 0.25 0.5 0.25 0.5 0.25 0.25 0 | Instancia 1 0.500000  Instancia 2 0.562500 |

VII Maratona de ProgramaÃ§Ã£o IME-USP 2003.


# Problem 1819

Descrição
----------

China is a major producer of food, but also huge consumer. Chinese researchers discover that in certain moments of their history the agricultural production was higher than consumption, and at other times this situation was reversed. Worried with the future of the great nation, they started to collect data about the plantation area, the quantity of workers e the agricultural production. To better investing their resources , now they want to make a forecast about the production of the country.

The data set that the researchers collect is composed by triples (Xi, Yi, Zi), where Xi representes the area of plantation, Yi the quantity of workers and Zi the agriculture production. As this production is directly linked with the other data collected, they decided to estimate the future production using a linear function a1+a2x+a3y, that minimizes the sum of the square errors

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1819.png)

where n is the total of triples availables. Thus they will be capable to better plan the production and the consume of the next years. Your goal is to calculate the desired linear function.

Input
-----

The input consistes of many instances. For each input instance is given one integer number 3 â¤ **n** â¤ 1000 indicating how much triples was obtained in the data collection. In each one of the next lines is given a triple **Xi**, **Yi** and **Zi** as acreage (thousand acres), the number of workers involved (given in thousands), and agricultural production (given in tonnes of food), respectively. The input file ends when **n** = 0 is found. Assume that there is no linear relationship between the number of workers and the acreage, then, there is no constants Î±,Î² such that, for every i, Xi= Î±yi + Î². Assume also that 0 â¤ **X**i,**Y**i,**Z**i â¤ 1000 and that all data values are integers.

Output
------

For each instance solved, you may print a identifier Instance **h** where **h** is a integer number, sequential and growing from 1. On the next line, you may print 3 numbers **a1**, **a2** and **a3**, representing the quotients of the requested linear function. These numbers need to be represented in three decimal places.

A blank line shoud divide the output of each instance


| Sample Input | Sample Output |
| --- | --- |
| 3  1 0 0  5 1 1  3 2 2  5  1 3 2  3 7 3  5 10 4  7 400 5  9 4 6  0 | Instancia 1  0.000 0.000 1.000  Instancia 2  1.500 0.500 0.000 |

VIII Maratona de ProgramaÃ§Ã£o IME-USP 2004.


# Problem 1829

Descrição
----------

Lucas and Pedro are high school friends. They were really impressed after a math class that introduced factorial numbers:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1829.png)

where *n* is a natural number and 0! = 1. They have a question: what is the operation that produces the biggest number, factorial or exponential?

Trying to find out the answer, both proposed the Biggest Number Game. In this game, two players call, at same time, as fast as they can, an operation that results in a big number. The player that calls the operation that results in the biggest number is the winner. Beto, friend of both, was the judge: he wrote down the operations. Lucas only called exponentials and Pedro only called factorials.

At the end of game, none of the three friends could tell who was the winner. Write a program that helps them to decide who won each round and who was the champion (the player that won most rounds).

Input
-----

The first line contains an integer **N** (**N** â¤ 1.000), indicating the number of rounds played.

Each round is described by two lines: the first contains Lucas's exponential, in the form **a**^**b** (2 â¤ **a, b** â¤ 10.000); the second contains Pedro's factorial, in the form **n**! (2 â¤ **n** â¤ 10.000). The numbers **a, b, n** are integers and the expression **a**^**b** means "**a** raised to the **b**-th power".

Output
------

The first line of the output must be the message "Campeao: **C**!", where **C** is the champion, or the message "A competicao terminou empatada!", if the game was a tie.

After the initial message, for each round played must be printed the message "Rodada #**r**: **V** foi o vencedor", where **r** is the round number (the couting starts on one) and **V** is the winner of the round **r**.

Any printed message must be followed by a newline character.


| Input Samples | Output Samples |
| --- | --- |
| 4  99^99  100!  57^199  874!  123^488  123!  7601^5684  7449! | A competicao terminou empatada!  Rodada #1: Lucas foi o vencedor  Rodada #2: Pedro foi o vencedor  Rodada #3: Lucas foi o vencedor  Rodada #4: Pedro foi o vencedor |

Translation reviewed by Gustavo Jaruga


# Problem 1830

Descrição
----------

A chocolate factory produces three kinds of chocolates. The basic ingredients to make a unit of each kind are listed bellow:

Crocante:
peanut (5g), white chocolate (25g) and milk chocolate (20g);
Misto:
white chocolate (25g) and milk chocolate (25g);
Tradicional:
milk chocolate (50g).

The factory sells three different boxes of chocolates. Each box contains 30 units. The name and composition of each box are:

Especial:
30 Crocante;
Predileta:
10 Crocante and 20 Misto;
Sortida:
10 chocolates of each kind.

Knowing that in a month the factory processed **X** kg of peanut, **Y** kg of white chocolate and **Z** kg of milk chocolate. How many boxes of each kind were produced in that month?

Input
-----

The input is composed by several test cases. Each test case is described by a single line that contains real numbers **X**, **Y** e **Z** (0 â¤ **X,Y,Z** â¤ 10000), in kilograms, separated by one space. A line with three zeros marks the end of the input: don't process this last line.

The values of **X, Y, Z** have, at most, three decimal digits.

Output
------

For each test case the program must print a line with the message "Caso #**t**: **A** Especial, **B** Predileta e **C** Sortida", where integers **A,B,C** are the amounts of each type of box and **t** is the test case number (the counting starts with one).


| Input Samples | Output Samples |
| --- | --- |
| 4 40 46  0.25 2 2.25  0.4 3.75 4.85  13.5 102.5 139  8.7 96.5 116.8  0 0 0 | Caso #1: 10 Especial, 30 Predileta e 20 Sortida  Caso #2: 1 Especial, 1 Predileta e 1 Sortida  Caso #3: 1 Especial, 2 Predileta e 3 Sortida  Caso #4: 50 Especial, 20 Predileta e 100 Sortida  Caso #5: 13 Especial, 77 Predileta e 58 Sortida |

Translation reviewed by Gustavo Jaruga


# Problem 1831

Descrição
----------

JosÃ© works selling oranges. He has a team of employees that packs the oranges in sacks for sale and distribution. Each sack has the same number of oranges.

He hired new employees to match the raise in production. In the first day, the newcomers packed 5 oranges in each sack, and 2 oranges remained unpacked. The team didn't know that the number of oranges per sack was changed to 7: the work was redone, and the repacked sacks now have 7 oranges each. In the end 3 oranges were left unpacked.

JosÃ© checked the sacks before sending them to the trucks and noted that the employees forgot the New Year promotion where each sack must contain 9 oranges. Once again the work was redone, and this time there were no leftovers.

After the trucks departure the team of workers realized that one more mistake was made: nobody counted the total of oranges packed nor the number of sacks sent! Before telling JosÃ© the new mistake, one of them suggested that is possible deduce the missing information using only the known facts.

Can you write a software that helps the workers in this hard working day?

Input
-----

The input consist of a series of test cases. Each test case is composed by three lines. Each line informs the number of unpacked oranges **ri** (0 â¤ **ri** < **Li**) and the number of oranges per sack **Li** (2 â¤ **Li** â¤ 1000), separated by a single space, with **i** = 1, 2, 3. You may assume that **Li** and **ri** are co-prime integers (there isn't other positive common divisor between **L1, L2, L3** than one).

Output
------

For each case the following message must be printed: "Caso #**t**: **N** laranja(s)", where **t** is the test case number (the counting starts with one) and **N** is the total of oranges. If there are more than one solution to the problem, you must choose the smallest positive integer solution.


| Input Samples | Output Samples |
| --- | --- |
| 2 5  3 7  0 9  0 10  0 17  0 23  1 3  1 4  1 5  4 5  6 7  8 9 | Caso #1: 297 laranja(s)  Caso #2: 3910 laranja(s)  Caso #3: 1 laranja(s)  Caso #4: 314 laranja(s) |

Translation reviewed by Gustavo Jaruga


# Problem 1839

Descrição
----------

The city of ChapecÃ³, in the west of the brazilian state of Santa Catarina, is where are located the governance of the Federal University of Southern Border and one of the 6 *campi* of the university. In the next August 25, the 98th anniversary of the city shall be celebrated, and the city councilmen are already making the preparations for the party. The goal of this party, besides the anniversary celebration, is to raise funds to the construction of the new city Council's building, which is going to be a Chamber of Secrets, where the city councilmen will be able to vote more peacefully the increases of the bus fare without being so disturbed by the students.

The Chamber of Secrets is going to be a real maze, so eventual invaders will not exit so easily. But the architects are not sure about the plan and want to make some changes in the project. In order to make the work easier, they have projected the entire plan of the building over a grid of square units, so that each square unit would be either fully wall or free space, as in the figure below.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1839_a.jpg)

Willing to attack the problem in a more restricted manner, the architects have even picked up some regions of the plan so they could study each region isolated. Now, they want to know what is the number of possibilities they have to rearrange the square units of wall of each region only inside the region itself. For example, for the region highlighted in the figure above, there are 5 possibilities, which we illustrate in the figure below.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1839_b.jpg)

Input
-----

The first line of the input tells the dimensions **N** and **M** (1 â¤ **N**, **M** â¤ 50) of the plan in square units, which represent respectively the number of lines and the number of columns of the grid, and the **N** following lines describe the grid, so that free square units are represented by the character â.â and wall square units by the character â#â. Each one of the remaining lines of the input consists of four integers **xA**, **yA**, **xB** and **yB** (1 â¤ **xA** < **xB** â¤ **N**, 1 â¤ **yA** < **yB** â¤ **M**), which define a region by the up-leftmost point (**xA**, **yA**) and by the down-rightmost point (**xB**, **yB**) of the regions. The input ends in end of file.

Output
------

For each region described in the input, print a line containing singly the number of possibilities the architects have to rearrange the square unities of wall of the region only inside the region itself. As the number of possibilities can be very large, print only the remainder that is left when this number is divided by 109 + 7.


| Input Samples | Output Samples |
| --- | --- |
| 4 6 #...#. ..#.#. ##.... ...... 2 2 3 3 3 3 4 6 1 1 4 6 | 5 0 134595 |

4Âº Maratona UFFS


# Problem 1841

Descrição
----------

One of the trials of the Triwizard Tournament will be a football match, and *Chapecoense* has been training hard to face Hogwarts players. The Chapecoense Football Association (in Portuguese: *AssociaÃ§Ã£o Chapecoense de Futebol*, or shortly ACF, or simply *Chapecoense*) is the football team of the city of ChapecÃ³. Founded in 1973, the team nowadays plays among the best teams of Brazil, and it is not some freak teenagers of hat and broomstick that are going to frighten our brave warriors, even though we all have been shocked when the Goblet of Fire chose our muggle players to participate of the Triwizard Tournament. As we have previously mentioned, the history of the team begins in 1973 whenâ¦

We interrupt this text for the transmission of an urgent message of the Minister of Magic.

| Good afternoon, muggle ladies and gentlemen! Cursed be the day in which Dolores Umbridge has left the prison. Now, she lives to piss me off with those Math problems. And she knows I'm not good at these things. So, can you write a program to help me? The problem is: she says to me an integer **N** and asks me to tell how many divisors **N** has and to keep this **N** in my head. So far so good. I'm not that stupid and I don't need help in this part. But then she keeps saying to me some prime numbers and, for each prime **p** she says, I'm supposed to multiply **p** by **N**, updating the value of **N** in my head, and, as if it were not enough, I still have to tell her how many divisors this new **N** has which are composed only by prime factors less than **p**. For example, if I have kept in my head **N** = 630 and she says **p** = 5, I must update **N** to 3150 and say 6, for the only divisors of 3150 composed only by prime factors less than 5 are: 1, 2, 3, 6, 9 and 18. But the number **N** grows very quickly, and I don't want to lose the game to her. Please do something! |
| --- |

Input
-----

The input consists of at least 2 and at most 105 lines. The first line consists of the single integer **N** (2 â¤ **N** â¤ 1012). Each one of the next lines consist of a single prime number **p** (2 â¤ **p** â¤ 107). The integers are given in the input in the order that Dolores Umbridge says them. The input ends in end of file.

Output
------

For each prime number **p** said by Dolores Umbridge, print a line consisting only of the answer that the Minister of Magic was supposed to give her. As the answer can be a very large number, print only the remainder that is left when the answer is divided by 109 + 7.


| Input Samples | Output Samples |
| --- | --- |
| 630 5 7 2 3 11 | 6 18 1 3 108 |

| 2 3 5 7 11 | 2 4 8 16 |

| 2 2 2 2 3 | 1 1 1 5 |

4Âº Maratona UFFS


# Problem 1869

Descrição
----------

In a country called TresdoislÃ¢ndia , all numbers are treated in base 32 , in which each number represents the numerical order , and the following numbers using letters from A to V. For example , the number 31 in base 32 is the fifth digit, and the number 32 on the base 32 becomes 10 .

Write a program that , given an integer in decimal base , convert to base 32 .

Input
-----

There will be several test cases . Each test case starts with an integer N ( 0 â¤ N â¤ 263 ), indicating a number in decimal base. The last test case is indicated when N = 0 .

Output
------

For each test case , print the amount corresponding to the input in base 32 .


| Input Sample | Output Sample |
| --- | --- |
| 31  32  1024  1300  0 | V  10  100  18K  0 |

V OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2015


# Problem 1872

Descrição
----------

A palindrome is a word , phrase or any other sequence of units (like a chain of DNA; Restriction enzyme ) that has the property of being able to be read either from right to left and from left to right. Capicua or palindrome number is a number (or set of numbers ) integers whose reverse is himself. This problem want you to analyze a real number and verify that the lowest value that should be added to this so that it becomes a real palindrome without specific name so far. For example , if the number is 101.099 , to add to 0,002 , we get the real palindrome 101.101 . Another example would be the number 13.31 , which is already a real palindrome and must add 0 so that it stays that way. A final example is the number 100.9 , which should add 0.1 so that the sum becomes 101 .

Write a program that , given a real number , check the lower value to be added so that it becomes a real palindrome.

Input
-----

There will be several test cases . The first number being read C is an integer representing the number of test cases. Each test case has a real number R ( 0 â¤ R â¤ 999,999.999999 ) . Recalling that the entry will have a maximum of 6 decimal places, and the decimal separator is the point instead of comma.

Output
------

For each test case output the expected value with the amount of required homes.


| Input Sample | Output Sample |
| --- | --- |
| 3  101.099  13.31  100.9 | 0.002  0  0.1 |

V OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2015


