# Problem 1909

Descrição
----------

After asking for a square ball to his mother, Kiko did not receive just one, but several birthday balls! Kikos loves to drop multiple balls at once on the ground and keep watching them bounce. As the balls have size, weight and are made of different materials, the bounce time from one to another is variable. In this problem we will assume that every ball bounces infinitely according to its bouncing time.

Kiko released at the same time **N** balls and realized that depending on the bounce time of the balls, in a few moments, all the balls bounce at the same time, and he loved it!

Given the bounce time in seconds of the **N** balls that Kiko choose and a time **T**, which is the second that Kiko wants all the balls bounce together, your task is to find the lowest bounce time for another ball so all the N + 1 balls, when they are released together, all of them will bounce at the same time for the first time exactly in the second **T**.

The bouncing time that you will choose canât be identical to any previously chosen by Kiko and should be greater than 1.

Bounce time is the difference of the time that the ball touch the ground twice in succession. If a ball has bounce time = 4, we will consider that it will bounce at seconds 4, 8, 12, 16...

Input
-----

There will be several test cases. The first line of each case begins with two integers **N** (1 â¤ **N** â¤ 100) and **T** (1 â¤ **T** â¤ 105) representing the amount of balls that Kiko has and the second that Kiko want to see the N+1 bouncing at the same time for the first time. On the next line, **N** integers in the range **[1, T]** follows, representing the bounce time of each ball.

The input ends with **N** = **T** = 0, which should not be processed.

Output
------

For each case, output the bounce time of the ball that you choose, or "impossivel" if there doesnât exist a ball that will satisfy Kikoâs whishes.


| Input Sample | Output Sample |
| --- | --- |
| 2 12  2 4  2 20  3 2  3 100  4 5 20  0 0 | 3  impossivel  25 |

Codando na Vila - 2015


# Problem 1921

Descrição
----------

Guilherme loves kites, kites of different colors, forms and sizes. He realized that in order to kites become stable, and thus fly higher, they must have a taut string connecting all pairs of non-neighboors tips.

Despite being a very creative and clever child, Guilherme doesnât know how to determine the number of strings necessary to make a kite of *n* sides stable. Could you help him?

Input
-----

The single line of the input contains an integer 3 â¤ **n** â¤ 105, the number of sides of the kite.

Output
------

Print a single number, the number of strings that Guilherme needs to make a kite of **n** sides stable.


| Input Samples | Output Samples |
| --- | --- |
| 4 | 2 |

| 10 | 35 |

| 11 | 44 |

Tribute to my brother Guilherme, he loves kites.  

Tapioca's Round I, 2015


# Problem 1926

Descrição
----------

Marianne is programming her own game called âHero of the Guitarâ . Itâs a extremely tiresome work, that needs a lot of time and effort, but nothing that some free time doesn't solves. Someday she received an e-mail, in the e-mail Mari has encountered a very curious problem proposed by the cousins RenÃ¨ and Leonhard and the twins Isaac and Carl.

The problem is described as the following:

âA natural number is prime, if itâs divided by exactly two numbers: number one and it self (one isn't prime). A number is twin prime, if and only if, itâs prime and there is another prime number b, such that |a - b| = 2. An example: number 3 is twin prime, because itâs prime and thereâs another prime (5) with |3 - 5| = 2. But number 23, despite being a prime number, isn't twin prime. Could you tell me how much twin primes there is between two numbers *x* and *y*?â

Marianne loves to solve this kind of problem, but she is busy programming her game. Could you help her?

Input
-----

In the first line there is an integer 1 â¤ **Q** â¤ 105, the number of querys, each of the next **Q** lines will have two numbers, 1 â¤ **X**, **Y** â¤ 106.

Output
------

For each query **Q**, print the quantity of twin primes between **X** and **Y**, inclusive.


| Input Samples | Output Samples |
| --- | --- |
| 3  1 7  5 7  8 12 | 3  2  1 |

| 2  1 10  1 100 | 3  15 |

Special thanks to Marianne, for helping me throughout Contest creation process. Thank you, Mari.  

Tapioca's Round I, 2015


# Problem 1946

Descrição
----------

A great TV show gives prizes to the audience through the Pyramid of Fortune. One guest throws at the top of the pyramid (which is actually a triangle) and it goes down to the left or to the right until it hits one of the slots at the pyramid base. The guest wins the prize that is mapped to that slot.

The grand prize is always at the middle of the pyramid base. So, its base always have an odd number of slots. The figure shows one pyramid with 15 slots.

![Pyramid](https://resources.beecrowd.com/gallery/images/problems/UOJ_1946.png)

The TV show producers wants to save as much as possible and have asked you to calculate what is the probability of winning the grand prize, given the number of slots at the pyramid base. Consider that, in each point of the pyramid, the ball has the same probability to go to the left or to the right.

Input
-----

The input is given in a single line, which contains the number **S** of slots at the pyramid base (3 â¤ **S** â¤ 4999). **S** is always an odd number.

Output
------

The output must be given in a single line, which contains the probability of the ball hits the slot with the grand prize. The probability must be printed with 2 decimal places.


| Input Samples | Output Samples |
| --- | --- |
| 3 | 50.00 |

| 5 | 37.50 |

| 15 | 20.95 |

III Maratona de ProgramaÃ§Ã£o FACE - 2015


# Problem 1949

Descrição
----------

A shift register is a circuit that shifts the elements of a bit array by one position. A shift register has an input (one bit) and an output (also one bit), and is driven by a clock pulse. When the clock pulse happens, the input bit is shifted to the position of the least significant bit, the most significant bit is sent to the register output, and all other bits are shifted by one position to the direction of the array's most significant bit (towards the output).

A Linear Feedback Shift Register (LFSR) is a shift register in which the input bit is determined by the value of the EXCLUSIVE-OR of some of the register bits before the clock pulse. The bits that are used in the register's feedback are called taps. The figure below shows a LFSR with 8 bits and three taps (bits 0,3 and 5).

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1949_en.png)

In this problem you must write a program that, given the number of bits of a LFSR, the information of which of its bits are taps, a start state and a final state, determines how many clock pulses are needed so that, starting from the start state, the LFSR reaches the final state (or determines that that is impossible).

Input
-----

The input contains several test cases. Each test case is composed by three lines. The first line contains two integers **N**, **T**, indicating respectively the number of bits (2 â¤ **N** â¤ 32) and the number of taps (2 â¤ **T** â¤ **N**). The bits are identified by integers from 0 (least significant) to **N** - 1 (most significant). The second line contains **T** integers, separated by spaces, describing the bits that are taps, in increasing order. Bit 0 is always a tap. The third line contains two numbers **I** and **F** in hexadecimal notation, separated by a blank space, representing respectively the start state and the final state of the lfsr.

The end of input is indicated by a line that contains two zeros separated by a blank space.

Output
------

For each test case in the input your program must print a single line. If it is possible to reach the final state from the given start state, the line must contain a single integer, the smallest number of clock pulses needed for the lfsr to reach the final state given. If that is not the case, the line must contain just the character '\*'.


| Input Sample | Output Sample |
| --- | --- |
| 8 3 0 3 5 a9 35 5 2 0 4 1b 2 7 3 0 2 3 4d 1a 0 0 | 3 \* 61 |

XIV Maratona de ProgramaÃ§Ã£o da SBC 2009


# Problem 1967

Descrição
----------

It is the year of 2,265, and the University of the Final Frontier of the Space (UFFS) has already got many campuses around the galaxy, so that all undergraduate courses of UFFS are offered at all campuses. Each course promotes many activities each year, and the activities promoted by a course are the same for all UFFS campuses. In order that every activity can happen, the University needs to buy a certain number of materials, but the prices of each material are not the same for all campuses. A pencil, for example, may cost É2 (2 bitcoins) for the campus of ChapecÃ³, at planet Earth, and É7 (7 bitcoins) for the campus of ShiKahr, at planet Vulcan. Despite cost differences, it's never a good idea to buy the materials in a campus to send them to another campus, due to the very high transportation costs and import and export duties. Thus, in order that all the University's activities can be accomplished, the Rectory needs to transfer to each course of each campus the exact amount of bitcoins
needed so the courses can buy the materials by themselves.

Input
-----

The first input line consists of four positive integers, **G**, **A**, **M** and **C** (**G** â¤ 600; **A**, **C** â¤ 100; **M** â¤ 2000), which represent respectively the number of undergraduate courses, the total number of types of activity that can happen, the total number of types of material that can be needed and the number of UFFS campuses. The courses are designated in the input by the integers from 1 to **G**, the types of activity by the integers from 1 to **A**, the types of material by the integers from 1 to **M** and the campuses by the integers from 1 to **C**. Then three tables of non-negative integers follow. Each table is preceded by a blank line, between two consecutive columns of a same table there is a column of spaces of width 1, and additional spaces may precede each integer of a table in order to right align all
columns of that table, existing at least one integer in a column which is not preceded by additional spaces. The first table consists of **G** lines, each one containing **A** integers not greater than 10, so that the **j**th integer of the **i**th line represents how many activities of type **j** an undergraduate course **i** needs to accomplish in the current year. The second table consists of **A** lines, each one containing **M** integers not greater than 10, so that the **j**th integer of the **i**th line represents how many materials of type **j** are needed in order to accomplish an activity of type **i**. The third and last table consists of **M** lines, each one containing **C** integers not greater than 100, so that the **j**th integer of the **i**th line represents the price, in bitcoins, of one unit of the material of type **i** in the planet at which the campus **j** is located.

Output
------

Print **G** lines containing **C** integers each, so that the **j**th integer of the **i**th line represents the amount of bitcoins the Rectory needs to transfer to the course **i** of the campus **j**. Follow strictly the same spacing rules between columns of the input.


| Input Sample | Output Sample |
| --- | --- |
| 2 3 3 2  1 2 3 3 2 1  2 0 1 0 1 3 2 4 4  2  7  11 13 100  3 | 2070 295 1382 173 |

3rd UFFS *Junior* Programming Contest


# Problem 1968

Descrição
----------

Last October 12th we celebrated in Brazil the Children's Day. We adults should live more in children's world, for the opposite is not working, not at all. We adults have split the world into nations, and the children are those who suffer the most from the wars. We adults have built a wealth distribution system, and the children are those who suffer the most from hunger. But there is an Undiscovered Country, not so far from those who still preserve a little bit of imagination, that belongs to the children. There is no war there, or poverty, or hunger. There the children play day and night.

But a catastrophe is happening to the Undiscovered Country. A catastrophe! The sheep which used to live in the Undiscovered Country have ended up getting old, or sick, or swallowed by boa constrictors. This way, the baobabs have started to grow and spread over the entire country. Now, the citizens have to move urgently. In order to facilitate the evacuation, all the citizens have been numbered from **A** to **B** (it is obvious that this idea has come from the adults â they love these things!). In order to define who would be the leaders of the groups during the evacuation, someone has suggested that the leaders should be all those who have received a prime number (it is obvious that this idea has come from a child â children have a lot of imagination and they love pleasing themselves with things that need no further explanation!). But soon another idea came forth:

â A prime number is a number that has exactly 2 divisors. What if the leaders were those who have received a number with exactly **N** divisors?

All the children loved the idea. The adults, on the other hand, needed a long time to debate how the number **N** should be chosen. When finally the number **N** was chosen, each citizen who were not leader of a group should pick up the group he or she liked the most to enter it. No other restriction was imposed to the groups. Nothing was preventing, for example, a group of consisting only of its leader. Note that, depending on the value of **N**, there would not be any group at all.

Knowing the values of **A**, **B** and **N**, release the child inside you and try to figure out the total number of possibilities for the formation of the groups. If, for example, **A** = 5, **B** = 8 and **N** = 4, situation in which the leaders are the citizens 6 and 8, there are 4 possibilities:

* both citizens 5 and 7 choose enter the group led by citizen 6;
* both citizens 5 and 7 choose enter the group led by citizen 8;
* citizen 5 chooses enter the group led by citizen 6 and citizen 7 chooses enter the group led by citizen 8;
* citizen 5 chooses enter the group led by citizen 8 and citizen 7 chooses enter the group led by citizen 6.

Input
-----

The single input line consists only of the positive integers **A**, **B** and **N** (**A** â¤ **B**; **B**, **N** â¤ 107).

Output
------

Output a line containing a single value which represents the number of possibilities for the formation of the groups. As this number can be very large, print only the remainder it leaves when divided by 109 + 7.


| Input Samples | Output Samples |
| --- | --- |
| 5 8 4 | 4 |

| 1 10 2 | 4096 |

| 1 100 5 | 494092823 |

3rd UFFS *Junior* Programming Contest


# Problem 1969

Descrição
----------

It is not possible yet to build a machine that allows time travel to a body made of matter. However, the physicist Asdrubal Keyla Monteiro has already developed a machine able to send messages through time, communicating with generations of the future. Theoretically it would be also possible to use this machine to send messages to generations of the past, but they would not have the technology to receive those messages. Each message is a binary sequence of a fixed length settled by the generation with which A. K. M. is communicating. The end of each message is always marked by **11**, a pattern that obviously cannot happen in any other place of the message, otherwise the message would arrive truncated at its destination. For example, if the message length settled by the generation with which A. K. M. is communicating is 6, there are 5 possibilities for the message sent to that generation:

000011      001011      010011      100011      101011

The interesting thing about this communication protocol is that, by concatenating the messages it is possible to enter a single file into the machine so that the machine sends a message to each one of a specified set of generations. For example, if A. K. M. wants to communicate with the generations registered in the machine respectively as 1, 2 and 3, and if the message lengths settled by the generations are respectively 3, 5 and 3, there are 3 possibilities for the file that can be entered into the machine:

01100011011      01101011011      01110011011

The machine developed by A. K. M. only sends messages. For now, it is not possible to receive messages from the future. The only thing possible to receive from a generation of the future is the message length information. Often the generations update this value, and A. K. M. needs to be alert.

Input
-----

The first input line consists of two integers, **G** e **E** (1 â¤ **G**, **E** â¤ 105), which represent respectively the number of generations registered in the machine and the number of events described in the input. The generations are identified in the input by the integers from 1 to **G**. The second input line consists of **G** integers, in a way that the **i**th integer, **Ci** (2 â¤ **Ci** â¤ 1010, 1 â¤ **i** â¤ **G**), represents the message length settled by the generation **i**. Each one of the **E** lines following represents an event and follows one of formats below:

| **-> A B** | indicates that A. K. M. has entered a file into the machine to send a message to each generation from **A** to **B** (1 â¤ **A**, **B** â¤ **G**); |
| --- | --- |
| **<- A C** | indicates that the message length settled by the generation **A** must be updated to **C** (1 â¤ **A** â¤ **G**, 2 â¤ **C** â¤ 1010). |

Output
------

For each event of the form **-> A B**, output a line containing a value that represents the number of the possibilities for the file entered into the machine. After processing all events, output an extra line containing a value that represents the number of possibilities for the file which A. K. M. would enter into the machine if he wanted to send a message for all the **G** generations. As the numbers of possibilities represented in each output line can be very large, output only the remainder they leave when divided by 109 + 7.


| Input Sample | Output Sample |
| --- | --- |
| 3 6 3 5 3 -> 1 3 <- 1 4 -> 2 3 <- 3 6 -> 1 2 -> 1 3 | 3 3 6 30 30 |

3rd UFFS *Junior* Programming Contest


# Problem 1981

Descrição
----------

Now you've ever helped Gabriel with the first data required for your logic game, he needs your help again.  

This time he needs that your program can handle cases where words can has repeated letters.

Input
-----

The input consists of several test cases. Each test case will have a single line with an word **S** (1 â¤ **S** â¤ 10000), composed only with characters from 'a' and 'z'. The entry ends when **S** = 0 and should not be processed.

Output
------

For each test case you should print how many different anagrams are possible to be formed with the informed characters. As the numbers can be large, print the response module 100000007.


| Input Sample | Output Sample |
| --- | --- |
| abc abcde abcdefg aabb 0 | 6 120 5040 6 |

Contest BalÃµes na Serra


# Problem 1989

Descrição
----------

A young couple uses to make their time as productive as possible. This activity is quite stressful, so they decided to "waste" some time watching their favorite TV series.

The series has **N** seasons, and each season has a possibly different number of chapters according to its success, actors availability, production time and other external factors. Each chapter has a duration of exactly **M** minutes.

To keep up with the plot, before watching each new season, they watch, without any rest, all the chapters of all the previous seasons. This has just made them concern about how much time they will be spending with this hobby, which should keep them calm. They need your help so they don't get back to the stressful situation they had.

Input
-----

The input contains several test cases. Each test case is described in two lines. The first line has two integers **N** and **M** representing respectively how many seasons the series has and the duration in minutes of each chapter (1 <= **N** <= 105, 1 <= **M** <= 106). The next line has **N** integers **C\_i** representing how many chapters each season has sorted chronologically. (1 <= **C\_i** <= 100 for 1 <= **i** <= **N**). The last line of the input contains the number -1 twice and should not be processed as a test case.

Output
------

For each test case output a single line with an integer representing the number of minutes the couple spends in watching the whole series.


| Input Sample | Output Sample |
| --- | --- |
| 6 20 24 23 15 22 24 17 1 100 100 10 1000000 99 99 99 99 99 99 99 99 99 99 -1 -1 | 9000 10000 5445000000 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2011


# Problem 1990

Descrição
----------

The mean and the median usually confuse the students because of their similar spelling, but they are quite different concepts. In this problem we are going to work with the mean and the median of a set consisting of **N** pairwise distinct integers, where **N** is odd. The mean of such set is defined, as usual, as the sum of the numbers divided by **N**, while the median is the unique element in the set that is greater than (**N**-1)/2 of its elements, and less than the other (**N**-1)/2 elements in the set. For instance, if the set is {0, 2, 6, 4, 13}, then the mean is 5 while the median is 4.

We aim to make student's lives easier by generating "balanced" sets, that is, sets consisting of an odd number of pairwise distinct integers where the mean and the median coincide. For example, the set {0, 2, 6, 4, -2} is balanced, since it has **N**=5 different integers, and the mean and the median are both equal to 2.

The following procedure has been suggested in order to obtain balanced sets. A set with an even number of distinct integers is chosen, and an extra integer distinct from every element in the set is added to it, in such a way that the resulting set is balanced. We want you to check if the given procedure works. Therefore your task is, given **N**-1 distinct integers, with odd **N**, count the number of balanced sets that can be formed by following the described procedure.

Input
-----

The input contains several test cases. Each test case is described with two lines. The first line contains a single odd positive integer **N** that indicates the number of elements the balanced set must have (3 <= **N** <= 499). The second line contains **N**-1 distinct integers **Z\_i** that represent the given elements of the set (-1014<= **Z\_i** <= 1014 for 1 <= **i** <= **N**-1). The last line of the input contains the number -1, and should not be processed as a test case.

Output
------

For each test case, output line by line with an integer representing the total number of different balanced sets that can be obtained by adding an integer to the given set, as explained in the problem description.


| Input Sample | Output Sample |
| --- | --- |
| 5 0 2 6 4 7 1 2 3 4 5 8 3 -100000000000000 100000000000000 -1 | 3 1 3 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2011


# Problem 1992

Descrição
----------

Gabriela drives a school bus. Being one of the few women who have that job, she is always mocked by the male drivers. To improve her status, she decided that besides driving responsibly she is going to drive more efficiently. Her idea is to finish her route spending as little time as possible, without violating any traffic rule.

The bus Gabriela drives has a very modern driving system that allows her to adjust the acceleration to any real number instantly. Hence, the acceleration is constant by intervals, jumping to another acceleration whenever Gabriela decides so. If *v* is the bus' speed at a given instant of time, and *a* its acceleration that remains constant over a period of time *t*, then the speed at the end of that period will be *v + at*. Moreover, the bus will move a distance of *at2/2 + vt* during that period of time.

The traffic rules prevent vehicles from using an acceleration greater than **A**, or a deceleration less than **D**, i.e. the acceleration *a* at any time must satisfy -**D** <= *a* <= **A**. Moreover, there are check points along the route of the bus where the speed must lie within a certain given interval.

Gabriela knows in advance the location of the check points, the total length of the route, and the constants **A** and **D**. At the beginning of the route the speed and acceleration of the bus are both 0. There are no additional restrictions regarding the speed or the acceleration the bus must have at the end of the route (in particular, it is not necessary to stop in the end). Your job is to use this data to determine the minimum time that Gabriela needs in order to finish the route without violating the rules.

Input
-----

The input contains several test cases. Each test case is described using several lines. The first line of each test case contains four integers **N**, **L**, **A** and **D**. **N** represents the total number of check points that are present in Gabriela's route (1 <= **N** <= 105). **L** indicates the length of the route in meters (2 <= **L** <= 107). **A** and **D** represent, respectively, the maximum allowed acceleration and deceleration for the bus (1 <= **A**, **D** <= 100). Each of the following **N** lines describe a different check point using three integers **X**, **V** and **W** that represent, respectively, the distance between the check point and the starting point of the route (1 <= **X**<= **L**-1),
the minimum speed, and the maximum speed allowed for the bus at the time it passes by that check point (1 <= **V**, **W** <= 100). Assume that in each test case the check points are given in ascending order of distance from the start point of the route, and no two check points are at the same distance from the start point. In this problem, the length is expressed in m (meters), the speed in m/s, and the acceleration in m/s2. The end of the input is indicated by a line containing the number -1 four times, and should not be processed as a test case.

Output
------

For each test case, output a single line containing a rational that represents the minimum time (in seconds) needed for Gabriela to finish her route without violating any traffic rule, or an asterisk if it is impossible to do that. Round the answer to the nearest rational with two decimal digits. In case of a tie, round up. Print exactly two digits after the decimal point, even if that means ending the number with 0's.


| Input Sample | Output Sample |
| --- | --- |
| 1 40 10 1 20 21 21 1 40 10 5 20 20 20 1 20 10 50 10 14 15 5 1000 2 5 400 30 80 600 35 50 700 10 30 900 30 40 950 10 30 -1 -1 -1 -1 | \* 2.83 2.00 35.96 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2011


# Problem 1995

Descrição
----------

The Modern Club Association organizes every year a tournament of CompuTenis, which is a sport specially adapted to a public without any mensurable physical qualities. The rules of CompuTenis are very complex (suffices to say that they involve coding with your elbow glued to your ear), but fortunately it is not necessary to know them in detail to solve this problem. You just need to know that in a CompuTenis match two players oppose each other, and the match is won by the player that first wins **S** sets; in turn, each set is composed of several games, and to win a set a player must win at least **J** games, with a difference of at least **D** more games won than the opponent.

The tournament has **K** rounds, and there are **N** = 2**K** players in it, who all participate in the first round. In each round each of the remaining participating players is paired with another participating player, in order to play a single match. The winning player of each of these matches advances to the next round, whereas the losing player is automatically disqualified from the tournament. The winner of the only match of round **K** is thus the winner of the tournament.

It is desirable to make the tournament as long as possible, considering that the matches are broadcast on television and the Association is paid for every minute on air. Given any pair of different players, the Association knows the probability for one of them to win a game against the other. You are a member of the organizing committee, and your task is to prepare the fixture for the matches of each round in order to maximize the expected number of games played in the tournament. Doing this involves deciding which pairs of players will play a match in the first round, and then for each of the following rounds deciding which pair of matches from the previous round will provide the winning players for each match in that round. Note that this can only depend on the identification of the matches in the previous round. The following figure shows a possible fixture for **K** = 3 rounds and **N** = 23 = 8 players.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1995_en.png)

