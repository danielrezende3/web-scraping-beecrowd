# Problem 2100

Descrição
----------

Harbin has one of the biggest movie theaters in the world. The "Xing Tzen Zu" movie theater is very wide, with few rows and many chairs. The chinese goverment has specific rules for people to go to the movies: each couple must sit on the same row (the first row is occupied by farmers, drivers, mechanics, the second by teachers, salesmen, firemen, and so on). But, at the same time, it is forbidden for people to sit on the same position in two nights. That worried the mayor, who then tried to find how many nights the movie theater could open without the need to repeat a layout that had occurred before. An important restriction is that couples must always occupy neighboring seats on the row.

Your task on this problem is to determine, given the number of seats **N** and the number of couples **M**, how many different ways the couples can seat on the chairs in a way they are not separated.

Input
-----

The input is composed by several instances. The first line of the input has an integer number **T** indicating the number of instances. Each instance is composed by a line that has two integer numbers **N** (2 â¤ **N** â¤ 4000) and **M** (1 â¤ **M** â¤ **N**/2).

Output
------

For each instance print a line that has the number of different ways the couples could sit on the chairs in a way they are not separated.

The answer must be in MOD1300031.


| Sample Input | Sample Output |
| --- | --- |
| 2  10 2  20 6 | 224  574954 |

XIII Maratona de ProgramaÃ§Ã£o IME-USP, 2009


# Problem 2101

Descrição
----------

We are in 2433 and the Pythanic spaceship has just been launched with the first group of humans to inhabit another planet. This journey has been long awaited since the life conditions on Earth became extremelly difficult after a failed attempt of a terrorist to exterminate the human race using mutant bacteria, about 400 years ago. Once the bacteria were very poorly made, with a lot of last minute kludges, the only thing he achieved was a terrible stench in the environment.

Before the beginning of the journey, some decisions had to be taken with respect to the way of life that these people would take on the other planet. One of those decisions was that the duration of a day would be the same in all planets inhabited by humans, that is, the word "day" becomes simply a term that means "24 hours" and no more a term that specifies a complete rotation of the planet around itself. However, it was decided that the duration of the month may vary from planet to planet. Worried about the confusion it could generate, the analists from the interplanetary colonization comittee asked you to create a program that, given the duration of the months (in days) in two different planets, say how much different combinations of pairs (D1, D2) exist, where D1 is a day on planet 1 and D2 is a day on planet 2 (not necessarilly days of the same month). You may assume that the first day 1/1 (the first day of the year) occurs at the same time on both planets.

For example, if a planet has 2 days in a month and the other has 3, we'll have 6 different day combinations: (1,1), (2,2), (1,3), (2,1), (1,2) and (2,3). If a planet has 4 days in a month and the other has 2, there will be only 4 combinations: (1,1), (2,2), (3,1) and (4,2).

Given D1 and D2, your program must determine how many combinations exist.

Input
-----

The input contains various instances.

Each instance is composed by only one line containing two integers **D1** and **D2** (1 â¤ **D1**, **D2** â¤ 1.000.000.000), that correspond to the number of days in a month on the two different planets. The input finishes then **D1** = **D2** = 0.

Output
------

For each instance of the input, print a line containing the number of different day combinations between the two planets.

The answer must be given in modulo 1713371337.


| Sample Input | Sample Output |
| --- | --- |
| 4 2 10 25 0 0 | 4 50 |

XIII Maratona de ProgramaÃ§Ã£o IME-USP, 2009


# Problem 2107

Descrição
----------

The pyramids are very frequent structures on ancient civilizations all over the world. The most famous, the Egypt ones, were built more than 2000 years before Crist's passage on Earth. Other famous pyramids are the ones from Mexico and Central America, linked to the Mayan and Aztec civilizations.

Little known, however, are the pyramids built on the Ural mountains, near the city of Ekaterinburg. These pyramids date back to the early Christian era, and is believed to have been built by Mongolian peoples, who invaded the Europe through the Ural mountains, coming from Asia. Unlike the other known pyramids, these had triangular base. Thus, these pyramids had 4 triangular faces. Many of these pyramids were built on columns, allowing non-parallel to ground constructions and even exposing the pyramid's base.

That was very important, because the faces of the pyramid were painted with figures representing ancient gods, mythological figures, planets and other celestial bodies and so on. Thus, at some point in the city, a citizen could see one or more faces of the pyramid. This was important to the local religion, and find a house whose window glimpsed the best faces of the pyramids was much appreciated at the time.

Your task is, given the positions on space of a pyramid's vertices, and the position on space of an observer, determine which faces of the pyramid are visible to him, considering that there is no obstacle between the observer and the pyramid.

Input
-----

The input is composed by various instances and ends with end of file (EOF).

Each instance consists of 5 lines. Each line contains three integers, separated by spaces, and represent the coordinates of the points **A**, **B**, **C**, **D** and **X**, respectivelly, where **X** is the position of the observer and the other points are the vertices of the pyramid.

