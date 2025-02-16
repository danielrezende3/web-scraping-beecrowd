# Problem 3029

Descrição
----------

We are definitely not going to bother you with another generic story when Alice finds about an array or  

when Alice and Bob play some stupid game. This time youâll get a simple, plain text.

First, let us define several things. We define function **F** on the array **A** such that **F**(**i**, 1) = **A**[**i**] and  

F (i, m) = A[F (**i**, **m** â 1)] for **m** > 1. In other words, value **F** (**i**, **m**) represents composition **A**[...**A**[**i**]]  

applied **m** times.

You are given an array of length **N** with non-negative integers. You are expected to give an answer on **Q** queries. Each query consists of two numbers â **m** and **y**. For each query determine how many **x** exist such that **F**(**x**, **m**) = **y**.

Input
-----

The first line contains one integer **N** (1 â¤ **N** â¤ 2 Â· 105 ) â the size of the array **A**. The next line contains **N** non-negative integers â the array **A** itself (1 â¤ **Ai** â¤ **N** ). The next line contains one integer **Q** (1 â¤ **Q** â¤ 105 ) â the number of queries. Each of the next **Q** lines contain two integers m and **y** (1 â¤ **m** â¤ 1018 , 1 â¤ **y** â¤ **N** ).

Output
------

Output exactly **Q** lines with a single integer in each that represent the solution. Output the solutions in the order the queries were asked in.


| Input Sample | Output Sample |
| --- | --- |
| 10 2 3 1 5 6 4 2 10 7 7 5 10 1 5 7 10 6 1 1 10 8 | 3 0 1 1 0 |

Bubble Cup 2019


# Problem 3036

Descrição
----------

Some students of the Federal University of ViÃ§osa walk in the campus wearing a red shirt with the sentence: "This shirt is blue if you run fast enough". Tereu, one of the fastests students of the college, was shocked by the sentence written on the shirt and asked his teacher how the shirt could change its color. The professor said that an object can reflect the light in diffrent wavelengths and each wavelength is related to a color in the visible light, thus, let \(\lambda\) be this wavelength, the color will the determinated according with the following list:

* \(\lambda\) \(<\) \(400 nm\): invisivel (invisible)
* \(400 nm\) \(\leq\) \(\lambda \) \(<\) \(425 nm\): violeta (violet)
* \(425 nm\) \(\leq\) \(\lambda \) \(<\) \(445 nm\): anil (indigo)
* \(445 nm\) \(\leq\) \(\lambda \) \(<\) \(500 nm\): azul (blue)
* \(500 nm\) \(\leq\) \(\lambda \) \(<\) \(575 nm\): verde (green)
* \(575 nm\) \(\leq\) \(\lambda \) \(<\) \(585 nm\): amarelo (yellow)
* \(585 nm\) \(\leq\) \(\lambda \) \(<\) \(620 nm\): laranja (orange)
* \(620 nm\) \(\leq\) \(\lambda \) \(<\) \(750 nm\): vermelho (red)
* \(\lambda \geq\) \(750 nm\): invisivel (invisible)

The words between the parentheses are the translates of the colors in portuguese, but it cannot be printed on the output, which has to present the words in portuguese.