For the moment, the Association only wants to estimate their earnings, so it is sufficient to tell them the maximum expected number of games that can be played in the tournament.

Input
-----

The input contains several test cases. Each test case is described using several lines. The first line contains four integer numbers, **K**, **S**, **J** and **D**. The value **K** denotes the number of rounds in the tournament (1 <= **K**<= 3). The value **S** denotes the number of sets that a player must win to win a match (1 <= **S** <= 10). The value **J** denotes the minimum number of games that a player must win in order to win a set, whereas **D**indicates that a player should win **D** more games than its opponent for him to win the set (1 <= **D** <= **J** <= 100). The players are identified by different integer numbers from 1 to **N** = 2**K**. Each of the following **N** lines contains **N** values.

In the **i**-th line, the **j**-th value is an integer number **P\_ij** such that **p\_ij** = **P\_ij**/100 is the probability that player number **i** wins a game against player number **j** (0 <= **P\_ij** <= 100 for 1 <= **i**, **j** <= **N**). You may assume that **P\_ii** = 0 (no player opposes himself) and that **P\_ij** + **P\_ji** = 100 for **i** and **j** different.

The end of the input is denoted by a line containing four times the number -1.

Output
------

For each test case, you should print a line containing a rational number representing the maximum expected number of games that the given tournament can have. The result should be rounded to the nearest rational number with 2 decimal digits. In case of ties, round up. Note that you should always print 2 digits after the dot, even if this means ending with a zero.


