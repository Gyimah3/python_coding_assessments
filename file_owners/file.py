# This function must contain your implementation of the solution
def solution(files, **kwargs):
    owners = defaultdict(list)
    for file, owner in files.items():
        owners[owner].append(file)
    return 


# The main function where you must built the user-interface as
# a command-line interface for everyone to use the made function
# using this interface
def main():
    files = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'}
 return solution

if __name__ == "__main__":
    main()
