# Problem 2499

Descrição
----------

Given a triangle ABC with area **S**, and **N** equidistant points on the side AB and **M** equidistant points on the BC side, calculate the triangle's area determined by one of these points in AB with coordinate **C1** and two others over BC with coordinates **C2** and **C3**.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2499.PNG)

Input
-----

The input is composed by several test cases. The first line of a test case contains three integers **S** (1 â¤ **S** â¤ 106), **N** (0 â¤ **N** â¤ 103) and **M** (0 â¤ **M** â¤ 103) as specified in the text and the second line of a test case contains the coordinates **C1** (0 â¤ **C1** â¤ **N**+1), **C2** (0 â¤ **C2** â¤ **M**+1) and **C3** (0 â¤ **C3** â¤ **M**+1). The input ends when **S**=**N**=**M**=0.

Output
------

The output is composed by one line per test case containing the integer representing the area of the Triangle determined. It is always guaranteed that the area is an integer.


| Input Sample | Output Sample |
| --- | --- |
| 4112 3 3 3 1 2 1000 3 4 2 1 2 0 0 0 | 771 100 |


# Problem 2500

Descrição
----------

William recently learned some properties of the bit to bit operator xor (represented by the operator '^' in C language ). He realized that he can do many interesting algorithms with it: Find lonely elements in a sequence, exchange values ââwithout auxiliary variable, encryption and many others. Then he began to experiment and decided to name an operation using xor with its name, the w-xor. The w-xor operation is performed on a sequence of values. Example: it is an **S**={a1, a2, a3, a4}, applying w-xor over the sequence **S** once is equivalent to:

a1= a1^a2^a3^a4

a2= a1^a2^a3^a4

a3= a1^a2^a3^a4

a4= a1^a2^a3^a4

a1= a1^a2^a3^a4

If **S**={a1, a2, a3, a4, a5} then applying w-xor over **S** once is:

a1= a1^a2^a3^a4^a5

a2= a1^a2^a3^a4^a5

a3= a1^a2^a3^a4^a5

a4= a1^a2^a3^a4^a5

a5= a1^a2^a3^a4^a5

a1= a1^a2^a3^a4^a5  


Given a sequence **S** and applying w-xor **M** times over it, you would know what the value of the **K**-th position?

Input
-----

The input consists of several test cases. Each test case begins with three integers 2 â¤ **N** â¤ 103, 1 â¤ **M** â¤ 106  and 1 â¤ **K** â¤ **N** representing the number of elements of the sequence, the number of w-xor operations applied and the position of the value to be found (note that the first position is 1), respectively. On the next line, there will be **N** integer values ââ-109 â¤ **A****i** â¤ 109. The entry ends when **N=M=K=0**.

Output
------

The output consists of one line per test case containing the value of the **K**-th position of the sequence after applied **M** times the w-xor on it.


| Input Sample | Output Sample |
| --- | --- |
| 4 2 2  7 3 9 3  5 3 2  5 4 3 2 1  0 0 0 | 3  2 |


# Problem 2505

Descrição
----------

Some numbers in mathematics, due to their uniquiness, are given a special name. Particularly, there is a set of numbers, we will call "*Autopotential*". A number **N** is called Autopotential when *NN* gives a result where the last digits is, exactly, **N**. For example:

1: 11= 1 -> It is autopotential.  

3: 33= 27 -> it is not autopotential.  

10: 1010= 10,000,000,000 -> It is not autopotential.  

11: 1111 = 285,311,670,611 -> It is autopotential.

Input
-----

The input is defined as several test cases. Each line represents a test case and contains a unique integer value **N**, where 0 < **N** < 1,000,000.

Output
------

For each test case from input, your program must generate on output one unique line that contains a single word: "SIM", if the value from input is an Autopotential numer, or "NAO" otherwise.


| Input Sample | Output Sample |
| --- | --- |
| 1 3 6 10 11 | SIM NAO SIM NAO SIM |

This problem was applied on CPU2016 (University Coding Competition) at Santa Cruz State University - UESC.


# Problem 2514

Descrição
----------

In a galaxy far, far away, there is the planet NlÃ´guÃ©rrÃ , predominantly inhabited by dinosaurs. There are three moons orbiting NlÃ´guÃ©rrÃ . The orbit of each moon has the form of a circumference whose center is NlÃ´guÃ©rrÃ , as indicated by the figure in the left:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2514.png)