| Input Sample | Output Sample |
| --- | --- |
| 1 1 2 2 0 50 50 0 3 3 6 2 0 88 2 76 71 24 50 4 12 0 54 37 84 95 88 98 98 46 0 66 36 13 33 33 24 63 34 0 29 21 96 63 29 16 64 71 0 0 47 13 76 5 87 79 100 0 56 89 50 12 67 4 53 44 0 23 96 2 67 37 87 11 77 0 -1 -1 -1 -1 | 4.00 224.08 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2011


# Problem 1999

Descrição
----------

Every year the kingdoms of Cubiconia, Quadradonia and Nlogonia organize a ball to commemorate the end of the war that ravaged the region for many years. A certain number of noblemen of each kingdom is invited to participate in this event, and it is expected that every pair of guests coming from different kingdoms will dance together exactly once. That is, each of the guests from Cubiconia shall dance once with every guest from Quadradonia and Nlogonia; in turn, each of the guests from ;Quadradonia shall also dance once with every guest from Nlogonia. However, guests coming from the same kingdom are not allowed to dance with one another.

To help organize the ball, the total number of dances that will take place is determined beforehand, so that care must be taken when choosing the number of noblemen that shall be invited from each kingdom. For example, if it is decided that the ball must have N = 20 dances, one possibility is to invite 6 noblemen from Cubiconia, 2 from Quadradonia and 1 from Nlogonia, which can be represented by the expression(6, 2, 1). This is a valid option because the total number of dances would then be 6\*2 +6\*1+ 2\*1 = 20.

