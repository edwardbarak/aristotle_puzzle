# Magic Hexagon
![*What the puzzle looks like.*](./images/newaristotle-1-of-2.jpg)

> **Description**
> Each row (not just horizontal, but also diagonal) add up to 38? There are 15 rows in all directions to complete, each made up of 3, 4 or 5 pieces. This brilliant concept allows you to complete the puzzle by using every number from 1 – 19. *([professorpuzzle.com](https://www.professorpuzzle.com/products/aristotles-number-puzzle/))*

There are **121,645,100,408,832,000** permutations for this puzzle. Certainly not something you want to brute force. 

## The Challenge
Write a program that doesn't take a month of 24/7 calculating to find all the possible answers.

## The Method
Using permutations and process of elimination, the program starts from the outer ring and works its way to the center in a spiral fashion.

If you go by the image above, it calculates the pieces in the following order:

1. Tiles 9, 11, & 18
2. Tiles 17 & 3
3. Tiles 19 & 16
4. Tiles 12 & 10
5. Tiles 13 & 15
6. Tile 14
7. Tiles 8 & 6
8. Tile 1
9. Tile 7
10. Tile 2
11. Tile 4
12. Tile 5

## Equations
### Functions
1. ![f(x)](./images/magic-hexagon-fx.png)
2. ![g(x)](./images/magic-hexagon-gx.png)
3. ![h(x)](./images/magic-hexagon-hx.png)

### Main Equation
![main1of2](./images/magic-hexagon-main1.png)
![main2of2](./images/magic-hexagon-main2.png)


## The Result
On my laptop, I'm able to get 12 solutions in  ~13s +/- 1s.
I won't post the answers here, but if you really want to know the answers, you can obviously just run the program using <code>python main.py</code>

## FAQ

**How do I run this?**
1. Clone this repository
- In the directory, run <code>pip install -r requirements.txt</code>
- Run main.py from your command line using <code>python main.py</code>

Depending on the specifications of the computer you are using, the code may take a few seconds to run. The output shows a list of arrays contained valid solutions.

**Why did you do this?**
Someone gave me this puzzle as a present, and I thought it was an interesting challenge.

## Some peformance tips and lessons learned:
- Most numpy functions compile to C. 
- You can do static typing with numpy.
- Loops kill your performance. Use list comprehensions instead. 
- Use iterators and generators.
- Use an efficient algorithim. If one doesn't exist, create one.
