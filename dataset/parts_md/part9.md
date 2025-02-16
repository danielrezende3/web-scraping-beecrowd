# Problem 2820

Descrição
----------

Bruna is learning to count. She already knows d digits. Her brother, Carlos, told her that she can't even form n distinct numbers using those digits only. Bruna, to prove that he is wrong, will write the n smallest numbers that she can make using only the digits she knows in a sheet of paper, but she doesn't know when to stop. Can you help her wit that task?

Input
-----

The first line of input consists of a number **t**(**t**=100) , the number of test cases.

Each case starts with an integer**d** (2<=**d**<=9): the number of digits Bruna has already learned.

The following line will contain d integers **v****i** (1<=**v****i**<=9): the digits Bruna knows.

The last line of each case will be the number **n**(1<=**n**<=1018).

Output
------

For each case, print the nth smallest number that can be made using the digits Bruna knows.


| Input Sample | Output Sample |
| --- | --- |
| 2  2  1 3  4  3  9 7 8  5 | 13  78 |

OBI Warm-Up Regional Phase


# Problem 2822

Descrição
----------

Happy Birthday! As a birthday gift, your mother made your biggest dream come true and gave you a little pet graph. It's breed is very rare: it has n vertices and each one of them has a value. Initially the vertice i has value i ( 1<= i <= n) and for each pair of vertices the is an edge connecting them with weight equal to the magnitude of the difference of their values.

You little graph is in its development stage, that means that the value of vertice i can change to k at any time! Besides that, graphs eat a lot and you must feed them daily with an amount of food equal to the weight of their **maximum** spanning tree.

Write a program to take good care of your graph, or your mother might take it from you!

**Note:**The maximum spanning tree of a graph is the tree which vertices are vertices of the original graph and edges are edges of the original graph that has the maximum sum of weight of it's edges.

Input
-----

The first line of input is an integer **t** (**t**<=10): the number of test cases.

Each case starts with an integer **N** (0<=**N**<=2\*105): the number of vertices of the graph.

The next line will be an integer **Q** (1<=**Q**<=2\*105) : the number of instructions to be followed.

An instruction can be of the following types:

**1 i k**: the value of vertice **i** (1 <= **i** , **k** <= **n**) changes to **k** ( the edges connected to it must change accordingly).

**2** : the weight of the maximum spanning tree of your graph.

Output
------

For each instruction of the type 2, print the weight of the maximum spanning tree of the graph.


| Input Sample | Output Sample |
| --- | --- |
| 1  5  3  2  1 3 5  2 | 12  14 |

OBI Warm-up -2018 Regional Phase


# Problem 2828

Descrição
----------

An anagram is a permutation of the letters in a word.  

For instance, the strings **ananab** and **anbana** are anagrams of the word **banana**.

Your task, in this problem, is to compute how many distinct anagrams exist for a given word.

Since this number can be very large, compute the remainder of the division of the number of anagrams by our favorite prime number: \(10^9+7\).

Input
-----

The input has a single line, with a single word, with at most \(10^5\) characters. The word only has lowercase characters from **a** to **z**.

Output
------

The output contains only a single line with a single integer, the result.


| Input Samples | Output Samples |
| --- | --- |
| aaa | 1 |

| abc | 6 |

| aab | 3 |

Seletiva UFFS 2018 - Open Contest


# Problem 2839

Descrição
----------

For some unknown reason Rangel only has a pair of socks of each color.

Today he's late to go to college and still needs to get a pair of socks, but the socks are all mess.

Given the number of pairs of socks in Rangel's drawer, he wants to know how many socks he needs to get to have at least one pair of the same color.

Input
-----

Each case is composed of the only integer **N** (1 â¤ **N** â¤ 105) corresponding to amounts of pairs of socks in the drawer.

Output
------

You should print a line with a single integer that matches the minimum amount of socks that Rangel needs to pick up.


| Input Sample | Output Sample |
| --- | --- |
| 1 | 2 |


# Problem 2859

Descrição
----------

A *Digit Root* is a feature of numbers used in mathematical recreation, but can also be used to check the results of simple operations such as sum and multiplication. One of its main properties is that the *Digit Root* of a number is always equal to *Digit Root* of the sum of its digits.

For example, the *Digit Root* dofe 18446744073709551615 is the same as 87 because 1+8+4+4+6+7+4+4+0+7+3+7+0+9+5+5+1+6+1+5=87 is the same of 15 because 8+7=15, which in turn is the same as 6, since 1+5=6. Therefore the *Digit Root* of all these numbers is 6 since 6 is its own *Digit Root*.