All points provided have integer coordinates between -100 and 100.

The points **A**, **B**, **C** and **D** are not coplanar.

All points provided are distinct.

The point **X** neither belong to the interior of the pyramid nor to any face of it.

Output
------

For each instance, print a line containing 4 characters. The first character must be *S*if the observer sees the face of the pyramid that is oposite to vertex A, and *N* otherwise. Analogously for the second, third and fourth characters, but relative to the vertices **B**, **C** and **D** respectivelly.


| Sample Input | Sample Output |
| --- | --- |
| 0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 -1 -1 -1 0 0 0 1 0 0 0 1 0 0 0 1 1 1 0 | SNNN NSSS SNNN |

XVII Maratona de ProgramaÃ§Ã£o IME-USP, 2013


# Problem 2114

Descrição
----------

Poker is played with a traditional deck of 52 cards (13 values in 4 suits). The values on the cards, in ascending order, are: *2*, *3*,â¦, *10*, *Jack*, *Queen*, *King*, *Ace*. Given a round of a poker game with two players, your job is to determine the winner.

Each player has two card of their own and there are five cards common to both players on the table. The player with the best hand of five cards among his own two and the five on the table wins. A card from the table can be used by both players at the same time and the player hand can be obtained by ignoring the two cards of their own and using the five cards common to both of them.

In order to compare two hands, you have to check which hands they match on the list below. If a hand matches more than one type, you must choose the most valuable one. If two hands match a same type, you apply the tiebreaker rule specific to this type.

The list of hands, sorted from the least valuable to the most valuable, and their respective tiebreaker criteria is:

* *High card*: any hand that does not matches any other hand. The tiebreaker rule is to compare the five cards one by one, from the most valuable to the least, until a hand presents a card with more value than the other.
* *One pair*: two cards of the same type. The tiebreaker rule is similar to the high cardâs rule, only that you compare first the pair and then the other cards.
* *Two pairs*: two pairs. The tiebreaker rule is similar to the high cardâs rule. You first compare the most valuable pair, then the least valuable pair and then the remaining card.
* *Three of a kind*: three cards of the same value. The tiebreaker rule is similar to the one pairâs rule.
* *Straight*: five cards sequence of consecutive values. In this case, the Ace can take the value of both the least valuable card (before the 2) or of the most valuable (after the king). The tiebreaker rule is done by the most valuable card on the straight. Note that the Ace is the least valuable card if it appears before the 2.
* *Flush*: five cards of the same suit. The tiebreaker rule is the same of the high cardâs rule.
* *Full House*: a three of a kind and a pair. The tiebreaker rule is done by comparing first the values of the three of a kind. If the tie remains, the pair values must be compared.
* *Four of a kind*: four cards with the same value. The tiebreaker rule is comparing the values of the four of a kind and then the remaining card.
* *Straight Flush*: Straight and Flush simultaneously. The tiebreaker rule is the same of the straightâs rule.

Note that it is possible for a tie to remains even after the tiebreaker rules are applied. The cards suits are only to be considered to define a flush, and are not be taken in account in any tiebreaker rule.

Input
-----

The input has several instances and ends with an end of file (EOF).

Each instance is composed of three lines. The two first lines contain the description of two cards each one, separated by a blank space. The first line corresponds to the cards of the first player while the second line corresponds to the cards of the second player. The third line contains the description of the five cards on the table, also separated by blank space.

| Character | Card |
| --- | --- |
| '2'- '9' | 2 - 9 |
| 'T' | 10 |
| 'J' | Jack |
| 'Q' | Queen |
| 'K' | King |
| 'A' | Ace |
| 'e' | Spades |
| 'c' | Hearts |
| 'o' | Diamonds |
| 'p' | Clubs |

The description of a card is given by two characters, the first indicating the value of the card and the second its suit, according to the input sample.

Output
------

For each instance, print a line containing a single integer. Print 1 if the first player wins the instance, print 2 if the second player wins or print 0 if there is a tie, even after the tiebreaker rules are applied.


| Sample Input | Sample Output |
| --- | --- |
| Te Je  Tp Jp  Qe Qp Ke Kp Ae  Ae 7o  Ac 8e  Ap Ao 9e Jc Kp  Ae 7o  Ac 8e  Ap Ao 6e 3c Kp | 1  0  2 |

XVII Maratona de ProgramaÃ§Ã£o IME-USP, 2013


# Problem 2129

Descrição
----------

John is a very smart sixth grade boy. He likes Maths a lot, and he found out that his teacher is very lazy. At the tests, the teacher asks the kids to circle their answers with a coloured square, and also asks them to make the number's first non-zero digit (right-to-left) specially big, using a pen. John suspected that the teacher used only that digit to grade the question.