When all three moons align between the planet and the sun, as indicated by the figure in the right, a horrible catastrophe happens! The last time it occurred, exactly **M** years ago, a big drought doomed the entire planet, reducing the number of dinosaurs by half. The first moon takes **L1** years to complete an orbit around the planet; the second moon takes **L2** years to complete an orbit around the planet; and the third moon takes **L3** years to do so. Determine how many years will pass until the next alignment.

Consider that both the planet and the sun are stacionary.

Input
-----

The input contains several test cases. The first line of each test case contains the integer **M** (1 â¤ **M** â¤ 109), indicating that the last alignment occurred **M** years ago. The second line contains three integers **L1**, **L2** and **L3** (1 â¤ **L1**, **L2**, **L3** â¤ 103), the time it takes, in years, for each moon to complete its orbit around the planet. It is guaranteed that no alignment occurred in the last **M**-1 years, and no alignment occurs this year.

The input ends with end-of-file (EOF).

Output
------

For each test case, print a line containing a number **X** indicating that the next alignment between the planet and the sun will occur in **X** years from this day.


| Input Sample | Output Sample |
| --- | --- |
| 2 1 2 3 3 2 4 8 | 4 5 |

14th UFPR Trainning Session


# Problem 2516

Descrição
----------

To get fit until next summer, you and your friend decided to run on the streets in the campus every morning. Usually, you run together. However, today your friend started running early and, hence, he is a little ahead of you now.

Right now, your friend is **S** meters away from you. You are running at a constant speed of **va** meters per second, and your friend is running at a constant speed of **vb** meters per second. The following figure shows the situation:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2516.png)

Your task is to determine whether you will reach your friend, and, if so, how many seconds it will take.

Input
-----

The input contains several test cases. The only line in each test case contains three integers **S**, **va** and **vb** (1 â¤ **S**, **va**, **vb** â¤ 103), the current distance between you and your friend (in meters), your speed (in meters per second) and your friendâs speed (in meters per second), respectively.

The input ends with end-of-file (EOF).

Output
------

For each test case, if you cannot reach your friend, print a line containing â*impossivel*â (without quotes). Otherwise, print a line containing the time it takes, in seconds, for you to reach your friend. Round and print the answer with exactly two decimal places.


| Input Sample | Output Sample |
| --- | --- |
| 1 2 1 2 3 4 | 1.00 impossivel |

Competitive Programming, UFPR


# Problem 2584

Descrição
----------

It is possible to calculate the area of ââa regular pentagon, that is, a geometric figure with five equal sides, given the length of one side. So, do it.

![Pentagono](https://resources.beecrowd.com/gallery/images/problems/UOJ_2584.png)

Write a program that, given the length of one side of a regular pentagon, computes your area.

Input
-----

There will be a value **C** that indicates the number of test cases. Then there will be an integer **N** for each case (1 â¤ **N** â¤ 10000), indicating the length of the side of a regular pentagon.

Output
------

For each test case, print the corresponding value of the area of ââthe respective pentagon, with three decimal digits of precision.


| Input Sample | Output Sample |
| --- | --- |
| 3 1 2 3 | 1.720 6.882 15.484 |

VII OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2017


# Problem 2589

Descrição
----------

Prime gap âârefers to the difference between consecutive prime numbers. For example, the distance between prime ââ7 and 11 is 4, just as the distance between prime ââ23 and 29 is 6. The challenge is, given a number, considering all previous and the number itself, what is the largest distance between Consecutive prime numbers?

Write a program that, given a number, computes the biggest prime gap.

Input
-----

There will be several test cases. Each test case will have an integer **N** (2 â¤ **N** â¤ 109). The entry ends with end of file.

Output
------

For each test case, print the largest distance between consecutive cousins, from 1 to **N**.


| Input Sample | Output Sample |
| --- | --- |
| 10 11 12 30 | 2 4 4 6 |

VII OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2017


# Problem 2596

Descrição
----------

Kogu is searching for the dragon spheres to summon Xenlonguinho and ask him to relive his friend Kuriri, who unfortunately died in the last battle of Z's warriors.

However Kogu is having a great deal of trouble finding the spheres, so Xenlonguinho, who is his known for a long time, decided to make an exception and agreed to be invoked in case Kogu finds all spheres whose number of divisors of the number of stars in the sphere are even.

For example if there are seven spheres, Kogu would not have to find the one- and four-star spheres because they have an odd number of divisors, so he only needs to take 5 spheres to summon Xenlonguinho.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2596.png)