Your task is, given the two integers, **B** and **E**, calculate the *Digit Root* of **B****E** (**B** raised to th **E**-th power).

Input
-----

The input consists of two lines. The first contains the number **B** (1 â¤ **B** â¤ 10105). The second contains the number **E** (1 â¤ **E** â¤ 10105).

Output
------

The output consists of a single line containing the*Digit Root*.


| Sample Input | Sample Output |
| --- | --- |
| 2  7 | 2 |

| 25  5 | 4 |

| 6  10 | 9 |

OBI Warm-Up 2018 National Phase


# Problem 2864

Descrição
----------

Nick is a scientist who travels through several parallel universes along with his grandson, Mory. In one of these universes, there was a television program, which rewarded those who guessed the maximum heights of fruit pitches. At this location, the fruit mass did not influence the maximum height of the pitch. Nick calculated the angle of the pitch, which always formed a parabola, and extracted a second-degree function from the trajectory. Help Nick and Mory win many awards in this program.

Input
-----

The input is composed of several test cases. The first line contains an integer T (2 <= T <= 99) relative to the number of test cases. The following T lines have three integer values ââ**A** (**A** < 0), **B** and **C** (-100 <= **B, C** <= 100), representing the coefficients of a second degree function, in the form ax2 + bx + c.

Output
------

For each entry test case in your program, you should print a real number, to the nearest two decimal places, the maximum pitch height of a fruit.


| Input Sample | Output Sample |
| --- | --- |
| 3 -1 4 1 -1 3 0 -1 -1 3 | 5.00 2.25 3.25 |

VIII OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2018


# Problem 2869

Descrição
----------

1 is a divisor of 6. In addition to 1, it has 3 more divisors of 6: 2, 3 and 6. In total, 6 has 4 divisors, and it is the smallest number that has 4 divisors. Talking about divisor, given a number n, what is the smallest number that has n divisors?

Input
-----

The input is composed of several test cases. The first line contains an integer C, with the total of test cases. The following C lines have an integer N (1 <= N <= 100).

Output
------

For each input test case in your program, you must print an integer containing the smallest number that has N divisors. Some values ââwill have relatively large numbers. In this way, print in the form of MOD 1000000007


| Input Sample | Output Sample |
| --- | --- |
| 4 1 4 11 100 | 1 6 1024 45360 |

VIII OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2018


# Problem 2873

Descrição
----------

According to some historians, Tales probably spent a period of his life in Egypt and Babylon, devoting himself to research in contact with astronomers and mathematicians. In the period in which it passed in Egypt, it was realized that the Egyptians could not calculate the height of a great pyramid of Cheops and presented a solution to the problem. Tales supposed that the rays of the Sun are parallel when they reach the Earth, because of the distance that separates it from the Sun. (A.J. Philippi .; M.A. Romero; G.C. Bruna (editors)). Let us consider that Tales has chosen a position of illumination of the Sun, such that it is possible to calculate the height of the pyramid given the value of A in meters (width of the pyramid), the value of B in meters (length of the leftover pyramid), of C in meters (the height of any rod) and the value of D in meters (rod length), as shown in the figure.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2873.png)

Suppose we go back in time and that Tales has now been hired by the Egyptians to calculate the height of all the pyramids in Egypt. However, he does not understand much of programming and asked for his help to develop a system that allows him, through his Tablet, to enter with the data that is provided and the system generate the height of the pyramid.

Input
-----

The input is composed of several test cases. Each test case has a single line containing a real value A (2 <= A <= 10000), a value B (2 <= B <= 20000), a value C (1 <= C <= 100) and a value D (1 <= D <= 200). The data entry is finalized when the values ââA = 0, B = 0, C = 0 and D = 0 are read.

Output
------

For each test case in your program, you must print a single line containing a real number with five decimal digits.


| Input Sample | Output Sample |
| --- | --- |
| 4 3 2 3 10 5 2 6 8 4 5 10 20 5 6 12 0 0 0 0 | 3.33333 3.33333 4.00000 7.50000 |

VIII OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2018


# Problem 2878

Descrição
----------

VÃ´ Giuseppe ganhou de presente um cortador profissional de pizza, daqueles do tipo carretilha e, para comemorar, assou uma pizza retangular gigante para seus netos! Ele sempre dividiu suas pizzas em pedaÃ§os fazendo cortes ao longo de linhas contÃ­nuas, nÃ£o necessariamente retilÃ­neas, de dois tipos: algumas comeÃ§am na borda esquerda da pizza, seguem monotonicamente para a direita e terminam na borda direita; outras comeÃ§am na borda inferior, seguem monotonicamente para cima e terminam na borda superior. Mas VÃ´ Giuseppe sempre seguia uma propriedade: dois cortes do mesmo tipo nunca podiam se interceptar. Veja um exemplo com 4 cortes, dois de cada tipo, na parte esquerda da figura, que dividem a pizza em 9 pedaÃ§os.

