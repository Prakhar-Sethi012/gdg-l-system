import turtle

#generating l-system final string

def generate(axiom,rule,n):
    current_str=axiom
    for i in range(n):
        pat=''   
        for j in current_str:
            if j in rule:
                pat+=rule[j]
            else:
                pat+=j
        current_str=pat
    return current_str

#function to draw the turtle according to the final string

def drawing(answer,angle,step):
    p=turtle.Turtle()
    sc=turtle.Screen().bgcolor("white")
    p.color("cyan")
    p.speed(0) 
    
    for i in answer:
        if i=='F':
            p.forward(step)
        elif i=="+":
            p.right(angle)
        elif i=="-":
            p.left(angle)

    turtle.done()

if __name__=="__main__":
    print("L-System Turtle Visualiser :")
    
    axiom=input("Enter axiom :")
    count=int(input("Enter number of rules :"))

    rules={}
    
    # A for loop for taking input of the rules in the form of dictionary
    for i in range(count):
        value = input("Enter symbol to replace: ")
        replace = input(f"Enter replacement for {value}: ")
        rules[value] = replace
    
    n=int(input("Enter Number Of Iterations :"))
    angle=float(input("Enter Angle (In Degrees) :"))
    step=float(input("Enter Length To Move Forward :"))

    answer=generate(axiom,rules,n)
    drawing(answer,angle,step)