As Koku is not very good at calculations, he asked you to write a program that given the total of existing balls, show the minimum amount of spheres he needs to look for.

Input
-----

The first line contains an integer **C** that represents the number of test cases. Next lines contain an integer **N** (2 â¤ **N** â¤ 1000) representing the amount of spheres required to invoke Xenlonguinho.

Output
------

Your program should display the minimum amount of spheres Kogu has to look for.


| Input Sample | Output Sample |
| --- | --- |
| 1 7 | 5 |

The First Contest 2017 - IFSULDEMINAS


# Problem 2597

Descrição
----------

Kogu is searching for the dragon spheres to summon XenlongÃ£o and ask him to relive his friend Kuriri, who unfortunately died in the last battle of Z's warriors.

However Kogu is having a great deal of trouble finding the spheres, so XenlongÃ£o, who is his known for a long time, decided to make an exception and agreed to be invoked in case Kogu finds all spheres whose number of divisors of the number of stars in the sphere are even.

For example if there are seven spheres, Kogu would not have to find the one- and four-star spheres because they have an odd number of divisors, so he only needs to take 5 spheres to summon XenlongÃ£o.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2597.png)

As Koku is not very good at calculations, he asked you to write a program that given the total of existing balls, show the minimum amount of spheres he needs to look for.

Input
-----

The first line contains an integer **C** that represents the number of test cases. Next lines contain an integer **N** (2 â¤ **N** â¤ 109) representing the amount of spheres required to invoke XenlongÃ£o.

Output
------

Your program should display the minimum amount of spheres Kogu has to look for.


| Input Sample | Output Sample |
| --- | --- |
| 1 7 | 5 |

The First Contest 2017 - IFSULDEMINAS


# Problem 2598

Descrição
----------

TaxilÃ¢ndia's government is facing a huge problem, the people of TaxilÃ¢ndia love cars and speed, so they are running a lot in the avenues of the city. To mitigate this problem the government will install radars on the avenues, so that each section is covered by at least one radar. It is important to know that a radar covers miles along the avenue.

You were hired by the government to make a program that given the length of the avenue and the radar coverage area, inform the minimum amount of radars needed to cover the avenue.

The image below shows an avenue of size 15 kilometers and radars with a coverage of 4 kilometers, each color represents a radar, so it is possible to notice that the minimum number of radars needed to cover the avenue is 4.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2598.png)

Input
-----

The first line consists of an integer **C** that represents the number of test cases. Each test case is made up of two integers **N** and **M** which indicate the size of the avenue and the radar coverage area.

(1 â¤ **N** â¤ 109)

(1 â¤ **M** â¤ 109)

Output
------

You should display the least amount of radars needed to cover the avenue.


| Input Sample | Output Sample |
| --- | --- |
| 1 10 3 | 4 |

The First Contest 2017 - IFSULDEMINAS


# Problem 2636

Descrição
----------

Pedro, like many other undergraduates, was fascinated by the beauty and sophistication of cryptography. He began to read historical references, to study the main algorithms and to search for articles and news that approached the subject in the most different aspects.

However, the large volume of information gained in a short period of time has led to some questions and fears. Worried about quantum computing, which in theory would cripple RSA encryption, and motivated by the history of the DES algorithm, which had a more secure evolution called 3DES, he decided to propose a more secure version of RSA, called 3-RSA.

In 3-RSA, the module n, composed in the original algorithm by two distinct prime numbers, would now consist of 3 distinctly odd primes! Pedro was right that this modification would bring greater difficulty in breaking the algorithm, since the attackers now would have to find 3 factors of n, not only 2.

Knowing that in cryptography, sometimes less is more, and willing to show to the motivated and well-intentioned Peter that the proposed modification actually weakens the RSA, factor the n module of the 3-RSA algorithm, showing its three prime factors.

Input
-----

The input consists of a series of test cases. Each test is represented by a single line, contains the integer **n** (105 â¤ **n** â¤ 1018), which represents the module of the 3-RSA algorithm. The input ends with the value **n** = 0, which should not be processed.

Output
------

For each test case a line containing the message *ân = p x q x râ* should be printed, where **p**, **q**, **r** are the prime factors of **n**, with 3 â¤ **p** x **q** x **r**.


