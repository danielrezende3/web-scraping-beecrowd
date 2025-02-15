# Problem 1289

Descrição
----------

Probability has always been an integrated part of computer algorithms. Where the deterministic algorithms have failed to solve a problem in short time, probabilistic algorithms have come to the rescue. In this problem we are not dealing with any probabilistic algorithm. We will just try to determine the winning probability of a certain player.

âA game is played by throwing a dice like thing (it should not be assumed that it has six sides like an ordinary dice). If a certain event occurs when a player throws the dice (such as getting a 3, getting green side on top or whatever) he is declared the winner. There can be N such player. So the first player will throw the dice, then the second and at last the N th player and again the first player and so on. When a player gets the desired event he or she is declared winner and playing stops. You will have to determine the winning probability of one (The I th) of these players.

Input
-----

Input will contain an integer **S** (**S** â¤ 1000), at first, which indicates how many sets of inputs are there. The next **S** lines will contain S sets of inputs. Each line contain an integer **N** (**N** â¤ 1000) which denotes the number players, a floating point number **p** which indicates the probability of the happening of a successful event in a single throw (If success means getting 3 then **p** is the probability of getting 3 in a single throw. For a normal dice the probability of getting 3 is 1/6), and **I** (**I**â¤ **N**) the serial of the player whose winning probability is to be determined (Serial no varies from 1 to **N**). You can assume that no invalid probability (**p**) value will be given as input.

Output
------

For each set of input, output in a single line the probability of the I th player to win. The output floating point number will always have four digits after the decimal point as shown in the sample output.


| Sample Input | Sample Output |
| --- | --- |
| 2 2 0.166666 1 2 0.166666 2 | 0.5455 0.4545 |


# Problem 1297

Descrição
----------

Arsenic & Cyanide Mining (ACM) is a corporation that has recently decided to start developing its mines in the lands near your hometown. As a member of the citizen's regulatory committee for ACM's operations, your task is to control how much the corporation can mine from those lands, so that you get to keep the jobs and other benefits without sacrificing the environment and the health of the local residents.

The ACM has plans to mine several rectangular patches of land. A patch of land has width W, can be dug up to a maximum depth D, and has a at surface which we consider to be at depth 0. The minerals in a patch are organized in three layers, which may vary in their depth along the width of the patch, but always have the same profile along its whole length. This is why the ACM is only interested in the profile along the width of each patch, and has performed exploratory work in order to precisely determine its shape.

âAs a result, they discovered that the two interfaces between the three layers of minerals can be represented by two functions y1(x) and y2(x), where the first describes the boundary between the top layer and the middle layer, and the second describes the boundary between the middle layer and the bottom layer. These functions are always such that

  

-D < y2(x) < y1(x) < 0 for 0 â¤ x â¤ W ,

  

so that the layers' boundaries never touch each other. Besides, each function has the form yi(x) = pi(x)/qi(x), where

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1297_a_en.png)â

  

for i = 1; 2 and a certain integer K. The figure below shows the profiles of two patches of land in the way the ACM represents them. The patch on the left has width W = 6 and depth D = 9, while the patch on the right has W = 8 and D = 10. The boundaries of the layers of each patch are described by the functions defined below them.

  

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1297_b_en.png)â

  

The ACM will dig everything in a patch of land up to a certain digging depth d, and then sell all the minerals thus obtained to make a profit. However, the minerals in the top and the bottom layers are essentially worthless, so the profit of the whole operation comes exclusively from those minerals in the middle layer. In fact, the profit is proportional to the area A of the middle layer in the profile that is at depth at most d. Given the description of a patch of land and an integer A, you would like to know the digging depth d you should allow the ACM to dig the patch so that they get an area of minerals from the middle layer in the profile of exactly A. In the figure above you can see the answer for the two test cases in the sample input. For the patch on the left, in order to get an area A = 14 the digging depth must be d = 4.00000, while for the patch on the right an area A = 14 requires a digging depth d = 5.51389.

Input
-----

Each test case is described using 5 lines. The first line contains four integers **W**, **D**, **A** and **K**, where **W** is the width of the patch of land the ACM wants to mine (1 â¤ **W** â¤ 8), **D** is its depth (1 â¤ **D** â¤ 10), **A** is the area of the middle layer in the profile that the ACM must get (1 â¤ **A** â¤ **W** x **D**), and **K** allows the definition of the interfaces y1(x) and y2(x) as explained above (0 â¤ **K** â¤ 8). Each of the other lines contains **K** + 1 integers between -108 and 108, inclusive. The second line contains the coeffificients of p1(x) from **P**1,0 to **P**1,K. The third line contains the coeficients of q1(x) from **Q**1,0 to **Q**1,K. The fourth line contains the coeficients of p2(x) from **P**2,0 to **P**2,K. The fifth line contains the coeficients of q2(x) from **Q**2,0 to **Q**2,**K**. Within each test case **A** is strictly less than the total area of the middle layer in the profile, and there exists a single value d such that a digging depth d yields an area of minerals from the middle layer in the profile of exactly **A**. Besides, q1(x) 6= 0, q2(x) 6= 0 and -**D** < y2(x) < y1(x) < 0, for 0 â¤ x â¤ **W**.

Output
------

For each test case output a line with a rational number representing the depth **d** that the ACM should be allowed to dig the patch of land so that they get an area of minerals from the middle layer in the profile of exactly **A**. The result must be output as a rational number with exactly five digits after the decimal point, rounded if necessary.


| Sample Input | Sample Output |
| --- | --- |
| 6 9 4 1 -10 1 2 0 -16 1 2 0 8 10 14 4 -1392 864 -216 24 -1 1312 -864 216 -24 1 -73 36 -54 36 -9 17 -4 6 -4 1 | 4.00000 5.51389 |

ACM/ICPC South America Contest 2012.


# Problem 1304

Descrição
----------

You have bought a car in order to drive from Waterloo to a big city. The odometer on their car is broken, so you cannot measure distance. But the speedometer and cruise control both work, so the car can maintain a constant speed which can be adjusted from time to time in response to speed limits, traffic jams, and border queues. You have a stopwatch and note the elapsed time every time the speed changes. From time to time you wonder, "how far have I come?". To solve this problem you must write a program to run on your laptop computer in the passenger seat.

