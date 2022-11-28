import csv
import random
import turtle

A = []
B = []
C = []
D = []

COLORS = ["orange", "lightgreen", "pink", "gold"]

def read_data(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            A.append(record[0].strip())
            B.append(record[1].strip())
            C.append(record[2].strip())
            D.append(record[3].strip())

def generate():
    turtle.reset()
    screen = turtle.Screen()
    screen.bgcolor(COLORS[random.randint(0, len(COLORS) - 1)])
    
    string = A[random.randint(0, len(A) - 1)] + " " + B[random.randint(0, len(B) - 1)] + " " + C[random.randint(0, len(C) - 1)] + " " + D[random.randint(0, len(D) - 1)]
    
    turtle.write(string, move=False, align='center', font=('Arial', 18, 'normal'))
    turtle.hideturtle()
    quit = input()
    if quit != "" and quit[0].lower() == "q":
        return False
    return True

def main():
    read_data("Pep_Talk_Generator.csv")
    print("Press enter to get a pep talk! To quit, type 'quit'")
    input()
    q = generate()
    while (q):
        q = generate()

if __name__ == '__main__':
    main()