| Input Sample | Output Sample |
| --- | --- |
| 105  231  7163  89348965057411  0 | 105 = 3 x 5 x 7  231 = 3 x 7 x 11  7163 = 13 x 19 x 29  89348965057411 = 17393 x 51437 x 99871 |

Maratona de ProgramaÃ§Ã£o UnB/CIC 2015.


# Problem 2660

Descrição
----------

American "periodical cicadas" have the longest life cycle of any known insect. Every 17 years, these periodical cicadas mature, mate, lay eggs, and die. Their young take refuge underground, 20 centimeters deep, where they will feed on root sap for 17 years, until their day comes to seek a place in the sun.

It is believed that this number did not happen by chance; other cicada species in the region have 13-year cycles, so these two species emerge at the same time only every 221 years. This is desirable because in this way the chance of the two species mixing considerably decreases, and undesirable characteristics from one population are not introduced into the other.

Inspired by this phenomenon, a new variation of the evolutionary algorithm was created. In the last step of this algorithm the best possible solutions are divided into populations so that each population **i** has a life cycle **Ci** . In addition an extra population is also added, so that the number of iterations until the life cycles of all populations match is as large as possible. These populations are then evaluated until they all have the same life cycle, and the best solution at the end of the process is chosen. Since it is not interesting to wait too long for the algorithm to generate an answer, an upper limit **L** on the number of iterations must also be respected.

Given the life cycles of the populations created and the limit on the number of iterations **L**, your task is to compute the optimal period for the extra population that will be added

Input
-----

The first input line contains two integers **N** and **L**, respectively, the amount of populations generated by the previous steps of the algorithm and the limit on the amount of iterations, 2 â¤ **N** â¤ 104 , 1 â¤ **L** â¤ 106.The next line contains the **N** values **Ci** representing the amount of iterations in the life cycle of each population, where 1 â¤ **Ci** . You can assume that the life cycles of the current populations coincide in less than **L** iterations.

Output
------

Your program needs to produce a single line with an integer representing the period of the extra population that maximizes the amount **T** of iterations until the life cycles of all populations coincide, respecting the constraint that **T** â¤ **L**. If there is more than one possible value print the smallest of them.


| Input Sample | Output Sample |
| --- | --- |
| 2 5000  105 55 | 4 |

| 2 512  3 14 | 72 |

| 3 80  6 10 15 | 4 |

Maratona de ProgramaÃ§Ã£o da SBC â ACM ICPC â 2017


# Problem 2661

Descrição
----------

All positive integers can be written as a product of powers of primes. For example, 252 = 22 \* 32 \* 7. An integer is stripped if it can be written as a product of two or more distinct primes, without repetition. For example, 6 = 2 \* 3 and 14 = 2 \* 7 are stripped, but 28 = 22 \* 7, 1, 17 are not stripped.

Input
-----

The input consists of a single line that contains an integer **N**(1 â¤ **N** â¤ 1012).

Output
------

Your program is required to produce a single line with an integer representing the number of divisors stripped of **N**.


| Input Sample | Output Sample |
| --- | --- |
| 252 | 4 |

| 6469693230 | 1013 |

| 8 | 0 |

| 1 | 0 |

| 88290298627 | 0 |

Maratona de ProgramaÃ§Ã£o da SBC â ACM ICPC â 2017


# Problem 2667

Descrição
----------

A popular children's game is 21 of Mouth . The game is played as follows: the first player says a number, **n0**, which can be either 1 or 2. The second player can then say a number **n1** such that **n1** â{ **n0** + 1 , **n0** + 2 }. And so on, the players alternate, always saying a number that is one or two greater than the previous one. The player who says 21 wins the game. For example, the sequence of numbers could be: 1, 3, 5, 6, 6, 7, 9, 11, 12, 14, 15, 16, 18, 19, 21. In this game, the first player always loses, if the second player knows how to play well.

With each new generation, children get smarter. Nowadays, although they find 21 of Mouth an interesting game, many kids don't feel challenged enough and so they decided to generalize the game, creating **N** of Mouth. Given an integer **N**, instead of 21, the first player can choose 1 or 2. From then on the players alternate, adding 1 or 2 to the previous number, until one of them says the number **N** and wins the game. Knowing that both players are excellent and can play very well, your problem is to determine which starting integer the first player must choose to win the game.

Input
-----