![BR](https://resources.beecrowd.com/gallery/images/contests/pizza_sbc_2878.png)

Acontece que VÃ´ Giuseppe simplesmente ama geometria, topologia, combinatÃ³ria e coisas assim; por isso, resolveu mostrar para as crianÃ§as que poderia obter mais pedaÃ§os, com o mesmo nÃºmero de cortes, se cruzamentos de cortes de mesmo tipo fossem permitidos. A parte direita da figura mostra, por exemplo, que se os dois cortes do tipo dos que vÃ£o da esquerda para a direita puderem se interceptar, a pizza serÃ¡ dividida em 10 pedaÃ§os. VÃ´ Giuseppe descartou a propriedade, mas nÃ£o vai fazer cortes aleatÃ³rios. AlÃ©m de serem de um dos dois tipos, eles vÃ£o obedecer Ã s seguintes restriÃ§Ãµes:

â¢ Dois cortes tÃªm no mÃ¡ximo um ponto de interseÃ§Ã£o e, se tiverem, Ã© porque os cortes se cruzam naquele ponto;

â¢ TrÃªs cortes nÃ£o se interceptam num mesmo ponto;

â¢ Dois cortes nÃ£o se interceptam na borda da pizza;

â¢ Um corte nÃ£o intercepta um canto da pizza.

Dados os pontos de comeÃ§o e tÃ©rmino de cada corte, seu programa deve computar o nÃºmero de pedaÃ§os resultantes dos cortes do VÃ´ Giuseppe.

Entrada
-------

A primeira linha da entrada contÃ©m dois inteiros **X** e **Y** , (1 â¤ **X**, **Y** â¤ 109 ), representando as coordenadas (X, Y ) do canto superior direito da pizza. O canto inferior esquerdo tem sempre coordenadas (0, 0). A segunda linha contÃ©m dois inteiros **H** e **V** , (1 â¤ **H**, **V** â¤ 10ââââââââââââââ5 ), indicando, respectivamente, o nÃºmero de cortes que vÃ£o da esquerda para a direita, e o nÃºmero de cortes que vÃ£o de baixo para cima. Cada uma das **H** linhas seguintes contÃ©m dois inteiros **Y1** e **Y2** definindo as ordenadas de encontro dos lados verticais da pizza com um corte que vai do lado esquerdo, na ordenada **Y1**, para o lado direito, na ordenada **Y2**. Cada uma das **V** linhas seguintes contÃ©m dois inteiros **X1** e **X2** definindo as
abscissas de encontro dos lados horizontais da pizza com um corte que vai do lado inferior, na abscissa **X1**, para o lado superior, na abscissa **X2**.

SaÃ­da
------

Imprima uma linha contendo um inteiro representando o nÃºmero de pedaÃ§os resultantes.


| Exemplos de Entrada | Exemplos de SaÃ­da |
| --- | --- |
| 3 4  3 2  1 2  2 1  3 3  1 1  2 2 | 13 |

| 5 5  3 3  2 1  3 2  1 3  3 4  4 3  2 2 | 19 |

| 10000 10000  1 2  321 3455  10 2347  543 8765 | 6 |

Maratona de ProgramaÃ§Ã£o da SBC 2018


# Problem 2886

Descrição
----------

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2886.png)

Neste estranho sistema planetÃ¡rio, **N** planetas seguem Ã³rbitas circulares ao redor de uma estrela que estÃ¡ nas coordenadas (0, 0) do sistema. A estrela estÃ¡ estritamente contida no interior de todos os cÃ­rculos que definem as Ã³rbitas, mas o centro dessas Ã³rbitas nÃ£o estÃ¡ necessariamente nas coordenadas (0, 0). As Ã³rbitas circulares estÃ£o em posiÃ§Ã£o geral: se duas Ã³rbitas se interceptam, entÃ£o elas se interceptam em dois pontos distintos; alÃ©m disso, trÃªs Ã³rbitas nÃ£o se interceptam em um ponto comum.