Traditions whose origins nobody can now remember indicate that the number of invited noblemen from Cubiconia must be greater or equal to the number of those coming from Quadradonia, and at the same time the number of invited noblemen from Quadradonia must be greater or equal to those coming from Nlogonia. Thus, for N = 20 dances there are exactly 5 possible ways to choose the number of guests from each kingdom, namely (5, 4, 0),(4, 2, 2), (10, 2, 0) and (20, 1, 0) as well as the aforementioned (6, 2, 1).

With so many restrictions, the organizing committee has problems finding the ideal way to choose the number of guests from each kingdom. Your task is to help this committee by counting the different ways in which the number of guests can be chosen for a ball with N dances. Two of these ways are considered different if they differ in the number of invited noblemen from at least on of the three kingdoms.

Input
-----

Each test case is described using a single line, containing an integer N representing the total number of dances that the ball must have (1 â¤ N â¤ 104). The end of the input is signalled by a line containing the number -1.

Output
------

For each test case, print a single line containing the number of different ways in which the number of guests from each kingdom can be chosen in order to have a ball where there are exactly N dances, with all the restrictions mentioned in the problem statement.


| Input Sample | Output Sample |
| --- | --- |
| 20 1 9747 -1 | 5 1 57 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2012


# Problem 2001

Descrição
----------

Bile is a smart kid who likes quite recurrences. He was participating in a competition in which the best sequence wins a prize. Bile created a sequence *F*, in the sequence, the first *N* values are known, and to discover the value of *F**k* for a *K* *N* is used to formulate below.

For *N* *K*: *F**K* = 1\**F**K*-1 + 2\**F**K*-2 + ... + *N*\**F**K-N*

But he does not know calculate quickly the values of their sequence and asked for your help.

  

In the first test case: *N* = 2, *K* = 3, *F*1 = 2, *F*2 = 5, *F*3 = *F*2 + 2\**F*1 = 9, *F*4 = *F*3 + 2\**F*2 = 19 ...

Input
-----

The input consists of several test cases. Each test case consists of two lines. The first line of each test case contains two integers, **N** ( 2 â¤ **N** â¤ 100 ) and **K** ( **N** â¤ **K** â¤ 1018 ), representing the number of values of the first known sequence Bile. The second line consists of **N** integers **F**i ( **F**1, **F**2, â¦ ,**F****N** ) and ( 0 â¤ **F****i** â¤ 1010 ) representing the values initially known. The entry ends with the final file (EOF).

Output
------

For each test case you should to print the value **F****K** and the sum of all elements of bile function minor or equal to **F****K**, separated by a single space. Your answers should be submitted in module 303700049.


| Input Sample | Output Sample |
| --- | --- |
| 2 3 2 5 5 6 1 2 3 4 5 | 9 16 35 50 |

OlimpÃ­ada Cearense de InformÃ¡tica - 2015


# Problem 2007

Descrição
----------

At the early age of 40, Alice and Bob decided to retire. After more than two decades working as examples for networking protocols, game theoretical books and several other texts, they were tired. To remain active, they decided to get into gardening.  

  

Alice and Bob planted several vegetable plants in a huge field. After finishing, they realized that their plants needed protection from wild animals, so they decided to build a fence around them. The field is represented as the XY plane, and each vegetable plant as a different point in it. A fence is represented as a polygon in the plane. However, not every polygon is a valid fence. The fence needs to be a single simple polygon with each of its sides parallel to one of the axes. Of course, the polygon should contain all the points representing vegetable plants. A fence too close to the plants or to itself could make it difficult to walk around, so each side of the polygon needs to be away from all plants and all non-adjacent sides.  

  

