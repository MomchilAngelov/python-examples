import sys, os

def generate_string(iteration = 1):
    generated_string = ''

    generated_string = "for x in range(int(" + str(number_of_palatki) + ")):\n"
    if iteration > 1:
        for x in range(1, iteration):
            generated_string = generated_string + x*"\t" + "for " + variable_names[x] \
            + " in range(" + variable_names[x-1] + "+1, number_of_palatki): \n"

    generated_string = generated_string + "\t"*(iteration) + "if (number_of_students < "
    for x in range(0, iteration):
        generated_string = generated_string + "people[" + variable_names[x] + "] + "
    generated_string = generated_string + "+ 1) and (weight_carrying >= "
    for x in range(0, iteration):
        generated_string = generated_string + "weight[" + variable_names[x] + "] + "
    generated_string = generated_string[:-2]
    generated_string = generated_string + "): \n" + (iteration+1)*"\t"
    generated_string = generated_string + """print("Палатките """
    for x in range(0, iteration):
        generated_string += "{" + str(x) + "} "
    generated_string = generated_string + "са решения!\".format("
    for x in range(0, iteration):
        generated_string = generated_string + variable_names[x] + "+1,"
    generated_string = generated_string[:-1]
    generated_string += "))"

    if iteration == number_of_palatki:
        generated_string = generated_string + "\n" + (iteration+1)*"\t" + "sys.exit(0)"

    return generated_string

data = input("Брой ученици и колко нацепен е Ангел: \n")
data2 = input("4 двойки тегло/хора: \n")

number_of_palatki = 5
variable_names = ['x', 'y', 'z', 'j', 'k', 'l', 'm', 'n']

weight = []
people = []

number_of_students, weight_carrying = data.split()

number_of_students = int(number_of_students)
weight_carrying = int(weight_carrying)

for idx, val in enumerate(data2.split()):
    if idx%2 == 0:
        weight.append(int(val))
    else:
        people.append(int(val))

for x in range(1, number_of_palatki+1):
    code = generate_string(x)
    #print(code)
    cc = compile(code, '<string>', 'exec')
    exec(cc)