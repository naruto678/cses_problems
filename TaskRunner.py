import argparse
from exceptions import * 

def find_module(problem_name, input_file): 
    return None, None


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("problem", help='specify the problem name that you want to submit ')
    parser.add_argument("--file", help='specify the path of the input file name. If not specified it would use the input.txt file present in the subfolder of the problem directory')
    args=parser.parse_args()

    module, input_file=find_module(args.problem, args.file)

    if module is None: 
        raise ProblemNotFound("Problem name not present in the current directory . Please correct the problem name or create a problem directory of the same name")
    if input_file is None:
        raise InputFileNotFound(" Input file not present in the specified problem direcotry . Please provide a path to the input file by specifying the file name inline by using the --file option . For more run the script ./run.sh with -h option ")

        
    '''
    The main objecttive of the module is to be able to run soem file directly . 
    usage would be as follows: 
        The directory would be as follows: 
            cses_problems: 
                    -> Problem1: 
                        input.txt
                        problem_statement.txt
                    ->Problem2: 
                        input.txt
                        problem_statment.txt

        ./TaskRunner.py <problem-name>
        ./TaskRunner.py <problem-name> --file <file-name to be used instead of the input.txt file present in the problem name directory >
        
    
    Exception_handling : 
        if input.txt is not found then prompt the user to put the input.txt file there ---> Future versions for this should try to login to the cses_problme set site 
            and try parsing the html and getting the input to check it out . This is also would be used to document my journey of going through the cses problem set

    Ideas: 
    Also idea could be to run a single command and get the entire cses problem set and make the directory directly . 
    Currently let us just support python and then we could move on to java / go-lang or rust. my new fav languages



    '''
    print("Please visit later. Currently at work ")

