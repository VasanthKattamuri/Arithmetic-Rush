import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 1
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left)+ " " + operator + " " + str(right)
    # print(expr)

    #after generating the problem we also have to find the answer for the randomly gereated question

    answer = eval(expr)
    #eval function function in python evaluates the python expression if it is valid
    #instead of eval we can use if else conditions and say if + then add,if - then subtract....instead of that just use eval

    
    return expr,answer
    #The return expr line is not essential if you only want to print the generated expression. However, if you plan to use the generated 
    #expression (expr) outside of the generate_problem function, then return expr is necessary to pass the result to other parts
    #of your code.


wrong = 0
input("Press enter to start!")
print("----------------------")

expr,answer = generate_problem()
# print(expr,answer)

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + " : " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()


# total_time = end_time - start_time ---->Gives the time taken in decimals like 15.254612222
total_time = round(end_time - start_time,2) #Round it 2 digits


print("----------------------")
print("Nice Work, You finished in :",total_time,"seconds!")

print("Wrong answers :",wrong)
#for printing the number of wrong answers

correct = TOTAL_PROBLEMS - wrong
accuracy = (correct/TOTAL_PROBLEMS)*100
print("Your accuracy :",round(accuracy,2),"%")
#for printing the Accuracy