The input consists of a single line containing the integer **N** (3 â¤ **N** â¤ 10100) chosen for the current mouth **N** match.

Output
------

Your program is required to produce a single line with an integer representing the number, in {1,2}, which the first player must choose, to win the game. If this is not possible, then the integer must be zero.


| Input Samples | Output Samples |
| --- | --- |
| 7 | 1 |

| 9 | 0 |

| 12341234123412341234123412341234 | 2 |

Maratona de ProgramÃ§Ã£o da SBC-ACM ICPC 2017


# Problem 2668

Descrição
----------

Given a real number **X** of the form **A** + â **B**, with **A** and **B** positive integers and â1 < **A** â â **B** < 1, and two integers **N** and **K**, your task is to determine the **K**-th least significant digit of the integer part of **XN**. For example, if **K** = 1, you need to determine the units digit of [**XN**].

Input
-----

The input consists of a single line, which contains four integers, **A**, **B**, **N** and **K**, with 1 â¤ **A**, **B** â¤ 104, 1 â¤ **N** â¤ 109 and 1 â¤ **K** â¤ 4.

Output
------

Your program should print a single line, containing the **K**-th least significant digit of the integer part of **XN**.


| Input Sample | Output Sample |
| --- | --- |
| 3 10 1 1 | 6 |

| 3 10 2 1 | 7 |

| 3 10 1000000000 1 | 1 |

| 10 90 1000000000 2 | 9 |

Maratona de ProgramÃ§Ã£o da SBC-ACM ICPC 2017


# Problem 2674

Descrição
----------

The Association of Indivisible Primes ââelected a category of prime numbers called Super Primes. A number is considered super prime if in addition to being prime, all its digits are prime, too. The Association asked you to make a program to characterize the numbers.

Input
-----

The input contains several test cases, each test case being an integer **N** (0 < **N** < 105) on a single line. The entry ends in the last test case.

Output
------

For each test case, the entry number classification is expected in a single line, which can be: "Super", if the number is a Super Prime; "Primo" if the number by a prime number only; Or "Nada" if the number has divisors beyond 1 and itself.


| Input Sample | Output Sample |
| --- | --- |
| 23 33 43 | Super Nada Primo |

This problem is the number seven problem in the ProgBASE-2017 competition, which takes place within ERBASE (Bahia Alagoas and Sergipe Regional School Congress).


# Problem 2680

Descrição
----------

This government, as always, is very worried about the payroll. This year, however, the way the payments are made will be changed. Instead of paying workers as usual, the formula used to pay their salaries will be simpler: The sum of the divisors of the enrollment number of each worker.

To avoid frauds, help the government to do the math!

Input
-----

The input starts with a line with a single number 1 â¤ **N** â¤ 104 that is the number of workers. Each of the N following lines represents a worker and contains the workers enrollment number 1 â¤ **M** â¤ 108.

Output
------

The output consists of **N** lines, each containing the salary of a worker in the same order of input.


| Input Sample | Output Sample |
| --- | --- |
| 7  1  2  3  4  50  60  77 | 1  3  4  7  93  168  96 |

5Âª Maratona De ProgramaÃ§Ã£o Da UFFS


# Problem 2681

Descrição
----------

The Hanoi tower problem is very famous. However, very few people remember the original legend: It is sand that monkeys were tasked to solve the problem, and when they finish, the world ends.

The problem consists of 3 pins, and in the fist pin is sitting a stack of disks, one larger than the other. As we know, it is not allowed to place a larger disk above a smaller. This means that, to transfer one disk from the pile, one must first remove all the smaller ones first. Besides that, it is only allowed to move one disk at once.

The problem is solved when all disks from the first pin are transferred to the third pin.

We know that the monkeys started working at midnight (00:00:00), and that they work 24 hours per day, non stop, and they take at least 1 second to move each disk. Your task is to foresee the exact time of the day or night, in the format hh:mm:ss, of the earliest time possible the monkeys finish the game and the world ends.

Input
-----

The input consists of a single line containing a single integer 0 < **X** < 1040, that is the number of disks in the starting stack.

Output
------

The output consists of a string in the format **A:B:C**, where 0 â¤ **A** < 24 e 0 â¤ **B, C** < 60


| Exemplo de Entrada | Exemplo de SaÃ­da |
| --- | --- |
| 1 | 00:00:01 |

| 2 | 00:00:03 |

