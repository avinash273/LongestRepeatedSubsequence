
import sys

#This Funtion takes Input_Sequence from command line
#uses dynamic programming approach to 
def Longest_Repeated_Sub_Sequence(Input_Sequence):
    String_Length = len(Input_Sequence)
    Sequence_Array = [[0 for x_axis in range(String_Length+1)] for y_axis in range(String_Length+1)]

#x_axis and y_axis vaiables control the matrix operations and the index postion of the array.
#To ensure that we do not allow overlapping indexes in comparison we omit such records to be included
#By including x_axis!=y_axis overlapping index is avoided	
    for x_axis in range(1, String_Length + 1):
        for y_axis in range(1, String_Length + 1):
            if (Input_Sequence[x_axis-1] == Input_Sequence[y_axis-1] and x_axis != y_axis):
                Sequence_Array[x_axis][y_axis] = 1 + Sequence_Array[x_axis-1][y_axis-1]
            else:
                Sequence_Array[x_axis][y_axis] = max(Sequence_Array[x_axis][y_axis-1], Sequence_Array[x_axis-1][y_axis])

#Declaring Results vaiable
    Results = ''
#Reinitializing the matrix variables to String_Length	
    x_axis = String_Length
    y_axis = String_Length
    while (x_axis > 0 and y_axis > 0):
        if (Sequence_Array[x_axis][y_axis] == Sequence_Array[x_axis-1][y_axis-1] + 1):
            Results += Input_Sequence[x_axis-1]
            x_axis -= 1
            y_axis -= 1

        elif (Sequence_Array[x_axis][y_axis] == Sequence_Array[x_axis-1][y_axis]):
            x_axis -= 1
        else:
            y_axis -= 1

#Reversing the Results as the Longest_Repeated_Sub_Sequence funtion follows bottom  while traversing for the results			
    Results = ''.join(reversed(Results))
#Return results back to the function where were are printing the output
    return Results

#Input_Sequence received from command line
#Performing Validations
#Checking for correct input given or not

if __name__ == "__main__":
    '''
    try:
        Input_Sequence = sys.argv[1]
    except IndexError:
        print("You have not entered a valid Input in command line\nPlease Try Again in the Below Format!!!")
        print("Sample Usage: >python dynamic.py ATACTCGGA")
        sys.exit(1)
        '''
        

#Calling the function and passing input
    Output_Data = Longest_Repeated_Sub_Sequence('ATACTCGGA')
    if (Output_Data == ""):
        print("No Longest Repeated Subsequence Present for the entered input\nPlease try a different input")
        print("Sample Usage: >python dynamic.py ATACTCGGA")
    else:    
        print("Longest Repeated Subsequence Using Dynamic Approach:",Output_Data)
#Code End