Unfortunately, Alice and Bob subcontracted the construction of the fence to a nasty multinational. The company had a lot of lawyers on payroll, but no good fence designers, so they failed to comply to all requirements. They built a fence which is a simple polygon with sides parallel to the axes and whose sides are away from plants and itself. However, they forgot to make the fence contain all the plants!  

  

Alice and Bob want to assess the extent of the problem. Since not all plants are equally valuable to them, they want to know the total value of the plants that were left outside the fence

Input
-----

The first line contains two integers **P** and **V** , representing respectively the number of plants and the number of vertices of the polygonal fence (1 â¤ **P, V** â¤ 105 ). Each of the next **P** lines describes a different plant with two integers **Xp** and **Yp**, indicating the coordinates of the plant (â109 â¤ **Xp, Yp** â¤ 109 ). The value of the **p**-th plant in the input is p, for **p** = 1, 2, . . . , **P**. Each of the next V lines describes a vertex of the fence with two integers **Xv** and **Yv**, indicating the coordinates of the vertex (â109 â¤ **Xv, Yv** â¤ 109). Vertices are given in counter clockwise order. Each of these points is an actual vertex of the polygon, that is, it is not collinear with its two
adjacent vertices. The represented polygon is a simple polygon with each side parallel to an axis. No two plants are in the same position, and no plant lies on a fenceâs side.

Output
------

Output a line with an integer representing the sum of the values of all the plants that lie outside the fence.


| Input Samples | Output Samples |
| --- | --- |
| 4 8 1 2 1 0 5 3 3 4 0 1 6 1 6 4 4 4 4 3 2 3 2 5 0 5 | 6 |

| 6 12 6 5 1 9 3 6 3 4 2 0 4 4 5 8 5 3 2 3 2 5 4 5 4 7 0 7 0 1 7 1 7 10 0 10 0 8 | 15 |

| 1 4 1 1 2 0 2 2 0 2 0 0 | 0 |

ICPC Latin American Regional â 2015


# Problem 2033

Descrição
----------

Where can, Danilo purchase accessories for your computer because it works as a programmer and always seeks to improve the performance of your PC. Once Danilo resolved to do a general upgrade on your computer, but as I was without money at the time, he decided to request a loan on money with his friend Maclaud that is moneylender. Maclaud then decided to borrow the money to his friend Danilo and advised him to find what would be its debt if the regime were applied "Simple Interest" or "Interest Compound" since it would know that the moneylender would not increase the value.

Danilo got confused and decided to go to your house and calculate what would be the final values according to each interest regime. But Daniel is not very good calculation and decided to ask the help of a programmer who was able to create a program that informed the loan amount, the interest rate "monthly" and the term "months" you need to repay the loan with interest, calculate and show:

- The Difference between the final value with simple interest and the final amount with compound interest;

- The Difference between the amount to be borrowed and the final value with simple interest;

- The Difference between the amount to be borrowed and the final amount with compound interest;

Input
-----

The input consists of several test cases and ends with EOF. Each case contains two floating point values of double precision, a **C** (0.01 â¤ **C** â¤ 20000.00) and other **i** (0.01 â¤ **i** â¤ 1.00), representing, respectively, the loan amount and the interest rate, and an integer n (1 â¤ **n** â¤ 20) representing the amount of "months" concerning the deadline for payment of the loan to the moneylender, as with the applied interest.

Output
------

In each case, the output is composed of three lines. The first contains the "DIFERENCA DE VALOR = " message, followed by the value of the difference between the final value with simple interest and the final amount with compound interest. In the second line will display the "JUROS SIMPLES = " message, followed by the value of the difference between the amount to be borrowed and the final value with simple interest. And the third line will show the message "JUROS COMPOSTO = " followed by the value of the difference between the amount to be borrowed and the final amount with compound interest.

- Not sure to put the spaces in the messages and by a line break at the end of each trip.


| Input Sample | Output Sample |
| --- | --- |
| 200.00  0.06  6  3520.50  0.13  8  10000.00  1.00  9 | DIFERENCA DE VALOR = 11.70 JUROS SIMPLES = 72.00 JUROS COMPOSTO = 83.70  DIFERENCA DE VALOR = 2177.23 JUROS SIMPLES = 3661.32 JUROS COMPOSTO = 5838.55  DIFERENCA DE VALOR = 5020000.00 JUROS SIMPLES = 90000.00 JUROS COMPOSTO = 5110000.00 |

Dedicated to my friends (Nivaldo, L.C.Junior, Danilo, L.Eduardo, Anderson, MoisÃ©s, Jonas, Eduardo, David, Bruno, Emanuel, AriÃ©lio, Henrique, Allan, Enock, Werner) from GTI UNIPÃ 2015.


# Problem 2034

Descrição
----------

The mathematician Georg Cantor was a lover of both sets and infinity, but he didn't get along too well with his colleagues. One morning he woke up with the idea of defining a set so strange that, when made public, would make the rest of the mathematicians lose their sleep for several days. And he was successful.

The set he defined is called the Cantor set, and it is formed by all the real numbers in the interval [0, 1]whose decimal expression in base 3 uses exclusively the digits 0 and 2. This set has amazing properties, which we will not mention here so that you can sleep tonight. Moreover, and luckily for everyone involved, in this problem we will not be working with the Cantor set, but with a generalization of this set to the integer numbers.

We will say that an integer number is of Cantor type, or a cantiger for short, if its expression in a given base B uses solely the digits in a given set C contained in {0, 1, ..., B-1}. Thus, the fact that a given number is a cantiger depends on how we choose B and C.

Your task is to count cantiger numbers, in order to prevent the mathematicians of the entire world from loosing their sleep. More precisely, given two integers D and H, along with B and C, you have to count the number of cantigers with respect to B and C from D to H inclusive.

Input
-----