| 3 | 00:00:07 |

| 4 | 00:00:15 |

5Âª Maratona De ProgramaÃ§Ã£o Da UFFS


# Problem 2711

Descrição
----------

During cryptography class, Rangel is bored.

-Gu, hey, Gu! - Rangel calls his friend.

-Hey, man! - Gustavo replies.

-Can I borrow your phone? - Rangel says hopefully.

-No way, you are going to comment my social media posts â says Gustavo.

-Ok â Rangel replies sadly.

Gustavo is a nice guy and does not want to see his friend sad. Considering that in his mind, he calls VÃ¢nia and they both come up with a challenge to get rid of Rangel's boredness and make him like cryptography.

-Let's go Rangel, we challenge you! - say Gustavo and VÃ£nia, both smiling.

-Challenge? What kind of challenge? - says Rangel.

-Don't you want to use my phone? Come on, we have a challenge for you. Do you accept it? - they ask him.

-Yes, let's do it! - says Rangel, even more curious.

- OK, we are going to explain it:

We are going to change the password of my phone, and you have to find out what it is. It is not going to be an easy task. We will give you three numbers B, N and M, and we want you to find out the fourth number. This number will be my password! However, do not think this is going to be easy, because to discover the fourth number you need to solve the following equation:

**BE = N mod M**

Simple, right? We are interested that you discover the value of **E**, we assure you that the value of **E** is between **[0, M - 1]** and **M** is a prime number! Hahaha - Come on, you need to be fast! Well, you only have class time to solve!

-Ok, I'll take it, but I will use my laptop to help me â says Rangel cheerfully.

-Ok, show me what you can do. - say Gustavo and VÃ¢nia.

-I am going to give you a clue. Remember, Rangel, the value is between **[0,M -1]**, but if it is not, it is **-1**!

Rangel is ready to take the challenge and decided to use programming to help him out. He asked your help to develop the code. Are you going to turn down this challenge?

Input
-----

There are several case tests. Each case consists of three integers **B**, **N**, **M** where **B** and **N (0 < B, N < 105)** and **M** are a prime number.

Output
------

For each case, you will have to print the value for E, and if this value does not follow the following property **[0, M - 1]**, you wll have to print **-1**. Let's go, help Rangel!


| Input Sample | Output Sample |
| --- | --- |
| 2 64 107  5 15625 18047  5 1458 107  77 12 19  1 1 3 | 6  6  27  -1  0 |

VI Maratona Interna de ProgramaÃ§Ã£o UNIFESO


# Problem 2726

Descrição
----------

It's Christmas Eve, and it's almost time for the sled to leave. Everything is already in Santa's sack and the reindeer in position, there is only one thing left: decide which helpers will work with Noel this year. Yes, contrary to popular belief, the good old man does not do everything himself. He always takes with him a group of elves on his round the world in one night.

However, the elves must be chosen carefully, because their weight will directly affect the aerodynamics of the Sled. If it is very light it will swing very much during the flight and if it is very heavy it will tire the reindeers very early.

As it is in hurry Noel decided to make a try and chose a group of helpers. But the Reindeers soon accused them of being too light. Then Noel made a second attempt, chose another group. But again the Reindeers complained, however, stating that it was now too heavy. The good old man, who has an appointment time, became irritated and gave an ultimatum to his subordinates: "That's enough! Choose **K** elves soon to go in such a way that the sled is neither too light nor too heavy! That is, the sum of the weights can not be less than that of the first group that I tried and neither greater than the second one.

Of course the little ones despaired. Apart from the restriction of weights and now the number of Elves that have to be exact, they still have the fact that each Elf weighs twice as much or more than an Elf younger than him. Which obviously only complicates everything.

Knowing that all Elves are of different ages can you help these little ones tell how many ways they can choose a group to go with Santa respecting all the requirements?

Input
-----

The first line of the entry contains an integer **T** that represents the number of test cases. Then there are **T** test cases. The first line of a test case contains two integers **N** (1 â¤ **N** â¤ 50) and **K** (1 â¤ **K** â¤ 50) respectively representing the total number of Elves and the determined number of Elves to be boarded on the sled. The second line of a test case contains **N** integers **Pi** (1 â¤ **Pi** â¤ 1018) representing the weight in mg of the Elves. The third and last line of a test case contains two integers **A** and **B** (0 â¤ **A** â¤ **B** â¤ 1019) representing respectively the weight of the lighter group tested and the weight of the heaviest group tested. Both in mg.

