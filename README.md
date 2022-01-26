# RUNCPP
As the name implies, this Python project aims to be a helper in creating C/C++ programs, automating the boring stuff of an otherwise incredibly rewarding task: programming in C/C++. Managing many projects through the terminal might be a bit boring sometimes: cd-ing to the directories, running on debugs, compiling them again, changing directory to another file that needs to be updated... 

RUNCPP seeks to make the engineer/developer life easier by storing the source files and their compiled binaries' locations under an alias that the user choses (to make it easier to remember). Saved on a .txt file in the same directory as the runcpp.py for ease of access. 

The current version of the project sports the creation of an alias (saving the location of the source file) as well as creating the compiled binary through the use of `g++/gcc`

Further updates will come, adding many new features.

## How to use it
* 'runcpp file\_name\_alias' [`-c` or `--Compile`] -> compiles the executable file. If '', then binary name will be the same as the 		original file name, without the extention. If '--Compile', the user will specify a name for the binary name to go by

* 'runcpp file\_name\_alias' [`-r` or `--Run`] -> runs the executable file [future]

* 'runcpp -c file\_name\_alias' [`-c` or `--Candr`] -> compiles and runs the file [future]

* 'runcpp -l file\_name\_alias \<path/to/file>' [`-l` or `--Location`] -> saving a new/updating file alias

* 'runcpp -d file\_name\_alias' [`-d` or `--Delete`] -> deletes the alias from the aliases.csv [future]

* 'runcpp -o file\_name\_alias' [`-o` or `--Open`] -> opens the source code (if available) in the preferred editor [future]
       [`-o`, `--with` or `--openwith`] will open the source code in the specified editor -- one time thing [future]

* 'runcpp -s' [`-s` or `--Show`] -> lists all currently aliased files. It also checks if all files are still on [future] their last known location

* 'runcpp --Help' [`--Help`] -> prints help page


## Features that will be brought in future updates
* Refactoring of the codebase to make it easier to comprehend

* Automatically setting the binary name as the same as the source file if no name is passed after `-c`

* Add run, 'compile and run', delete, open and show commands

* SQL integration

* Support to Windows, as well as to other compilers (e.g., clang)

* A bash script for calling RUNCPP from the terminal without .py