The class learned to calculate the factorial of a number, and that is going to be the subject for the next test. John is convinced that he doesn't need to actually write the right number, as long as the first digit (right-to-left) is right. Your task in this problem is to help John calculate, for an integer number n from the input, the first digit (right-to-left) in n! that is different to zero.

Input
-----

The input consists in many instances. The first line for each instance consists in an integer **n** (1 â¤ **n** â¤ 1000000).

The input ends with file end.

Output
------

For each instance, you'll have to print a **k** instance identifier, where **k** is the current instance number. At the next line, print the first digit (right-to-left) that is different to zero.

After each instance, print a blank line.


| Sample Input | Sample Output |
| --- | --- |
| 5 | Instancia 1 2 |

XI Maratona de ProgramaÃ§Ã£o IME-USP, 2007


# Problem 2133

Descrição
----------

Recent archaeological discoveries of researchers from the University of Alberta in Canada, showed that a strange sequence of numbers were found on the walls of pyramids in Egypt, in ruins of Macchu Picchu and on the rocks of Stonehenge. Intrigued by the apparent coincidence, the researchers contacted the Department of Mathematics to decipher what was special about that sequence or numbers.

The discovery was stunning. All numbers were generated by matrices of Dinostratus. Dinostratus was a famous greek mathematician who lived from 390 to 320 BC and had worked in important geometry problems like squaring the circle. Dinostratus studied matrices M of size 3 x 3 formed by nine distinct integers with the property that for every position (i, j), i = 1 ,..., 3, j = 1 ,..., 3 of matrix, the element Mi,j is a multiple of its neighbors Mi-1,j, Mi-1,j-1 and Mi,j-1 (if they exist). In his honor, we say that N is a Dinostratus number if exist a matrix M with the property above such that M3,3 = N.

See an example for N = 36.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2133.png)

The relationship between the Dinostratus numbers, the pyramids of Egypt, the stones of the Stonehenge and the ruins of Machu Picchu still remains a great mystery. Even though, researchers in Alberta are willing to study these magic numbers. Your task is to make a program that receives an integer N and checks whether this is a Dinostratus number.

Input
-----

The input consists of several instances. Each instance is given by a line containing an integer **N** (1 â¤ **N** â¤ 1048576). The input ends with end of file.

Output
------

For each instance, you must print an identifier *Instancia* **K** (which means: *Instance* **K**), where **K** is the number of the current instance. On the next line print *sim* (which means: *yes*) if **N** is a Dinostratus number otherwise print *nao* (which means: *no*).


| Sample Input | Sample Output |
| --- | --- |
| 36 37 38 | Instancia 1 sim  Instancia 2 nao  Instancia 3 nao |

XI Maratona de ProgramaÃ§Ã£o IME-USP, 2007


# Problem 2135

Descrição
----------

The teacher Cris became known as a machiavellian person in your institution. For those not aware of the situation, the teacher required students to form a queue in lexicographical order (by name) with at most k permutations. This meant that many students do not even enter the room to take the test. However, this selective she resolved to redeem himself against students, and decided to apply a little trouble retrieval.

Your task, even if not disapproved, is given a sequence of n integers a1, a2, ..., an. Where -30 â¤ aj â¤ 30 for j = 1, ..., n, print, if there is an integer ak such that ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2135.jpg) . If more than an integer that satisfies this condition, print the first in the sequence.

Note from teacher: "Boys, remember that the sum of any nonzero number is not zero! Okay?"

Input
-----

The entrance is composed of several instances. The first line of each instance consists of an integer; **n;**(1 â¤ **n** â¤100) indicating the number of integers in the following line should to be processed. The entry ends with end of file.

Output
------

For each instance, you must print an identifier "Instancia **k"**, where **k** is the number of the current instance starting with 1. On the next line print the integer that satisfies the restriction described above. If no such integer exists print "nao achei".

After each instance print a blank line.


| Sample Input | Sample Output |
| --- | --- |
| 1  0  7  1 2 3 4 5 6 7  3  5 20 35 | Instancia 1  0  Instancia 2  3  Instancia 3  nao achei |

XI Maratona de ProgramaÃ§Ã£o IME-USP, 2007


# Problem 2145

Descrição
----------

A natural number loves another number if the sum of its divisors is a divisor of the other number. For example, 9 loves 12, because the sum of the divisors of 9 is 4, which is a divisor of 12. However, 12 doesn't love 9, because 16 (sum of the divisors of 12) is not a divisor of 9. In this case, 9 loves 12 and is unrequited, which makes it a 'friendzoned' number.

Nevertheless, there are cases in which the love is requited: when the sum of the divisors of a number is equal to or a divisor of the other number and vice versa. On the other hand, an almost requited love occurs when the sum of the divisors of a number is equal to the sum of the divisors of the other number.  


Input
-----

The input contains several test cases. Each test case consists of two integers **N** and **M** (2 â¤ **N**, **M** â¤ 109), being **N** and **M** different numbers. Read input until N = M = 0.

