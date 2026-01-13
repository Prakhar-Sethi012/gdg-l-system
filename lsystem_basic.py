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
b={}
print("Enter axiom :")
axiom=input()
print("Enter number of rules :")
rl=int(input())
for i in range(rl):
    print("Enter what to replace : \t")
    ch=input()
    print(f"Enter with which to replace {ch}: \t")
    ch1=input()
    b[ch]=ch1
print("Enter number of iterations :")
n=int(input())
print(generate(axiom,b,n))
