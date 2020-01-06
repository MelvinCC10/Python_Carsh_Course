""" Read entier file """
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

""" Read file line by line """
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

""" Write to file """
outputFilename = 'SimpleOutputFile.txt'
with open(outputFilename,'w') as file_object:
    file_object.write("I love programing.\n")
    file_object.write("programing loves me.\n")

""" append to file """
with open(outputFilename, 'a') as file_object:
    file_object.write("I would like to know the meaning of life.\n")
    file_object.write("maybe the meaning of life can be programed?.\n")
