# Ask the user if they are planning on building a python script
yesno1 = input("Let's get started. Do you want to build a python script? (y),(n)")

    if (yesno1 == "y"):
        
        # Determine what type of files or data we are to be working with
        # Need to figure out how to multiple select 
        python_data_prompt_1 == input("Great! What type of data/files are you working with? (CSV, XLXS, .txt,)") 

            if python_data_prompt_1 == "CSV":
                # Demonstrate how to load the file
                print("CSV - Awesome, here are some options on how to load the data.\
                    \
                    # Require dependencies pandas and os\
                    file = os.path.join('..','Resources','samplefile.csv')\
                    dataset = pd.read_csv(file)\
                    \
                    # In order to write into the CSV\
                    with open('filepath','w',newline =') as csvfile:\
                    csvwriter = csv.writer(csvfile,delimiter = ',')"

                documentation_prompt_csv == input("If that doesn't help and you need further documentation, enter (d), if it worked, continue on with (n)ext")
                
                if (documentation_prompt_csv == "d"):
                    # Provide further documentation on how to open a CSV
                    print("'csv.reader'\
                        csv.reader(csvfile, dialect='excel', **fmtparams)\
                        Return a reader object which will iterate over lines in the given csvfile.\
                        csvfile can be any object which supports the iterator protocol and returns a string each time its __next__() method is called — file objects and list objects are both suitable.\
                        If csvfile is a file object, it should be opened with newline=''.\
                        [1] An optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV dialect.\
                        It may be an instance of a subclass of the Dialect class or one of the strings returned by the list_dialects() function.\
                        The other optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.\
                        For full details about the dialect and formatting parameters, see section Dialects and Formatting Parameters.\
                        >>> import csv\
                        >>> with open('eggs.csv', newline='') as csvfile:\
                        ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')\
                        ...     for row in spamreader:\
                        ...         print(', '.join(row))\
                        Spam, Spam, Spam, Spam, Spam, Baked Beans\
                        Spam, Lovely Spam, Wonderful Spam\
                        \
                        'csv.writer'\
                        (csvfile, dialect='excel', **fmtparams)\
                        Return a writer object responsible for converting the user’s data into delimited strings on the given file-like object.\
                        csvfile can be any object with a write() method.\
                        If csvfile is a file object, it should be opened with newline='' [1].\
                        An optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV dialect.\
                        It may be an instance of a subclass of the Dialect class or one of the strings returned by the list_dialects() function.\
                        The other optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.\
                        For full details about the dialect and formatting parameters, see section Dialects and Formatting Parameters.\
                        To make it as easy as possible to interface with modules which implement the DB API, the value None is written as the empty string.\
                        While this isn’t a reversible transformation, it makes it easier to dump SQL NULL data values to CSV files without preprocessing the data returned from a cursor.fetch* call.\
                        All other non-string data are stringified with str() before being written.\
                        >>> import csv\
                        >>> with open('eggs.csv', 'w', newline='') as csvfile:\
                        ...    spamwriter = csv.writer(csvfile, delimiter=' ',\
                        ...                            quotechar='|', quoting=csv.QUOTE_MINIMAL)\
                        ...    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])\
                        ...    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])\
                        \
                        'FOR MORE WAYS TO OPEN A CSV TRY GOOGLING IT'")

                if (documentation_prompt_csv == "n"):
                    # Ask if you are importing any more data/files 

                    next_prompt_1 == input("Will you be importing any other files? (y),(n)")
                    # Return to the Python data prompt

A short usage example:

Each row read from the csv file is returned as a list of strings. No automatic data type conversion is performed unless the QUOTE_NONNUMERIC format option is specified (in which case unquoted fields are transformed into floats).

A short usage example:










# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r" and computer_choice == "p"):
    print("You chose rock. The computer chose paper.")
    print("Sorry. You lose.")

elif (user_choice == "r" and computer_choice == "s"):
    print("You chose rock. The computer chose scissors.")
    print("Yay! You won.")

elif (user_choice == "r" and computer_choice == "r"):
    print("You chose rock. The computer chose rock.")
    print("A smashing tie!")

elif (user_choice == "p" and computer_choice == "p"):
    print("You chose paper. The computer chose paper.")
    print("A smashing tie!")

elif (user_choice == "p" and computer_choice == "s"):
    print("You chose paper. The computer chose scissors.")
    print("Sorry. You lose.")

elif (user_choice == "p" and computer_choice == "r"):
    print("You chose paper. The computer chose rock.")
    print("Yay! You won.")

elif (user_choice == "s" and computer_choice == "p"):
    print("You chose scissors. The computer chose paper.")
    print("Yay! You won.")

elif (user_choice == "s" and computer_choice == "s"):
    print("You chose scissors. The computer chose scissors.")
    print("A smashing tie!")

elif (user_choice == "s" and computer_choice == "r"):
    print("You chose scissors. The computer chose rock.")
    print("Sorry. You lose.")

else:
    print("I don't understand that!")
    print("Next time, choose from 'r', 'p', or 's'.")
