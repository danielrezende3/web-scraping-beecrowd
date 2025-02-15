# Problem 1580

Descrição
----------

A long time ago, in a galaxy far, far away, the Unidade Federativa Fazedora de Segredos (UFFS) often used to send e-mails to the Unidade Receptora do ImpÃ©rio (URI) with the codes that should be changed every hour in the Death Star security system. Fearing that the e-mails could be intercepted by the Rebel Alliance, UFFS signed each e-mail with one of the 12 different anagrams of its own acronym, as FUFS or SUFF, for example. It has not taken so long to the habit turn into an addiction among the imperial organs, and some more curious *stormtroopers* started to ask themselves how many anagrams would have any word.

Input
-----

The input consists of a list of words, one per line, and ends up with EOF (end of file). A word in turn is composed by at least one and at most 103 letters of the latin alphabet, capital only, with no blank spaces nor any other symbols.

Output
------

For each word print a line containing an integer which represents the number of anagrams which is possible to form with that word. As this number can be very big, print just the remainder it leaves when divided by 109 + 7.


| Sample Input | Sample Output |
| --- | --- |
| UFFS QUIDESTVERITASESTVIRQUIADEST | 12 610881623 |

Aquecimento para a OBI 2014


# Problem 1582

Descrição
----------

Pythagoras was a greek mathematician before Euclid who lived between 570 and 495 BC, considered by Aristotle as âthe first mathematicianâ. One of the most ancient and most important theorems in History, the Pythagorean Theorem states that, in any right triangle, the square of the hypotenuse equals the sum of the squares of the catheti. The Theorem has several applications and is the base of many results in Mathematics, Engineering, Physics and Computer Science. Although the Theorem takes Pythagoras's name, it is believed that babylonian mathematicians, even more ancient, had yet knowledge of the formula.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1582.jpg)

We call a positive integers triple (**x**, **y**, **z**) a pythagorean triple if it is possible to exist a right triangle with sides **x**, **y** and **z**, no matter the order the integers appear in the triple. For example, (3, 4, 5), (6, 8, 10) and (5, 13, 12) are pythagorean triples, because 52 = 32 + 42, 102 = 62 + 82 and 132 = 52 + 122. However, triple (6, 8, 10) is just triple (3, 4, 5) multiplied by 2, and, for that, we say that (6, 8, 10) is not a primitive pythagorean triple. A pythagorean triple (**x**, **y**, **z**) is said to be primitive if gdc(**x**, **y**, **z**) = 1. Euclid proved in 3rd century BC that there are infinite primitive pythagorean triples.

Input
-----

Each line of the input consists of 3 integers **x**, **y** e **z** (1 â¤ **x**, **y**, **z** â¤ 104), separated by a blank space and given not necessarily in any order and it ends with EOF.

Output
------

Print for each input line the line âtripla pitagorica primitivaâ (without quotation marks) if the given integers form a primitive pythagorean triple, âtripla pitagoricaâ if they form a non-primitive pythagorean triple, or âtriplaâ if they form no pythagorean triple at all.


| Sample Input | Sample Output |
| --- | --- |
| 3 4 5 6 8 10 5 13 12 4 5 6 | tripla pitagorica primitiva tripla pitagorica tripla pitagorica primitiva tripla |

Aquecimento para a OBI 2014


# Problem 1585

Descrição
----------

Anastasia really loves to build kites to her friends. Peter, knowing that, took some bamboo pieces from the furniture factory of his uncle that it would be descarted, to give to Anastasia. When Peter gave the bamboos to her, he asked what was the biggest kite that could be built with those patches of bamboo. Anastasia, that is not very good with calculus, wants you to help her with this task.

Note .: Each kite is built with two pieces of bamboo tied cross-shaped, forming a lozenge.

Input
-----

The input contains many test cases. The first line of input contains an integer **N** that represents the among of kites that will be built. Each one of the **N** following lines contains two integer numbers **x** (10 â¤ **x** â¤ 100) and **y** (10 â¤ **y** â¤ 100) that indicates the size of the two bambus used to built the kite.

Output
------

For each test case, print a truncate integer number corresponding to the area of the kite created, in cm2, followed by a blank space and the text "cm2", without the quotes.


| Sample Input | Sample Output |
| --- | --- |
| 4 10 20 20 14 10 100 100 100 | 100 cm2 140 cm2 500 cm2 5000 cm2 |

Special Thanks to Michele Selivon   

Aquecimento para a OBI 2014


# Problem 1620

Descrição
----------

In mathematics, a Delaunay triangulation for a set of points P on the plane is a DT (P) where no point in P is inside the circumference formed by any triangle in DT (P). The Delaunay triangulation maximizes the smallest angle of all triangles in the triangulation; this tends to avoid triangles with very small internal angles.

