'''
Quadratic equation= ax^2+bx+c=0
where a,b,c are real and a!=0
Solution=(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
'''
a=1
b=5
c=6

alpha=(b**2-4*a*c)**0.5
solution1=((-b)+alpha)/(2*a)
solution2=((-b)-alpha)/(2*a)
print(f"The Given Quadratic Equation is {a}X^2+{b}X+{c}=0")
print(f"Solution for Given Quadratic Equation are{solution1} and {solution2}")