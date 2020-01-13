# parking-lot-shell
This is a basic command line program that could be used for keeping track of vehicles entering and leaving a parking lot.  It has some basic search utilities included for finding where vehicles with certain properties are parked.  

This project was built and tested using Python 3.7 using only the python standard library.  

To run the shell, use "python3 pl_shell.py" at the base of the project  
To use a file filled with input commands, use "python3 pl_shell.py file_inputs.txt > file_output.txt"  
To run tests, use "python3 -m unittest discover -v" at the base of the project  

There were no clear requirements for exception handing, but it was important to handle them in some way. The default behavior from an exception was to throw the user out of the shell.  This causes workflow to be interupted, and all memory of the objects to be forgotten, as all data is held within the python objects with no persistance outside of the program.  My solution was to simply wrap the commands in a general exception hander, which refers the user to documentation for correct usage.