The triangulation was invented by Boris Delaunay in 1934 for a set of points on a line there is no Delaunay triangulation (the concept of triangulation is broken for this case). For four or more points on the same circle (ie, the vertices of a rectangle) the Delaunay triangulation is not unique: each of the two possibilities of triangulation that divides the quadrilateral into two triangles satisfy the "Delaunay condition", ie that the circumferences of all triangles have hollow interiors. Whereas the circles are spheres, the notion of Delaunay triangulation extends to three dimensions. Generalizations are possible for different metrics of Euclidean. However, in these cases it can not guarantee the existence or uniqueness of the Delaunay triangulation.

The Mad Doctor da Silva, for his doctorate, he decided to check the statement on the Delaunay triangulation previously said was true. Analyzed settings perfect polygons, as shown.

![](https://resources.beecrowd.com/gallery/images/novos/delaunay_fig1.jpg)

It is true and found that the amount of arches that create the Delaunay triangulation for the same number of points was always the same. For example, to 3 is always three points, 4 points is always 5, 5 is always points 6 points 7 and 9 and is always so forth.

He then decided to create a real number (X) determined by the ratio of the amount of arch (I) with the number of points (L) which is:

![](https://resources.beecrowd.com/gallery/images/novos/delaunay_formula.jpg)

Help the Doctor doing a program that calculates the value of the real number X.

Input
-----

The input consists of a test set containing a single row with an integer value **L** (3 â¤ **L** â¤ 1080). The input ends when **L** = 0.

Output
------

For the input your program must produce one actual outcome **X** with accuracy of six decimal places. Use double variables.


| Sample Input | Sample Output |
| --- | --- |
| 3  4  5  6  0 | 0.000000  0.250000  0.400000  0.500000 |

XIV Contest Algar Telecom 1620


# Problem 1623

Descrição
----------

Germanium an intergalactic warrior and conqueror of planets has trouble speaking when he gets nervous, he gets a little stutter. So, words like WANT, he speaks WWANT, GO, he speaks GGO and so on.

Annoyed by this, Germanium decided that all new conquest of a new planet he would invent a new language. Given an alphabet, where there is no character repetition, for example, QABCDEFG, all of the new language words begin with the letter Q twice. In this case, the word QQABCDEFG be valid.

You reviewed the case, and made the suggestion that the characters to be repeated can occur in any part of the new word since they are always in the same order and together. In the example given, ABCDEFGQQ would be valid as well.

The Warrior beloved Germanium liked his idea and asked you to calculate how many words these new languages ââwill. But if the language has a very large number of words he wants to discard this language.

Input
-----

There will be several test cases. Each test case starts with two integers **N** and **Q** (1 < **N** â¤ 100000, 1 â¤ **Q** <**N**), indicating the size of the alphabet and the number of characters of the alphabet that will be considered in the repetition that can occur in anywhere in the word, respectively. The second line consists of a integer **T** (1 â¤ 105000) indicating the maximum number of words allowed by the language.

The latter test case is indicated when **N** = **Q** = 0, which should not be processed.

Output
------

For each test case, print a line containing an integer indicating the number of distinct words that have this new language. And print "descartado" if the word count exceeds the value of **T**.


| Sample Input | Sample Output |
| --- | --- |
| 4 1  100  5 2  30  6 3  10  0 0 | 24  24  descartado |

XIV Contest Algar Telecom 2014


# Problem 1624

Descrição
----------

Dr Luis Claudio, a man attuned to the deals offered by VemQueTem supermarket, which is close to your residence, walking very smiley lately. It turned out that he was drawn in a promotion offered by the supermarket. In this promotion, the person could enter the supermarket alone and take all the products that could carry. However, some rules were established.

1) Login alone

2) Only one product of each type can be selected and picked

3) A list L containing the prices and weights of products should be followed

4) A maximum weight P was established

You have been hired by the nosy neighbor Dr Luis Claudio to find out what the total value of the goods which he managed to take home.

Input
-----

The input consists of **T** test cases. Each test case starts with an integer **N** (1 â¤ **N** â¤ 100) indicating the number of products on the list **L**. The following **N** lines are formed by two integers pe **P**. The first integer **p** (1 â¤ **p** â¤ 1000) represents the price of the product. The second integer **P**, (1 â¤ **P** â¤ 30) represents the weight of the product. The next line contains an integer **M**, which indicates the maximum weight allowed. The end of input is represented by a 0.

Output
------

For each test case print an integer that represents the total of products Dr Luis ClÃ¡udio can take home.


| Sample Input | Sample Output |
| --- | --- |
| 4  72 17  44 23  31 24  22 2  26  3  72 17  44 23  31 24  25  0 | 94  72 |

XIV Contest Algar Telecom 2014


# Problem 1625

Descrição
----------

Robocopy are drones that once activated they copy rotational motion each other. When a drone is activated along with others, they work together as if they were one.

Daniel recently bought a factory of robocopy. A robotic arm places each robocopy randomly in an area, thus forming a set of robocopy. Each set may be composed of different numbers of robocopy. And to test them, they are activated. The activated robocopy must pass a treadmill for later deactivated and stored. Several sets of rodocopy can go through the same treadmill. The treadmill width should always be the lowest possible, but that it contains all the sets.