Input
-----

Standard input contains several lines of input: Each speed change is indicated by a line specifying the elapsed time since the beginning of the trip (hh:mm:ss), followed by the new speed in km/h. Each query is indicated by a line containing the elapsed time. At the outset of the trip the car is stationary. Elapsed times are given in non-decreasing order and there is at most one speed change at any given time.

Output
------

For each query in standard input, you should print a line giving the time and the distance travelled, in the format below, using the standard rounding.


| Sample Input | Sample Output |
| --- | --- |
| 00:00:01 100 00:15:01 00:30:01 01:00:01 50 03:00:01 03:00:05 140 | 00:15:01 25.00 km 00:30:01 50.00 km 03:00:01 200.00 km |

Adapted by Gerson Groth


# Problem 1306

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1306.jpg)

In my country, streets donât have names, each of them are just given a number as name. These numbers are supposed to be unique but that is not always the case. The local government allocates some integers to name the roads and in many cases the number of integers allocated is less that the total number of roads. In that case to make road names unique some single character suffixes are used. So roads are named as 1, 2, 3, 1A, 2B, 3C etc. Of course the number of suffixes is also always limited to 26 (A, B, â¦, Z). For example if there are 4 roads and 2 different integers are allocated for naming then some possible assignments of names can be:

| 1, 2, 1A, 2B |
| --- |
| 1, 2, 1A, 2C |
| 3, 4, 3A, 4A |
| 1, 2, 1B, 1C |

Given the number of roads (**R**) and the numbers of integers allocated for naming (**N**), your job is to determine the minimum number of different suffixes that will be required (of all possible namings) to name the streets assuming that two streets can't have the same names.

Input
-----

The input file can contain up to **10002** lines of inputs. Each line contains two integers **R** and **N** (**R** < 10001, 0 < **N**). Here **R** is the total number of streets to be named and **N** denotes the number of integers allocated for naming. The end of input is determined by '0 0' and must not be processed.

Output
------

Each line of input produces one line of output. This line contains the serial of output followed by an integer **D** which denotes the minimum number of suffixes required to name the streets. If it is not possible to name all the streets print âimpossibleâ instead (without the quotes).


| Sample Input | Sample Output |
| --- | --- |
| 8 5 100 2 0 0 | Case 1: 1 Case 2: impossible |

Special Thanks: Sohel Hafiz. Adapted by Gerson Groth.


# Problem 1307

Descrição
----------

*"All you need is love. All you need is love.  

All you need is love, love... love is all you need."  

The Beatles*

  

There was invented a new powerfull gadget by the International Beautifull Machines corporation called the love machine! Given a string made of binary digits, the love machine answers if it's made only of love, that is, if all you need is love to build that string. The definition of love for the love machine is another string of binary digits, given by a human operator. Let's say we have a string L which represents "love" and we give a string S for the love machine. We say that all you need is love to build S, if we can repeatly subtract L from S until we reach L. The subtraction defined here is the same arithmetic subtraction in base 2. By this definition it's easy to see that if L > S (in binary), then S is not made of love. If S = L then S is obvious made of love.

Let's see an example. Supose S = "11011" and L = "11". If we reapetly subtract L from S, we get: 11011, 11000, 10101, 10010, 1111, 1100, 1001, 110, 11. So, given this L, all you need is love to build S. Because of some limitations of the love machine, there can be no string with leading zeroes. That is, "0010101", "01110101", "011111" etc. are invalid strings. Strings which have only one digit are also invalid (it's another limitation).

âYour task in this problem is: given two valid binary strings, S1 and S2, find if it's possible to have a valid string L such that both S1 and S2 can be made only of L (i.e. given two valid strings S1 and S2, find if there exists at least one valid string L such as both S1 and S2 are made only of L). For instance, for S1 = 11011 and S2 = 11000, we can have L = 11 such that S1 and S2 are both made only of L (as we can see in the example above).

Input
-----

The first line of input is a positive integer **N** (**N**< 10000) which stands for the number of teste cases. Then, **2\*N** lines will follow. Each pair of lines consists in one teste case. Each line of the pair stands for each string (**S1** and **S2**) to be entered as an input for the love machine. No string will have less than 2 or more than 30 characters. You can assume that all strings in the input will be valid acording to the rules above.

Output
------

For each string pair, you must print one of the following messages:

Pair #p: All you need is love!  

Pair #p: Love is not all you need!

âWhere p stands for the pair number (starting from 1). You should print the first message if there exists at least one valid string L such as both S1 and S2 can be made only of L. Otherwise, print the second line.


| Sample Input | Sample Output |
| --- | --- |
| 5 11011 11000 11011 11001 111111 100 1000000000 110 1010 100 | Pair #1: All you need is love! Pair #2: Love is not all you need! Pair #3: Love is not all you need! Pair #4: All you need is love! Pair #5: All you need is love! |

Maratona de ProgramaÃ§Ã£o da SBC 2001.  

Adapted by Neilor.


# Problem 1308

Descrição
----------

A troop of Etruscan warriors is organized as follows. In the first row, there is only one warrior; then, the second row contains two warriors; the third row contains three warriors, and so on. In general, each row *i* contains *i* warriors.

We know the number of Etruscan warriors of a given troop. You have to compute the number of rows in which they are organized.

Please note that there may be some remaining warriors (this could happen if they are not enough to form the next row). For example, 3 warriors are organized in 2 rows. With 6 warriors you can form 3 rows; but you can also form 3 rows with 7, 8 or 9 warriors.

Input
-----

The first line of the input contains an integer indicating the number of test cases. For each test case, there is a single integer **N** (0 â¤ **N** â¤ 1018), indicating the number of Etruscan warriors.

Output
------

For each test case, the output should contain a single integer indicating the number of rows that can be formed.


| Sample Input | Sample Output |
| --- | --- |
| 6 3 6 7 8 9 10 | 2 3 3 3 3 4 |

OMP'09, Facultad de Informatica. Universidad de Murcia (SPAIN).