Output
------

Print the connection between the given numbers, according to the conditions below:

1 - If the love is requited, print "Friends and lovers <3";  

2 - If the love is almost requited, print "Almost lovers!";  

3 - If the love is unrequited, print "X friendzoned Y!", in which the sum of the divisors of X is different from the sum of the divisors of Y and X is a multiple of the sum of the divisors of Y (Y loves X) but Y is not a multiple of the sum of the divisors of X (X doesn't love Y);  

4 - If there's no connection, that is, the sum of the divisors of X is different from the sum of the divisors of Y and X is not a multiple of the sum of the divisors of Y and Y is not a multiple of the sum of the divisors of X, print "No connection.".

Note: In this problem, the sum of the divisors doesn't include the number itself, and in the cases in which the love is requited and also almost requited, prevails the requited love.


| Input Sample | Output Sample |
| --- | --- |
| 2 14  6 25  12 9  9 12  7 3  0 0 | 14 friendzoned 2!  Almost lovers!  12 friendzoned 9!  12 friendzoned 9!  Friends and lovers <3 |

Warm-up contest for IFSULDEMINAS' VI OlimpÃ­ada Interna de ProgramaÃ§Ã£o - OLIP 2016


# Problem 2148

Descrição
----------

Every Sunday, a group of friends gathered in a park to talk. In addition, they played something called "dadinho", that in other regions is called "zezinho". Each player starts with one die and makes a guess. Then they throw the die, and if the guess is correct, they take a second die. Each round, the process repeats, and the player tries to guess the sum of the dice thrown. Whoever gets it right, would take another die. The game ends when a player makes a correct guess after having 13 dice. Consider that all dice used in the game are fair and have six faces, numbered from 1 to 6. As the amount of dice increases, it becomes more and more difficult to make a guess. Thus, they asked you to make a program which, given a guess, and an amount of dice, calculate the probability of getting the guess right.

![Dice](https://resources.beecrowd.com/gallery/images/problems/UOJ_2148.png)

Write a program that - given an integer, representing the guess, and another integer, the amount of dice to be played - calculates the probability that the guess is right.

Input
-----

The first value is an integer **C**, indicating the number of test cases. Each test case consists of two integers **S** and **D** ( 1 â¤ **S** â¤ 80, 1 â¤ **D** â¤ 13 ), indicating the guess and the amount of dice.

Output
------

For each test case, print a line containing a value, double precision, with 15 decimal digits, informing the probability that the guess is right when that amount of dice is thrown.


| Input Sample | Output Sample |
| --- | --- |
| 3  1 2  78 13  7 2 | 0.000000000000000  0.000000000076566  0.166666666666667 |

VI OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2016


# Problem 2149

Descrição
----------

Will Bonati live in the city of Belo Air, along with the family of his uncle, Phill Bonati . Will usually does some things that his uncle did not like, such as, for example, listen to music at high volume. One day, Phill poses a challenge to his nephew. He would spend the first numbers of a sequence he created. If Will could find the next number in this sequence, his uncle would have to put up with his music, with high volume, and still make a soup for them. If not discovered, Will would have to stop listening to such songs, leaving the quieter uncle. The first numbers of this sequence are below. Will asked for your help to write a program that can identify the next number in this sequence .

0       1       1       1       2       2       4       8       12

Write a program that, given an integer, tell what is the value corresponding to this position in the proposed sequence.

Input
-----

There will be several test cases. Each test case starts with an integer **N** ( 1 â¤ **N** â¤ 17), indicating the position requested in sequence. The entry ends with end of file.

Output
------

For each test case, print the amount corresponding to requested position in the sequence.


| Input Sample | Output Sample |
| --- | --- |
| 1  4  10 | 0  1  96 |

VI OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2016


# Problem 2154

Descrição
----------

The calculation of a derivative of a function in the form xn is defined by:

f(x) = xn    â     f(x)â = n.xn-1

Here's an example:

f(x) = 4x3 + 3x2    â     f(x)â = 12x2 + 6x

Write a program that, given a simple polynomial, calculate its derivative.

Input
-----

There will be several test cases. Each test case is formed by an integer **T**, which is the number of terms that has the polynomial. In the next line, there is the polynomial itself, formed by **T** ( 1 â¤ **T** â¤ 100) terms, each separated by a space, a sum signal and another space, and each containing an integer **C** ( 2 â¤ **C** â¤ 100), the letter ***x*** and an integer **E** ( 2 â¤ **E** â¤ 100 ), and the coefficient **C** and **E** the exponent of the term. The entry ends with end of file.

Output
------

For each test case, print the polynomial with the derivative applied.


| Input Sample | Output Sample |
| --- | --- |
| 2  7x3 + 3x2  3  3x4 + 4x3 + 2x2 | 21x2 + 6x  12x3 + 12x2 + 4x |

VI OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2016


# Problem 2170

Descrição
----------

  

In an investment project, whose initial capital value is **X**, yield after a period a **Y** value you want to know what this project interest rate. You want to know what the internal rate of return on investment, because that way you can check the percentage of interest.

Input
-----

There are several designs to be analyzed, and each project is given the initial capital contribution (1 < **X** < 1020), and its return (**X** < **Y** < 1020).

Output
------

For each project show the amount of interest for each application. Show as the sample output.


| Input Sample | Output Sample |
| --- | --- |
| 20000 35000 2500 5000 7535 160000 | Projeto 1: Percentual dos juros da aplicacao: 75.00 %  Projeto 2: Percentual dos juros da aplicacao: 100.00 %  Projeto 3: Percentual dos juros da aplicacao: 2023.42 % |


# Problem 2177

Descrição
----------

Maria loves sports and she is very excited about the Olympic Games Rio 2016. She was so excited that se bought a lot of tickets for the games, but unfortunately due to the distance between her house and the competition's arenas, that can be very large, she may not be able to watch all the games.

Maria knows you love programming challenges as much as she loves sports, so she asked you to make a program that given the position of the arenas of each game and how much time is left until the match begins, tells which games she will be able to watch if she leaves right now from her current position and go to the arena (she has to get there before the game starts).

Maria is at a certain position (x, y) and moves with velocity of 1 meter per minute (despite of the excitement Maria walks slowly so she can pass by the maximum number of pokestops), the distance of the locations, also in meters, is the Euclidian Distance between the positions, and the time left to the beginning of the game is also in minutes.

Input
-----

The first line of the input consists of Maria's position, **x** and **y** (0 â¤ **x**, **y** â¤ 1000), and the number **n** (1 â¤ **n** â¤ 10â¶) that represents the number of tickets Maria bought.

The next **n** lines consits of 3 number, **xi, yi, ti**, respectly the position **x** of game **i**, the position **y** of game **i**, and the time left to the beginning of the game **i**. (0 â¤ **xi**, **yi** â¤ 1000 e 1 â¤ **ti** â¤ 1000000).

Output
------

The output is just one line that contains the sorted indexes of the games Maria will be able to watch. If Maria will not be able to watch any game just print "-1" (without the quotation marks)


| Input Samples | Output Samples |
| --- | --- |
| 0 0 3  0 1 1  1 0 2  0 1 2 | 2 3 |

| 0 0 3  4 5 10  2 3 3  10 10 20 | 1 3 |

Aquecimento para a OBI 2016 - Fase 2


# Problem 2180

Descrição
----------

A group of scientists are making new experiences to create a starship that allows a trip to Mars, much faster than todays day. This starship will use two rockets with a new fuel, a lot more efficient than those used until today. But the speed that new rockets can provide to the starship is directly related to the weight of the stored fuel these rockets (in kg) and a curious relation of weight primes. For example, if the total weight of the rocket fuel is 1010 kg, the attained speed (in km/h) will be the sum of the tenth prime number starting from 1010 (including it): 1013 -> 1019 -> 1021 -> 1031 -> 1033 -> 1039 -> 1049 -> 1051 -> 1061 -> 1063, or 10380 km/h.

Scientists are very intrigued by this existing mathematical relationship and want that you build a program that calculate how much the starship would take to get from Earth to Mars with this new fuel given the weigh of rockets (of course, they are trying to create the biggest possible rockets) and assuming that the distance from earth to mars on the launch day will be 60 million kilometers.

Input
-----

The input contains a single integer **weight** (1000 < **weight** â¤ 60000) indicating the maximum weight of fuel (in kg) that can stored by the rockets.

Output
------

Your program must print two lines. The first line contains the velocity acchieved by the starship, followed by text "km/h". The second line contains the estimated time to travel to Mars in hours and days (truncated) with corresponding text messages, like shown below.â


| Input Samples | Output Samples |
| --- | --- |
| 1010 | 10380 km/h 5780 h / 240 d |

| 60000 | 600578 km/h 99 h / 4 d |

Aquecimento para a OBI 2016 - Fase 2


# Problem 2204

Descrição
----------

With the games coming, like in any other big event, the public security forces realize many trainings and simulations in order to be ready for anythings. Your friend David, who does'nt feel happy with his Computer Science course - result of his poor programming skills, dream to join one of the public security forces and, when he was studying about those simulations, he found the following problem:

*"In a given situation, the tatical defense team must find an alarm clock - which simulates a bomb - which will have a screen showing two numbers **A** and* **B***. To disarm the bomb, the team need to write the Gratest Common Divisor of all numbers from **A** to **B**."*

Nobody knows why someone would simulate a bomb which such requisit, but, David is curious to know which should be the correct numbers to stop the bomb. As you know, he's not good with those 'programming or math stuff' so, he asks your help to find out the answer to the following problem:

"Given two integers **A** and **B**, print the greates common divisor of all integers in the interval [**A**, **A**+1, **A**+2, ... **B**]"

Input
-----

The input start with an integer **T** that represents the number of test cases. Follows **T** lines, each one with two integers **A** and **B** ( 1 <= **A** <= **B** <= 10Â¹Â°Â°).

Output
------

For each test case your problem should print in a single line, the answer to the problem.


| Input Sample | Output Sample |
| --- | --- |
| 2  1 2 122 122 | 1 122 |


# Problem 2218

Descrição
----------

So so far away there is a pacific kingdom called LÃ¡-Ara. LÃ¡-Ara leader, the king Naldo, a great pokemon master, is in trouble. A rare mathematician pokemon called Evil-Son invades his territory and it threatened to destroy everything if nobody answer the challenge described as follow.

A set of lines in the pane is said to be in *general position*
if no two lines are parallel and no three lines intersect at a common point. Inside the rectangle of figure (A) we have a set of lines in general position, in other hand, inside the rectangle of figure (B) we have represented a set of lines that isn't in general position.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2218.png)

The challenge consists in compute the number of regions in the plane created by a set of **N** lines in general position. The king Naldo needs your mathematics and programming skills to save the LÃ¡-Ara kingdom of evil Evil-Son.

Input
-----

The input consists of many instances of the problem. The first line contains just an integer **T** that represents the number of instances.

Each instance consists of one line thats has the number **N**
representing the number of lines in the set.

Output
------

For each instance in the input, prints a line with the number of regions created in the plane by the lines in the set.


| Input Sample | Output Sample |
| --- | --- |
| 3 1 3 7 | 2 7 29 |

II Maratona de programaÃ§Ã£o do IFCE-Aracati


# Problem 2222

Descrição
----------

Dabriel is a fissured boy for mathematics, today he learned at his school some set operations.  

After spending the afternoon playing with some sets that he has, it's time to solve the homework, but he is already very tired and afraid to make some mistakes, asked for your help.

Dabriel wants a computer program that given **N** sets and the elements of each set, it can perform some operations, they are:

**1 X Y**: Returns the number of distinct elements in the intersection of the set **X** and **Y**.

**2 X Y**: RReturns the number of distinct elements in the union of the set **X** and **Y**.

Input
-----

The input consists of several test cases. Each test case starts with an integer **T**, indicating the number of instances. Each instance starts with an integer **N** (1 â¤ **N** â¤ 10â´), representing the number of sets that Dabriel has. The next **N** lines begin with a integer **Mi** (1 â¤ **Mi** â¤ 60), indicating the total number of elements that set **i** have, then follows **Mi** integers **Xij** (1 â¤ **Xij** â¤ 60), representing the value of each element. The next line has a integer **Q** (1 â¤ **Q** â¤ 10â¶), representing how many operations Dabriel want to perform. In the next **Q**  lines have the description of an operation. The input ends with **N** = 0 and should not be processed.

Output
------

For each operation, your program should print the number of elements, as explained in the description.


| Input Samples | Output Samples |
| --- | --- |
| 1 4 1 1 2 1 5 3 2 4 6 4 1 3 5 7 5 1 1 2 1 1 4 2 1 4 2 3 4 1 2 4 | 1 1 4 7 2 |

II Maratona de programaÃ§Ã£o do IFCE-Aracati


# Problem 2232

Descrição
----------

Pascal's Triangle (also known as Tartaglia Triangle in some countries), is an infinite numeric triangle formed by binomial numbers ![Binomial](https://resources.beecrowd.com/gallery/images/contests/UOJ_2232_b.png), where **n** represents the row number and **k** represents the column number (0-indexed). The triangle was discovered by the chinese mathematician Yang Hui, and 500 years later, many of its properties was studied by Blaise Pascal. Each number in Pascal's Triangle is equal to the sum of the number immediately above it and its predecessor.

![Pascal's Triangle](https://resources.beecrowd.com/gallery/images/contests/UOJ_2232_a.png)

David, the mastermind of your competitive programming team, found that the sum of the **i****th** row of the Pascal's Triangle is **2i**. Now, he wants to find the sum of the first N rows of the triangle. However, he thinks this problem is too easy and does not deserve his attention (he decided to try to solve a problem about bipartite graphs instead, a much harder topic), thus, you are the one who must solve this problem.

Input
-----

First line of input contains an integer **T**, the number of test cases. The next **T** lines contain a number **N** (1 â¤ **N** â¤ 31), the number of lines in the Pascal's Triangle you must solve.

Output
------

For each test case, the output must contain a line with an integer **S**, the sum of the first **N** lines in the Pascal's Triangle.


| Input Sample | Output Sample |
| --- | --- |
| 4 1 2 5 31 | 1 3 31 2147483647 |


# Problem 2238

Descrição
----------

Think a positive number ***n***. Now tell me an **A** divisor of ***n***. Now give me another **B** number than ***n*** divider. Now a multiple **C**. and a non multiple **D**. The number you thought is ...

It looks like a magic trick, but math! Does knowing the numbers **A**, **B**, **C** and **D**, you can discover what the original number ***n***? Note that there may be more than one solution!

This problem, given the values of **A**, **B**, **C** and **D**, you should write a program that determines which the smallest number ***n*** that may have been thought or conclude that there is no possible value.

Input
-----

The input consists of a single row containing four integers **A**, **B**, **C**, and **D**, as described above (1 â¤ **A**, **B**, **C**, **D** â¤ 109).

Output
------

Your program should produce a single line. If there is at least a number ***n*** for which **A**, **B**, **C** and **D** make sense, the line must contain the lowest possible ***n***. Otherwise, the line must contain -1.


| Input Samples | Output Samples |
| --- | --- |
| 2 12 8 2 | 4 |

| 3 4 60 105 | 6 |

Maratona de ProgramaÃ§Ã£o da SBC â 2016


# Problem 2291

Descrição
----------

Perfect numbers are numbers that are equal to the sum of its divisors , excluding himself. Based on this concept, divine numbers are numbers that are equal to the sum of the sum of each divisor of which number from 1 to **N**.

For example , 15 is the fourth divine number because
1 is the sum of divisors of 1 ,
3 is the sum of the divisors of 2,
4 is the sum of the divisors 3 ,
7 is the sum of divisors of 4 ,
and 15 = 1 + 3 + 4 + 7 .

Given a number **N** find the **N**th Divine number.

Input
-----

The input consists of several test cases . Each test case contains a single integer **N** (1 â¤ **N** â¤ 106) which corresponds to the Divine order number as specified. The input ends when **N** = 0.

Output
------

The output consists of one line per test case containing the **N**th Divine number.


| Input Sample | Output Sample |
| --- | --- |
| 1 2 3 4 100 0 | 1 4 8 15 8299 |


# Problem 2335

Descrição
----------

Arquibaldo is a very smart boy known to be the "bam-bam-bam" of mathematical questions related to geometric figures. Calculation of areas, perimeters, side measures, Arquibaldo was tired of small challenges. For him, it was all very easy. His aunt Helena, however, being a math english teacher, decided to give him a little harder challenge. Helena showed him four identical triangles and formed with them a square such that their sides were the measures of the hypotenuse of the chosen triangles. Then she told the nephew that depending on the measures of right triangles, there may or there may not be a smaller square in the center of the second largest. The illustrations below show clearly these cases:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2335.png)

She challenged him: "If I give the sides of the inner and outer square, l1 and l2, for example, can you tell me the smallest internal angle's measure, in degrees, of the triangle that would form with three other identical triangles a square with side mesure l1 and other with side mesure l2? ". Arquibaldo, has started to solve the challenge. Because he can't use calculator, her aunt was a good girl and allowed that only the integer parte of the answer was presented, ie, without decimal places. This way, Arquibaldo has now to find the greatest integer measure of the right triangle's smaller angle, such that the side of the inner square made by this new triangle (with the inner angle's measure being integer) be greater or equal to the inner square's side, that is, this should "fit" in the new inner square. For example, if the sides of the inner and outer squares have measures 1 and 5, respectively, then the smallest angle will approximate measure of 36,87Âº (degrees), however, the
greatest integer measure is 36, because for a set of four angles of right triangles 36 and 54 (complement) form squares of side 5 and 1,10 units of measure, that is, the square of side 1 would "fit" in a square of side 1.10, with this angle.

"Watch out for the existence of the triangle! Remember: now the angle measurements can only be integer numbers, "warned Helena to Arquibaldo for possible mistakes because she's brother. In the above example, the triangle has angles of 36, 54 and 90 degrees. Knowing that you are a programmer (it was not reported to Helena if you were good or not), Helena asked you to do a program to inform the feedback from figures provided by her to Arquibaldo, to see if he really knew how to solve the challenge.

Input
-----

The input consists of several test cases. Each case corresponds to a row containing the values of the internal and external sides of the squares, **L1** e **L2** (1 <= **L1**, **L2** <= 105) not necessarily in that order.

Output
------

For each test case, print the entire greater extent smaller inner angle of the right triangle, respecting the above conditions. If the angle of the triangle in question does not exist, print the message "Nao existe tal triangulo.".


| Input Sample | Output Sample |
| --- | --- |
| 102 100 100 101 40 40 2 1 1 5 1 10 32293 22321 | 1 Nao existe tal triangulo. Nao existe tal triangulo. 24 36 40 15 |


# Problem 2337

Descrição
----------

Francisco is a big fan of the game "Letâs flip a coin" and loves to play it with your lucky coin, but Francisco has some playing conditions. He always chooses "Head" and in each round of the game can be multiple currency pitches. Another thing is that Francis hates when the currency falls with the "Tail" face in two consecutive pitches. Curious, Francisco wanted to know what is the probability that in a game of "Letâs flip a coin" will not occur "Tail" in two consecutive shots, however, as he only likes to play, he asked you to do a program that calculates it to him.

Input
-----

The input contains several test cases, each line of input will contain an integer **N** (0<**N**â¤40) representing the amount of pitches in a single match.

Output
------

For each input line should be only one output line. The output should contain the probability of no consecutive "Tails". The answer must be in the form of irreducible fraction.


| Input Sample | Output Sample |
| --- | --- |
| 1  10 | 1/1  9/64 |

Thanks Wesley Rocha and William Azevedo the name of the question.


# Problem 2474

Descrição
----------

Christmas is comming, and Santa needs to evaluate how well each kid behave along the year, in order to define how many gifts each one of them are going to receive this year. The avaliation works in very strange way:

First, the Santa's assistants, capable of observing all the kids in the world, will assign to each kid an integer number **N**. Then, the number of gifts a kid receives is equal to **N-D**, where **D** is the greatest divisor of **N**, differente than **N**.

Planing to cheat in the distribution of the gifts to bennefit of some kids, a group of assistants decided to change the process. In the new version, the value **N** is subdivided int **Q** "parts", each being **ni** (1 < **ni**)**,** in a way that **N = Î£ni**, (1 â¤ **i** â¤ **Q**), and the number of gifts is calculated individually for each of these parts. The total number of gifts a kid receives in this new aproach is equal to the sum of the number of gifts for all the values **ni**.

Your task is, given the avaliation **N** for each kid, help the assistants to perform this division in order to maximize the number of gifts each kid receives. Note that the assistants are free to define the number of parts **Q**, as well as the value of each of the individual parts, as long as they add up to **N**.

Input
-----

Input consists of the value **N** for a number of kids. (1 < **N** â¤ 1010)

Output
------

For each kid, print the maximum number of gifts that this kid can receive, considering the choice for the value of **Q** and the subdivision are done in an optimal way.


| Input Sample | Output Sample |
| --- | --- |
| 2 4 33 10000000000 | 1 2 31 9999999998 |

Contest de Natal 2016.


# Problem 2489

Descrição
----------

Olivera Queen is a very skilled archer. She can hit any target at long distances without much difficulty. This time, she wants to train with her two hunting buddies in a somewhat unusual way: the target will be a stuffed rabbit. The archer will choose his own posture and his distance to the tree where the rabbit will be positioned, and from this information, the rabbit must be positioned in a way so that the archer can straightly hit it, without making any further movement. The image below shows the situation in a generic way:

![](https://resources.beecrowd.com/gallery/images/contests/UOJ_231_F.jpg)

The distance between the archer and the tree is represented by **D**, the height of the archer's shoulders to his feet is represented by **A** and the height at which the stuffed rabbit must be positioned so that the archer can hit its head is **H**. The angle of the tree and the angle of the archer with respect to the ground are always 90Âº, and the angle of the archer's arm with respect to his own body will be chosen by himself.

So, help Olivera Queen and her two promising hunting buddies train the way they planned: write a program that returns the appropriate value **H** so the stuffed rabbit can be hit in the head, according to the given information. Consider the arrow always goes straightly, regardless of its distance to the target.

Input
-----

The input contains several test cases. Each line constains a real number **A** (1 â¤ **A** â¤ 2) indicating the height of the archer, a real number **D** (5 â¤ **D** â¤ 40) indicating the distance between the archer and the tree and a real number **R** (50 â¤ **R** â¤ 150) indicating the angle, in degrees, between the archer's arm and his body. It's guaranteed that the input is always valid and doesn't generate unexpected outputs. Read input until EOF.

Output
------

For each test case, print the value of **H** with accuracy of 4 decimal places.


| Input Sample | Output Sample |
| --- | --- |
| 1.60 20 89.999  2 40 92  1.34 6.77 87.212 | 1.5997  3.3968  1.0103 |

The Last Contest 2016 - IFSULDEMINAS


# Problem 2494

Descrição
----------

Professor Alex is passionate about his programming marathons, if he could make it every end of the month, but he receives few resources to give the students. One of these events will win a lot of blue and black pens, but he does not know how much he should receive. And it wants to distribute in equal packages for each team.

He asked for his help, based on the amount of pens he receives, blue and black, he wants to pack all these pens so that each package contains only pens with the same color ink and will give it to all participating teams.

Input
-----

You will receive 3 values, in which the first will be the amount of blue pens, the second the amount of black pens and the third the amount of teams. The three values will be (1 <= **n**<= 1000);

Output
------

You will get a "sim" answer if you get packages for all teams and "nao" if you do not leave. Do not forget the end of line after the product, otherwise your program will display the message: *â**Presentation Errorâ*.


| Input Sample | Output Sample |
| --- | --- |
| 224 160 12  1 1 2  890 900 300 | sim  sim  nao |