As Daniel is an inexperienced entrepreneur, did not do a proper planning and then had to hire additional staff to manually check which size mat he has to configure to support different sets of robocopy. Of course, this process is very costly and time consuming.

To reduce costs and increase efficiency, Daniel hired you to calculate automatically, which the smaller track width for all sets robocopy can be stored properly.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1625_a.png)

Figure 1.

  

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1625_b.png)

Figure 2.

  

In Figure 1, for example, 3 robocopy were activated by the machine(A, B and C) and the smallest distance is a = 2, among BC. When the machine does the other set of robocopy (A, B, C and D) of Figure 2, the smallest distance is AB or DC, b = 3, and in this case the set of robocopy must be rotated 90 degrees to pass over the treadmill which has size 3. So, if these sets were passing by the treadmill, this would have to have a minimum width of 3.

Input
-----

The input consists of several test cases.

The first line consists of an integer **N** (1 â¤ **N** â¤ 10000) that represents the number of test cases.

Each test case consists of an integer **C** (1 â¤ **C** â¤ 100) indicating the number of sets of robocopy manufactured. Each set consists of an integer **c** (1 â¤ **c** â¤ 10 000) representing the number of robocopy of the set, followed by **c** rows of integers indicating the coordinate -100000 â¤ (**x**, **y**) â¤ 100 000 of each one robocopy of the in **C**.

Output
------

In each row should be printed the size of the smallest treadmill to produce all sets of robocopy with accuracy of 10 decimal places.


| Sample Input | Sample Output |
| --- | --- |
| 1  2 4 1 4 1 1 5 1 5 4 3 1 1  1 3 3 3 | 3.0000000000 |

XIV Contest Algar Telecom 2014


# Problem 1626

Descrição
----------

The universities from the brazilian region known as Southern Border (Fronteira Sul, in Portuguese) have been joining ACM ICPC South America/Brazilian Subregional for many years, alternating the First Phase site especially between the cities of Erechim, in the state of Rio Grande do Sul, and ChapecÃ³, in the state of Santa Catarina. Since last year, our site has been being the 2nd greatest of the country. In this year of 2014, 34 teams of 12 institutions have joined the contest at UNOCHAPECÃ, at ChapecÃ³. The institutions involved in the organisation of the contest â particularly UNOCHAPECÃ, UNOESC and just created UFFS â believe that Programming contests are one of the main goals to strengthen Programming culture, promoting scientific and technological independence and inovation and greater relevance in the national scenario.

After 2014 First Phase Awards, students and professors from the above institutions went to a caster pizza house for two reasons: 1. to end the hunger; 2. to talk about the organisation of the Programming contest at the knowledge, culture and education fair of ChapecÃ³, named âFeira de Conhecimento, Cultura e EducaÃ§Ã£oâ (FACE), which would happen two weeks later. But one of the professors during the talk proposed: âWhy don't we realise a contest right here, not a Programming contest, but a pizza one? Whoever eats less pizza pays a round of beer for all!â. Everybody agreed, and therefore happened the 1st Incredible Chapecoense Pizza Contest (ICPC). The loser however wanted first to avoid paying the beer. âI pay only if someone can tell me a perfect number which is also a factorial numberâ, he said. â6â, answered another student quickly.

*Is there another perfect number which is also a factorial number?* Of course not, but the loser, outraged after paying beer for all, decided to make a program to convince himself. Recall: a positive integer **M** is said to be perfect if it equals the sum of all its divisors different from **M** (e.g. 6 = 1 + 2 + 3 and 28 = 1 + 2 + 4 + 7 + 14), and is said to be a factorial if there is a natural number **N** such that **N**! = **M**.

Input
-----

Each line of input consists of a single integer **N** (2 â¤ **N** â¤ 105). The input ends in end-of-file (EOF).

Output
------

For each integer **N** read from input, print a line containing two values: the sum of the divisors of **N**! different from **N**! and **N**! itself. As both values can be very large, print just the remainder they leave by 109 + 7.


| Sample Input | Sample Output |
| --- | --- |
| 2 3 4 5 | 1 2 6 6 36 24 240 120 |

II Maratona FACE 2014


# Problem 1630

Descrição
----------

Marcos works for a construction company, his task is to surround with stakes the sites where buildings will be constructed. There are two restrictions regarding these stakes distribution, they should be placed in a way the distance between two stakes is always the same, and the second restriction is that Marcos should use the smallest possible number of stakes. Marcos is your friend and he has asked you to develop a program to help him.

Input
-----

There will be several test cases, each test case is described in a line by two numbers **X** and **Y** (1 â¤ **X**, **Y** â¤ 100000000), which represent the dimensions of the site. The input end is indicated by end of file.

Output
------

For each test case print a line with the minimum number of stakes needed to surround the site.


| Sample Input | Sample Output |
| --- | --- |
| 2 2 3 3 2 5 8 3 76 50 | 4 4 14 22 126 |

II Maratona FACE 2014


# Problem 1634

Descrição
----------

Even in times of an economic crisis, people in Byteland still like to participate in lotteries. With a bit of luck, they might get rid of all their sorrows and become rich.