# Problem 1309

Descrição
----------

Often it is necessary to write monetary amounts in a standard format. We decided formatting quantities in the following way:  

   1. The montande must begin with '$';  

   2. The number must end with a decimal point and exactly two digits following;  

   3. The digits to the left of the decimal point must separate in groups of three oir commas.

Your task in this problem is to create a program that, given two integer values ââto dollars and cents return String formatted properly.

Input
-----

The input consists of several test cases. Each test case consists of two integers, **dollars** (0 â¤ **dollars** â¤ 2 \* 109) and **cents** (0 â¤ **cents** â¤ 99), respectively.

Output
------

For each test case print a string formatted according to the formatting rules.


| Sample Input | Sample Output |
| --- | --- |
| 123456 0 49734321 9 20502030 70 | $123,456.00 $49,734,321.09 $20,502,030.70 |

\* Este problema Ã© de autoria do TopCoder (www.topcoder.com/tc) e foi adaptado por Mateus Lazarotto para utilizaÃ§Ã£o (autorizada) no URI OJ.  

\* A reproduÃ§Ã£o nÃ£o autorizada deste problema sem o consentimento por escrito de TopCoder, Inc. Ã© estritamente proibida.


# Problem 1323

Descrição
----------

Richard Phillips Feynman was a well known American physicist and a recipient of the Nobel Prize in Physics. He worked in theoretical physics and also pioneered the field of quantum computing. He visited South America for ten months, giving lectures and enjoying life in the tropics. He is also known for his books "Surely You're Joking, Mr. Feynman!" and "What Do You Care What Other People Think?", which include some of his adventures below the equator.

His life-long addiction was solving and making puzzles, locks, and cyphers. Recently, an old farmer in South America, who was a host to the young physicist in 1949, found some papers and notes that is believed to have belonged to Feynman. Among notes about mesons and electromagnetism, there was a napkin where he wrote a simple puzzle: "how many different squares are there in a grid of N ÃN squares?".

In the same napkin there was a drawing which is reproduced below, showing that, for N=2, the answer is 5.

