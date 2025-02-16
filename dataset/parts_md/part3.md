# Problem 1433

Descrição
----------

The ACM (All Can Meet) club was created with the purpose of attracting people of all ages, with the idea that the people could sit together and share their life experience, to the beneï¬t of all. But as it happened, the club became such a huge success that it was practically impossible to gather all its members at the same place and time. The club then decided to split its members into smaller âsectionsâ. In order to make sure that sections are âniceâ, the director of the club decided to impose the following requirements:

A. all members of the same age should be in the same section,

B. all members should be part of exactly one section,

C. in each section, the maximum number of people with the same age should not be more than **R** times the minimum number of people with the same age, where **R** is a rational number between 1.0 and 2.0. The number **R** is called the splitting factor of the club.

The last condition makes sure that there is no relatively small-age group which might feel uncomfortable in the section. For instance, let denote by [**N**, **M**] a group with **N** members who are **M**-years old. Then in section {[10, 50], [6, 45], [70, 12], [43, 23]} the maximum number of people with the same age is 70, the minimum number of people with the same age is 6. If **R** = 2.0, then we say this section does not satisfy the requirement (**C**) since 70/6 > 2.0. However, we can split this section into two smaller sections, namely {[10, 50],[6, 45]} and {[70, 12], [43, 23]}, which satisfy all the requirements.

Given the splitting factor **R** and a list of the members of the club, you must write a program to ï¬nd the minimum number of sections satisfying the three requirements above.

Input
-----

Your program should process several test cases. The ï¬rst line of a test case contains an integer **K** and a rational **R**. **K** represents the number of different ages in the club (1 â¤ **K** â¤ 120), and **R** represents the splitting factor set by the club director (1.0 â¤ **R** â¤ 2.0). The next **K** lines describe the group members, each line containing two integers **N** and **M**, indicating that there are **N** members who are **M**-years old in the club (1 â¤ **N** â¤ 10000 and 1 â¤ **M** â¤ 120). The end of input is indicated by a line with **K** = 0 and **R** = 0.0.

The input values will be such that the eventual error in the internal binary representation of **R** will not affect the result.

*The input must be read from standard input.*

Output
------

For each instance of the problem you should output a single line, containing the minimum number of groups satisfying the three requirements above.

*The output must be written to standard output.*


| Sample Input | Sample Output |
| --- | --- |
| 5 1.7 100 7 18 10 11 17 567 25 62 34 3 1.0 12 18 107 11 250 57 0 0.0 | 3 3 |

ACM/ICPC South America Contest 2003.


# Problem 1434

Descrição
----------

In ancient times, patrollers were used to ensure that all the cities of the Roman Empire were under control. A patrollerâs job consisted in continuously visiting the cities of the empire, trying to minimise the interval between two visits to each city. The Military Society (MS) wants to simulate the behavior of one such patroller to see how eï¬ective they were.

Each cycle of the simulation corresponds to one time unit. The Instantaneous City Idleness (ICI) for a city **X** after **T** cycles of the simulation is the number of cycles elapsed since the last visit of the patroller to the city **X** (i.e. the number of time units the city **X** remained unvisited). All of the cities have initial Instantaneous City Idleness equal to zero at the start of the simulation. The Instantaneous Empire Idleness (IEI) after each given cycle is the sum of the Instantaneous City Idleness of all cities after that given cycle. Finally, the Empire Idleness (EI) for an **N**-cycle simulation is the sum of the Instantaneous Empire Idleness after each of the **N** cycles of simulation.

After visiting a city **X**, the patroller always chooses to visit the neighbour city **Y** with the highest Instantaneous City Idleness (if more than one city has the highest idleness, the one with the lowest identiï¬er is chosen). Cities **X** and **Y** are neighbour if there is a road linking the two cities directly, without going through any intermediate city. In the beginning of the simulation, the patroller is located in one of the cities, and is given a map of the Roman Empire containing a description of all the roads in the empire, indicating the length (in kilometers) and which two cities each road connects. A road between cities **X** and **Y** can be used both to go from **X** to **Y** and from **Y** to **X**.

Assuming that a patroller travels one kilometer in one time unit (one simulation cycle) and that the time to visit a city is negligible (equal to zero), MS asks you to determine the Empire Idleness after an **N**-cycle simulation.

For clarity, consider the example of an empire which contains 3 cities (1, 2 and 3) and two roads of length 1 km. The first road connects cities 1 and 2, while the second road connects cities 2 and 3. Below you ï¬nd a trace of a 3-cycle simulation for such a scenario, considering that the patroller starts at city 1.

Start of the simulation  

Patroller at: 1  

ICI1 = 0, ICI2 = 0, ICI3 = 0  

IEI = 0  

EI = 0

After cycle 1  

Patroller at: 2  

ICI1 = 1, ICI2 = 0, ICI3 = 1  

IEI = 2  

EI = 2

After cycle 2  

Patroller at: 1  

ICI1 = 0, ICI2 = 1, ICI3 = 2  

IEI = 3  

EI = 5

After cycle 3  

Patroller at: 2  

ICI1 = 1, ICI2 = 0, ICI3 = 3  

IEI = 4  

EI = 9

Therefore, for such a scenario, after 3 simulation cycles the Empire Idleness is 9.