O cientista JoÃ£o Kepler estÃ¡ interessado em testar uma nova teoria e, para isso, pediu sua ajuda para computar o nÃºmero de pontos de interseÃ§Ã£o entre as Ã³rbitas, caso esse nÃºmero seja menor que ou igual a 2**N**. Caso contrÃ¡rio, precisamos apenas saber que o nÃºmero Ã© maior do que 2**N**.

Entrada
-------

A primeira linha da entrada contÃ©m um inteiro **N** (2 â¤ **N** â¤ 150000), representando o nÃºmero de Ã³rbitas. Cada uma das **N** linhas seguintes contÃ©m trÃªs nÃºmeros reais, com exatamente 3 dÃ­gitos decimais, **X**, **Y** (â25.0 â¤ **X**, **Y** â¤ 25.0) e **R** (1.0 â¤ **R** â¤ 200000.0), definindo as coordenadas do centro e o raio das Ã³rbitas.

SaÃ­da
------

Imprima uma linha contendo um inteiro, representando o nÃºmero de pontos de interseÃ§Ã£o entre as Ã³rbitas, se esse nÃºmero for menor ou igual a 2**N**. Caso contrÃ¡rio, imprima âgreaterâ.


| Exemplos de Entrada | Exemplos de SaÃ­da |
| --- | --- |
| 6  0.000 1.000 4.000  0.000 0.000 10.500  4.000 0.000 6.000  1.000 1.000 1.750  -1.000 -1.000 8.000  2.000 -2.000 4.000 | 10 |

| 4  -1.000 -1.000 3.000  1.000 -1.000 3.001  -3.004 3.003 5.002  1.000 1.000 3.005 | greater |

Maratona de ProgramaÃ§Ã£o da SBC 2018


# Problem 2890

Descrição
----------

A designer invented a brand for a company in tetrahedron form. He has several colors available to paint and want to know how many different ways a tetrahedron can be colored using any combination of  colors  on  the  faces  of  the same. Note that, if by convenient rotations, the coloring of two tetrahedra match, then it is the same coloration.

Help this designer do this calculation.  


Input
-----

Each input line contains an integer **N**, 1 â¤  **N**â¤  104 , the number of colors available. The input ends with a value of 0, which should not be processed.

Output
------

For each input, print the number of distinct colorings of the tetrahedron  with the given number of colors. As the result can be very large, present it as the rest of the division by 1000007.


| Input Sample | Output Sample |
| --- | --- |
| 1 8 2250 0 | 1 400 878008 |


# Problem 2892

Descrição
----------

Three cyclists are training on the velodrome for the next Olympics.  They start up together and make thousands of  laps every day, on a regular basis.  Each takes a certain time to complete the lap and always runs at the same speed. The coach scored the time of one lap for the first two cyclists and only knows,  in relation to the third, the time it takes for the three to line up again on the line of departure.

You will help the technician by calculating all the possible times the third rider takes a lap.

Input
-----

Each input line contains three integers: **T**,  1 â¤  **T**â¤  106,  the time that the cyclists take to meet again in the departure line,         **A, B**,  1 â¤  **A, B**â¤  102,  the respective times that cyclists 1 and 2 take to complete one lap.

Output
------

For each input line, print, in an orderly way, the possible times that the third rider takes to complete a lap, so that the mentioned coincidence occurs.


| Input Sample | Output Sample |
| --- | --- |
| 42 6 7 40 5 4 58652 11 62 0 0 0 | 1 2 3 6 7 14 21 42 8 40 172 1892 5332 58652 |


# Problem 2903

Descrição
----------

Bob has a symmetry craze. Everything in his life must be symmetric: his house, his clothes, his car, even his food. And pizza is no exception. For him to eat a pizza, all the toppings, like tomatoes, olives, pepperoni or basil, must be arranged with some degree of rotational symmetry. This evening Bob ordered some pizza. As usual, when it arrived, he asked the delivery driver to demonstrate that the pizza met his demands for rotational symmetry. The driver demonstrated the symmetry then, as they are trained to do, using the following procedure:

* take a picture of the pizza with a cellphone;
* rotate the pizza by R degrees around its center;
* take another picture;
* show Bob the two pictures side by side, so that he sees that the pizza appears identical in both.

Satisfied, Bob paid for the pizza and took it to the kitchen. In order to test his brand new laser pizza cutter, he decided to cut the pizza in as many slices as possible. Of course, Bob wants to cut the slices in a way that all of them look exactly the same, in accordance with another of his crazes. Now given the angle R of the symmetry demonstration, Bob wants to know the maximum amount of equal slices he can cut the pizza in.

Entrada
-------

The input consists of a single line that contains a rational number **R** (0 < **R** < 360) indicating the angle of the rotational symmetry demonstration. This number has exactly two digits after the decimal point.

