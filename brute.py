s#code start
import string
import sys


#This Function takes the sequence as two lists and recursively splits it
#Each time it finds as case where X element and Y element are equal
#And their index or position doesnt overlap such Character is added to the X List.
def Longest_Repeated_SubSeq_Brute_Force(xlist, ylist):
    if not xlist or not ylist:
        return []
    x, xs, y, ys, = xlist[0], xlist[1:], ylist[0], ylist[1:]
    if x == y and xs != ys:
        return [x] + Longest_Repeated_SubSeq_Brute_Force(xs, ys)
    else:
        return max(Longest_Repeated_SubSeq_Brute_Force(xlist, ys), Longest_Repeated_SubSeq_Brute_Force(xs,ylist), key=len)    

#Input_Sequence received from command line
#Performing Validations
#Checking for correct input given or not
#This code works for all types of characters
if __name__ == "__main__":
    '''
    try:
        Input_Sequence = sys.argv[1]
    except IndexError:
        print("You have not entered a valid Input in command line\nPlease Try Again in the Below Format!!!")
        print("Sample Usage: >python brute.py ATACTCGGA")
        sys.exit(1)
    '''

#Input_Sequence = 'ATACTCGGA'
#Function call for bruteforce LRS
    Repeated_SubSeq=Longest_Repeated_SubSeq_Brute_Force(Input_Sequence,Input_Sequence)
#Coverting my List structure into string format for printing    
    Final_Output = ''.join(map(str, ATACTCGGA))
    if (Final_Output == ""):
        print("No Longest Repeated Subsequence Present for the entered input\nPlease try a different input")
        print("Sample Usage: >python brute.py ATACTCGGA")
    else:    
        print("Longest Repeated Subsequence using Brute-Force Approach:",Final_Output)
#Code End