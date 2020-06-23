"""
Completed: 22.06.20
Evaluating polynomials.
"""

def eval_polynomial(poly, x):   #evaluates polynomials. e.g. f(x).
    total = 0
    for i in range(len(poly)):
        total += poly[i] * (x**i)
    return total

def add_polynomial(p, q):       #adds two polynomials together.
    if len(p)>=len(q):
        big=p
        small=q
    else:
        big=q
        small=p
    result = []
    for i in range(len(big)):
        if i>=len(small):
            small.append(0)
        result.append(big[i] + small[i])
    return result

def product_polynomial(p,q):        #finds the product of two polynomials.
    if len(p)>=len(q):
        big=p
        small=q
    else:
        big=q
        small=p
    result=[]
    for i in range(len(big)+len(small)-1):
        result.append(0)
    for i in range(len(big)):
        if i>=len(small):
            small.append(0)
        for j in range(len(small)-1):
            result[i+j] += big[i]*small[j]
    return result

def to_latex(p):        #outputs the polynomail so that it's readible by latex.
    output=""
    for i in range(len(p)):
        if i==0:
            output = str(p[i])
            last=p[i]
        elif p[i] != 0 and p[i] != 1 and last>0:
            output = str(p[i]) + "x^{" + str(i) + "}+" + output
            last=p[i]
        elif p[i] != 0 and p[i] != 1 and last<0:
            output = str(p[i]) + "x^{" + str(i) + "}" + output
            last=p[i]
        elif p[i] == 1 and last>0:
            output = str(p[i]) + "x+" + output
            last=p[i]
        elif p[i] == 1 and last<0:
            output = str(p[i]) + "x" + output
            last=p[i]
    return output



q = [2,0,3]
p = [1,-7,0,4]
x = 0

print(to_latex(p))