The change of the color happens because when an observer moves, it sees a wavelength \(\lambda'\), which is diffrent from the \(\lambda\) real one. This phenomenon is called "Doppler Effect" and it's matematically explained by the formula (it works when we consider positive the velocity when the observer approaches the source):

\({\lambda' - \lambda\over\lambda} = \sqrt{c - v\over{c + v}} -1 \)

\(v\) is the speed of the observer and \(c\) is the speed of light in the vacuum.

The shirt is red and it reflects the light in the wavelength \(\lambda = 700 nm\), the speed of light in the vacuum is \(c = 3\times10^8 m/s\).

Tereu would see the shirt in a wavelenght \(\lambda' = 495 nm\), that is, blue, if he reached a speed close of \(10^8 m/s\). He knows he is not able to reach this velocity, then, he wants you to create a program which returns the color he would see if he was in a speed **V**.

Input
-----

The input has only a integer number  **V**(\(-3\times10^8 < \) **V**\(< 3\times10^8\)), which represents the speed of Tereu in m/s.

Output
------

The output has to have the color of the shirt observed by Tereu when he runs in the velocity of the input. The color must be written in portuguese as it is in the list of the wavelengths in the visible spectrum.


| Input Samples | Output Samples |
| --- | --- |
| 100000000 | azul |

| 0 | vermelho |


# Problem 3049

Descrição
----------

Se pegarmos uma nota de 100 reais e a cortarmos, usando uma tesoura, em dois pedaÃ§os, quanto vale cada um dos pedaÃ§os? A regra Ã© simples: se um dos pedaÃ§os possuir estritamente mais da metade da Ã¡rea da nota original, entÃ£o ele vale 100 reais; e o outro pedaÃ§o nÃ£o vale nada. Veja que se cada pedaÃ§o possuir exatamente metade da Ã¡rea original, entÃ£o nenhum dos dois tem valor.

Felix e Marzia decidiram fazer um corte, em linha reta, que comece no lado inferior da nota, a base, e termine no lado superior, o topo. A nota Ã© um retÃ¢ngulo de comprimento 160 centÃ­metros e altura 70 centÃ­metros, como mostrado na parte esquerda da figura abaixo. Felix sempre vai ficar com o pedaÃ§o mais Ã  esquerda da nota e Marzia com o pedaÃ§o mais Ã  direita. A parte direita da figura ilustra dois possÃ­veis cortes. No de cima, Marzia ficaria claramente com o maior pedaÃ§o, que vale 100 reais; e no de baixo, dÃ¡ para ver que Felix Ã© quem ficaria com o maior pedaÃ§o.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_3049.png)

O corte reto vai comeÃ§ar na base a uma distÃ¢ncia de **B** centÃ­metros a partir do lado esquerdo da nota; e terminar no topo a uma distÃ¢ncia de **T** centÃ­metros tambÃ©m a partir do lado esquerdo da nota. Veja a indicaÃ§Ã£o na parte direita da figura.

Neste problema, dados os valores **B** e **T**, seu programa deve computar quem vai ficar com o pedaÃ§o que vale **100** reais, ou se o valor da nota se perdeu.

Entrada
-------

A primeira linha da entrada contÃ©m um inteiro **B** (0 < **B** < 160) representando a distÃ¢ncia do ponto inicial do corte, na base, para o lado esquerdo da nota. A segunda linha da entrada contÃ©m um inteiro **T** (0 < **T** < 160) representando a distÃ¢ncia do ponto final do corte, no topo, para o lado esquerdo da nota.

SaÃ­da
------

Seu programa deve imprimir uma linha contendo um nÃºmero inteiro: 1, se Felix ficou com o pedaÃ§o que vale 100 reais; 2, se Marzia ficou com o pedaÃ§o que vale 100 reais; ou 0, se o valor da nota se perdeu.


| Exemplos de Entrada | Exemplos de SaÃ­da |
| --- | --- |
| 50  86 | 2 |

| 70  90 | 0 |

| 130  138 | 1 |

OlimpÃ­ada Brasileira de InformÃ¡tica â OBI2019 â Prog. NÃ­vel 1 â Fase Local


# Problem 3078

Descrição
----------

If you went to Goias you've certainly experienced or at least heard about the pequi. The pequi is a typical fruit from the region with some few edible seeds.

In this year ICPC (InstÃ¢ncia Competitiva do Pequi CampeÃ£o) will take place. The ICPC is a competition to determine the best pequi. To make the competition less obvious and more dynamic, the quality of a pequi with **n** seeds will be determined by a non-linear equation.

Define  ââââ***\(\textbf{b} = \textbf{n} \hspace{1mm} MOD \hspace{1mm} 257 \)***,  ***\(\textbf{c} = \textbf{n} \hspace{1mm} MOD \hspace{1mm} 193\)***  and  **\(\textbf{d} = \sqrt[22]{\textbf{b}^{16}}\*\textbf{b}^{3\over11} - \textbf{b} + 4 \)**, the equation that determines the quality of the pequi is given by  \(\textbf{x}^{\textbf{d}} + \textbf{bx}^2 + \textbf{c} = 0 \).

Based on the number of roots of the built equation, a pequi can receive one of the following grades of quality:

* "So o ouro", case the built equation has no real roots.
* "Bom", case the equation has only a real root;
* "Regular", case the equation has more than one real root.

Your task is given the quantity of seeds to discover the degree of quality of a pequi.

Input
-----

The input consist of several test cases. Each test case has a single line with an integer **n** (0 â¤ **n** â¤ 105), the quantity of seeds of the pequi.  

The last test case contains **n** = -1 and must not be processed.

Output
------

For each test case print on a separate line the degree of quality of the pequi without quotation marks ("So o ouro", "Bom" or "Regular").


| Input Sample | Output Sample |
| --- | --- |
| 0 1 -1 | Bom So o ouro |

PUC GoiÃ¡s Marathon #1


# Problem 3079

Descrição
----------

After many complaints on city hall, residents of a specific street will finally have their houses illuminated. To make it possible will be necessary to build a pole network on this street obeying the following constraints:

* any two adjacent poles have a distance ***k***between them;
* there should be at least one pole in front of each house.

The street has ***N*** houses and is considered a strait line. A house is represented by a segment of the street and a pole is said to be in front of this house if it is inside this segment. The ***i***-th house means the segment between ***Ai***  and ***Ai***+1 - 1, inclusive, where 1 â¤ ***i*** < ***N***, and the last house means the segment between ***AN*** and ***M***, inclusive.

The city mayor intends to minimize the number of poles that should be installed by maximizing the distance ***k***. Write a program that finds the biggest distance ***k*** that satisfies the above constraints.

Input
-----

The first line of the input contains two integers  ***N*** and ***M*** (2 â¤ ***N*** â¤ 103,2 â¤ ***M*** â¤ 105), which describes the number of houses and the length of the street, respectively. The second line contains ***N*** integers ***Ai***  (0 â¤ ***Ai*** < ***M***; ***Ai***  < ***Ai***+1 for all 1 â¤ ***i*** < ***N***), which represents the coordinates of the beginning of each house in the street. It is guaranteed that ***A1*** = 0.

Output
------

The output contains just one line with an integer ***k***, that means the biggest possible distance between two adjacent poles obeying the above constraints.


| Input Samples | Output Samples |
| --- | --- |
| 3 26 0 12 15 | 13 |

| 5 20 0 4 8 9 12 | 3 |

| 6 121 0 29 46 55 81 114 | 23 |

PUC GoiÃ¡s Marathon #1


# Problem 3096

Descrição
----------

Ribeiro is very fond of factorial numbers, but recently he was calculating the factorial of some numbers and was not able to arrive at the final answer, since the number that was forming was with many digits and not even his calculator was able to help him.  


The factorial of a number **N** is defined by **N**! = 1 \* 2 \* 3 \* .. \* **N**.  


As Ribeiro saw that in many cases that he would try to find the factorial would result in overflow, he was content to know how many digits the factorial of **N** has.  


Example: 5! is equal to 120, so the number of digits is 5! is 3.  


Your task is to help Ribeiro and inform how many digits there is **N**!.  


Input
-----

The entry contains an integer **N** (1 <= **N** <= 10^8) as explained the problem.  


Output
------

The output must contain the number of digits **N**!.  



| Input Samples | Output Samples |
| --- | --- |
| 5 | 3 |

| 10 | 7 |

CONTEST DE FÃRIAS IFSULDEMINAS 2020


# Problem 3099

Descrição
----------

Ribeiro, after the defeat of the Brazilian team by 7 x 1 in 2014, has serious problems with these two digits. Now every number he sees, he wants to know how many digits **1** and how many digits **7** appear in all the numbers **1** through **N**, inclusive.

He knows that you are a great programmer and will help you. To "facilitate" his life, Ribeiro said he wants to know only the sum of the number of digits **1** with the number of digits **7** that appear between all the numbers from **1** to **N**, inclusive.

For example, think of the number 11: The numbers 1 through 11 are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 11. As we can see the digit 1 appears 4 times, already the digit 7 appears only once. Therefore, the sum of the number of digits 1 and 7 is equal to 5.

You will be given an integer **N**, you must inform Ribeiro the sum of the number of digits **1** with the number of digits **7** that appear between all the numbers **1** through **N**.

Input
-----

The input contains an integer **N** (1 <= **N** <= 10 ^ 12).

Output
------

The output should show the sum of the number of digits 1 with the number of digits 7, as it explains the problem.


| Input Samples | Output Samples |
| --- | --- |
| 11 | 5 |

| 17 | 12 |

| 15725 | 18147 |

CONTEST DE FÃRIAS IFSULDEMINAS 2020


# Problem 3102

Descrição
----------

Every Dragon Ball fan knows the famous attack of the character Tenshinhan, KIKOHO. Recently Tenshi, for the intimate, went to battle with the warrior Cell. It was an epic battle, he managed to hit some attacks on Cell, but unfortunately he didn't win it. However, he was satisfied with the total area that his attack covered. Let's say that Tenshi's attack is basically a triangle, he doesn't know what area that attack came to, but he knows where the vertices of the formed triangle are.

Can you help Tenshi telling what is the total area his attack had?

See an exemple of how is his attack and how it looks like a triangle.

![](https://resources.beecrowd.com/gallery/images/contests/UOJ_3389.png)

Input
-----

The first line of entry contains an integer **N** (1 <= **N** <= 20) representing the number of test cases. The next **N** lines contain 3 pairs of coordinates in the Cartesian plane, (**X1, Y1, X2, Y2, X3, Y3**) (-700 <= **Xi, Yi** <= 1000), informing the vertices of the triangle that the attack formed after hitting the ground. The given points are guaranteed to form a triangle.

Output
------

The output should show what is the area of Tenshiâs KIKOHO, with 3 decimal places.


| Input Sample | Output Sample |
| --- | --- |
| 2  4 1 -2 3 0 -6  0 0 4 -2 6 8 | 25.000  22.000 |

CONTEST DE FÃRIAS IFSULDEMINAS 2020


# Problem 3104

Descrição
----------

John was previously settling all the questions proposed by his colleague, which made him very angry. Such a "colleague" believed that John was getting the questions right because the first number, in this case **A**, was not so big. So, he took a sheet and filled it whole, with just one number, representing **A**. As he thought it would be impossible to discover such an answer with this gigantic number, he asked one of his friends to choose a second number, this time without exaggeration, to represent **B**.

As John knows many mathematical theories, this challenge was not at all difficult for him and he found the rest of the **A** Ã· **B** division with all the precision and certainty of the world.

Your task is to report the number that John found by calculating the remainder of the division of **A** Ã· **B**, since you are the only person he told the answer to.

Input
-----

The input contains two numbers **A** (1 <= **A** <= 10 ^ 100000) and **B** (1 <= **B** <= 10 ^ 9).

Output
------

The output contains a single integer which is the remainder of the division of **A** Ã· **B**.


| Input Sample | Output Sample |
| --- | --- |
| 8  3 | 2 |

CONTEST DE FÃRIAS IFSULDEMINAS 2020


# Problem 3110

Descrição
----------

Xorshift random number generators are a class of pseudorandom number generators that were discovered by George Marsaglia. They have a particularly efficient implementation without using excessively sparse polynomials. They generate the next number in their sequence by repeatedly taking the exclusive or of a number with a bit-shifted version of itself. This makes them extremely fast on modern computer architectures.

In an attempt to create its own encryption, Farcos converts a message into an array of 64-bit integers and applies exclusive or to each element **Ei** with **Ki**-th element of an Xorshift sequence that uses **S** as the seed. In other words, a **E** array was created such that:

![UOJ_3110_E_a](https://resources.beecrowd.com/gallery/images/problems/UOJ_3110_E_a.png)

An this:

![UOJ_3110_E_b](https://resources.beecrowd.com/gallery/images/problems/UOJ_3110_E_b.png)

The code snippets shown are implemented in c++.

Provided arrays **E**, **K**, and seed **S**, your task is to decipher the original array **D**.

Input
-----

The first line of input contains five integers: **N** (0 < **N** â¤ 102), the number of elements in the arrays; **S** (0 < **S** < 264), the seed to Xorshift; **A**, **B** and **C** (0 < **A**, **B**, **C** < 64), the Xorshift parameters shown in the code.

The second line of input has **N** integers **Ei** (0 < **Ei** < 264) separated by a blank space.

The third line of input has **N** integers **Ki** (0 < **Ki** < 264) separated by a blank space.

Output
------

The output consists of a single line containing **N** integers **Di** separated by a blank space and representing the deciphered array.


| Input Samples | Output Samples |
| --- | --- |
| 3 49 63 62 63 48 49 50 98 57 22 | 1 2 3 |

| 4 1 1 2 3 31 80255 345 7119 1 4 2 3 | 4 31396 79 1947 |


# Problem 3138

Descrição
----------

Today is Tobias birthday (congratulations!) and as we are currently going through a moment of social isolation, he decided to have an online party in order to celebrate the date with his friends.

Like all good programmers, Tobias is very fond of balloons. And of course it was not on their birthday that they would be left out. He decided to hang some on his wall in order to leave his room decorated for the virtual party later.

Tobias had balloons of various colors kept at home and started to hang them next to each other. While hanging he was wondering if that order was good, or if he should put them in some different order and how many ways he could change those balloons to get a different sequence.

Given the list of how many balloons of each color Tobias found at home, can you help him know what number of different strings he can get by rearranging the position of his balloons?

Note that changing two balloons of the same color in place does not generate a new sequence and it is guaranteed that Tobias will use all the balloons he found and that this number does not exceed 20.

Input
-----

An integer **N** (0
\(\leq\) **N** \(\leq\) 20). Then there will be **N** lines, each with a string **S** (1 \(\leq\) |**S**| \(\leq\) 15) and an integer **B** (1 \(\leq\) **B** \(\leq\) 20) separated by a space. The name of a color and the number of balloons respectively.

The string **S** is formed only by lowercase letters of the english alphabet without spaces and it is guaranteed that the sum of the total number of balloons does not exceed 20.

Output
------

An integer, the total number of distinct strings that Tobias can obtain by changing the order balloons.

As today is his birthday, print **"Feliz aniversario Tobias!"** (without quotes) one line before printing the answer. :)


| Input Sample | Output Sample |
| --- | --- |
| 3 vermelho 2 azul 2 verde 1 | Feliz aniversario Tobias! 30 |

P.S.: Tobias, I did not use the number 14 in this problem, but it will still appear in some other one! ;)
  

Aquecimento - II Maratona UFSC Campus AraranguÃ¡


# Problem 3154

Descrição
----------

Famous interplanetary traveler, ET Bilu wants to invite people from the planet he is visiting to a Great Party. In Bilu culture, a party can only be considered a Grand Party if at least two participants were born on the same day.

Unlike planet Earth, which has 365 or 366 days each year, the planets Bilu visits have a number of different days.

Even with all the advanced technology of intergalactic travel, Bilu does not know how to calculate the chance that this big event will happen. Therefore, you, who were at a Great Party held on planet Earth, will help Bilu to incorporate a program to estimate the chance of a Great Party on the ship's computer.

Given the number of days per year on the planet Bilu is visiting and the number of people at the party, determine the likelihood that the party will be considered a Great Party.

Input
-----

The entry consists of two integers D and P indicating the number of days and people, respectively.

Limits:

50 <= D <= 10 ^ 5;

2 <= P <= D - 1.

Output
------

The output should be the percentage chance of the event being a Grand Party with two decimal places.


| Input Samples | Output Samples |
| --- | --- |
| 365 23 | 50.73 |

| 366 23 | 50.63 |

| 100000 500 | 71.34 |

X OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2020


# Problem 3165

Descrição
----------

Write a program which reads an given integer **N** and prints a twin prime which has the maximum size among twin primes less than or equals to **N**.

According to wikipedia "A twin prime is a prime number that is either 2 less or 2 more than another prime numberâfor example, either member of the twin prime pair (41, 43). In other words, a twin prime is a prime that has a prime gap of two".

Input
-----

The entry must contain an integer **N**, where (5 â¤ **N** â¤ 1000).

Output
------

The output must contain two integers **X** and **Y** separated by space, representing the two closest twin prime numbers less than or equal to **N**.


| Input Sample | Output Sample |
| --- | --- |
| 44 | 41 43 |


# Problem 3179

Descrição
----------

Being educated in Computer Science and Mathematics is not always easy. Especially not if you have âfriendsâ who repeatedly insist on showing you their new âproofsâ that P equals NP, that the Riemann Hypothesis is true, and so on.

One of your friends recently claims to have found a fantastic new compression algorithm. As an example of its amazing performance, your friend has told you that every file in your precious collection of random bit strings after compression would be at most **B** bits long! Naturally, you find this a bit hard to believe, so you want to determine whether it is even theoretically possible for this to be true.

Your collection of random bit strings consists of **N** files, no two of which are identical, and each of which is exactly 1000 bits long.

Input
-----

The input consists of two integers **N** (1 â¤ **N** â¤ 1015) and **B**(0 â¤ **B**â¤ 50), giving the number of files in your collection and the maximum number of bits a compressed file is allowed to have.

Output
------

Output a line containing either âyesâ if it is possible to compress all the **N** files in your collection into files of size at most **B** bits, or ânoâ otherwise.


| Input Samples | Output Samples |
| --- | --- |
| 13 3 | yes |

| 1 0 | yes |

| 31415926535897 40 | no |

Nordic Collegiate Programming Contest 2008


# Problem 3182

Descrição
----------

As you didnât show up to the yearly general meeting of the Nordic Club of Pin Collectors, you were unanimously elected to organize this years excursion to Pin City. You are free to choose from a number of weekends this autumn, and have to find a suitable hotel to stay at, preferably as cheap as possible.

You have some constraints: The total cost of the trip must be within budget, of course. All participants must stay at the same hotel, to avoid last years catastrophe, where some members got lost in the city, never being seen again.

Input
-----

The first line of input consists of four integers: **N** (1 â¤ **N** â¤ 200), the number of participants, **B** (1 â¤ **B** â¤ 500000), the budget, **H** (1 â¤ **H** â¤ 18), the number of hotels to consider, and **W** (1 â¤ **W** â¤ 13), the number of weeks you can choose between. Then follow two lines for each of the **H** hotels. The first gives **P** (1 â¤ **P** â¤ 10000), the price for one person staying the weekend at the hotel. The second contains **W** integers, **A** (0 â¤ **A**â¤ 1000), giving the number of available beds for each weekend at the hotel.

Output
------

Output the minimum cost of the stay for your group, or âstay homeâ if nothing can be found within the budget.


| Input Samples | Output Samples |
| --- | --- |
| 3 1000 2 3 200 0 2 2 300 27 3 20 | 900 |

| 5 2000 2 4 300 4 3 0 4 450 7 8 0 13 | stay home |

Nordic Collegiate Programming Contest 2008


# Problem 3183

Descrição
----------

A certain big IT company which we will not name in order not to get sued, are preparing to launch a new version of their flagship product. Having just been employed as a developer on the project, you have been given a list of open bugs that should be fixed in the new version.

Being bugs, you are not exactly certain how to fix them, even though you have some ideas. For each bug you are able to estimate your ability to quickly fix the bug. Of course, these estimates may be wrong, so if you try to fix a bug and fail, you will revise the estimate of your ability to fix this bug.

To be specific, we use the following probabilistic model for the bug fixing process: for each bug, there is an associated fix probability **P**. Every hour, you choose one bug to work on, and work on this bug for the entire hour (if you manage to fix the bug in less then an hour, you celebrate by having coffee and taunting your coworkers for the remaining part of the hour). The probability that you succeed in fixing the bug during this hour is p. If you fail to resolve the bug, the fix probability for this bug is reduced to **P** Â· **F**, where **F** â¤ 1 is a factor indicating how much faith you lose in your ability after a failure. The fix probabilities for the other bugs remain unchanged. The next hour, you again choose an open bug to work on, and so on. This is repeated until the new version is released, and you are allowed to go home and sleep.

In addition, each bug has a severity **S** indicating how severe the bug is (or alternatively, the value of fixing the bug). Clearly, it is possible that you will not manage to fix all the bugs before the product is released. In order to make as good an impression on your boss as possible, you would like to maximize the total severity of those bugs which you do manage to resolve, by carefully choosing which bugs to work on. What will be the expected value of the total severity of fixed bugs, provided that you, every hour, choose which bug to work on in such a way that this quantity is maximized?

Input
-----

The first line of input contains three numbers **B** (0 â¤ **B** â¤ 10), **T** (0 â¤ **T** â¤ 100) and **F** (0 â¤ **F** â¤ 1), where **B** is an integer giving the number of open bugs, **T** is an integer giving the number of hours left until the new version is released, and **F** is a real number as described above.

Each of the following **B** lines describe an open bug. Each such description contains two numbers **P** (0 â¤ **P** â¤ 1) and **S** (0 â¤ **S** â¤ 10 000), where **P** is a real number giving the initial fix probability of the bug and **S** is an integer giving the severity of the bug.

Output
------

Output a line containing the expected total severity of bugs fixed, provided you work in a way which maximizes this quantity. Any answer with either absolute or relative error smaller than 10â»â¶ is acceptable.


| Input Samples | Output Samples |
| --- | --- |
| 1 2 0.950000  0.700000 50 | 44.975000 |

| 2 2 0.500000  0.750000 100  0.750000 20 | 95.625000 |

Nordic Collegiate Programming Contest 2008


# Problem 3185

Descrição
----------

The young reporter Janne is planning to take a photo of a secret government installation. He needs to obtain evidence of the many serious crimes against good sense that are being committed there, so as to create a scandal and possibly win a Pulitzer. Unfortunately, the base is surrounded by a high fence with high voltage wires running around. Janne does not want to risk being electrocuted, so he wants to take a photo from outside the fence. He can bring a tripod as high as the fence to take a photo, so if he wants he can stand right beside the fence and take his picture. The secret installation is a convex polygon. The fence has a form of a circle. Of course Janne wants to make a photo with maximal possible detail level. The detail level of the photo depends on the view angle of the base at the point from which the photo is taken. Therefore he wants to find a point to maximize this angle.

Input
-----

The first line of the input file contains two integer numbers: **N** and **R** â the number of vertices of the polygon and the radius of the fence (3 â¤ **N** â¤ 200, 1 â¤ **R** â¤ 1000 ). The following n lines contain two real numbers each â the coordinates of the vertices of the polygon listed in counterclockwise order. It is guaranteed that all vertices of the polygon are strictly inside the fence circle, and that the polygon is convex. The center of the fence circle is located at the origin, (0, 0).

Output
------

Output the maximal view angle a for the photo (0 â¤ **A** < 2Ï). Any answer with either absolute or relative error smaller than 10â»â¶ is acceptable.


| Input Sample | Output Sample |
| --- | --- |
| 4 2  -1.0 -1.0  1.0 -1.0  1.0 1.0  -1.0 1.0 | 1.5707963268 |

Nordic Collegiate Programming Contest 2008


# Problem 3187

Descrição
----------

Simon Haples is a somewhat peculiar person. Not quite hip, not quite square, he is more of a triangular nature: ever since childhood, he has had an almost unhealthy obsession with triangles. Because of his discrete nature, Simonâs favorite kind of triangles are the Pythagorean ones, in which the side lengths are three positive integers **A**, **B**, and **C** such that **A** â¤ **B** and **AÂ²**+ **BÂ²** = **CÂ²**.

Recently, Simon has discovered the fantastic world of counting modulo some integer **N**. As you may imagine, he quickly realizes that there are multitudes of Pythagorean triples to which he has previously been oblivious! Simon therefore sets out to find all Pythagorean triples modulo **N**, i.e., all triples of integers **A**, **B** and **C** between 1 and **N** â 1 such that **A** â¤ **B** and **AÂ²** + **BÂ²** â¡ **CÂ²** (mod **N**).

As Simonâs best friend, you realize that there is not much hope in deterring Simon from his crazy plans, so you decide to help him by computing how many such triples there are, so that Simon will know when his work is done.

Input
-----

The input consists of a single integer **N**, satisfying 2 â¤ **N** â¤ 500 000.

Output
------

Output the number of Pythagorean triples modulo **N**.


| Input Samples | Output Samples |
| --- | --- |
| 7 | 18 |

| 15 | 64 |

Nordic Collegiate Programming Contest 2008


# Problem 3216

Descrição
----------

A test for allergy is conducted over the course of several days, and consists of exposing you to different substances (so called allergens). The goal is to decide exactly which of the allergens you are allergic to. Each allergen has a live duration **D** measured in whole days, indicating exactly how many days you will suffer from an allergic reaction if you are allergic to that particular substance. An allergic reaction starts to show almost immediately after you have been exposed to an allergen which you are allergic to. The test scheme has two action points per day:

I At 8 oâclock each morning, at most one of the allergens is applied to your body.

II At 8 oâclock each evening, you are examined for allergic reactions.

Thus an allergen with live duration **D** will affect exactly **D** allergic reaction examinations.

Of course, if you have two or more active allergens in your body at the time of an observed reaction, you cannot tell from that information only, which of the substances you are allergic to.

You want to find the shortest possible test scheme given the durations of the allergens you want to test. Furthermore, to allow simple large scale application the test scheme must be non-adaptive, i.e. the scheme should be fixed in advance. Thus you may not choose when to apply an allergen based on the outcome of previous allergic reaction examinations.

Input
-----

The first line of the input contains a single integer **K** (1 â¤ **K** â¤ 20) specifying the number of allergens being tested for. Then follow **K** lines each containing an integer **D** (1 â¤ **D** â¤ 7) specifying the live duration of each allergen.

Output
------

The number of days of the shortest conclusive non-adaptive test scheme.

*A scheme ends the morning when you no longer have active allergens in your body, thus a test scheme for a single allergen with live duration **D** takes **D** days.*


| Input Samples | Output Samples |
| --- | --- |
| 3  2  2  2 | 5 |

| 5  1  4  2  5  2 | 10 |

Nordic Collegiate Programming Contest 2009


# Problem 3223

Descrição
----------

You are soon to graduate from the mathemagician school of Hagworts, and youâre quite content with yourself; all the hard work and elbowing has finally paid off. Being successful at most of your endeavors you would normally end up a herald of sound reasoning and good mathemagics. You, however, are different; not only have you spent your young years secretly hacking away at computers, writing code to do your assigned routine homework for you, but of late you have started planning how to cram all your mathemagical skills into a computer to completely eliminate the need for mathemagicians! To show the others just how great a visionary you are, you plan to make your graduation ceremony something they will never forget.

To do this you need to break into the safe of your arch-nemesis, Hairy Peter. The safe is locked by a code mechanism: All natural numbers from 1 to **N** need to be typed in in the correct order, set by Hairy Peter. Fortunately you know that Hairy, being a good mathemagician, has a certain weakness; he has a rather unhealthy obsession with the number **K**. (For instance he always has to introduce himself **K** times whenever he meets new people, making him quite annoying to be around.) Thus you are certain that his code, when viewed as a permutation of the **N** first naturals, has order exactly **K**. (i.e. **K** is the smallest positive number such that if you **K** times replace **x** â {1, . . . , **N**} with the position of **x** in Hairyâs code, you end up with the **x** you started with, for all **x**. Thus e.g. the order of the
permutation corresponding to the code 2 3 1 is 3, as 1 â 3 â 2 â 1 and 2 â 1 â 3 â 2 and 3 â 2 â 1 â 3.) While this does not help you directly, it greatly reduces the number of code inputs you may have to try before you find the correct one. âHow many?â is the question you are pondering right now. You must know the exact number, lest you risk preparing too little time for cracking the safe.

Now you also have a certain mathemagical weakness â arguably a bit worse than Hairy Peterâs: Because of your dark scheme to program mathemagical computers, you insist there are no numbers greater than what can be represented by a signed 32-bit integer, namely the prime **P** = 2Â³Â¹ â 1. Of course there must be nothing your computers cannot count. In fact you hate this upper limit **P** so intensely that you have decided to make a new mathemagics where **P** equals 0. Ha, take that! (Well, you are quite aware that you are really just counting modulo **P**, but it will have to suffice until you find better ways of punishing **P**.) In fact this turns out to be quite an advantage for you! For instance, if the number of code permutations you have to check turns out to be 2Â³Â¹, there will actually be just one permutation for you to check, as 2Â³Â¹ mod **P** = 1. (Or at least you think so...) Thatâs just
magnificent!

Input
-----

The input consists of two integers **N** (1 â¤ **N** â¤ 100) and **K** (1 â¤ **K** â¤ 2Â³Â¹ â1) respectively.

Output
------

The number of permutations of **N** elements of order **K**, modulo 2Â³Â¹ â 1.


| Input Samples | Output Samples |
| --- | --- |
| 3 2 | 3 |

| 6 6 | 240 |

| 15 12 | 1789014075 |

Nordic Collegiate Programming Contest 2009


# Problem 3257

Descrição
----------

Farmer Jon has recently bought **N** tree seedlings that he wants to plant in his yard. It takes 1 day for Jon to plant a seedling (Jon isnât particularly hardworking), and for each tree Jon knows exactly in how many days after planting it grows to full maturity. Jon would also like to throw a party for his farmer friends, but in order to impress them he would like to organize the party only after all the trees have grown. More precisely, the party can be organized at earliest on the next day after the last tree has grown up.

Help Jon to find out when is the earliest day when the party can take place. Jon can choose the order of planting the trees as he likes, so he wants to plant the trees in such a way that the party will be as soon as possible.

Input
-----

The input consists of two lines. The first line contains a single integer **N** (1 â¤ **N** â¤ 100 000) denoting the number of seedlings. Then a line with **N** integers **T*áµ¢*** follows (1 â¤ **T*áµ¢*** â¤ 1 000 000), where **T*áµ¢*** denotes the number of days it takes for the ***i***-th tree to grow.

Output
------

You program should output exactly one line containing one integer, denoting the earliest day when the party can be organized. The days are numbered 1, 2, 3, . . . beginning from the current moment.


| Input Samples | Output Samples |
| --- | --- |
| 4  2 3 4 3 | 7 |

| 6  39 38 9 35 39 20 | 42 |

Nordic Collegiate Programming Contest 2013


# Problem 3259

Descrição
----------

Lukas is to hold a presentation on useful mathematical tricks. E.g., to take the square root of a number you just need to remove the first half of the number. To convince his audience he uses the well tested method of proof by example: â 25 = 5 and â 5776 = 76 so the method obviously works. To multiply a number by **X** = 2.6 all you have to do is move the first digit to the end of the number, 135Ã2.6 = 351 and 270270Ã2.6 = 702702.

Lukas wants to demonstrate that this last method works for any **X**. To do this he will ask his audience for values of **X** and then show them example multiplications for which the method works. Lukas has noticed that he can not just pick arbitrary numbers for his examples, so now he wants your help. Can you write a program that given **X** gives a list of integers for which multiplying by **X** is equivalent to moving the first digit to the end of the number? Lukas does not like very large numbers so do not list any numbers with more than 8 digits.

Input
-----

The input is a single decimal number **X** (1 â¤ **X** < 1000) with at most 4 digits after the decimal point.

Output
------

Output a list of all positive integers less than 10â¸ for which Lukasâ second trick works. Write the numbers in ascending order, one number per line. If the list is empty, output instead âNo solutionâ.


| Input Samples | Output Samples |
| --- | --- |
| 2.6 | 135  270  135135  270270 |

| 3.1416 | No solution |

Nordic Collegiate Programming Contest 2013


# Problem 3265

Descrição
----------

Marek loves dancing and he has danced a lot in the last couple of years. He has actually danced so much that he became too good in all of the traditional dances like swing, salsa, ballroom and hip-hop and now all partners he dances with can not keep up with him. Therefore he started to invent his own dances and even tries to convince other people to dance these new dances with him.

Marek got really excited when he heard about the coming wedding of his best friend Miroslav. For a whole month he worked on a special dance for the wedding. The dance was performed by **N** people and there were **N** marks on the floor. There was an arrow from each mark to another mark and every mark had exactly one incoming arrow. The arrow could be also pointing back to the same mark.

At the wedding, every person first picked a mark on the floor and no 2 persons picked the same one. Then Marek played some music and every 10 seconds there was a loud signal when all dancers had to move along the arrow on the floor to another mark. The placement of the marks was such that everybody could follow the arrow to the next mark in 10 seconds without any trouble. If an arrow was pointing back to the same mark, the person at the mark just stayed there and maybe did some improvized dance moves on the spot.

A year has passed since Miroslavâs wedding and another wedding is coming up. Marek would like to do a similar dance at this wedding as well. He lost all the drawings he had, but luckily he found two photos from exactly when the dance started and when it ended. Marek also remembers that the signal was triggered **K** times during the time the song was played, so people moved **K** times along the arrows.

Given the two photos, can you help Marek reconstruct the arrows on the floor? On the two photos it can be seen for every person to which position he or she moved. Marek therefore numbered the people in the first photo from 1 to **N** and then wrote the number of the person whose place they took in the second photo.

Marekâs time is running out, so he is interested in any placement of arrows that could produce the two photos.

Input
-----

The first line of the input contains two integers **N** and **K**, 2 â¤ **N** â¤ 10 000, 1 â¤ **K** â¤ 10â¹. The second line of the input contains **N** space separated integers **A**1, . . . , **AN** , denoting that dancer number ***i*** ended at the place of dancer number **A*i*** . You may assume that 1 â¤ **A*i*** â¤ **N** for all ***i*** and every number between 1 and **N** inclusive appears exactly once in the sequence.

Output
------

If it is impossible to find a placement of arrows such that the dance performed **K** times would produce the two photos, print âImpossibleâ. Otherwise print **N** numbers on a line, the ***i***-th number denoting to which person the arrow leads from person number ***i***.


| Input Samples | Output Samples |
| --- | --- |
| 6 2  3 4 5 6 1 2 | 5 6 1 2 3 4 |

| 4 2  3 4 1 2 | 2 3 4 1 |

Nordic Collegiate Programming Contest 2013


# Problem 3266

Descrição
----------

Jaap is playing darts at the local pub with a group of friends. His darts throwing skills are not that great, so he just tries to aim at the center of the dartboard. His mathematical skills are better though, and he wonders what is his expected score for one dart.

After a while Jaap estimates that his darts hit the dartboard (or often miss it) with a probability distribution that depends only on the radius **r** from the center of the board, and has the Gaussian form (This implies that the total probability is never larger than one).

![dartboard-a](https://resources.beecrowd.com/gallery/images/problems/dartboard-a.png)

That is, the probability of hitting a small surface area â**x**Â·â**y** at a distance **r** from the center is given by f(**r**)â**x**Â·â**y**. Here **Ï** denotes the standard deviation, and Jaap found out that this depends strongly on how many beers he has had.

For those not familiar with the game of darts, a dartboard is depicted below. The score for hitting each of the regions of the dartboard is as follows:

* the inner bullâs eye is worth 50 points;
* the bull annulus is 25 points;
* each pie has worth of the respective number 1 up to 20, but
* the inner triple ring has triple the worth of the pie, while
* the outer double ring has double the worth.

Finally, if the dart lands outside the double ring, the score is zero. Note that the pies of all numbers have equal area.

![dartboard-b](https://resources.beecrowd.com/gallery/images/problems/dartboard-b.png)

Figure J.1: A standard dartboard (from Wikimedia, CC BY-SA 3.0 licensed by Tijmen Stam).

Input
-----

The first line contains 6 floating point numbers of strictly increasing size: the radii of the bullâs eye, bull, inner and outer triple ring, and inner and outer double ring, all in centimeters. The second line contains the standard deviation Ï in centimeters as a floating point number. All floating point numbers are in the range [10â»Â³ , 100].

Output
------

Print the expected score of one dart for Jaap as a floating point number on a single line. The answer must have nine decimal places.


| Input Samples | Output Samples |
| --- | --- |
| 1.27 3.1 10.9 11.7 16.2 17.0  17.0 | 5.266210658 |

| 1.27 3.1 10.9 11.7 16.2 17.0  0.5 | 49.00690019 |

| 0.1 0.2 0.3 0.4 99.9 100  20 | 10.50283655 |

Nordic Collegiate Programming Contest 2013


# Problem 3270

Descrição
----------

Last weekend you and your friends went to visit the local farmerâs market at the town square. As you were standing around in a circle talking, you couldnât help overhearing two of your friends musing over what sounded like an interesting problem: They were considering the number of ways in which you could all shake hands, such that everyone in the circle simultaneously shaked hands with one other person, but where no arms crossed each other.

After a few secondsâ thought you decided to join your two friends, to share (with them) the solution to their problem. âIf we are **2n** personsâ, you said, âpick any particular person, and let that person shake hands with somebody. That person will have to leave an even number of people on each side of the person with whom he/she shakes hands. Of the remaining **n** â 1 pairs of people, he/she can leave zero on the right and **n** â 1 pairs on the left, 1 on the right and **n** â 2 pairs on the left, and so on. The pairs remaining on the right and left can independently choose any of the possible non-crossing handshake patterns, so the count **Cn** for **n** pairs of people is given by:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_3270_A.png)

which, together with the fact that **C0** = **C1** = 1, is just the definition of the Catalan numbers.â By consulting your handy combinatorics book, you find out that there is a much more efficient formula for calculating **Cn**, namely:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_3270_B.png)

After a collective groan from the group, your particularly cheeky friend Val called out âWell, since we are at the town square, why donât you try to square your Catalan numbers!â. This was met with much rejoicing, while you started to think about how to square the Catalan sequence. . .

Task
----

Let **Cn** be the **n**th Catalan number as defined above. By regarding the sequence (**Cn**) **n**â¥0 of Catalan numbers, we can define a sequence (**Sn**) **n**â¥0 , corresponding to âsquaring the Catalan sequenceâ, by considering the Cauchy product, or discrete convolution, of (**Cn**) **n**â¥0 with itself, i.e.,

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_3270_C.png)

Your task is to write a program for calculating the number **Sn**.

To see why (**Sn**) **n**â¥0 could be said to correspond to the square of the Catalan sequence we could look at Cauchy products of power series. Suppose that **p(x) = Î£ân=0 anxn** and **q(x) = Î£ân=0 bnxn**, then **p(x)\*q(x) = Î£ân=0 cnxn** where **cn = Î£nk=0 akbn-k**.

Input
-----

The input contains one line containing one non-negative integer: **n**, with 0 â¤ **n** â¤ 5000.

Output
------

Output a line containing **Sn**.


| Input Samples | Output Samples |
| --- | --- |
| 0 | 1 |

| 59 | 1583850964596120042686772779038896 |

NCPC - Nordic Collegiate Programming Contest 2014