SaÃ­da
------

Output a single line with an integer representing the maximum amount of equal slices Bob can cut the pizza in, based on the provided information


| Exemplos de Entrada | Exemplos de SaÃ­da |
| --- | --- |
| 45.00 | 8 |

| 180.00 | 2 |

| 240.00 | 3 |

| 35.00 | 72 |

| 2.50 | 144 |

| 11.34 | 2000 |

Final Nacional da XXIII Maratona SBC de ProgramaÃ§Ã£o


# Problem 2937

Descrição
----------

Snake Norato is a Brazilian folklore legend, with an indigenous origin from Brazil northern region, mainly in the Amazon.

*According to legend, an Indian tapuia from the Amazon region got pregnant by a boto.*

*Twins were born (a boy and a girl), who were actually snakes. The girl was named Maria Caninana, and the boy was baptized Norato.* 

*The twins were left on the Tocantins River and grown up alone.*

*Snake Norato was good, he saved who was drowning and helped the boatmen and fishermen in danger. Caninana was the opposite: she attacked people.*

*Norato used to visit his mother and attend the city dances, because he loved to dance. In these days he would come out of the water, leave the huge snake skin on the bank, and turn into a man. Late in the evening, he would put on snake skin and return to the river.*

*Norato wanted to be disenchanted, to become a real man and he gave the recipe to break the enchant to several friends, but none of them had the courage to go to the end. Finally, a soldier was able to disenchant him.*

The legend ends by telling that Cobra Norato's skin was burned and that the Honorato boy lived for many years in ParÃ¡, where he was loved by all.

What the legend doesn't tell is that the soldier and his battalion companions had to do a huge job to divide the snake's huge skin leather into parts and take it to another place where it would not cause a fire in the Wood.

The length of the leather was divided into varied pieces. The sizes of the pieces were according to the fixed length that each soldier carried in a trip to the fire.

In addition, the battalion was such that a stronger soldier could always take, in a single trip, exactly multiple times the size that a weaker soldier could, but no fraction more or less. And there was a soldier who always carried pieces of size one.

Given the length of the snake and the sizes each soldier can carry, determine the number of ways that the soldiers may have taken the snake's leather up to the fire.

One form is considered different from the other if the number of trips from the riverbank to the campfire is different for some soldier.

Input
-----

The first line of input contains **N** (1 â¤ **N** â¤ 40) being the quantity of soldiers. The next line contains **N** distincts integers **Ti** (1 â¤ **Ti** â¤ 1018)representing the size in meters of the piece that each soldier carries per trip. The third line of a test case contains an integer **C** (1 â¤ **C** â¤ 1018)representing the snake's length in meters.

Output
------

The output consists of one line containing an integer representing the number of ways to carry Snake Norato's leather from the margin to the burning area. Since this number can be very large, print only the rest of your division by 109+7.


| Input Samples | Output Samples |
| --- | --- |
| 3  6 1 3  10 | 6 |

| 4  1 5 10 20  20 | 10 |

| 2  4 1  3 | 1 |

III Maratona de ProgramaÃ§Ã£o do Norte


# Problem 2939

Descrição
----------

A group entirely formed by couples went out for dinner. When they arived at the restaurant they chosse a rectangular table with the amount of seats exactly the same as the people in their group. They all sat one couple at time, so as to occupy only the larger pair of opposite sides.

Given the number of couples and knowing that each person sat in front of or beside their pair, calculate the number of different ways that this group may have occupied the table.