Output
------

The output is composed of one line per test case containing an integer representing the number of ways to choose a group according to requirements.


| Input Sample | Output Sample |
| --- | --- |
| 3 3 2 10 1 3 4 13 4 3 20 10 50 1 21 81 6 3 14 70 3 1 6 31 10 74 | 3  4  11 |

Contest de Natal 2017


# Problem 2735

Descrição
----------

Nina got **N** distinctnumbers from 0 to N-1 for Christmas. She realized that those numbers can be used to form a permutation: an array of size **N** in which all numbers from 0 to N-1 appears once. She then remembered that she had kept a very special permutation of size **N**in her drawer, and she could use it to play with her new blocks. She came up with the following game:

At day 0, she will arrange the numbers in such a way that 0 is the fist one, 1 the second, and so on, until **N-1**, forming the array  **V0**. At day x, she will arrange the numbers to form the array **Vx**, in which **Vx[ i ] = Vx-1[ P [ i ] ]**, P being Nina's special permutation.

Her sister Nani got really jealous and decided to question Nina's knowledge about her permutation with questions of the following type: given two numbers **J** e **K**, what is the smallest number **Y**such that **VY [ ( J + K ) % N ] = J**?

Help Nina with her sister's questions.

Input
-----

The first line of input contains the number **t**(**t**=10) of test cases.

Each case starts with a line containing a number **N**(0<=**N**<=105): the number of blocks Nina got for Christmas. **N**distinct integers ranging from 0 to N-1 follow.

The next line will contain an integer **Q** (1<=**Q**<=105): the number of questions Nani will ask, followed by **Q** lines, each containing two integers **J** and **K**(0<=**J,K**<**N**).

Output
------

For each question, print the answer. If it does not exist, print -1.


| Input Sample | Output Sample |
| --- | --- |
| 1  5  2 0 1 4 3  3  0 2  2 0  2 1 | 2  0  -1 |

Made By Women Contest 2018


# Problem 2767

Descrição
----------

JoÃ£ozinho is organizing his birthday party with **N** men and **M** women, and he wants to know the number of good pairs that can be formed with his guests. A pair is good when it is composed of a man and a woman and the sum of the heights of the two persons is multiple of **K**. The same person can be part of more than one pair.

Input
-----

The input is composed of several test cases and ends with EOF.  

The first line of a test case contains the integers **N**, **M** and **K** (\(1 \leq N, M, K \leq 10^5\)). The second line contains **N** integers **Ai**, representing the height of the **N** men invited. The third and last line of the input contains **M** integers **Bi** representing the height of the invited women. (\(1 \leq Ai, Bi \leq 10^5\)).

Output
------

The output should contain one integer for each test case, indicating the number of good pairs that can be formed.


| Input Sample | Output Sample |
| --- | --- |
| 3 3 2 1 2 3 4 2 7 2 3 2 1 2 4 2 7 | 4 3 |

V Maratona Norte Mineira de ProgramaÃ§Ã£o


# Problem 2777

Descrição
----------

Dabriel just invented a new game that works as follows: He thinks of an integer **N** and must find the number of maximals\* subsets that exist using the numbers from 1 to **N** so that if the number i is chosen for the set, neither **i**-1 nor **i**+1 can appear. For small values Dabriel knows the answer, but with large numbers this task gets very difficult. Can you help him?

For N = 5 the valid sets are: {1,3,5}, {2,4}, {2,5}, {1,4}.

Input
-----

The input is composed of several test cases. Each case contains an integer **N** (1 â¤ **N** â¤ 1018).

Output
------

For each test case print the number of existing sets. Since this number can be very large, print only the rest of the division by 109+7.


| Input Sample | Output Sample |
| --- | --- |
| 1 5 30 | 1 4 4410 |

\* A maximal set S is a set where it is not possible to include any other element in it, that is, it has the largest possible size.   

V Maratona Norte Mineira de ProgramaÃ§Ã£o


# Problem 2801

Descrição
----------

A cipher process consists in change each symbol of a message to another symbol from the same alphabet used in the original message, in the way to has one by one correspondence to each other. It means that two different symbols can not be replaced by the same symbol.

