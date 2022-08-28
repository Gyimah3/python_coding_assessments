# This function must contain your implementation of the solution
def solution(input1, **kwargs):
    reversed_input1 = input1[::-1]
    status=1
    if(input1!=reversed_input1):
        status=0
    return status


    
   
   


# The main function where you must built the user-interface as
# a command-line interface for everyone to use the made function
# using this interface
def main():
   input1 = input("Enter the input1: ")
status= check_palindrome_1(input1)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")

if __name__ == "__main__":
    main()