Input
-----

The input consists of several test cases. The ï¬rst line of a test case contains four integers **C**, **R**, **N**, and **S**, indicating respectively the quantity of cities in the empire (2 â¤ **C** â¤ 1000), the number of roads (1 â¤ **R** â¤ **C**(**C** â 1)/2), the number of cycles to be simulated (1 â¤ **N** â¤ 1000) and the identiï¬er of the starting city of the patroller (1 â¤ **S** â¤ **C**). Each city is identiï¬ed by a distinct integer from 1 to **C**. Each of the following **R** lines contains three integers **X**, **Y** and **D** describing a road; **X** and **Y** represent cities (1 â¤ **X** â  **Y** â¤ **C**) and **D** represents the distance (1 â¤ **D** â¤ 1000), in kilometers, of the road that connects **X** and **Y** directly, without passing through any other city. Each pair of cities **X** and **Y** will appear at most once in a road description. You can assume that it is always possible to travel from any
city to any other city in the empire using the roads available. The end of input is indicated by **C** = **R** = **N** = **S** = 0.

Output
------

For each test case in the input, your program must produce one line containing the Empire Idleness after the **N**-cycle simulation.


| Sample Input | Sample Output |
| --- | --- |
| 2 1 1 1 1 2 2 2 1 2 1 1 2 2 2 1 3 1 1 2 2 2 1 4 1 1 2 2 3 2 3 1 1 2 1 2 3 1 0 0 0 0 | 2 4 8 10 9 |

ACM/ICPC South America/Brazil Regional Contest 2004.


# Problem 1436

Descrição
----------

There is a village in Bangladesh, where brick game is very popular. Brick game is a team game. Each team consists of odd number of players. Number of players must be greater than 1 but cannot be greater than 10. Age of each player must be within 11 and 20. No two players can have the same age. There is a captain for each team. The communication gap between two players depends on their age difference, i.e. the communication gap is larger if the age difference is larger. Hence they select the captain of a team in such a way so that the number of players in the team who are younger than that captain is equal to the number of players who are older than that captain.

Ages of all members of the team are provided. You have to determine the age of the captain.

Input
-----

Input starts with an integer **T (T â¤ 100)**, the number of test cases. Each of the next **T** lines will start with an integer **N (1 < N < 11)**, number of team members followed by **N** space separated integers representing ages of all of the members of a team. Each of these N integers will be between **11** and **20** (inclusive). Note that, ages will be given in strictly increasing order or strictly decreasing order. We will not mention which one is increasing and which one is decreasing, you have to be careful enough to handle both situations.

Output
------

For each test case, output one line in the format **âCase x: aâ** (quotes for clarity), where **x** is the case number and a is the age of the captain.


| Sample Input | Sample Output |
| --- | --- |
| 2 5 19 17 16 14 12 5 12 14 16 17 18 | Case 1: 16 Case 2: 16 |

Adapted by Gerson Groth.


# Problem 1444

Descrição
----------

Pirabeiraba is a district of Joinville, where german settlers installed themselves at the start of the 20th century. Annually there is the cassava party, a tuber that is also known as macaxeira in the brazilian northeast region. To accompany the cassava, there's nothing like a traditional germanic dish: the stuffed drake! For the culinary experts, there is a magic in this combination: drake with cassava. However, to kill the drake, you must capture him while his blood is very warm. For that, the drake must be tired. People say that his warm blood is synonymous with fertility, in other words: an aphrodisiac! But that's for another story.

In this game of chasing the drake, an idea came of tiring them with a race between themselves. The physical space of the Society Rio da Prata is limited, because of that they built only three lanes to do these races. The races are made with groups of two and three drakes. The drakes who gets the first places on the races are then arranged again in groups of 2 or 3 for another round. This goes on until there's only one drake left, the champion, which escapes from the saucepan (for now) as a prize. All the *surviving* drakes must race in the round, that is, if it's not possible to split all the drakes in groups of three, some groups of two must be formed in order to minimize the number of races. Examples are seen in the Figure 1.