![UOJ_casais](https://resources.beecrowd.com/gallery/images/contests/UOJ_casais.jpg)

One way of occupying the table is considered different from the other if at least one person is in a position different from his previous one.

Input
-----

The input consists in a single line containing an integer **N** (1 â¤ **N** â¤ 106) representing the quantity of couples.

Output
------

The output consists of a single line containing the number of ways the couples placed themselves on the table following the restrictions. Since this number can be very large, just print the number module 10 9+7.


| Input Samples | Output Samples |
| --- | --- |
| 1 | 2 |

| 2 | 16 |

| 3 | 144 |

III Maratona de ProgramaÃ§Ã£o do Norte


# Problem 2953

Descrição
----------

Fingolfin loves board games. One day, you are faced with a very strange game called "2 First primes". Basically this game consisted of a single-row horizontal board containing N houses. The player starts at house number 1 and the goal is to get to house N (not being able to get past). In each round, the player can move in two ways: walk 2 or 3 houses forward (oh yes, now makes sense the title of the game). Fingolfin found the game very easy (only to go forward), so his colleague FÃ«anor challenges him to say how many different possibilities there are of him to finish the game, that is, in how many different ways Fingolfin, from the house 1, can get to the house N. Fingolfin is a bit busy taking care of some housework and asked you, given the number of houses on the board, to solve the challenge.

Input
-----

Integer **N**(1 â¤ **N** â¤ 105), indicating the number of boxes on the board.

Output
------

Integer indicating the number of possibilities to end the game. The number of possibilities can be very large, so one should only show the remainder value of this value when it is divided by **109 + 7**.


| Input Samples | Output Samples |
| --- | --- |
| 3 | 1 |

| 100 | 505425294 |

| 23238 | 34135335 |

IX OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2019


# Problem 2955

Descrição
----------

No one has ever done this, but it is intuitive to say that Computer Science and Computer Science courses hold the greatest legends of the traditional Truco game. The computer people love this game so much that over the years they have been proposing new rules and new scoring systems to make the game ever more challenging.

We will not go into the details of the rules of the game, firstly because everyone should know, given the niche of this test; secondly that for this problem, we are not interested in the rules, but in the scoring system.

The game is done in rounds, and the team that reaches or exceeds **X** points wins (archaically they were 12 or 15 points, but over time they have made the trick a more dynamic experience). In each round, a team can win 1 or a multiple amount of 3 in points (the famous shouting).

If it is not necessary to "chew", that is, only 1 point is left to win, it is forbidden to chew. Universal rule, do not question.

Remember that if the multiple of 3 of the trick is greater than or equal to the remainder of the points to win the game, it is not necessary for the opponent to increase it more. (A lot of people like to continue screaming, even though it does not make sense, but here we have civilized and intelligent people).

It is also considered that a person won perfectly, when he can reach **exactly** the number of points, without going over.

Josh Homme is a freshman on the computer course and wants to get his hands on the trick. He already knows programming and wants to create a program that gives the number of points to win, indicate how many possibilities there are to win (reach **X** points or exceed) and the minimum number of rounds to win in a perfect way.

Input
-----

The entry contains an integer **X**(1 < **X** â¤ 1000), indicating the number of points required to win the game.

Limits: 1 <X â¤ 1000.

Output
------

The output contains two integers, indicating the number of chances to win and the minimum number of rounds for Josh to win the game perfectly.

Detail: The number of possibilities can be very large, so one must show the value that this number would leave of rest when being divided by 109 + 7.


| Input Samples | Output Samples |
| --- | --- |
| 2 | 2 2 |

| 15 | 664 1 |

| 82 | 123888505 2 |

IX OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2019 / QuestÃ£o em homenagem aos bons momentos de descontraÃ§Ã£o jogando Truco pelo IF e viagens com essa turma maravilhosa da Comp. Ã nÃ³is Cleison da carta amarela haha


# Problem 2956

Descrição
----------

The derivative of a function **y = f(x)** at a point **x = x0**, is equal to the value of the trigonometric tangent of the angle formed by the geometric tangent to the representative curve of **y = f(x)**, at the point **x = x0**, the derivative is the angular coefficient of the line tangent to the graph of the function at point **x0**.

The derivative of a function **y = f(x)** can also be represented by the symbols:

**y'**, **dy/dx** ou **f ' (x)**.

The derivative of a function **f(x)** at point **x0** is given by:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-a.png)

In classical geometry, the line tangent to the graph of the function f in a was the only line that passed through the point (a, f (a)) that did not find the graph of f across, meaning that the line did not pass directly through the graph. The slope of the secant to the graph of f in the image above, which passes through the points (x, f (x)) and (x + h, f (x + h)) is given by the quotient of Newton:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-b.png)

An alternative definition is: The function f is differentiable in ***a*** if there exists a function **Ïa** of I in continuous R in a such that:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-c.png)

For example, if we consider the function f of R in R defined by f (x) = xÂ² + x - 1, it is differentiable in 0. It is possible to observe in the image below the graphs of the constraints of that function at intervals [-1 , (1) and [-1 / 10,1 / 10] and it is clear that while the former is rather curved (and hence f (x) - f (0) is far from linear) is practically indistinguishable from a line segment (from slope 1). In fact, the more the graph is enlarged near (0, f (0)), the closer it is to being linear.

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-d.png)

When we derive the derivative of a function, the result is also a function of x and as such can also be differentiated. Calculating the derivative again yields the second derivative of the function f. Similarly, the derivative of the second derivative is called the third derivative, and so on. We can refer to the subsequent derivatives of f by:

![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-e.png)

If f is a function with real values ââin R, then the partial derivative of f measures its variation in the direction of the coordinate axes. For example, if f is a function of x and y, then its partial derivative measures the change in f in the x-direction and y-direction. However, they (partial derivatives) do not directly measure the variation of f in any other direction, such as that along the diagonal line y = x. These are measured using the directional derivatives. We can calculate the derivative of a function with 13 variables by means of ... "fake news, ok? There's nothing derived here. " This exercise is just for everyone learning to read something without judging by the titles and long texts. Given the base and height of a triangle, show your area. "Or will you say you forgot how to calculate triangle area too? Paulo Gueedes! "

Input
-----

Two floating point values ââ**P** and **T (0 < P**, **T â¤ 100000.00000)**, up to 5 decimal places, which indicate respectively the base and height of any triangle.

Output
------

Real value, with 5 decimal places, representing the area of ââthe triangle, next to the fake message: "We conclude that, given the input limit, the answer would be: y = f (x) =". Two spaces after the ':'.


| Input Samples | Output Samples |
| --- | --- |
| 1232.34343 323.98566 | Concluimos que, dado o limite da entrada, a resposta seria:  y = f(x) = 199630.79976. |

| 4.32434 3.23232 | Concluimos que, dado o limite da entrada, a resposta seria:  y = f(x) = 6.98883. |

| 2398.32323 132324.12122 | Concluimos que, dado o limite da entrada, a resposta seria:  y = f(x) = 158678006.90563. |

IX OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2019


# Problem 2978

Descrição
----------

Mike often needs to know if he could place a rectangular card of size **A** x **B**into an envelope of size **C** x **D** . In order to be faster, Mike doesnât really try to put a card into an envelope, he just places a card on the table and then tries to cover it with an envelope. Of course, both the card and the envelope can be rotated, but they cannot be folded.

Now, Mike wants to be even faster. He decided to find the answers for all sizes of cards and envelopes he operates with. Thatâs where you jump in. Your program should compute the answer for one particular case. The program should work the same way Mike does his tests, so in boundary cases the answer is âyesâ.

Input
-----

The first line contains four integers **A**, **B**, **C** and **D** and delimited by a space. All values are less than 2x109.

Output
------

The output contains only one string: âyesâ or ânoâ (without quotes).


| Input Sample | Output Sample |
| --- | --- |
| 2 3 3 4 | yes |

MDCS - Bubble Cup 2011


# Problem 2981

Descrição
----------

Earlier this year the Federal Government announced a budget blockade of several Federal Universities across the country and many of them have said they are unable to maintain activities by the end of the second semester of 2019. UFSC, for example, will only have resources to work until mid-October, but it is not known exactly when it will close.

Today, September 20, the financial sector has released the cash available amount and the daily cost estimate to keep the university open. As the university's economic team is busy trying to find solutions to extend the operation of the institution, you have been asked to help by calculating how many more days UFSC will be open and informing when it will close.

UFSC will only remain open as long as there are resources to maintain the university for a full day, when the remaining cash is not enough to cover the short daily, UFSC closes.

Input
-----

The input consists of two integers **C** and **G** (1 < **C**, **G** < 231) representing respectively the cash value that UFSC currently has and the daily expenditure to keep the university open. Today's cost has already been discounted from the cash available.

Output
------

Print, as the example provided, a single line containing the day UFSC will close in case the government does not release the funds.

UFSC closing data is guaranteed to be between September 21st and October 31st.


| Input Samples | Output Samples |
| --- | --- |
| 17088000 712000 | A UFSC fecha dia 15 de outubro. |

| 2850 300 | A UFSC fecha dia 30 de setembro. |


# Problem 2983

Descrição
----------

As stated in the title of the problem, not all problems will be about the strike, and this particular problem will be quite easy. Given a list of any positive integers, your task will be to tell how many and which of those numbers are prime. Just to say it's too easy, print the list in ascending order without repetition, as the same number may appear more than once in the entry.

Just to remember, a prime number is that number that is divisible only by 1 and by itself.

Input
-----

The first line has an integer **N** (1 â¤ **N** â¤ 1.000) that indicates how many numbers the list has. The next **N** lines have an integer **X** (0 â¤ **X** â¤ 109 + 7). Each of the numbers to check.

Output
------

Print a line with an integer **Y**, the total of different prime numbers in the list. On the next line print the **Y** prime numbers from the list, separated by a comma and a blank space. After the last number in the list print a full stop. Don't forget the "\ n" at the end. If there is no prime number in the list, leave the second line of the output blank.


