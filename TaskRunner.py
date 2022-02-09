#!/usr/bin/pytho

import argparse
from exceptions import * 
import importlib
from os import path 
from contextlib import contextmanager
from typing import Callable 

@contextmanager
def chdir(changed_path : Path ): 
    older_path=os.getcwd()
    try: 
        yield os.chdir(changed_path)
    except: 
        print("Error while changing path")
    finally: 
        os.chdir(older_path)

def execute_module(module : Callable , input_file_name: str, dir_name : Path) -> str : 
    output=None 
    with chdir(dir_name): 
        output= os.execute_module(module) 
    return output 



def find_module(problem_name : str, input_file : str = 'input.txt')-> Optional[Callable, str]:
    module, file_name=None, None
    try: 
        module=importlib.import_module(problem_name)
    except ImportError: 
        raise ProblemNotFound("{} not found ".format(problem_name))
    dir_name=path.dirname(module.__file__)

    if not path.exists(file_name): 
        raise InputFileNotFound("{} file not found ".format(file_name))
    
    

    return module,

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("problem", help='specify the problem name that you want to submit ')
    parser.add_argument("--file", help='specify the path of the input file name. If not specified it would use the input.txt file present in the subfolder of the problem directory')
    args=parser.parse_args()
    if arg.file: 
        module, input_file,dir_name = find_module(args.problem, args.file)
    else: 
        module, input_file, dir_name = find_module(args.problem)

    if module is None: 
        raise ProblemNotFound("Problem name not present in the current directory . Please correct the problem name or create a problem directory of the same name")
    if input_file is None:
        raise InputFileNotFound(" Input file not present in the specified problem direcotry . Please provide a path to the input file by specifying the file name inline by using the --file option . For more run the script ./run.sh with -h option ")
    
    execute_module(module, input_file, dir_name ) 

    print("Currently running the {} module with input file {}".format(module, input_file))    