Each test case is described using a single line. This line contains three integers, D, H and B, and a string L. The values of D and H indicate the endpoints of the closed interval [D, H] we are interested in (1 â¤ D â¤ H â¤ 1016). The value of B is the base mentioned in the problem statement (2 â¤ B â¤ 10). The stringL = L0 L1 ... LB-1 has exactly B characters, and describes the set C also mentioned in the problem statement. The character Li is the uppercase letter 'S' if i is in C, and the uppercase letter 'N' otherwise (i = 0, 1, ..., B-1). The set C is non-empty, so that there is at least one 'S' character in L. The end of the input is signalled by a line containing three times the number -1 and a single '\*' character.

Output
------

For each test case, you should print a single line containing an integer number, representing the number of cantigers (with respect to B and C) that are greater or equal to D and lower or equal to H.


| Input Sample | Output Sample |
| --- | --- |
| 1 10 3 SNS  99 999 5 NSSNS  1110 1111 10 NSNNNNNNNN  1 10000000000000000 10 NNNNNSNNNN  1 10000000000000000 7 SSSSSSS  -1 -1 -1 \* | 3  144  1  16  10000000000000000 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2012


# Problem 2044

Descrição
----------

Ignacio and Ines really like science. Luckily they live in Nlogonia, where as everyone knows there are Nscience museums. Both Ignacio and Ines have the next N Saturdays free, so they have agreed on a schedule to visit a different science museum each of these days.

Ignacio is quite stingy, so every Saturday he will tell Ines that he has forgotten to bring the money to pay the museum's entrance fee, and will therefore ask her to pay for him. Ines always does so, and because she knows him well she also knows that unless she asks for her money back, he will never pay up. In fact, Ines is certain that even if she asks Ignacio for her money back, he will only accept to pay if the cumulative debt is a multiple of 100, because otherwise he will argue that he has no change to pay exactly, and will thus pay nothing at all.

This being the situation, every Sunday if the cumulative debt is a multiple of 100 Ines will go to Ignacio's house to claim her money, and because he'll have no excuse left, he will pay without any type of protest. Of course he doesn't like this, but he is comforted by the idea that if the cumulative debt after visiting theN museums is not a multiple of 100, Ines shall not claim the last part of her money.

Ines would like to know how many times she will have to go to Ignacio's house to ask for her money. In order to calculate this, she can provide a list of the prices of the entrance fees to the N science museums in Nlogonia, in the order that she and Ignacio are going to visit them.

Input
-----

Each test case is described using two lines. The first line contains a single integer number N, indicating the number of science museums in Nlogonia (1 â¤ N â¤ 100). The second line contains N integers Pirepresenting the prices of the entrance fees to the different museums, in the order in which they are going to be visited (1 â¤ Pi â¤ 100 for i = 1, ..., N). The end of the input is signalled by a line containing the number -1.

Output
------

For each test case, you should print a single line containing an integer number, representing the number of times Ines is going to have to go by Ignacio's house to ask for her money.


| Input Sample | Output Sample |
| --- | --- |
| 3  50 50 50  5  50 100 100 100 100  9  25 50 75 100 25 50 75 100 25  5  35 45 20 22 33  3  100 100 100  -1 | 1  0  2  1  3 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2012


# Problem 2063

Descrição
----------

Diglett is a PokÃ©mon type of land that is digging underground tunnels and is almost never seen. It appears on the surface through a hole in the ground time to time, where you can view only his head.