An Affine cipher consists in suppose some symbols of a **T** size alphabet as numbers of an interval [0..**T**-1]. Two positive numbers **A** and **B** are chosen. To cipher a symbol is necessary to multiply its position value on the alphabet by **A** and the number **B** needs to be added to the result of this multiplication. In the end, the result will be the position of the symbol that will replace the original in the sequence. If this new position does not correspond to a valid position inside the size of the alphabet, it supposes that the alphabet will be repeated many times on the right, in the way to have all estimated positions.

For example, suppose an alphabet which its size is 7 and **A**=4 and **B**=2. To cipher any symbol from this alphabet is necessary to extend the alphabet to the right by 3 times, as shown below:

![](https://resources.beecrowd.com/gallery/images/contests/UOJ_360_H.png)

In this cipher, the symbol 6 is ciphered to the symbol 5 because **A** x 6 + **B**=26 and the symbol in position 26 is 5.

Need to be noted that not all Affine cipher is valid. A poorly made cipher can not produce a one-by-one correspondence between symbols, not guaranteeing that the decipher could be made in a unique way.

Your task is, given the parameters **A** and **B** and the alphabet size, decipher a message with **N** symbols or show that it not possible to do so.

Input
-----

The first line of the input consists in an integer number **N** (1 â¤ **N** â¤ 105) that corresponds to the message size. The second line consists of **N** integer numbers **Mi** (0 â¤ **Mi** < **T**) that correspond to the message itself. The third line contains three integers: **T** (1 â¤ **T** â¤ 109) that corresponds to the alphabet size; and **A** (1 â¤ **A** â¤ 109) and **B** (1 â¤ **B** â¤ 109) as specified before.

Output
------

The output consists in a single line containing the deciphered message, with its symbols separated by a single blank space, if will be possible to decipher each symbol of the alphabet in a single mode. Otherwise, print the message "DECIFRAGEM AMBIGUA" (ambiguous decipher).


| Input Samples | Output Samples |
| --- | --- |
| 7  2 6 3 0 4 1 5  7 4 2 | 0 1 2 3 4 5 6 |

| 3  6 79 44  108 73 41 | 1 2 3 |

| 3  73 60 49  119 25 48 | 1 10 100 |

II Maratona de ProgramaÃ§Ã£o do Norte


# Problem 2817

Descrição
----------

One of the consequences of the truck drivers strike was the lack of gasoline across the country. In Santa Rita do SapucaÃ­, a city in the south of Minas Gerais, it was no different. Hundreds of cars and motorcycles lined up at the last station with gasoline available to fill their tanks before it drained, it looked like a zombie apocalypse movie scene.

The station has **N** bombs and in each of them there is a row in a straight line with **M** veÃ­culos (carros ou motos). vehicles (cars or motorcycles). Bellow, there's an illustration of a station with 4 bombs and a row of 2 vehicles per bomb.

![](https://resources.beecrowd.com/gallery/images/contests/posto_do_darlan.png)

Darlan, owner of the station, limited the amount of gasoline that each car could fuel in 25 liters and each bike in 12 liters. Since all vehicles owners in queues were afraid they would never be able to refuel, they would certainly put the maximum gasoline allowed by Darlan.

The local TV station team was live with their drone filming the long lines of vehicles around Darlanâs station when a viewer asked a somewhat random question: "If we take into account that the rows of cars feature a matrix of **N** lines by **M** columns, what is the largest amount of gasoline that vehicles in a square of size **L** will put? Given that in this square there must be at least one vehicle of each type (car and motorcycle)."

The TV crew has no idea how to answer this question and needs your help!

Input
-----

The first line of the input has two integers **N**, **M (**1 â¤ **N, M**â¤ 1000), representing the number of pumps and the number of vehicles queued in each pump. They follow **N** lines, each containing **M** characters 'C' or 'M' representing a car or a motorcycle, respectively. After this there will be an integer **L (**1 â¤ **L**â¤ 1000), representing the size of the square side that the viewer wishes to know

Output
------

Display a single integer, the largest possible amount of gasoline that vehicles in a square **L** will fuel , given that there must be at least one vehicle of each type. If there is no square that characterizes the viewer's doubt, print -1.


| Input Sample | Output Sample |
| --- | --- |
| 4 2  CM  CC  MM  CC  2 | 87 |

| 2 2  CC  CC  2 | -1 |

| 3 5 CMMMC MMCMM MMMCM 3 | 147 |

OBI Warm-up - 2018 Regional Phase


