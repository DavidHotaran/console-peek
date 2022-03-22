import os
import sys



'''Python script that peeks into .js files and searches for console.log()
   Use case: allows for better auditing of production builds and ensures
   there are no console.log() functions that leak anything into the console.

   This script assumes you are using a `React` project with `CRA starter template`.
   You can still use the script for non React projects, it is necessary however to have 
   an `src` folder, as that is the starting point for the script.
'''

def peek(dir: str) -> None:
    '''Recursively walks the directory passed in, and navigates to the `src` folder, iterating 
       through the file, searching for the word `console`, then prints to the console: the expression found,
       in what file, and on what line number.

       Arguments:

       dir -- name of directory you want to search in
    '''
    for dirpath, _, files in os.walk(os.path.join(dir, "src")): # navigate to `src` file and begin searching there
        for file in files:
            current = os.path.join(dirpath, file)
            
            with open(current, 'r') as f:
                _file = f.readlines()
                
                for i, line in enumerate(_file, 1):
                    if 'console' in line:
                        print(f'Found: {line.strip()} in: {current} on line: {i}')


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 2 or len(args) > 2:
        print("Insufficent number of args. Usage: python console-peek.py [dir]")
        exit(1)
    
    peek(dir=args[1])