| Input Sample | Output Sample |
| --- | --- |
| 7 1 2 7 5 2 6 3 | 4 2, 3, 5, 7. |


# Problem 2986

Descrição
----------

Once, while studying for the Porgramption Marathon, Tobias and I come across an interesting problem, I hope you enjoy it too.

There is a staircase with **N** steps. You can choose to go down 1, 2, or 3 steps at a time with each move. How many different ways could you go down this stair with **N** steps?

Input
-----

A single integer **N** (1 â¤ **N** â¤ 1,000,000), the number of stairs in the ladder.

Output
------

A single integer, the number combinations of different ways down the ladder. The answer may be a little big, so print the rest of the division by our favorite cousin (109 + 7).


| Input Samples | Output Samples |
| --- | --- |
| 1 | 1 |

| 5 | 13 |

| 1000 | 509672692 |


# Problem 3002

Descrição
----------

Lilly lives in a country where her government charges her many taxes. In this country, the rule is: if your income is **N**, you will have to pay the value of the largest N divisor in taxes. For example, if **N** is 25, you will have to pay 5 for taxes, if for 2, you will have to pay 1.

Lilly is clever, as the saying goes, the world is the smart one, and will divide her income in separate quantities, so that the sum of each part equals **N**, and thus be able to pay less taxes. For example, if she has 24 of income and will divide into parts being 20, and 4, she will have to pay the sum of the highest divisor of each, which in this case is 10 + 2 = 12, which is not necessarily better division in as many parts as possible.

After a long programming marathon, Lilly has to pay her taxes this very day, but she has no time to figure out a way to minimize the amount she will have to pay, so she asked you to create a program that calculates this amount. Portions of size 1 are not possible as it would be very obvious to the government that Lilly is cheating.

Input
-----

Contains an **N** (2 â¤ **N** â¤ 2 \* 109).

Output
------

An integer representing the minimum total tax Lilly will pay.


| Input Samples | Output Samples |
| --- | --- |
| 4 | 2 |

| 27 | 3 |

IX OlimpÃ­ada Interna de ProgramaÃ§Ã£o do IFSULDEMINAS - OLIP 2019 / E viva a matemÃ¡tica!


# Problem 3004

Descrição
----------

One company wants to send a customer an envelope to get an answer and wants to know if it is possible to put that envelope inside another. Both envelopes are rectangular and the first can only be placed inside the second if its dimensions are both smaller. Given the size of the two envelopes, answer whether or not you can put the first one inside the second.

Input
-----

The input consists of many tests. The first line contains the number of test cases, an integer **n (1 â¤ n â¤ 20)**,  The next n lines contain, each one, a test case, composed of four integers:  the first two integers are the dimensions of the first envelope e the last two, the dimensions of the second envelope.

Output
------

For each test case print, in one line:

. **'S'** if the first envelope can be put inside the second one.

Otherwise, print **'N'**.


| Input Sample | Output Sample |
| --- | --- |
| 3  10 10  10 20  19 2 3 20  2 20 5  15 | N  S  N |


# Problem 3007

Descrição
----------

Lucas has a lot of tokens with integer values ââstamped on them. He started playing with tokens containing only values ââ3 and 7 and realized that he could collect tokens to make a total of 3, 6, 7, 9, 10, 12,13, 14, etc., but could not form sets whose sum was 4 , 5, 8 or 11. He wondered if 11 would be the largest sum for which such sets could not be formed. Well, the german mathematician Frobenius had already solved this problem for 2 types of values ââand 11 is really the right answer for this case. Given the value tokens **a** and **b**, this problem can only be solved when **MDC (a, b) = 1** and the largest sum that cannot be obtained is given by     **a \* b-(a+b)**. But the problem is still open when you have more than two types of values. Write a program to help Lucas find the largest sum that can't be obtained using up to 10 different token types.

Input
-----

The input consists of many tests. The first line contains the number of test cases, an integer **n (1 â¤ n â¤ 20)**,  The next n lines contain, each one, a test case. The first integer int each line, **q (2 â¤ q â¤ 10)**, indicates how many different kinds of tokens exist. This number is followed by **q** integers **pi ( 2 â¤  pi  â¤ 1000)**, the values of the tokens.

Output
------

For each test case print, in one line, the maximum sum that can not be obtained with the kinds of tokens given. If this value is unlimited or greater than 1,000,000, print -1.


| Input Sample | Output Sample |
| --- | --- |
| 3  2 3 7  3 46 66 78  2 995 997 | 11  -1  990023 |


