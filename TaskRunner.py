import argparse
from exceptions import * 
import importlib
from os import path 

def find_module(problem_name, input_file):
    module, file_name=None, None
    try: 
        module=importlib.import_module(problem_name)
    except ImportError: 
        raise ProblemNotFound("{} not found ".format(problem_name))
    dir_name=path.dirname(module.__file__)
    
    if input_file is None: 
        file_name=path.join(dir_name, 'input.txt')
    else: 
        file_name=path.expanduser(input_file)
    
    if not path.exists(file_name): 
        raise InputFileNotFound("{} file not found ".format(file_name))


    return module,file_name 

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
    print("Currently running the {} module with input file {}".format(module, input_file))    