![](https://resources.beecrowd.com/gallery/images/novos/Corrida%20dos%20Marrecos.png)

Figure 1: Examples: competition with 4, 5 and 6 drakes.

The losing drakes will be the first to go to the saucepan. You were invited to eat drake with cassava, but in exchange you must write a program that calculates the number of races that must be made to determinate the champion drake.

Input
-----

The program input is composed by various test cases. Each test case is composed by a line containing an integer **n**, where 0 â¤ **n** â¤ 100,000, and where **n** = 0 is used solely to mark the end of the input, which must be disconsidered.

Output
------

Your program must print in the standard output a line per test case, containing the number of races needed to choose the champion drake.


| Sample Input | Sample Output |
| --- | --- |
| 3 4 5 6 0 | 1 3 3 3 |

Maratona de Programacao UDESC 2013.


# Problem 1450

Descrição
----------

Ramesses II was the most prestigious of all egyptian pharaohs. He reigned between 1279 BC - 1213 BC, and built various temples, including the famous Nubian temples. The most famous one is a rock sculpture, in Abu Simpel, close to the second Nile waterfall, where the very same pharaoh is reproduced. With Nefertari and other wives he probably had more than 6 childs, with whom he liked to play a game called "highest pyramid". The game was played as follows: the kids received small parallelepipeds of different dimensions (which could be rotated), and with those cubes they had to build the highest pyramid they could. To build it they couldn't place a block on top of a smaller one, that is, if block A is on top of the block B, both the width and depth of A should be smaller than those of B.

Amenhotep, his first-born son, was very good on this game, and could build pyramids that are much taller than his father's. So Ramesses decided to call the great mathematic of the court, Narmer, to find the highest pyramid possible to build for each set of parallelepipeds, that is, the highest pyramid possible to build.

Input
-----

The input is composed of several test cases. The first line of the input contains an integer **T** indicating the number of test cases.

The first line of each instance contains an integer **N**, where 1 â¤ **N** â¤ 15, indicating the number of blocks. Each one of the **N** following lines will have three integers **X**, **Y** and **Z** that indicates the measurements of the block.

Output
------

For each instance print a line containing the height of the highest pyramid possible.


| Sample Input | Sample Output |
| --- | --- |
| 3 5 10 10 10 50 50 50 40 40 40 20 20 20 30 30 30 2 20 20 20 30 33 10 2 100 10 10 100 12 8 | 150 33 110 |

XIV Maratona de ProgramaÃ§Ã£o IME-USP 2010.


# Problem 1457

Descrição
----------

Every Computer Scientist worth his salt knows the book "The Hitchhiker's Guide to the Galaxy" and knows the answer to the fundamental question about life, the universe and everything. But what few know is that the story of Douglas Adams is based on an Egyptian legend, of an oracle located in Eskendereyya (Alexandria). Alexandria today is the largest city of Egypt, with more than 4 million inhabitants. It is in the Nile Delta, and stretches for 32km along the Mediterranean coast. In the past, the city founded in 331 BC by Alexander the Great, was one of the main cities in the world and there was the Lighthouse of Alexandria (one of the 7 Wonders of the Ancient World), the Library of Alexandria (the largest in the ancient world) and other fantastic works. The legend also says that there was the great oracle of Alexandria. The townspeople delivered the oracle small tickets with numbers noted, and received back a number, that would be the answer to a fundamental question of the universe
related to the two given numbers.

In his treatise of 227 AD Cleomenes of Naucratis (who became administrator of Alexandria when Alexander departed for his conquests) reports some results of the oracle:

* Given 8 and 1 the oracle returned 40320;
* Given 10 and 3, returned 280;
* Given 4 and 2, returned 8;
* Given 21 and 19, returned 42.

Modern studies realized that what the oracle returned was nothing more than a generalization of the factorial of an integer. As we know,

N! = N x (N-1) x ... x 1.

What the oracle returned for the data N and K, was the K-factor of N, in other words,

N x (N-K) x (N-2K) x (N-3K) x ...,

in which the product was made while the difference is greater than or equal to 1. We can represent the K-factor of a number for him followed by K exclamations:

* 8! = 40320;
* 10!!! = 280;
* 4!! = 8;
* 21!!!!!!!!!!!!!!!!!!! = 42

They say that when reading about the legend of oracle Eskendereyya, Douglas Adams got his inspiration for his work. Also, in Egypt is the inspiration of the restaurant at the end of the universe, but that's another story ...

Given the integers N and K your task is determine K-factor of N.

Input
-----

The input is composed of several instances. The first line of input contains an integer **T** indicating the number of instances.

The first (and only) row of each instance contains an integer **N** followed by **K** points exclamation, where 1 â¤ **N** â¤ 100 and 1 â¤ **K** â¤ 20.

Output
------

For each instance print a line containing the **K**-factor of **N**.

It is guaranteed that no instance in the input has a result greater than 1018.


| Sample Input | Sample Output |
| --- | --- |
| 4 3! 10!!! 19!!!! 4!! | 6 280 65835 8 |

XIV Maratona de ProgramaÃ§Ã£o IME-USP 2010.


# Problem 1465

Descrição
----------

Complex numbers are not only complex, but also complicated. So you would better try to solve another problem...

We have a complex number, **a**+**b**\***i**, where **i** is the square root of -1. We want to make it simple (I mean, real), by raising it to a natural power. For example, complex number 2+2\***i**, can be made simple by raising it to 4:

(2+2\***i**)4 = -64

You have to compute the smallest natural number, **N**, (zero is not included) such that (**a**+**b**\***i**)**N** is a real number. Besides, we require that the absolute value of (**a**+**b**\***i**)**N** is not bigger than 230.

Input
-----

The first line of the input contains an integer **M**, indicating the number of test cases.

For each test case, there is a line with two integers **A** and **B**. **A** is the real part of the complex number, and **B** is the imaginary part.

You can assume that -10000 â¤ **A** â¤ 10000, and -10000 â¤ **B** â¤ 10000.

Output
------

For each test case, the output should consist of a single positive natural number **N** in one line, indicating the power such that (**A**+**B**\***i**)**N** is real and its absolute value is not greater than 230. If there is no solution, you have to output "TOO COMPLICATED".


| Sample Input | Sample Output |
| --- | --- |
| 5 817 0 2 2 0 -1 18 92 -7 7 | 1 4 2 TOO COMPLICATED 4 |

Olimpiadas Murcianas de ProgramaciÃ³n 2009.


# Problem 1481

Descrição
----------

Zing Zhu owns an island that is a piece of flat land. Everyday, when the tide rises, the island is flooded by sea water. After much thinking and asking advice from members of his family, Zing Zhu decided to set up an oyster farm in the island. Zing Zhu uses a sophisticated system of plastic watertight modular fences to control the areas that will be flooded and the areas that will not be flooded during the rise of the tide. The fences used by Zing Zhu are either horizontal or vertical and come in strips that have different lengths and heights. Two fences can intersect in at most one point, not necessarily in their ends.

![](https://resources.beecrowd.com/gallery/images/novos/Zing%20Zhu%E2%80%99s%20Oyster%20Farm.png)â

Picture 1 (left): Map of fence strips installed in the farm, showing fence strip heights in centimeters.

Picture 2 (right): Non-flooded areas (shown in white) if the tide rises 110 centimeters.

You have been contacted by Zing Zhu to calculate, given the height the tide will reach and the position and height of all fence strips, the total area of land which will not be flooded during the high tide. You may assume that the widths of fence strips are so thin compared to the size of the land that, for the purpose of calculating the total area, fence strips may be considered as having widths equal to zero.

Input
-----

The input contains several test cases. The first line of a test case contains an integer **N** indicating the number of fence strips in the island (1 â¤ **N** â¤ 2000). Each of the next **N** lines contains five integers **X**1, **Y**1, **X**2, **Y**2 and **H**, representing respectively the start point of the strip (**X**1,**Y**1), the end point of the strip (**X**2,**Y**2) and the strip height (**H**). The last line of a test case contains an integer **W** representing the tide height. Coordinates are given in meters, heights in centimeters. Furthermore, **X**1 = **X**2 or **Y**1 = **Y**2 (but not both); â500 â¤ **X**1,**Y**1,**X**2,**Y**2 â¤ 500; and 1 â¤ **W**, **H** â¤ 1000. The end of input is indicated by **N** = 0.

Output
------

For each test case in the input your program must produce one line of output, containing one integer representing the total area (in m2) of the land which will not be flooded.


| Sample Input | Sample Output |
| --- | --- |
| 4 -20 20 20 20 200 20 20 20 -20 200 0 0 0 20 100 -10 0 20 0 200 100 4 -20 20 20 20 200 20 20 20 -20 200 0 0 0 20 100 -10 0 20 0 200 101 0 | 400 0 |

ACM/ICPC South America Contest 2004.


# Problem 1484

Descrição
----------

Strike Boy, as the name suggests, is a boy fanatic for all types of computer games. He is going on vacation in a paradise island where computers are not allowed. He had a great time playing with games on his cell phone, but now the battery is dead and since there is no electricity on the island, he stopped playing. Strike Boy then decided to invent a new hobby, using the keypad of his cell phone. In this new game, for two players, one chooses two integers *S* and *D*. The opposing player must then find a sequence of terms such that:

* Each term of the sequence is a number with  *D*  decimal digits, except for the last term, which can have between 1 and *D* digits;
* The sum of all terms of the sequence is equal to  *S* ;
* The digits used to form a term correspond to the keys of a standard cell phone keyboard ('0 'to '9');
* Each digit is used at most once in the sequence;
* The first term of a sequence can begin with any digit, but the order of the digits of the sequence when read from left to right, is such that the next key always corresponds to a key that is immediately adjacent to the previously used key (vertically, horizontally or diagonally).

For example, if  *S*  = 230 and  *D*  = 3, there are only two possible solutions obeying the rules of the game : [074, 156] and [085, 142, 3]. The sequence [230] is not a solution because the '3 'key is not a neighbor of the key '0 '.

![](https://resources.beecrowd.com/gallery/images/novos/Tecle%20%26%20Some.png)

Left picture: Keyboard illustrating the keys used to form the sequence [074, 156]

Right picture: Keyboard illustrating the keys used to form the sequence [085, 142, 3]

Help Strike Boy to check if his oponnent's answers are correct: write a program that, given  *S*  and  *D* , print all possible solutions .

Input
-----

The input contains several test cases. Each test consist in just one line, containing two integers **S** and **D**, separated by an empty space, representing the desired sum and the number of digits of each term (0 â¤ **S** â¤ 10.000.000.000 and 1 â¤ **D** â¤ 10). The end of the input is specified by **S** = **D** = â1.

Output
------

For each test case, your program must write one answer. The first line of an answer must contain an identifier of the test case, in the format '#i', where 'i' is initially 1 and is incremented for each test case. Then, if a solution for the problem exists, your program must display the list of the possible sequences of terms. If more than one sequence is possible, they must appear in ascending lexicographic order. Each sequence of terms must be printed in one line, with its terms separated by an empty space. If there is no solution, your program must print one line containing the word 'impossible'.

*Definition:* consider the sequences *Sa* = a1a2... a*m* and *Sb* = b1b2 ... b*n*. *Sa* preceeds *Sb* lexicographically if and only if Sb is non-empty and one of the following conditions is true:

* Sa is an empty sequence;
* a1 < b1;
* a1 = b1 and the sequence a2a3 ... am preceeds sequence b2b3 ... bn.

| Sample Input | Sample Output |
| --- | --- |
| 7 1 10 2 230 3 6311 4 2 2 -1 -1 | #1 0 7 1 2 4 1 4 2 2 1 4 2 4 1 2 5 4 1 2 4 2 1 5 2 7 7 0 #2 impossible #3 074 156 085 142 3 #4 0896 5412 3 0986 5321 4 0986 5324 1 0987 5324 #5 2 |

ACM/ICPC South America/Brazil Regional Contest 2005.


# Problem 1488

Descrição
----------

*"Os nÃºmeros sempre desempenharam um papel de acentuado relevo nÃ£o sÃ³ nos altos campos da FÃ© e da Verdade, como no humÃ­limos terreiros da SuperstiÃ§Ã£o e do Erro."* (Prof. MarÃ£o)

Malba Tahan, in his classic "The Man Who Counted", tells a tale of superstition involving the quadripartite numbers. Little did he know that centuries before the ancient Czech civilization superstition surrounding the quadripartite numbers was already present. In the antiquity, an important community living around Neratovice, used the properties of the quadripartite numbers to predict the future, baptize children and even to choose their leaders.

An integer *n* is quadripartite if there is some division of that number in four parcels integer (p1 + p2 + p3 + p4 = *n*) and an magical operator (*m*) so that the first portion added to the magical operator, the second reduced by it, the third multiplied by it and the fourth divided by it gives the same result (p1 + *m* = p2 â *m* = p3 \* *m* = p4 / *m*).

Thus, 128 is quadripartite because we can divide 128 into four parts (31, 33, 32 and 32) so that exists a magical operator (in this case, 1) that makes p1 + *m*, p2 â *m*, p3 \* *m* e p4 / *m* equal. In fact: 31 + 1 = 33 - 1 = 32 \* 1 = 32 / 1 = 32.

A group of researchers from Prague is reconstructing the past of Neratovice, and asked for your help. They want you to make a program that identifies when a number is quadripartite or not and what is the magic operator associated do it.

Input
-----

Each line of the input contains an integer **n** (0 â¤ **n** â¤ 500000) that your program should analyze and classify as quadripartite or not. The value **n** = 0 corresponds to the end of the input file and should not be processed.

Output
------

For each value of the input, your program should print an identifier **Instancia h**, where h is an integer, and increasing sequentially from 1. On the next line, separated by a blank space, the five numbers that prove the quadripartite condition when **n** is quadripartite. Follow the order: **m p1 p2 p3 p4**.

If **n** is not quadripartite, your program should print the message **n nao e quadripartido**. In the first case, it is possible that there is more than one sequence that meets the conditions. If this occurs, your program should choose the one with the highest possible value for **m**.

A blank line should separate the output of each instance.


| Sample Input | Sample Output |
| --- | --- |
| 128 1 8 0 | Instancia 1 7 7 21 2 98  Instancia 2 1 nao e quadripartido  Instancia 3 1 1 3 2 2 |

VII Maratona de ProgramaÃ§Ã£o IME-USP 2003.


# Problem 1492

Descrição
----------

Carl is right now the happiest child in the world: he has just learned this morning what the binary system is. He learned, for instance, that the binary representation of a positive integer k is a string ananâ1 Â· Â· Â· a1a0 where each ai is a binary digit 0 or 1, starting with an = 1, and such that k= Î£ni=0 ai Ã 2i. It is really nice to see him turning decimal numbers into binary numbers, and then adding and even multiplying them.

Caesar is Carlâs older brother, and he just canât stand to see his little brother so happy. So he has prepared a challenge: âLook Carl, I have an easy question for you: I will give you two integers A and B, and you have to tell me how many 1âs there are in the binary representation of all the integers from A to B, inclusive. Get readyâ. Carl agreed to the challenge.

After a few minutes, he came back with a list of the binary representation of all the integers from 1 to 100. âCaesar, Iâm readyâ. Caesar smiled and said: âWell, let me see, I chooseA = 1015 and B = 1016. Your list will not be usefulâ

Carl hates loosing to his brother so he needs a better solution fast. Can you help him?

Input
-----

The input consists of many test cases and ends with EOF. Each test case consist in a single line that contains two integers **A** and **B** (1 â¤ **A** â¤ **B** â¤ 1016).

Output
------

For each test case, print a line with an integer representing the total number of digits 1 in the binary representation of all the integers from **A** to **B**, inclusive.


| Sample Input | Sample Output |
| --- | --- |
| 1000000000000000 10000000000000000 2 12 9007199254740992 9007199254740992 | 239502115812196372 21 1 |

ACM/ICPC South America Contest 2013.


# Problem 1501

Descrição
----------

Given a decimal integer number you will have to find out how many trailing zeros will be there in its factorial in a given number system and also you will have to find how many digits will its factorial have in a given number system? You can assume that for a b based number system there are b different symbols to denote values ranging from 0 ... b-1.

Input
-----

There will be several lines of input. Each line makes a block. Each line will contain a decimal number **N** (a 20 bit unsigned number) and a decimal number **B** (1 < **B** â¤ 800), which is the base of the number system you have to consider. As for example 5! = 120 (in decimal) but it is 78 in hexadecimal number system. So in Hexadecimal 5! has no trailing zeros.

Output
------

For each line of input output in a single line how many trailing zeros will the factorial of that number have in the given number system and also how many digits will the factorial of that number have in that given number system. Separate these two numbers with a single space. You can be sure that the number of trailing zeros or the number of digits will not be greater than 231-1.


| Sample Input | Sample Output |
| --- | --- |
| 2 10 5 16 5 10 | 0 1 0 2 1 3 |


# Problem 1505

Descrição
----------

Here in Curoland are N factories that are identified by the numbers from 0 to n-1. The ith factory pays Ci coins each day to the people working there.  Initially, there are one worker in every factory. The workers want to save some coins for their vacations, the worker that initially was in the ith factory wants to save Ai coins.

Little Curo, the mayor of Curoland, wants some job rotation in factories so they don't become bored of their jobs. That's why every day, after the factories pays they workers for their job, the workers in the ith Factory have to move to the Gi Factory.

Little Curo wants to know the minimum number of days he have to wait until every worker have saved enough for their vacations. Because that day he will give a big party for them.

Input
-----

The input is composed of 4 lines. In line 1 there is a number **N**. The lines 2 to 4 have **N** numbers. The i-th number of the line 2 is **Gi** (0 < **Gi** < **N**), the i-th number of the line 3 is **Ci** (0 < **Ci** <= 10) and the i-th number of the line 4 is **Ai** (0 < **Ai** < 107)

Output
------

The program has to print the minimum number of days little Curo has to wait until every worker have saved enough.


| Sample Input | Sample Output |
| --- | --- |
| 3 2 0 1 2 5 7 15 15 15 | 4 |

Contest Maratona VerÃ£o 2014


# Problem 1512

Descrição
----------

Rafael decided to change the tiles from his living room, and for that he made some measurements and bought **N** white tiles from the store.

The fact that all the tiles are white got Rafael's attention about the design of his living room, and then he decided to paint some of the tiles to give a âmodern airâ to his house.

He positioned all the **N** tiles in a straight line, and enumerated all of them from 1 to **N**, from the left to the right.

To choose which tiles to paint, he thought about the following: Chose two integers **A** and **B**, and said he was going to paint all the tiles which enumeration was multiple of **A** and/or **B**.

Help Rafael to find out how many tiles are going to be painted at the total.

Input
-----

There will be several test cases. Each test case has three integers, **N**, **A** and **B** (3 â¤ **N** â¤ 10â¹, 2 â¤ **A**, **B** â¤ **N**).

The last test case is indicated when **N** = **A** = **B** = 0, which should not be processed.

Output
------

For each test case, print one line containing one integer, representing how many tiles are going to painted.


| Sample Input | Sample Output |
| --- | --- |
| 10 2 3 50 5 7 1000000 28 32 0 0 0 | 7 16 62500 |

Contest Bonilha 2014


# Problem 1526

Descrição
----------

One of the criteria for a programming marathon be considered as a success is that the contestants must not go hungry. Concerned about this, the organization chose one boy dedicated to the task of fetching snacks at supplier. To facilitate the transport of snacks this boy received a wheelbarrow.

Even with the wheelbarrow, this is a very tiresome task, so the organization allowed the boy to eat one of the snacks he carries every 100 meters traveled ( coming or going ) . In addition, each 100 meters, cabanas where he can temporarily store the snacks are prepared. Thus isn't necessary to transport all snacks directly from the supplier to the competition venue.

To know if the boy will ate more snacks than he can, the organization wants you to write a program that determines the maximum amount of snacks that can be delivered . You can assume that the boy eats a snack whenever allowed .

Input
-----

The input consists of several test cases and ends with end of file (EOF). Each test case consists of a line with three integers, **L**, **D**, and **C** **(10 â¤ L, D, C â¤ 100,000,000)** indicating, respectively, the amount of snacks bought, the distance between the supplier and the competition venue in hectometers and how many snacks fit in the wheelbarrow.

Output
------

For each test case, print the maximum amount of snacks that can be delivered, if this quantity is positive, or "impossivel" otherwise.


| Sample Input | Sample Output |
| --- | --- |
| 32 10 20 100 100 20 | 14 impossivel |


# Problem 1531

Descrição
----------

The famous Fibonacci sequence can be defined as follows:

* Fib( 1 ) = Fib( 2 ) = 1
* Fib( N ) = Fib( N-1 ) + Fib( N-2 ), for N > 2

Your task is simple, calculate the value of the remainder of Fib ( Fib ( N ) ) divided by M.

Input
-----

The input consists of several test cases and ends with EOF. Each test case consists of a line with two integers **N**and **M** (1 â¤ **N** â¤ 109, 2 â¤ **M** â¤ 106).

Output
------

For each test case, print a line containing an integer equal to the remainder of Fib ( Fib ( **N** ) ) divided by **M**.


| Sample Input | Sample Output |
| --- | --- |
| 1 100 2 100 3 100 4 100 5 100 5 2 6 100 | 1 1 1 2 5 1 21 |


# Problem 1537

Descrição
----------

Andre, Bruno and Carlos are friends for a long time, and if there is something that they know about each other is how punctual they are. Andre is known to be always the last one to arrive to a meeting between the three of them, and Carlos is always the first. Bruno always arrives before Andre, but never before Carlos.

It's the end of the month and the three friends need to go to the bank to pay some bills. Including them, there are **N** people at the line to use the bank teller. Knowing how they are punctual between them, in how many ways the bank line can be ordered?

Remember that the rules only apply between the three of them, for example, Carlos always arrives before Bruno and Andre, but may arrive later than other people at the line. Two orderings are considered different if there is at least one person who is in a different position in each ordering.

Input
-----

There will be several test cases. Each test case starts with one integer **N** (3 â¤ **N** â¤ 10âµ), indicating the number of people in the file, including Andre, Bruno and Carlos.

The last test case is indicated when **N** = 0.

Output
------

For each test case print one line, containing one integer, representing the number of ways the bank line can be ordered. As the result can be very high, print the result with rest of division in 1000000009.


| Sample Input | Sample Output |
| --- | --- |
| 3 4 5 10 0 | 1 4 20 604800 |

Contest Algar Telecom XIII


# Problem 1544

Descrição
----------

In this problem it will be given to you two decimal integer numbers **N**, **M**. You will have to find the last non-zero digit of the **NPM**. This means no of permutations of **N** things taking**M** at a time.

Input
-----

The input file contains several lines of input. Each line of the input file contains two integers **N** (0 â¤ **N** â¤ 20000000), **M** (0 â¤ **N**). Input is terminated by end-of-file.

Output
------

For each line of the input file you should output a single digit, which is the last non-zero digit of **NPM**. For example, if **NPM** is 720 then the last non-zero digit is 2. So in this case your output should be 2.


| Sample Input | Sample Output |
| --- | --- |
| 10 10 10 5 25 6 | 8 4 2 |


# Problem 1554

Descrição
----------

There are a lot of cue sports. The UFFS (Union of Fascinated Fans of Sports) has developed a new variant of Straight pool, called *N.1*.

In this variant the shooter may try to hit the white ball at its closest ball at the pool table, among *N* possible ones. The match is won by the player that gets more hits after 50 attempts.

The game difficulty is at finding out which of the *N* balls is the closest one to the white. Your task is to write a program that helps the match judges.

Input
-----

There are several test cases. The first line of input contains an integer **C** that determines the number of test cases. For each test case, the input begins with an integer **N** (1 â¤ **N** â¤ 50), which defines the number of available balls, besides the white one. The next **N** + 1 lines contain two integers, **x** and **y**, separated by a blank space, indicating the (**x**, **y**) ball position on the pool table, one ball for each line (0 < **x** < 1420 mm e 0 < **y** < 2840 mm). The first line indicates the position of the white ball. The rstrongaining ones indicate the position of the balls 1, 2, 3,. . . , **N**-1, **N** in that order.

Output
------

For each test case print a line containing only the number of the ball that is closest to the white one. The error allowed is 0.01 mm. If more than one ball satisfy the minimum distance, you must show the smallest number among the tied ones. Always end a line with the new line character (\n).


| Sample Input | Sample Output |
| --- | --- |
| 3 1 30 60 900 1800 2 710 30 710 2100 710 1000 3 710 30 710 2100 510 1000 910 1000 | 1 2 2 |

Aquecimento para a OBI 2014


# Problem 1555

Descrição
----------

In the last math class, Rafael, Beto and Carlos learned some new math functions. Each one of them liked one particular function, and they decided to compete to see which function had the higher outcome.

The function that Rafael chose is r(**x**, **y**) = (3**x**)Â² + **y**Â².

Beto chose the function b(**x**, **y**) = 2(**x**Â²) + (5**y**)Â².

Carlos, however, chose the function c(**x**, **y**) = -100**x** + **y**Â³.

Given the values of **x** and **y**, say who chose the function with higher outcome.

Input
-----

The first line of input contains an integer **N** that determines the number of test cases. Each test case consists of two integers **x** and **y** (1 â¤ **x**, **y** â¤ 100), indicating the variables to input in the function.

Output
------

For each test case print one line, containing one sentence, indicating who won the contest. For example, if Rafael wins the contest, print âRafael ganhouâ. Assume that there will be no ties.


| Sample Input | Sample Output |
| --- | --- |
| 6  5 3 2 30 2 100 30 20 15 5 30 2 | Beto ganhou Carlos ganhou Carlos ganhou Beto ganhou Rafael ganhou Rafael ganhou |

Aquecimento para a OBI 2014


# Problem 1563

Descrição
----------

Choosing randomly two integers A and B between 1 and N inclusive, what is the chance that the number B is less than or equal to the remainder of N divided by A?

For example, for N = 5, there are 25 possible choices for (A, B), but the only pairs that satisfy the condition are (2,1), (3,1), (3,2) and (4,1). Therefore, for N = 5 the probability is 4/25.

Input
-----

The input consists of several test cases. Each test case consists of a line containing an integer **N** (1 â¤ **N** â¤ 108).

Output
------

For each test, the output consists of a line containing the irreducible fraction that answers the given question.


| Sample Input | Sample Output |
| --- | --- |
| 1  2  3  4  5  6  7  8 | 0/1  0/1  1/9  1/16  4/25  1/12  8/49  1/8 |

Contest Dalalio 2014


# Problem 1567

Descrição
----------

You can see a (4x4) grid below. Can you tell me how many squares and rectangles are hidden there? You can assume that squares are not rectangles. Perhaps one can count it by hand but can you count it for a (100x100) grid or a (10000x10000) grid. Can you do it for higher dimensions? That is can you count how many cubes or boxes of different size are there in a (10x10x10) sized cube or how many hyper-cubes or hyper-boxes of different size are there in a four-dimensional (5x5x5x5) sized hypercube. Remember that your program needs to be very efficient. You can assume that squares are not rectangles, cubes are not boxes and hyper-cubes are not hyper-boxes.

![](https://resources.beecrowd.com/gallery/images/promocao/cubos.png)

Input
-----

The input contains one integer **N** (0 â¤ **N** â¤ 100) in each line, which is the length of one side of the grid or cube or hypercube. As for the example above the value of **N** is 4. There may be as many as 100 lines of input.

Output
------

For each line of input, output six integers **S2, R2, S3, R3, S4, R4** in a single line where **S2** means the number of squares inside the **(NxN)** two-dimensional grid, **R2** means the number of rectangles inside the **(NxN)** two-dimensional grid. **S3, R3, S4, R4** have the same meaning but in higher dimensions as described before.


| Sample Input | Sample Output |
| --- | --- |
| 1 2 3 | 1 0 1 0 1 0 5 4 9 18 17 64 14 22 36 180 98 1198 |

âA bus was running at full speed and suddenly the driver stopped it. As a result a passenger fell down from his seat and began scolding Newton as Newton invented inertia of motion.â


# Problem 1568

Descrição
----------

All the positive numbers can be expressed as a sum of one, two or more consecutive positive integers. For example 9 can be expressed in three such ways, 2+3+4, 4+5 or 9. Given an integer less than (9\*1014+1) or (9E14 + 1) or (9\*1014 +1) you will have to determine in how many ways that number can be expressed as summation of consecutive numbers.

Input
-----

The input file contains less than 1100 lines of input. Each line contains a single integer **N** (0 â¤ **N** â¤ 9E14). Input is terminated by end of file.

Output
------

For each line of input produce one line of output. This line contains an integer which tells in how many ways **N** can be expressed as summation of consecutive integers.


| Sample Input | Sample Output |
| --- | --- |
| 9  11  12 | 3  2  2 |

Math Loversâ Contest


# Problem 1570

Descrição
----------

X and Y are two integer numbers and X>=Y. The values of X and Y fits in 16-bit signed integer. When the summation of these two numbers is multiplied with Y we get P and when the absolute value of the subtraction of these two numbers is multiplied with X we get Q. Given the value of P and Q you must find the value of X and Y.

Input
-----

The first line of the input file contains an integer **N** (**N**<=75000) that denotes how many lines of inputs are there. Each of the next **N** lines contains two integers which denotes the values **P** and **Q** respectively, here |**P**| <2 31, |**Q**| < 231.

Output
------

For each line of input except the first one produce exactly two lines of output. The first line contains the serial of output and the next one contains possible values of **X** and **Y** (One pair of values in each line). If there is more than one solution print the pair with smaller **X** value. When the given values of **P** and **Q** is impossible for any integer value of **X** and **Y** print the line âImpossible.â instead.


| Sample Input | Sample Output |
| --- | --- |
| 3  160 48  200 100  300 200 | Case 1:  12 8  Case 2:  Impossible.  Case 3:  20 10 |


# Problem 1572

Descrição
----------

In this particular problem, The Unreal Tournament is a tournament, which consists of only two teams. Let these two teams be Abahoni and Mohamedan. They play in between them not more than 2N - 1 games, the winner being the first team to achieve n victories. You can assume that there are no tied games, the result of each game is independent and for any match there is a constant probability P that team Abahoni will win and hence there is a constant probability Q(Q = 1 - P) that team Mohamedan will win.

P(i, j) is the probability that team Abahoni will win the series given that they still need i more victories to achieve this, whereas team Mohamedan still need j more victories if they are to win. The P(i, j) can be computed with a function like the following:

**Function P(i, j){  

   if i = 0 then return 1  

   else if j = 0 then return 0  

   else return pP(i-1,j) + qP(i,j-1)  

}**

You will have to write a program that gives the probability of winning for any P, i and j and also gives the number of recursive calls required if the function above is used to get the probability P(i,,j).

Input
-----

The input file contains several sets of input. The first line of a set contains one floating-point number **P**(0 < **P** < 1), and an integer **N**(0 â¤ **N** < 1001) where **P** is the winning probability of Abahoni and **N** is the number queries to follow. Each of the next **N** lines contains two integers **i**(0 â¤ **i** â¤ 1000) and **j**(0 â¤ **j** â¤ 1000). Input is terminated by a set, which has zero as the value of **N**. This set should not be processed.

Output
------

For each query you should print two lines. The first line contains the value of **P**(i, j) with five digits after the decimal and the second line contains a round number which is the number of recursive calls needed if the function mentioned above was used to determine the value of **P**(i, j). If the value of **P**(i, j) is undefined you should print -1 as its value with similar formatting. A blank line should be printed between the outputs of two consecutive sets.


| Sample Input | Sample Output |
| --- | --- |
| 0.5 3 1 1 2 2 3 3 0.5 2 10 3 10 2 0.7 0 | 0.50000 2 0.50000 10 0.50000 38  0.01929 570 0.00586 130 |


