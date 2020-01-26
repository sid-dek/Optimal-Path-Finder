def compare_output(file_1 , file_2):
    file1=open(file_1,'r')
    file2=open(file_2,'r')
    i=0
    print ("\n\nFor ",file_1,' and  ',file_2,' :')
    for line1,line2 in zip(file1,file2):
        if(line1.strip() == line2.strip()):
            print(i+1,": Pass")
        else:
            print(i+1,": Fail")
        i+=1


## To generate a random matrix to try your code on
import random
def generate_matrix(method):
    matrix_height = 100
    matrix_width = 100
    no_targets = 50

    file = open('last_matrix.txt','w+')

    # Print tree method
    k = method + "\n"
    file.write(k)
    # Print w h
    k = str(matrix_width) + " " + str(matrix_height) + "\n"
    file.write(k)
    # Print start node
    k = "0 0\n"
    file.write(k)
    # Print elevation
    k = "7\n"
    file.write(k)
    # No of targets
    k = str(no_targets) + "\n"
    file.write(k)
    # Print targets
    for i in range(no_targets):
        k = str(random.randrange(matrix_width-1)) + " " + str(random.randrange(matrix_height-1)) + "\n"
        file.write(k)
    for i in range(matrix_width):
        for j in range (matrix_height-1):
            k = str(random.randrange(10)) + ' '
            file.write(str(k))
        file.write(str(random.randrange(10)))
        file.write("\n")
    file.close()


""" To use the above functions 
1. compare_output('file_to_compare' , 'destination_from_where_to_compare')
2. make_matrix("type_name_of_method_here:A*/UCS/BFS")