The most popular lottery in Byteland consists of m rounds. In each round, everyone can purchase as many tickets as he wishes, and among all tickets sold in this round, one ticket is chosen randomly, each one with the same probability. The owner of that ticket wins the prize money of this round. Since people in Byteland like powers of 2, the prize money for the winner of round i amounts to 2i Bytelandian Dollars.

Can you determine for each participant in the lottery the probability that he will win more money than anybody else?

Input
-----

The input consists of several test cases. Each test case starts with a line containing two integers **n** and **m**, the number of participants in the lottery and the number of rounds in the lottery. You may assume that **1 â¤ n â¤ 10000** and **1 â¤ m â¤ 30**.

The following **n** lines contain the description of the tickets bought by the participant. The **ith** such line contains **m** non-negative integers **c1, ..., cm**, where **cj** (**1 â¤ j â¤ m**) is the amount of tickets of round **j** bought by participant **i**. The total number of tickets sold in each round is between **1** and **109**.

The input ends with a line containing 2 zeros.

Output
------

For each test case, print n lines of output, where line **i** contains the probability as a reduced fraction that participant **i** wins the most money. See the sample output for details.


| Sample Input | Sample Output |
| --- | --- |
| 5 4  3 1 2 3  3 1 2 4  3 1 3 5  4 4 4 0  5 5 0 0  1 1  1  0 0 | 1 / 4  1 / 3  5 / 12  0 / 1  0 / 1  1 / 1 |

Univeristy of Ulm Local Contest 2009


# Problem 1635

Descrição
----------

Before the 2009 elections at the European Parliament, Bill and Ted have asked their friends to make guesses about the outcome of the ballot. Now, the results have been published, so Bill and Ted want to check who was right. But checking the results of their many friends would take a very long time, and they need the evaluation to be done by a computer. Since they are not so good at programming, they ask you for help.

Input
-----

The data provided by Bill and Ted has the following format: The first line consists of the number ***p*** of parties followed by the number ***g*** of guesses (with ***1 â¤ p â¤ 50*** and ***1 â¤ g â¤ 10000***). Then follow ***p*** lines, each line consisting of a unique party name of length â¤ 20 (only containing letters a-z, A-Z and digits 0-9) and the achieved vote percentage of this party with one digit after the decimal point. After the parties follow ***g*** lines, each consisting of a guess. A guess has the form ***P1 + P2 + ... + Pk COMP n***, where ***P1*** to ***Pk*** are party names, ***COMP*** is one of the comparison operators <, >, <=, >= or = and ***n*** is an integer between 0 and 100, inclusively. Each party name occurs at most once in each guess.

**Obs:** Be careful with the comparison of floating point values, because some values in the input (like 0.1) do not have an exact representation as a floating point number.

Output
------

For each guess, sum up the vote percentages of the parties and compare them with the specified integer ***n***. Then, print a line stating whether the guess was correct. See the sample output for details.


| Sample Input | Sample Output |
| --- | --- |
| 6 5  CDU 30.7  SPD 20.8  Gruene 12.1  FDP 11.0  DIELINKE 7.5  CSU 7.2  FDP > 11  CDU + SPD < 50  SPD + CSU >= 28  FDP + SPD + CDU <= 42  CDU + FDP + SPD + DIELINKE = 70 | Guess #1 was incorrect. Guess #2 was incorrect. Guess #3 was correct. Guess #4 was incorrect. Guess #5 was correct. |

Univeristy of Ulm Local Contest 2009


# Problem 1641

Descrição
----------

Traditionally after the Local Contest at Louisiana, judges and contestants go to their favourite restaurant, Alfredos Pizza Restaurant. The contestants are really hungry after trying hard for five hours. To get their pizza as quickly as possible, they just decided to order one big pizza for all instead of several small ones. They wonder whether it is possible to put the big rectangular pizza on the surface of the round table such that it does not overhang the border of the table. Write a program that helps them!

Input
-----

The input file contains several test cases. Each test case starts with an integer number **R**, the radius of the surface of the round table the contestants are sitting at. Input is terminated by **R** = 0. Otherwise, 1 â¤ **R** â¤ 1000. Then follow 2 integer numbers **W** and **L** specifying the width and the length of the pizza, 1 â¤ **W** â¤ **L** â¤ 1000.

Output
------

Output for each test case whether the ordered pizza will fit on the table or not. Adhere to the format shown in the sample output. A pizza which just touches the border of the table without intersecting it is considered fitting on the table, see example 3 for clarification.


| Sample Input | Sample Output |
| --- | --- |
| 38 40 60 35 20 70 50 60 80 0 | Pizza 1 fits on the table. Pizza 2 does not fit on the table. Pizza 3 fits on the table. |

Univeristy of Ulm Local Contest 2008/2009


# Problem 1644

Descrição
----------

Bruce Force has had an interesting idea how to encode strings. The following is the description of how the encoding is done:

Let x1,x2,...,xn be the sequence of characters of the string to be encoded.