![](https://resources.beecrowd.com/gallery/images/novos/Feynman.png)â

Input
-----

The input contains several test cases. Each test case is composed of a single line, containing only one integer **N**, representing the number of squares in each side of the grid (1 â¤ **N** â¤ 100).

The end of input is indicated by a line containing only one zero.

Output
------

For each test case in the input, your program must print a single line, containing the number of different squares for the corresponding input.


| Sample Input | Sample Output |
| --- | --- |
| 2 1 8 0 | 5 1 204 |

ACM/ICPC South America Contest 2008.


# Problem 1324

Descrição
----------

It's been 100 years since the detection of the first Higgs boson and now particle physics is a mainstream subject in all high schools. Obviously, kids love the fact that they can create tiny black holes using only their portable particle accelerators and show off to their friends and colleagues. Although the creation of big black holes that could swallow the whole planet is possible even with these portable particle accelerators, the devices are programmed to only thrown particles when this undesirable side effect is impossible.

Your granddaughter is trying to create her own black holes with a portable accelerator kit, which is composed of two small particle accelerators that throw, each one, a boson-sized particle. Both particles are thrown at the same time, and a black hole appears when the particles collide. However, your granddaughter doesn't know how much time she'll have to wait before this happens. Fortunately, each accelerator can predict the particle's trajectory, showing four integer values into its display, called A, B, C and D. Each value can be replaced into the following equations:

r = At + B

Î¸ = Ct + D

in order to determine the trajectory of the particle, in polar coordinates. The radius (r) is represented in distance units and the angle (Î¸) in degrees. The time (t) is given in time units and it is always a rational value which can be represented by an irreducible fraction. Your granddaughter knows that in polar coordinates a point has infinite representations. In general, the point (r, Î¸) can be represented as (r, Î¸ Â± k x360Â°) or ( -r, Î¸ Â±(2k + 1) Ã180Â°), where k is any integer. Besides, the origin (r = 0) can be represented as (0, Î¸) for any Î¸.

Using these parameters informed by each particle accelerator, your granddaughter wants to determine whether the particles will eventually collide and, if they do, the time when they will collide. After the first collision it is impossible to predict the particle's trajectory, therefore, only the first possible collision should be considered.

Although your granddaughter is really intelligent and has a deep knowledge of particle physics, she does not know how to program computers and is looking for some notes in her grandfather's (or grandmother's) ICPC notebook (don't forget, she is your granddaughter!). Fortunately for you, there is a note on your notebook which says that you wrote that code during the 2008 ICPC South America Regional Contest (or, to be more specific, this contest).

Input
-----

The input consists of several test cases, one per line. Each test case contains eight integer numbers separated by single spaces **A1** **B1** **C1** **D1** **A2** **B2** **C2** **D2**(-104 â¤ **A1** **B1** **C1** **D1** **A2** **B2** **C2** **D2**â¤ 104). The first four input values (**A1**, **B1**,**C1**, **D1**) correspond to the four parameters displayed by the first portable particle accelerator and the following input values (**A2**, **B2**, **C2**, **D2**) correspond to the four parameters displayed by the second portable particle accelerator when both particles are thrown. The end of the input
is represented by **A1**= **B1**= **C1**= **D1**= **A2**= **B2**= **C2**= **D2**= 0, which should not be processed as a test case, since these are the values displayed by the particle accelerators when a big black hole would be created if the particles were trown. Although the end of input is represented by a line with eight zeroes, note that the number zero is a possible input value.

The input must be read from standard input.

Output
------

For each test case, your program must output a line containing two non-negative integers ta and tbseparated by a single space. If there is no possibility of collision, ta = tb = 0, otherwise, ta/tb must be an irreducible fraction representing the earliest collision time. Even if the fraction results in an integer value, you still must output the number 1 as the denominator (see samples below).

The output must be written to standard output.


| Sample Input | Sample Output |
| --- | --- |
| 1 1 180 0 2 0 180 360 10 10 360 0 -24 18 180 72 5 5 180 0 -12 9 10 40 -9 5 5 180 2 5 5 180 0 0 0 0 0 0 0 0 | 1 1 0 0 4 17 0 1 |

ACM/ICPC South America Contest 2008.


# Problem 1338

Descrição
----------

In Ancient Egypt, the building of the pyramids is surrounded in mystery. Many researchers consider that the technology needed to build them wasn't available at the time, and suspect that the egyptians had extraterrestrial help to build them. An example of those mysteries are the "It-miha" numbers. In the egyptian province of It-miha, a rock with an inscripted sequence of numbers was found. Apparently the numbers had no connection to each other, until PoincarÃ©, at the end of the 19th century, conjectured that the recorded numbers were the first 500 square-free integers. A perfect square is an integer with an integer square root, such as 1, 4, 9, 16, 25, etc. We say that an integer is square-free if it isn't divisible by any perfect square greater than 1. It may sound simple to us today to determine those numbers, but over 3500 years ago, with a different numbering system, the calculations were very difficult to perform. The "It-miha" numbers are also very frequent in the design of the
pyramids. The Queops pyramid, for instance, has a base of 210 x 210 and height of 105 meters. All dimensions are "It-miha" numbers!!!

The first ten "It-miha" numbers are 1, 2, 3, 5, 6, 7, 10, 11, 13, 14. Your task in this problem is, given N, find the N-th "It-Miha" number.

Input
-----

The input has several test cases. The first line of the input contains an integer T corresponding to the number of cases. The first (and only) line of each test case contains an integer N, 1 â¤ N â¤ 20 000 000 000.

Output
------

For each test case, print a line containing the N-th square-free integer.


| Sample Input | Sample Output |
| --- | --- |
| 5 1 2 4 12 371 | 1 2 5 17 609 |

XIV Maratona de Programacao IME-USP 2010.


# Problem 1346

Descrição
----------

Natives from the tiny island of Tookutoo are keen on mathematics, and teach their children to play several math-oriented games. A popular puzzle in Tookutoo is played with ceramic slabs like the ones shown in the figure below.

![](https://resources.beecrowd.com/gallery/images/novos/Child%20Play.png)

As it can be seen in the figure above, slabs are similar to dominoes, being divided in two parts; in each part an integer value is imprinted. The slabs above have values [2, 1], [6, 3] and [3, 1]. Note that a slab [a, b] can also be written as [b, a].

The puzzle starts with a player receiving a set of slabs chosen randomly from a large and varied pool. Using the given set of slabs, the player has to find an arrangement in which the slabs are put side by side on the table in such a way that the sum of values on the upper side is equal to the sum of values on the lower side. For example, for the set in the figure above, a correct arrangement is

1 6 1  

2 3 3

If it is not possible to find an arrangement using all the slabs chosen, the player may discard one of them, but the value of the sum in the arrangement must be the highest possible. Besides, if more than one slab can be discarded while leaving the same sum, the player must discard the slab [a, b] such that a â¤ b and a is the least possible value considering all possible slabs to be discarded. You must write a program that, given a set of slabs, tries to find an arrangement that satisfies the conditions of the puzzle, discarding one slab if necessary.

Input
-----

Your program should process several test cases. The first line of a test case contains a single integer **N**, the number of slabs in the test (0 â¤ **N** â¤ 400). Each of the following **N** lines contains two integers **Xi** and **Yi** describing a slab that was given to the player (0 â¤ **Xi** â¤ 1000 and 0 â¤ **Yi** â¤ 1000) The value **N** = 0 indicates the end of input.

Output
------

For each test case your program must produce one line describing the result. If it is not possible to find an arrangement, print the word 'impossible'. If it is possible to find an arrangement, print its sum and the description of the discarded slab (if any). If you had do discard a slab, describe it in the form 'discard X Y', where **X** â¤ **Y**; otherwise print 'discard none'.


| Sample Input | Sample Output |
| --- | --- |
| 4 1 4 2 9 2 1 0 4 2 8 1 9 4 3 6 3 1 2 3 1 0 | 10 discard 1 2 impossible 8 discard none |

ACM/ICPC South America Contest 2003.


# Problem 1347

Descrição
----------

In the year of 2222, a terrible disaster happened at the kryptonite mine in Mars: a marsquake shook that part of the planet. Differently from earthquakes in Earth, marsquakes are not unusual on Mars. This one, however, caused the mine to start sinking slowly into the soil. The mine has a rectangular external shape, and its interior is like a maze, with high, straight walls and, most importantly, teleporters. Teleporters, as you know, can transport people instantly from one place to another. Teleporters in the mine are old models, using ancient technology, and can only teleport people if there is a clear view from one teleporter booth to another (that is, if there are no obstacles or walls in between the booths). You can see the map of the mine in the figure below.

![](https://resources.beecrowd.com/gallery/images/novos/Kryptonite%20Mine.png)â

You are trapped alone inside the mine. Fortunately, you have a map of the whole mine, know your current location, the positions of the walls, the locations of the exit and all teleporter booths. Unfortunately, the marsquake affected the energy system, and you know the teleporters can be used for a limited number of times only.

You want to get out of the mine walking as little as possible, since you sprained your ankle during the marsquake. You must find the route from your present location to the exit that requires the least amount of walking.

Input
-----

The input consists of many test cases. The first line of a test case contains three integers **N**, **M** and **L**, which indicate, respectively, the number of times the teleporters can be used, the number of walls in the mine and the number of teleporter booths (0 â¤ **N**, **M**, **L** â¤ 50). Each of the next **M** lines contains four integers **X**1, **Y**1, **X**2 and **Y**2, which represent the coordinates of the endpoints of a wall. You may ignore the thickness of walls and assume they do not intersect each other (â20000 â¤ **X**1 â¤ **X**2 â¤ 20000 and â20000 â¤ **Y**1 â¤ **Y**2 â¤ 20000). The next **L** lines contain the location of teleporter booths, given by two integers
**Xp** and **Yp**. The last line of each test case contains four integers **Xb**, **Yb**, **Xe** and **Ye** where (**Xb**, **Yb**) are the coordinates of your location and (**Xe**, **Ye**) are the coordinates of the mine's e xit. The end of input is indicated by **M** = **N** = **L** = 0.

Output
------

For each test case in the input your program must output a single line, containing an integer representing the distance you need to walk to get out of the mine. Of course, you should not consider the distances you teleported. The distance must be rounded to the nearest integer.


| Sample Input | Sample Output |
| --- | --- |
| 1 1 3 5 -4 5 4 1 0 5 5 9 0 0 0 10 0 1 1 3 5 -4 5 4 0 0 5 5 10 0 0 0 10 0 0 0 0 | 8 7 |

ACM/ICPC South America Contest 2003.


# Problem 1352

Descrição
----------

The government of the United Republic of Little Tower is developing a new kind of lottery. The main purpose of the lottery is to raise money to build Little Tower's Olympic Stadium, for an attendance of 400,000 people. The stadium is strategic for Little Tower's proposal to host the World Cup Finals in 2078. The lottery will run weekly. Each week, tickets in the form of square cards will be sold. Each ticket will have squares with printed numbers within, in a sequence of N rows and N columns, as shown in Figure 1.

![](https://resources.beecrowd.com/gallery/images/novos/Square%20Lottery.png)â  
Fig. 1: A sample lottery ticket, for N = 3.

In each ticket no number appears twice, and therefore all numbers from 1 to N2 are present (in random positions). There won't be two equal tickets sold in the same week. Nevertheless, all possible different tickets will be sold, since Little Towerâs citizens love lotteries. Tickets will be sold for T$1.00 (one Torreal, Little Towerâs monetary unit). To choose the winner(s), four numbers (between 1 and N2) will be picked randomly, and the ticket(s) whose chosen numbers positions are corners of a square will be awarded the prize money. For example, the ticket shown in Figure 1 is a winning ticket if the numbers picked are (6, 3, 2, 9), (1, 4, 2, 5) or (7, 8, 9, 6), but it is not a winning ticket if the numbers picked are (1, 7, 2, 9). If more than one ticket is a winner, customers who bought those tickets will share the weekâs lottery prize. The government of Little Tower asks your help to determine the prize value to be payed for each winning ticket, for a given N, and
a given percentage, over the total amount received for the tickets, that the government wants to pay as prizes.

Input
-----

Input will contain several test cases. Each test case is described in a line containing an integer **N** and a floating-point **P**, representing respectively the number of rows (and columns) of tickets, and the percentage of the money received that will be payed as prize (2 â¤ **N** â¤ 100 and 0 â¤ **P** â¤ 100.0). The end of input is indicated by **N** = **P** = 0.

Output
------

For each test case in the input your program should produce one line of output, containing a real value representing the prize to be payed to each winning ticket. The prize value must be printed with two digits precision, and the last decimal digit must be rounded. The input will not contain test cases where differences in rounding are significant.


| Sample Input | Sample Output |
| --- | --- |
| 2 100.0 2 80.0 3 50.0 0 0.0 | 1.00 0.80 10.50 |

ACM/ICPC South America Contest 2002.


# Problem 1353

Descrição
----------

I have a set of super poker cards, consisting of an infinite number of cards. For each positive integer **P**, there are exactly four cards whose value is **P**: Spade(**S**), Heart(**H**), Club(**C**) and Diamond(**D**). There are no cards of other values.

Given two positive integers **N** and **K**, how many ways can you pick up at most **K** cards whose values sum to **N**? For example, if **N** = 15 and **K** = 3, one way is 3**H** + 4**S** + 8**H**, shown below:

![](https://resources.beecrowd.com/gallery/images/novos/Super%20Poker.png)

Input
-----

There will be at most 20 test cases, each with two integers **N** and **K** (1 â¤ **N** â¤ 109, 1 â¤ **K** â¤ 10). The input is terminated by **N** = **K** = 0.

Output
------

For each test case, print the number of ways, modulo 1,000,000,009.


| Sample Input | Sample Output |
| --- | --- |
| 2 1 2 2 2 3 50 5 635645644 8 0 0 | 4 10 10 1823966 231863432 |

The Seventh Hunan Collegiate Programming Contest. Special Thanks: Jane Alam Jan. I/o by Neilor.


# Problem 1371

Descrição
----------

Madam Beauvoir has a mansion where she hosts her descendants (grandchildren and great-grandchildren) during their vacations. Her mansion has exactly N rooms (each room is numbered from 1 to N), and she has exactly N descendants (each descendant is also numbered from 1 to N).

Like all children, Mme. Beauvoir's descendants are really prankish. It's always the same mess: Every day, they wake up early in the morning before her, and meet in the garden. Then, each descendant, one at a time, enters the mansion and *switch the state* of the door of the rooms whose number is a multiple of his own number. *To switch the state* of a door means to close an open door or to open a closed door. So, for example, the descendant 15 will switch the state of the door of the rooms 15, 30, 45, and so on.

Initially, all doors are closed (all descendants close the doors before going to the garden). Also, each descendant enters exactly one time in the mansion (due to the mess, however, we don't know in which order). Which doors will be open once all descendants have entered the mansion?

Input
-----

The input consists of several test cases. Each test case is described by a line containing the integer **N** (0 â¤ **N** â¤ 25000000), the number of rooms and descendants. The last test case is followed by a line containing a single 0.

Output
------

For each test case, print the numbers of the rooms whose door will be open, in increasing order. Print a single space between consecutive numbers.


| Sample Input | Sample Output |
| --- | --- |
| 1 2 3 4 0 | 1 1 1 1 4 |

ACM/ICPC South America/Brazil Regional Contest 2006.


# Problem 1376

Descrição
----------

In the land of ACM ruled a great King who became obsessed with order. The kingdom had a rectangular form, and the King divided the territory into a grid of small rectangular counties. Before dying, the King distributed the counties among his sons.

However, he was unaware that his children had developed a strange rivalry: the first heir hated the second heir, but not the rest; the second heir hated the third heir, but not the rest, and so on . . . Finally, the last heir hated the first heir, but not the other heirs.

As soon as the King died, the strange rivalry among the Kingâs sons sparked off a generalized war in the kingdom. Attacks only took place between pairs of adjacent counties (adjacent counties are those that share one vertical or horizontal border). A county X attacked an adjacent county Y whenever the owner of X hated the owner of Y . The attacked county was always conquered by the attacking brother. By a rule of honor all the attacks were carried out simultaneously, and a set of simultaneous attacks was called a battle. After a certain number of battles, the surviving sons made a truce and never battled again. For example, if the King had three sons, named 0, 1 and 2, the figure below shows what happens in the first battle for a given initial land distribution:

![](https://resources.beecrowd.com/gallery/images/novos/Brothers.png)â

You were hired to help an ACM historian determining, given the number of heirs, the initial land distribution and the number of battles, what was the land distribution after all battles.

Input
-----

The input contains several test cases. The first line of a test case contains four integers **N**, **R**, **C** and **K**, separated by single spaces. **N** is the number of heirs (2 â¤ **N** â¤ 100), **R** and **C** are the dimensions of the kingdom (2 â¤ **R**, **C** â¤ 100), and **K** is the number of battles (1 â¤ **K** â¤ 100). Heirs are identified by sequential integers starting from zero (0 is the first heir, 1 is the second heir, ..., **N** â 1 is the last heir). Each of the next **R** lines contains **C** integers **Hr,c** separated by single spaces, representing initial land distribution: **Hr,c** is the initial owner of the county in row **r** and column **c** (0 â¤
**Hr,c** â¤ **N** â 1).

The last test case is followed by a line containing four zeroes separated by single spaces.

Output
------

For each test case, your program must print **R** lines with **C** integers each, separated by single spaces in the same format as the input, representing the land distribution after all battles.


| Sample Input | Sample Output |
| --- | --- |
| 3 4 4 3 0 1 2 0 1 0 2 0 0 1 2 0 0 1 2 2 4 2 3 4 1 0 3 2 1 2 8 4 2 1 0 7 1 6 2 5 3 4 0 0 0 0 | 2 2 2 0 2 1 0 1 2 2 2 0 0 2 0 0 1 0 3 2 1 2 7 6 0 5 1 4 2 3 |

ACM/ICPC South America Contest 2009.


# Problem 1380

Descrição
----------

Heinrich Hermann Robert Koch was a German doctor who lived from 1843 to 1910 and was famous for having isolated the bacillus that causes tuberculosis. His studies on the disease that caused many deaths until the mid-twentieth century enabled the development of a vaccine that saved millions of lives across the world. Robert Koch was awarded in 1905 with the Nobel Prize of Medicine and is considered one of the fathers of Microbiology.

One of the studies of Koch was connected to the growth rate of the population of bacilli. Koch noted that the bacilli take a moment of time to reach maturity and initiate the cellular division. Thereafter, the bacillus generates at each instant of time a new individual by a split. Thus, if we assume an initial population with only one individual in the next moment we will also have one (it reaches maturity for division), the following we will have 2, at the other 3, so the 5 and so on.

Your task is, given an integer K, determine the last three digits of the bacilli after K time steps, starting from an initial population with an individual.

Input
-----

The input consists of several instances. The first line of input contains an integer **T** indicating the number of instances.

Each instance consists of a single line containing an integer K (1 â¤ **K** â¤ 101000000).

Output
------

For each instance print a line containing the last three digits of the bacilli after **K** time instants.


| Sample Input | Sample Output |
| --- | --- |
| 5 1 4 10 21312 1000000 | 001 003 055 744 875 |

XII Maratona de ProgramaÃ§Ã£o IME-USP 2008.


# Problem 1381

Descrição
----------

Diophantus of Alexandria lived in the third century AD and is considered by many as the "father of algebra". His book "Arithmetica" was about the solution of algebraic equations with integer coefficients for which it also seeks integer solutions. These equations are known as Diophantine equations. A great scholar of Diophantus' work was Pierre de Fermat, a known French mathematician.

In this problem you must solve a class of Diophantine equations of the type x1 + x2 + ... +xn = C. That is, given integers N and C, determine how many non-negative integer solutions exist for the equation x1 + x2 + ... +xn = C, where0 â¤ xi â¤ C for all i = 1, 2, ... , N.

Input
-----

The input is composed of several test cases. The first line of input contains an integer **T** indicating the number of test cases. Each test case consists of a line containing two integers **N** and **C** (1 â¤ N, C â¤ 1000000). Due the possibility of this number be too big, so print it as module 1300031 (number % 1300031).

Output
------

For each test case print a line containing the number of integer solutions that satisfy the constraints.


| Sample Input | Sample Output |
| --- | --- |
| 2 7 4 3 5 | 210 21 |

XII Maratona de ProgramaÃ§Ã£o IME-USP 2008.


# Problem 1390

Descrição
----------

What do you get if you multiply 6 by 9? The answer, of course, is 42, but only if you do the calculations in base 13.

Given an integer B â¥ 2, the base B numbering system is a manner of writing integers using only digits between 0 and B - 1, inclusive. In a number written in base B, the rightmost digit has its value multiplied by 1, the second rightmost digit has its value multiplied by B, the third rightmost digit has its value multiplied by B2, and so on.

Some equations are true or false depending on the base they are considered in. The equation 2 + 2 = 4, for instance, is true for any B â¥ 5 - it does not hold in base 4, for instance, since there is no digit '4' in base 4. On the other hand, an equation like 2 + 2 = 5 is never true.

Write a program that given an equation determines for which bases it holds.

Input
-----

Each line of the input contains a test case; each test case is an equation of the form "EXPR=EXPR", where both "EXPR" are arithmetic expressions with at most 17 characters.

All expressions are valid, and contain only the characters '+', '\*' and the digits from '0' to '9'. No expressions contain leading plus signs, and no numbers in it have leading zeros.

The end of input is indicated by a line containing only "=".

Output
------

For each test case in the input your program should produce a single line in the output, indicating for which bases the given equation holds.

If the expression is true for infinitely many bases, print "B+", where B is the first base for which the equation holds.

If the expression is valid only for a finite set of bases, print them in ascending order, separated by single spaces.

If the expression is not true in any base, print the character '\*'.


| Sample Input | Sample Output |
| --- | --- |
| 6\*9=42 10000+3\*5\*334=3\*5000+10+0 2+2=3 2+2=4 0\*0=0 = | 13 6 10 \* 5+ 2+ |

ACM/ICPC South America Contest 2008.


# Problem 1392

Descrição
----------

Itâs year 2100. Electricity has become very expensive. Recently, your electricity company raised the power rates once more. The table below shows the new rates (consumption is always a positive integer):

![](https://resources.beecrowd.com/gallery/images/novos/Eletric%20Bill.png)

This means that, when calculating the amount to pay, the ï¬rst 100 CWh have a price of 2 Americus each; the next 9900 CWh (between 101 and 10000) have a price of 3 Americus each and so on.

For instance, if you consume 10123 CWh you will have to pay 2Ã100+3Ã9900+5Ã123 = 30515 Americus.

The evil mathematicians from the company have found a way to gain even more money. Instead of telling you how much energy you have consumed and how much you have to pay, they will show you two numbers related to yourself and to a random neighbor:

**A**: the total amount to pay if your consumptions were billed together; and  

**B**: the absolute value of the diï¬erence between the amounts of your bills.

If you canât ï¬gure out how much you have to pay, you must pay another 100 Americus for such a âserviceâ. You are very economical, and therefore you are sure you cannot possibly consume more than any of your neighbors. So, being smart, you know you can compute how much you have to pay. For example, suppose the company informed you the following two numbers: **A** = 1100 and **B** = 300. Then you and your neighborâs consumptions had to be 150 CWh and 250 CWh respectively. The total consumption is 400 CWh and then **A** is 2Ã100+3Ã300 = 1100. You have to pay 2Ã100+3Ã50 = 350 Americus, while your neighbor must pay 2Ã100+3Ã150 = 650 Americus, so **B** is |350 â 650| = 300.

Not willing to pay the additional fee, you decided to write a computer program to ï¬nd out how much you have to pay.

Input
-----

The input contains several test cases. Each test case is composed of a single line, containing two integers **A** and **B**, separated by a single space, representing the numbers shown to you (1 â¤ **A**, **B** â¤ 109). You may assume there is always a unique solution, that is, there exists exactly one pair of consumptions that produces those numbers.

The last test case is followed by a line containing two zeros separated by a single space.

Output
------

For each test case in the input, your program must print a single line containing one integer, representing the amount you have to pay.


| Sample Input | Sample Output |
| --- | --- |
| 1100 300 35515 27615 0 0 | 350 2900 |

ACM/ICPC South America Contest 2009.


# Problem 1393

Descrição
----------

The path to Mary's school is a straight line paved with hexagonal tiles. The picture below shows an example of the path with 12 numbered tiles.

![](https://resources.beecrowd.com/gallery/images/novos/Hexagonal%20Tiles.png)â

Mary loves mathematics. When going to school, she steps on the tiles of that path following these rules:

* She always starts from the tile with the smiling face (as nothing matches starting anything with a smile!). This tile is always present at the beginning of the path. The other tiles are numbered consecutively, in ascending order, starting from 1, as shown in the figure.
* She is not allowed to go back, that is, she must not step on a tile which bears a lower number than the tile she is on (when decided to go to school, there she goes!).
* She always steps from a tile to a neighboring one (no jumps in order to keep out of harm's way!).
* She must always finish on the highest numbered tile.

When classes are over, she is so tired that she avoids the path and walks on the lawn. Mary does not want to repeat any sequence of steps on the tiles and she would like to know, if the path is paved with N numbered tiles and a tile with the face, how many days will it take to make each possible sequence once.

For example, five days will be needed for her to try all possible step sequences if the path has N = 4 tiles, one day for each of the sequences: 1-2-3-4, 1-2-4, 1-3-4, 2-3-4 and 2-4. Write a program to determine how many different step sequences there are for a path with a given number N of tiles.

Input
-----

The input contains several test cases. Each test case is composed by a line containing an integer **N** (1 â¤ **N** â¤ 40), the number of tiles in the path. The last test case is followed by a line containing a single zero.

Output
------

For each test case, print a line containing a single integer, the number of different step sequences.


| Sample Input | Sample Output |
| --- | --- |
| 1 4 2 10 0 | 1 5 2 89 |

ACM/ICPC South America Contest 2009.


# Problem 1398

Descrição
----------

*Ocean deep  

I'm so afraid to show my feelings,  

I have sailed a million ceilings  

In my solitary room  

Ocean deep*

The lines above are from a very popular song of Cliff Richard. In this problem we will be dealing with a similar type of person. His name is Rampell-Stilt-Skin and another important thing is that he is a dead man. Someone has killed him a few days ago and you are the detective to solve the mystery. The problem with this guy is that he always tried to hide his information and feelings under the sea (I mean out of reach). He wrote a diary, which contained some statements and then a large binary number (May have as many as 10000 digits). If the number is divisible by a large prime number 131071 then the statement is true, otherwise the statement is false.

In this problem you will be given large binary numbers as input and you will have to verify if that number is divisible by 131071 or not. Your algorithm needs to be very efficient.

Input
-----

The input file contains several binary numbers. Each binary number starts in a new line but may expand in several lines. Each number is terminated by a *#* symbol. No line contains more than 100 digits.

Output
------

For every binary number print "*YES*" if the number is divisible by the given prime number, print "*NO*" if the binary number is not divisible by the given prime number.


| Sample Input | Sample Output |
| --- | --- |
| 0# 1010101# | YES NO |

âAfter my last exam of my undergraduate course, I discovered that I have studied boilers, electric motors,  

mechanical drawing, accounting, professionalism in computer science, Continuous Mathematics, etc in  

my undergraduate courses, but, I never had the chance to study Knuthâs âConcrete Mathematicsâ in  

any of my courses. So now, when I am reading it seriously, I realize that no one should be a  

Computer Science (& Engineering) Graduate before reading this book. But, surely, I  

would have to thank one of my teachers for letting me know about this book.â


# Problem 1399

Descrição
----------

Write a program to transform an array A[1], A[2],..., A[n] according to m instructions. Each instruction (L, R, v, p) means: First, calculate how many numbers from A[L] to A[R] (inclusive) are strictly less than v, call this answer k. Then, change the value of A[p] to u\*k/(R - L + 1), here we use integer division (i.e. ignoring fractional part).

Input
-----

The first line of input contains three integer **n**, **m**, **u** ( 1 â¤ **n** â¤ 300,000, 1 â¤ **m** â¤ 50,000, 1 â¤ **u** â¤ 1,000,000,000). Each of the next **n** lines contains an integer **A**[i](1 â¤ **A**[i] â¤ **u**). Each of the next **m** lines contains an instruction consisting of four integers **L**, **R**, **v**, **p** ( 1 â¤ **L** â¤ **R** â¤ **n**, 1 â¤ **v** â¤ **u**, 1 â¤ **p** â¤ **n**).

Output
------

Print **n** lines, one for each integer, the final array.


| Sample Input | Sample Output |
| --- | --- |
| 10 1 11 1 2 3 4 5 6 7 8 9 10 2 8 6 10 | 1 2 3 4 5 6 7 8 9 6 |

Explanation: There is only one instruction: L = 2, R = 8, v = 6, p = 10. There are 4 numbers (2,3,4,5) less than 6, so k = 4. The new number in A[10] is 11\*4/(8 - 2 + 1) = 44/7 = 6. I/O by Neilor.


# Problem 1400

Descrição
----------

There are n people standing in a line, playing a famous game called "counting". When the game begins, the leftmost person says "1" loudly, then the second person (people are numbered 1 to n from left to right) says "2" loudly. This is followed by the 3rd person saying "3" and the 4th person say "4", and so on. When the n-th person (i.e. the rightmost person) said "n" loudly, the next turn goes to his immediate left person (i.e. the (n - 1)-th person), who should say "n + 1" loudly, then the (n - 2)-th person should say "n + 2" loudly. After the leftmost person spoke again, the counting goes right again. There is a catch, though (otherwise, the game would be very boring!): if a person should say a number who is a multiple of 7, or its decimal representation contains the digit 7, he should clap instead! The following tables shows us the counting process for n = 4 ('X' represents a clap). When the 3rd person claps for the 4th time, he's actually counting 35.

| Person | 1 | 2 | 3 | 4 | 3 | 2 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action | 1 | 2 | 3 | 4 | 5 | 6 | X | 8 | 9 |
| Person | 4 | 3 | 2 | 1 | 2 | 3 | 4 | 3 | 2 |
| Action | 10 | 11 | 12 | 13 | X | 15 | 16 | X | 18 |
| Person | 1 | 2 | 3 | 4 | 3 | 2 | 1 | 2 | 3 |
| Action | 19 | 20 | X | 22 | 23 | 24 | 25 | 26 | X |
| Person | 4 | 3 | 2 | 1 | 2 | 3 | 4 | 3 | 2 |
| Action | X | 29 | 30 | 31 | 32 | 33 | 34 | X | 36 |

Given n, m and k, your task is to find out, when the m-th person claps for the k-th time, what is the actual number being counted.

Input
-----

There will be at most 100 test cases in the input. Each test case contains three integers **n**, **m** and **k** ( 2 â¤ **n** â¤ 100, 1 â¤ **m** â¤ **n**, 1 â¤ **k** 100) in a single line. The last test case is followed by a line with **n** = **m** = **k** = 0, which should not be processed.

Output
------

For each line, print the actual number being counted, when the **m**-th person claps for the **k**-th time. If this can never happen, print '-1'.


| Sample Input | Sample Output |
| --- | --- |
| 4 3 1 4 3 2 4 3 3 4 3 4 0 0 0 | 17 21 27 35 |

The Seventh Hunan Collegiate Programming Contest. Special Thanks: Yiming Li & Jane Alam Jan. I/O by UOJ.


# Problem 1422

Descrição
----------

Pietro Demazio is an Italian terrorist that escaped to Brazil and is now disguised as a game programmer. For his new plan to destroy the world, Pietro has developed a new kind of bacterium that is able to decimate the entire world population.

Demazio spent 4 days creating these microorganisms' colonies. In the end of the 4th day, however, he found out that their genetic code had an error. This error makes the bacteria die after living for 4 days. Since the first colony was created 3 days before, he quickly modified the genetic code (through radiation), in such a way that his bacteria reproduce every day. This is an asexual reproduction, and is done by bi-partitioning (i.e., one bacterium generates exactly one other bacterium in a day).

So, suppose that Pietro created 3 bacteria in the first day, 4 bacteria in the second day, 2 bacteria in the 3rd day and 5 bacteria in the 4th day. He will have 14 bacteria by the end of the 4th day, when he applies the mutation. Right after the mutation, they reproduce, and then he'll have 28 bacteria. Since the first colony (with 3 bacteria) dies in the end of the 4th day, the number of bacteria in the beginning of the 5th day is 25. By the end of the 5th day, these 25 bacteria reproduce, resulting in 50 bacteria. Since the second colony (with 4 bacteria) dies by the end of this day, he'll have 46 bacteria in the beginning of the 6th day.

Demazio carefully watches the growing of his bacteria population, and is already planning when to use them. To do so, he needs to know how many bacteria there will be after a given number of days. He is asking you to write a program that determines the number of bacteria that there will be after N days, given the number of bacteria of the colonies in the first 4 days.

Input
-----

The input consists of many test cases. Each test case consists of two lines. The first line contains the integer **N** (5 â¤ **N** â¤ 1,000,000,000), the number of days for which Pietro wants to know the number of bacteria he will have. The second line contains four integers **a1, a2, a3, a4** (1 â¤ **a1, a2, a3, a4** â¤ 1,000). The integer **ak** indicates the number of bacteria that were created in the **k**-th day.

The last test case if followed by a line with **N**=0.

Output
------

For each test case, print a line containing the number of bacteria Pietri will have after **N** days, modulo 13371337.


| Sample Input | Sample Output |
| --- | --- |
| 5 1 2 3 4 7 9 2 3 4 0 | 19 101 |

XIII Maratona de ProgramaÃ§Ã£o IME-USP 2009.