![Digglets](https://resources.beecrowd.com/gallery/images/problems/UOJ_2063.png)

The tunnels built by them are unidirectional and always connect an origin hole to a destination hole, for example: if there is a tunnel connecting the hole **A** to the hole **B**, then it is possible to go from **A** to **B** and not the opposite. Each Diglett has its own hole, which indicates that there **N** holes will be **N** Digletts. Each hole has exactly two tunnels: the first tunnel, which runs from it to another hole and the second tunnel, which comes to him from another hole.

The Digletts are walking from hole to hole every moment of time, for example: consider a hole **A** that has a tunnel that connects to a hole **B**, if one Diglett in the hole **A** at time **T**, then the next moment of time **T**+1 it will be in the hole **B**. When a Diglett arrives at his hole, it appears immediately on the surface. When not in his hole, it just remains underground and waiting for the next moment of time to walk the tunnel and go to another hole. It is guaranteed that each Diglett always returns to its hole in a moment of time.

Xisto is a PokÃ©mom Master and is looking to capture the greatest amount of Digletts with only a pokeball, this in turn is able to capture all visible Digletts in a given area. He needs your help to know what is the shortest time in which all Digletts will appear on the surface at the same time, so he could throw the pokeball and catch them all.

***Note**: At time zero Digletts are all in their respective hole and does not appear on the surface.*

Input
-----

The first row contains an integer **N** (2 â¤ **N** â¤ 100) representing the amount of holes. The next line contains **N** integers **Bi** (1 â¤ **Bi** â¤ **N**), where the ***i**-th* integer representing the***i**-th* hole, and indicates a unidirectional tunnel ***i-**th* hole to **Bi** hole.

Output
------

Print the shortest time in which all Digletts will appear together on the surface.


| Input Samples | Output Samples |
| --- | --- |
| 2  2 1 | 2 |

| 4  4 3 2 1 | 2 |

| 6  2 1 5 3 6 4 | 4 |

Aquecimento para a OBI 2016


# Problem 2066

Descrição
----------

A *reverse number* of a natural number **N** is the number which we obtain when we read the digits of **N** from the right to the left. For example, the reverse number of 1234 is 4321 and the reverse number of 150 (a number with 3 digits) is 51 (a number with 2 digits). In this problem, we say that a number is *well-reversible* if it is strictly less than its reverse number. Examples of well-reversible numbers are 1234, 15 and 819.

Input
-----

The single line of the input consists of a single positive integer **K** (**K** â¤ 18).

Output
------

The single line of the output shall consist singly of the number of numbers with exact **K** digits which are well-reversible.


| Input Samples | Output Samples |
| --- | --- |
| 1 | 0 |

| 2 | 36 |

| 18 | 404999999550000000 |

Aquecimento para a OBI 2016


# Problem 2068

Descrição
----------

Taynder is a very popular app. This app is used to meet new people, have relationships and set up dates. It was on Taynder that Mel and Tob met.

Mel and Tob already chatted for more than 40 minutes, so they think it's time to know each other in person, they set up a date in the city main square. The only problem is that they didn't define a exact time to the meeting, they only know the time interval that they are supposed to meet, but they don't know when the other will arrive. So who gets there first waits a predefined time, but if no one arrives the person goes home to meet someone else in Taynder.

An example: if Mel and Tob will meet in the real interval [16h, 17h] with maximum wait time equals to 15 minutes, it means that Mel and Tob can arrive at any time between 16h and 17h (including 16h and 17h), and who gets there first, in the time x for instance, will wait for the other person in the time interval defined by [x, x + 15].

Your work is to write a program that, given the time interval of the meeting and the maximum wait time, determines the probability that they'll meet.

Input
-----

Each test case is an unique line with 3 integers: **t1**, **t2**, **N**.

**t1**and **t2** represent the real time interval in hours such that **t2** > **t1** and 1 â¤ **t1**, **t2** â¤ 10â¶, **N** represents the maximum wait time in minutes such that 1 â¤ **N** â¤ (**t2**-**t1**)\*60.

Output
------

The output must be the probability of the date happens in the format **a**/**b**, such that **a**/**b** is an irreducible fraction.


| Input Samples | Output Samples |
| --- | --- |
| 1 2 15 | 7/16 |

| 1 2 60 | 1/1 |

Aquecimento para a OBI 2016


# Problem 2069

Descrição
----------

InÃªs Venezuela has decided to record on CD the videos she sent to *GranHermano* TV show, one video per CD. After putting each CD in a small square box, she realised that it was possible to organise the CDs in a manner that they would perfectly cover a square table of hers and no CD would be put over another CD.

Ana and Bob are two friends who are big fans of InÃªs Venezuela. They have also sent many videos to *GranHermano* and also recorded their videos on CDs, one video per CD. However, differently from Panterona (as Brazilians usually call InÃªs Venezuela), they want to organise their videos in knapsacks in a way that:

* in each knapsack there are only CDs either from Ana or from Bob;
* the number **N** of CDs in every knapsack is always the same.

They realised that there is not necessarily one possibility for the value of **N**, but, for all the possibilities of values for **N**, it would be also possible to organise all the InÃªs Venezuela's CDs in knapsacks in a way that in each knapsack there would be exactly **N** InÃªs Venezuela's CDs.

Knowing how many videos Ana and Bob have sent to *GranHermano* each, and knowing that the length of the side of each square box used by InÃªs Venezuela is 1 centimetre, calculate the length of the side of InÃªs Venezuela's square table.

Input
-----

The input consists only of two positive integers **A** and **B** (**A**, **B** â¤ 109), which respectively represent the number of Ana's CDs and the number of Bob's CDs.

Output
------

Print how many centimetres long is the side of the Internet Queen's square table. If there is more than one possible answer, print the smallest.


| Input Samples | Output Samples |
| --- | --- |
| 18 24 | 6 |

| 60 140 | 10 |

| 588 420 | 42 |

Aquecimento para a OBI 2016


# Problem 2076

Descrição
----------

Tjalling C. Koopmans won the Nobel Prize in economy in 1975 with the Russian mathematic Kantorovich for their contributions in important areas like the great allocation of resources. Koopmans was graduated in mathematic for the university of Utrcht, in Netherland, and specialized himself in mathematic economy. Throughout the Second World War he was involved in the study of the great allocation of resources, which 30 years later gave him the Nobel Prize. He is considering one of the pioneers in the linear theory program. His contribution has important applications in economy, mathematic, physics and in chemistry.

One of Koopmans' favorite problems were the great allocation of commodities. In this problem, is given an initial value and a final value of the application to be done. Although, not all the values can be applied in several investments. Each investment is defined through the integer number, and for convention, can be applied only when the value to be applied is a multiple at least of one number that defines an investment.

Your work in this problem is calculating the maximum value that can be applied. So, given the list of integer that defines the multiple applications and the initial value and in the final value to be applied, you may calculate the sum of the values that can be applied in the interval.

Input
-----

The input is composed of several instances. The first input line contains an integer **T** indicating the number of instances.

The first line of each instance has three integers **I**, **F** and **N** (1 < **I** < **F** < 1000000000 and 1 < **N** < 20) that represents the initial value, final value and the number of the elements in the application list. The next line contains **N** integers 1 < **ai** < 10000000000 indicating the list of applications.

Output
------

For each instance print a line containing the sum of values that can be apply in the break. This value can be too big so print the model result 1300031.


| Sample Input | Sample Output |
| --- | --- |
| 3 1 10 1 1 1 9 2 3 5 1 999 2 3 5 | 55 23 233168 |

XII Maratona de ProgramaÃ§Ã£o IME-USP, 2008


# Problem 2084

Descrição
----------

Right now presidential elections are being held in Nlogonia. For a candidate to win in the first round, he should obtain more votes than each of the other candidates. But that is not enough: he should also obtain at least 45% of all the votes, or at least 40% of all the votes and at least 10% more votes than each of the other candidates. This 10% has to be calculated from all votes. If no candidate wins in the first round, a new election is held as a second round.

Benicio is a political journalist in Nlogonia, and he always wants to scoop everyone else. This is why he has collected information from polls, and wants to know if according to these one of the candidates will win in the first round, or on the contrary there will be a second round. Benicio needs to decide this with haste, before someone else scoops him. Can you help him?

Input
-----

The first line contains an integer number **N**, representing the number of candidates (2 â¤ **N** â¤ 10). The second line contains Ninteger numbers **Vi** representing the amount of votes obtained by each of the candidates (0 â¤ **Vi** â¤ 1000 for **i** = 1, ..., **N**). At least one candidate obtained at least one vote, and there are no two candidates with the same number of votes.

Output
------

Print a line containing a single digit, indicating if there is a winner in the first round or not. If there is such a first round winner, the digit must be a '1'; otherwise (i.e. if there should be a second round) the digit must be '2'.


| Input Samples | Output Samples |
| --- | --- |
| 2  60 40 | 1 |

| 3  16 28 21 | 1 |

| 3  42 23 35 | 2 |

Torneo Argentino de ProgramaciÃ³n â ACMâICPC 2013