1. Choose an integer M and N pairwise distinct numbers p1,p2,...,pn from the set {1, 2, ..., N} (a permutation of the numbers 1 to N).
2. Repeat the following step m times.
3. For 1 â¤ i â¤ N set yi to xpi, and then for 1 â¤ i â¤ N replace xi by yi.

For example, when we want to encode the string "hello", and we choose the value M = 3 and the permutation 2, 3, 1, 5, 4, the data would be encoded in 3 steps: "hello" -> "elhol" -> "lhelo" -> "helol".

Bruce gives you the encoded strings, and the numbers M and p1, ..., pn used to encode these strings. He claims that because he used huge numbers m for encoding, you will need a lot of time to decode the strings. Can you disprove this claim by quickly decoding the strings?

Input
-----

The input contains several test cases. Each test case starts with a line containing two numbers **N** and **M** (1 â¤ **N** â¤ 80, 1 â¤ **M** â¤ 109). The following line consists of **N** pairwise different numbers p1,...,pn (1 â¤ **pi** â¤ **N**). The third line of each test case consists of exactly **N** characters, and represent the encoded string. The last test case is followed by a line containing two zeros.

Output
------

For each test case, print one line with the decoded string.


| Sample Input | Sample Output |
| --- | --- |
| 5 3 2 3 1 5 4 helol 16 804289384 13 10 2 7 8 1 16 12 15 6 5 14 3 4 11 9 scssoet tcaede n 8 12 5 3 4 2 1 8 6 7 encoded? 0 0 | hello second test case encoded? |

Univeristy of Ulm Local Contest 2008/2009


# Problem 1647

Descrição
----------

There are *n* bowls, numbered from 1 to *n*. Initially, bowl *i* contains *m*i marbles. One game step consists of removing one marble from a bowl. When removing a marble from bowl *i* (*i* > 1), one marble is added to each of the first *i*-1 bowls; if a marble is removed from bowl 1, no new marble is added. The game is finished after each bowl is empty.

Your job is to determine how many game steps are needed to finish the game. You may assume that the supply of marbles is sufficient, and each bowl is large enough, so that each possible game step can be executed.

Input
-----

The input contains several test cases. Each test case consists of one line containing one integer **n** (1 â¤ **n** â¤ 50), the number of bowls in the game. The following line contains **n** integers **mi** (1 â¤ **i** â¤ **n**, 0 â¤ **mi** â¤ 1000), where **mi** gives the number of marbles in bowl **i** at the beginning of the game.

The last test case is followed by a line containing 0.

Output
------

For each test case, print one line with the number of game steps needed to finish the game. You may assume that this number fits into a signed 64-bit integer (in C/C++ you can use the data type "long long", in JAVA the data type "long").


| Sample Input | Sample Output |
| --- | --- |
| 10  3 3 3 3 3 3 3 3 3 3  5  1 2 3 4 5  0 | 3069  129 |

Univeristy of Ulm Local Contest 2008/2009


# Problem 1650

Descrição
----------

You are visiting the Centre Pompidou which contains a lot of modern paintings. In particular you notice one painting which consists solely of black and white squares, arranged in rows and columns like in a chess board (no two adjacent squares have the same colour).

Since you are bored, you wonder how many 8 Ã 8 chess boards are embedded within this painting. The bottom right corner of a chess board must always be white.

Input
-----

The input contains several test cases. Each test case consists of one line with three integers **n**, **m** and **c**. (8 â¤ **n**, **m** â¤ 40000), where **n** is the number of rows of the painting, and **m** is the number of columns of the painting. **c** is always 0 or 1, where 0 indicates that the bottom right corner of the painting is black, and 1 indicates that this corner is white.

The last test case is followed by a line containing three zeros.

Output
------

For each test case, print the number of chess boards embedded within the given painting.


| Sample Input | Sample Output |
| --- | --- |
| 8 8 0 8 8 1 9 9 1 40000 39999 0 0 0 0 | 0 1 2 799700028 |

Univeristy of Ulm Local Contest 2007/2008


# Problem 1656

Descrição
----------

Every year there is the same problem at Halloween: Each neighbour is only willing to give a certain total number of sweets on that day, no matter how many children call on him, so it may happen that a child will get nothing if it is too late. To avoid conflicts, the children have decided they will put all sweets together and then divide them evenly among themselves. From last year's experience of Halloween they know how many sweets they get from each neighbour. Since they care more about justice than about the number of sweets they get, they want to select a subset of the neighbours to visit, so that in sharing every child receives the same number of sweets. They will not be satisfied if they have any sweets left which cannot be divided.

Your job is to help the children and present a solution.

Input
-----

The input contains several test cases.

The first line of each test case contains two integers **c** and **n** (1 â¤ **c** â¤ **n** â¤ 100000), the number of children and the number of neighbours, respectively. The next line contains **n** space separated integers **a**1,...,**a**n (1 â¤ **a**i â¤ 100000 ), where **a**i represents the number of sweets the children get if they visit neighbour **i**.

The last test case is followed by two zeros.

Output
------

