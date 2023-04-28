#Create a function
def oddeven():
    #Open text file containing the numbers and output text files for separation
    with open("twenty.txt") as input_file, open("odd.txt", "a") as output_odd, open("even.txt", "a") as output_even:
        #Convert string to integer
        for line in input_file:
            integer = int(line)
            #Separate odd and even numbers
            if integer % 2 == 0:
                output_even.write(str(integer) + "\n")
            else:
                output_odd.write(str(integer) + "\n")
#Start Program
oddeven()
