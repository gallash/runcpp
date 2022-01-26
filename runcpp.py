#!/usr/bin/env python3

# Developed by Phillip Gallas
#
# RUNCCPP (or runcpp) does what its name suggests: it runs C/C++ files
# through the usage of the g++ or gcc compilers
# 
# How to use it it:
# 'runcpp file_name_alias' ['' or --Compile] -> compiles the executable file. If '', then binary name will be the same as the 		original file name, without the extention. If '--Compile', the user will specify a name for the binary name to go by
# 'runcpp file_name_alias' [-r or --Run] -> runs the executable file [future]
# 'runcpp -c file_name_alias' [-c or --Candr] -> compiles and runs the file [future]
# 'runcpp -l file_name_alias <path/to/file>' [-l or --Location] -> saving a new/updating file alias
# 'runcpp -d file_name_alias' [-d or --Delete] -> deletes the alias from the aliases.csv [future]
# 'runcpp -o file_name_alias' [-o or --Open] -> opens the source code (if available) in the preferred editor [future]
#       [-o --with or openwith] will open the source code in the specified editor -- one time thing [future]
# 'runcpp -s' [-s or --Show] -> lists all currently aliased files. It also checks if all files are still on [future]
# their last known location
# 'runcpp --Help' [--Help] -> prints help page


import os
import csv
import sys
import glob
import argparse




# ---- The function receives arguments, parses them, and returns the object 'args'
def parsing():
    parser = argparse.ArgumentParser(description=__doc__)


    # Devo transformar Alias em optional flag
    parser.add_argument(
        'Alias',
        type=str,
        help="A nickname to reference the file"
    )

    # I want to receive two strings at the same time: file_alias and file_location
    parser.add_argument(
        '-l','--Location',
        type=str,
        help="Location of the file to be indexed"
    )
    
    parser.add_argument(
        '-c','--Compile',
        type=str, # Would have to add 'default=' or 'store_false'
        help="Specify a name for the binary and then compile it"
    )
    
    #parser.add_argument(
    #    '-r','--Run',
    #    type=str,
    #    default=True,
    #    help="Specify a name for the binary and then compile it"
    #)
    
    parser.add_argument(
        '-d','--Delete',
        type=str,
        help="Specify a name for the binary and then compile it"
    )

    # parser.add_argument(
    #     '-r','--run', # 'run',
    #     metavar= 'file',
    #     type=str,
    #     help = "Run the script. E.g., 'runcpp run file'"
    # )

    # parser.add_argument(
    #     'candr',
    #     metavar= 'file',
    #     type=str,
    #     help = "Compile and run the script. E.g., 'runcpp run file'"
    # )

    #parser.add_argument(
    #    '-s','--Show','--List',
    #    type=str,
    #    help="Lists all currently aliased files"
    #)
    
    parser.add_argument(
        '--Help',
        help="Prints help menu"
    )

    args = parser.parse_args()
    return args





# ---- Control: selects what to do
def control(args):
    # First mandatory check
    # Checking whether an alias was given or if it resembles one
    for element in ['/','~','\\',':']: # Linux, MacOs and Windows
        if element in args.Alias:
            sys.exit("Need to pass an alias, not a location.")




    # Checking whether the given location resembles a location. 
    # If it does, then adds to or updates the aliases.csv
    if args.Location is not None:
        for element in ['/']:
            if element not in args.Location:
                print(args.Location)
                # I need to find a way to parse these elements: '~','\\',':'
                sys.exit("Need to pass a location (absolute path).")
                
        else:
            manage_aliases(args,'add')

    
    # Using 'elif' instead of 'if' makes the program accept only one additional flag to work with 

    # If Delete was passed, it checks whether the alias or location exists in the database
    # If they do, deletes the row by copying the contents to another file named aliases.csv 
    # ignoring the row to be deleted
    elif args.Delete is not None:
        manage_aliases(args,'delete')

    # elif args.Help is not None:
    #     print("Printing help menu")


    #elif args.Run:
    # 	run_alias(args)
    	
    # elif args.Show:
    #     show_aliases(args)

    elif args.Compile is not None:
        compile_alias(args,args.Compile)

    else:
        # If no flag was passed by the user, the default action will be to compile the program
        # CALL g++ ON THE ALIAS'S LOCATION'S FILE AND AFTER THE COMPILER IS DONE, RUN THE SCRIPT
        compile_alias(args)



def compile_alias(args,binaryname=None):
    # Retrieve alias location
    with open('aliases.csv','r',newline="") as csvfile:
        file = csv.reader(csvfile,delimiter=',')
        for row in file:
            if row[0] == args.Alias:
                filelocation = row[2]
    
    if binaryname is None:
        binaryname = filelocation[filelocation.rfind('/')+1:] # filename.cpp
        binaryname = binaryname[0:binaryname.rfind('.')] # filename
                
    # I have to add the locale of the original fine
    os.system(f'cd {filelocation[:filelocation.rfind("/")]} && g++ {filelocation} -o {binaryname}') 
    # Can sport more options if needed be, in which case, make proper alterations
    
    # Add to csv [4] [future]






def manage_aliases(args,action:str):
    # Reads, adds, removes and updates to aliases.csv

    # Tries to open file. It aliases.csv does not exist, then create it (except branch)
    # First, check whether the alias is already there. If it is, then updates. 
    if action == "add":
        try:
            with open('aliases.csv','r',newline="") as csvfile:
                file = csv.reader(csvfile,delimiter=',')
                for row in file:
                    if row[0] == args.Alias:
                        # If the user passed an existing Alias, it can mean that he/she wants to 
                        # update the location. Prompt the user:
                        print(args.Alias,"already exists in database.")
                        prompt_user = input("The program is about to update the location of 'Alias' from\n",
                            row[2],
                            "\nto\n", 
                            args.Location,".\n",
                            "Do you want to proceed? ['Y', 'yes' to update, other input to exit]")

                        if prompt_user.lower() in "yes" or prompt_user.lower() in "y":
                            print("Updating the alias is yet to be implemented")

                            # Find the location of the Alias in the aliases.csv
                            # Update the answer
                            # Test if it was updated
                            
                            print("The location pointed by Alias was updated.")
                            os._exit(1)
                        else:
                            print("Answer interpreted as not wanting to update the Alias.")
                            os._exit(1)

                else:
                    # If Alias is new, adds to the end
                    # The Exception is raised simply to avoid repeating too many lines of code
                    raise Exception
        
        except:
            # If there is no aliases.csv, then create it together with its first entry
            with open('aliases.csv','a',newline="") as csvfile:
                file = csv.writer(csvfile,delimiter=',')
                file_name = args.Location[args.Location.rfind('/')+1:] # Finds file name from its path
                if file_name[file_name.rfind('.')+1] not in ["cpp", "c", "C", "cxx", "c++", "h", "hpp"]:
                    print(file_name,"is not a C/C++ file.")
                    os._exit(1)

                file.writerow([args.Alias,file_name,args.Location])
                print(file_name," was added under the alias: '",args.Alias,"'.",sep="")
                # os._exit(1) # If I add this too soon, the buffer will not send the message to the file

    if action == "read":
        sys.exit("Yet to be implemented")


    if action == "delete":
        # Special string "args.Delete = '_all'" deletes all rows in the aliases.csv
        # Prompt the user 
        sys.exit("Yet to be implemented")
    



if __name__ == "__main__":
    args = parsing()
    control(args)