For each test case output one line with the indices of the neighbours the children should select (here, index **i** corresponds to neighbour **i** who gives a total number of **a**i sweets). If there is no solution where each child gets at least one sweet, print "no sweets" instead. Note that if there are several solutions where each child gets at least one sweet, you may print any of them.


| Sample Input | Sample Output |
| --- | --- |
| 4 5  1 2 3 7 5  3 6  7 11 2 5 13 17  0 0 | 3 5  2 3 4 |

University of Ulm Local Contest 2007/2008


# Problem 1658

Descrição
----------

Consider *n* points on a unit circle with numbers *k = 0, 1, ..., n-1*. Initially point *k* makes an angle of *360 Â· k / n* degrees to the x-axis, measured in counter-clockwise direction. We are going to perform two different kind of operations on that set of points:

* rotation by *360 / n* degrees in clockwise direction
* reflection with respect to the x-axis

The following picture shows an example of these operations:

![](https://resources.beecrowd.com/gallery/images/promocao/dihedral%20groups.png)

Given a sequence of operations, we are interested in the shortest sequence of operations which gives the same result, i.e., the position of every single point is the same after performing either of those sequences of operations.

The sequence is given as a string consisting of the characters 'r' and 'm' which represent clockwise rotation and reflection respectively ("to the right" and "mirror"). Multiple consecutive occurrences of the same character are collected into the representation <character><number>, and for convenience this will also be done for single occurrences. So "rrmrrrrrrrrrrrr" will be abbreviated to "r2 m1 r12". The representations of different operations are always separated by a single space.

Input
-----

The input file consists of several test cases. Each test case starts with a line containing **n** (3 â¤ **n** â¤ 108), the number of points. The second line of each test case consists of an abbreviated sequence of operations as described above. All numbers will be positive and less than 108. There will be no empty line in the input file, and no line will contain more than 100000 characters. The last test case is followed by a line containing 0.

Output
------

For each test case print one line containing the abbreviated format of the sequence with the minimum number of operations which results in the same configuration of points as the input sequence. In case of multiple optimal solutions, print any solution.


| Sample Input | Sample Output |
| --- | --- |
| 4 r2 100 m1 r100 m1 54 r218 m3 r1 0 | r2  r1 m1 |

Univeristy of Ulm Local Contest 2006/2007


# Problem 1660

Descrição
----------

Flavius Josephus once was trapped in a cave together with his comrade soldiers surrounded by Romans. All of Josephus' fellow soldiers preferred not to surrender but to commit suicide. So they all formed a circle and agreed on a number *K*. Every *K-th* person in the circle would then commit suicide. However, Josephus had different priorities and didn't want to die just yet. According to the legend he managed to find the safe spot in the circle where he would be the last one to commit suicide. He surrendered to the Romans and became a citizen of Rome a few years later.

It is a lesser known fact that the souls of Josephus and his comrades were all born again in modern times. Obviously Josephus and his reborn fellow soldiers wanted to avoid a similar fiasco in the future. Thus they asked a consulting company to work out a better decision scheme. The company came up with the following scheme:

* For the sake of tradition all soldiers should stand in a circle. This way a number between 0 and *N-1* is assigned to each soldier, where *N* is the number of soldiers.
* As changing numbers in the old scheme turned out to be horribly inefficient, the number assigned to a soldier will not change throughout the game.
* The consulting company will provide two numbers *A* and *B* which will be used to calculate the number of the next soldier as follows: Let *X* be the number of the current soldier, then the number of the next soldier is the remainder of *AÂ·X2< + B mod N*.
* We start with the soldier with number 0 and each soldier calculates the number of the next soldier according to the formula above.
* As everyone deserves a second chance a soldier will commit suicide once his number is calculated for the second time.
* In the event that the number of a soldier is calculated for the third time the game will end and all remaining soldiers will surrender.

You are to write a program that given the number of soldiers *N* and the constants *A* and *B* determines the number of survivors.

Input
-----

The input file consists of several test cases. Each test case consists of a single line containing the three integers **N** (2 â¤ **N** â¤ 109), **A** and **B** (0 â¤ **A**, **B** < **N**) separated by white space. You may safely assume that the first soldier dies after no more than one million (106) steps. The input is terminated by a single number 0 which should not be processed.

Output
------

For each test case output a single line containing the number of soldiers that survive.


| Sample Input | Sample Output |
| --- | --- |
| 2 1 1  5 1 1  10 3 7  101 9 2  698253463 1 181945480  1000000000 999999999 999999999  0 | 0  2  4  96  698177783  999999994 |

Univeristy of Ulm Local Contest 2006/2007


# Problem 1662

Descrição
----------

Assume you have a square of size n that is divided into nÃn positions just as a checkerboard. Two positions (x1,y1) and (x2,y2), where 1 â¤ x1,y1,x2,y2 â¤ n, are called "independent" if they occupy different rows and different columns, that is, x1â x2 and y1â y2. More generally, n positions are called independent if they are pairwise independent. It follows that there are n! different ways to choose n independent positions.

Assume further that a number is written in each position of such an nÃn square. This square is called "homogeneous" if the sum of the numbers written in n independent positions is the same, no matter how the positions are chosen. Write a program to determine if a given square is homogeneous!

Input
-----

The input contains several test cases.

The first line of each test case contains an integer **n** (1 â¤ **n** â¤ 1000). Each of the next **n** lines contains **n** numbers, separated by exactly one space character. Each number is an integer from the interval [-1000000,1000000].

The last test case is followed by a zero.

Output
------

For each test case output whether the specified square is homogeneous or not. Adhere to the format shown in the sample output.


| Sample Input | Sample Output |
| --- | --- |
| 2 1 2 3 4 3 1 3 4 8 6 -2 -3 4 0 0 | homogeneous not homogeneous |

Univeristy of Ulm Local Contest 2006/2007


# Problem 1674

Descrição
----------

To play the "fraction game" corresponding to a given list *f1, f2, ..., fk* of fractions and starting integer N, you repeatedly multiply the integer you have at any stage (initially N) by the earliest fi in the list for which the answer is integral. Whenever there is no such fi, the game stops.

Formally, we define a sequence by *S0=N*, and *Sj+1=fiSj*, if for 1 â¤ I â¤ k, the number *fiSj* is an integer but the numbers *f1Sj, ..., fi-1Sj* are not.

For example, if we have the list of eight fractions f1=170/39, f2=19/13, f3=13/17, f4=69/95, f5=19/23, f6=1/19, f7=13/7, f8=1/3, and start with N=21, we produce the (finite) sequence (21,39,170,130,190,138,114,6,2). In general, the sequence may be infinite.

Given a fraction list and a starting integer calculate a part of the defined sequence. Actually, we are interested only in the powers of 2 that appear in the sequence.

Input
-----

The input contains several test cases. Every test case starts with three integers **m, N, k**. You may assume that 1 â¤ **m** â¤ 40, 1 â¤ **N** â¤ 1000, and 1 â¤ **k** â¤ 100. Then follow k fractions **f1, â¦, fk**. For each fraction, first its numerator is given, followed by its denominator. You may assume that both are positive integers less than 1000 and their greatest common divisor is 1. The last test case is followed by a zero.

Output
------

For each test case output on a line **m** numbers **e1, ..., em**, separated by one space character, such that **2e1, ..., 2ek** are the first **m** numbers in the defined sequence that are powers of 2. You may assume that there are at least **m** powers of 2 among the first 7654321 elements of the sequence.


| Sample Input | Sample Output |
| --- | --- |
| 1 21 8 170 39 19 13 13 17 69 95 19 23 1 19 13 7 1 3 20 2 14 17 91 78 85 19 51 23 38 29 33 77 29 95 23 77 19 1 17 11 13 13 11 15 2 1 7 55 1 0 | 1 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 |

Univeristy of Ulm Local Contest 2004/2005


# Problem 1688

Descrição
----------

During his last visit to planet Tatooine, Han Solo was captured by Jabba, the Hutt's mercenaries and was taken to his palace. Jabba, knowing that Solo was still not able to pay his debts, proposed a deal. Both would to play a game of Intergalactic Nim, and if Han won, he would be clear of his debts, otherwise, his debt would double.

Intergalactic Nim is a variation of the well known game of Nim, where stones are arranged in columns and on each turn a player must remove one or more stones from one of the columns. The player that is unable to make a move is considered the loser. On Intergalactic Nim one of the players (in this case Jabba) picks a number N and the stones are arranged in N columns, with the i-eth column having i stones (First column with 1 stone, second column with 2 stones, and so on).

Having great knowledge in these kinds of games, and knowing that who makes the first move (in this case Jabba) is more likely to win the game, Han proposed a little change to the game. He would be able to pick three integers A, B and K and add K stones to every column between columns A and B (inclusive). Jabba accepted the proposal but added a limitation, Jabba's counselor would consider Q possible operations of this type and Solo would have to apply each of these operations independently to the original game. Since Han is not accompanied by his fellow friend Chewbacca (that usually helps him in these situations), he asked you to help him beat Jabba.

Input
-----

The input consists of several test cases and ends with **EOF**.

The first line of a test case consists of two integers **N** (**1** <= **N** <= **1018**) and **Q** (**Q** <= **105**), the number picked by Jabba, and the number of operations suggested by the counselor.

The next **Q** lines consist in **3** integers **A**, **B** (**1** < = **A** <= **B** <= **N**) and **K** (**-A** <= **K** <= **1018**) describing each operation selected by the counselor.

Output
------

For each test case, the output consists of **Q** lines containing the winner of the game (considering both players play optimally) for each one of the operations suggested.


| Sample Input | Sample Output |
| --- | --- |
| 8 3  4 6 5  3 6 -2  1 1 8 | JABBA  JABBA  HAN |

The operations selected by the counselor are independent.  

Contest Road to Fortaleza II 2014


# Problem 1694

Descrição
----------

Pinkie Pie is feeling lucky. She is going to the local lottery office to place a bet and test her luck.

The lottery ticket consists of a matrix of N rows by M columns. The cells are numbered from 0 to N\*M-1 in such a way that the number located at the r-th row and c-th column (0-indexed) is r \* M + c. A bet consists of choosing K distinct numbers among those displayed.

![](https://resources.beecrowd.com/gallery/images/contests/20_3_en.png)

Pinkie senses that the winning numbers will be close to each other, so she decides to choose numbers that are all either in the same row or in the same column. Pinkie also thinks that prime numbers bring bad luck. She will disregard any bet that contains at least one prime number.

Twilight was passing by and noticed Pinkieâs incapableness of making a decision. Willing to put her math skills to the test, she decided to count, while Pinkie makes up her mind, how many different bets can Pinkie Pie place. Two bets are considered different if there is at least one element present in one bet and not present in the other.

Input
-----

There are several tests cases. Each test case consists of a single line containing three integers **N**, **M** and **K** (**1** â¤ **N**, **M** â¤ **50**; **1** â¤ **K** â¤ **10**). The last test case is followed by a line containing three zeroes.

Output
------

For each test case, print a single line containing the number of different bets Pinkie Pie can place, such that every chosen number is either in the same row or same column, and no prime number is chosen. A prime number is a natural number greater than **1** that has no positive divisors other than **1** and itself.


| Sample Input | Sample Output |
| --- | --- |
| 2 3 4 3 4 3 3 6 3 25 14 8 0 0 0 | 0 2 11 7988161 |

Contest Road to Fortaleza III 2014


# Problem 1697

Descrição
----------

Jaida likes positive integers very much, currently she is playing a game called "multiply game".

"Multiply game" is just an educational game in which you have a list of *N* numbers. You can take two of them and add the their product to the list. You can do this as many times as you want.

Jaida wants the list to contain all the numbers from 1 to *X* (with possible repetitions or greater numbers). Help little Jaida telling her what is the maximum value of *X* she can achieve.

Input
-----

The first line in the input contains a number **T** which is the number of test cases. Every test case is described by 2 lines:

The first line contains number **N** (0 < **N** <= 106) as described in the statement. The second line contains **N** positive integers **ai**, which are the initial numbers in Jaida's list (0 < **ai** <= 109).

Output
------

For each test case print a line containing the maximum value **X** Jaida can achieve. If it is not possible, output **0**.


| Sample Input | Sample Output |
| --- | --- |
| 3  6 1 2 3 4 5 12 3 2 3 4 3 1 2 3 | 6 0 4 |

Contest Road to Fortaleza IV 2014


# Problem 1703

Descrição
----------

Petr is playing a game called "Jumping Stones".

In this game, there are N slots in a line numbered from 1 to N. On each slot there is a stone with a number written on its top. The written numbers go from 1 to N and are all different.

Petr starts at slot 1 and takes K steps. At each step, he looks the number written on the current stone and jumps to the slot correspondent to that number.

Given integers N and K, determine among all possible configurations the probability that he will return to slot 1 after K steps. Assume that different configurations has the same probability.

Input
-----

You will be given **T**, number of test cases, and then **T** lines follow with **N** and **K** from the statement (1 <= **N**,**K** <= 10^5).

Output
------

For each test case output a single line with the answer. Your answer will be considered correct if the absolute erro is less than 0.00001

**Ps.:** Following the example input For the second case we have the following possibilites:   

1 2 3   

1 3 2   

2 1 3   

2 3 1   

3 1 2   

3 2 1   

In the first and second configurations we finish at the slot 1 after 1 step.


| Sample Input | Sample Output |
| --- | --- |
| 2  1 1  3 1 | 1.000000  0.333333 |

Contest Road to Fortaleza V 2014


# Problem 1705

Descrição
----------

In order to improve her scientific skills Princess Bubblegum has learned to program using BMO (the best computer in the Candy Kingdom), and as any programmer she has become a binary lover.

By her addiction to binary stuff, she also loves any decimal number that looks like a binary number (i.e. a decimal number that only has digits 0 and 1, for example 101), so she was trying to find a multiple of a given decimal number N that looks like a binary number, but for some numbers it was taking a long time to find such multiple, even with the help of BMO. Due to the princess addiction to problem solving, she hasnât been doing anything until she gets the desired multiples. That situation was perfect for the Earl of Lemongrab, who took over the Candy Kingdom. As Finn and Jake, the Candy Kingdom heroes, canât do anything against the Earl of Lemongrab and donât know nothing about multiples, they asked you to save the Candy Kingdom by finding the desired multiples.

Input
-----

The input will consist of at most 2\*10^5 lines, each line consist of an integer **N** (0 < **N** < 10^12) for which Princess Bubblegum wants to find the described multiple **M**(**M** != 0), this number must be less than 10^12, otherwise it wouldnât fit in the BMO architecture.

Output
------

For each integer in the input print a line with the required multiple, if there exist several solutions print the smallest of them, if there is no solution print -1.


| Sample Input | Sample Output |
| --- | --- |
| 143  1217  3123  1783  101 | 1001  101011  -1  1100111  101 |

Contest Road to Fortaleza VI 2014


