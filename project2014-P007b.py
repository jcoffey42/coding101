# Created on a win8.1 system with IDLE
# project2014-P007b.py
# A program to decode a file of numbers that are the line and field for a
# sustitution code. You provide a text file to use as the key.
# This is a companion program to project2014-P007.py
# The original unencrypted messge will never be written to a file.


# First lets define some things

KeyFileName = "c:\data\key.txt" #The name of the key file
Message = "c:\data\secretmessage.txt" # the name message file



def decode(LineCnt,x):
    Continue = True # Prime the while loop
    Line = "" # Used to read in the key line
    LineCount = 0 # Used to keep track of which line we are on
    Working = [] # Used to split the Line for printing the word x
    LineCnt = int(LineCnt) # Convert the string to an interget
    x = int(x) # Convert the string to an interget
    while Continue:  # Decoding loop
        for line in key: # Read in a line of the key
            working = line.split(" ") # Split the key
            if (LineCnt-1) == LineCount: # Subtract one for old ways, and compare 
                print working[x] # Right line! Print the word from the key
                Continue = False  # End the loop
                return  # Return for the next code
            else:
                LineCount = LineCount + 1 # Not the right line, add one and do it again

    return # If thing slip just go back



# Now lets open the files
record=open(Message,"r") # Open the message file
key=open(KeyFileName,"r") # Open the message file


ans = True # Prime ans to keep the input loop running
work = [] # Setup the list for spliting the code
code = "" # Setup the string for reading in the message
while ans: # This is the beginning of the input loop

    # Get the message, one word at a time, to encode
    print " Decrypting your message"
    for code in record: #read in a line of the code
        work = code.split("|") #Split it up 
        decode(work[0],work[1]) # Call the decode function  and pass LineCnt,x
    ans = False # Once done reading the message end the loop

record.close() # Close the message file.
key.close() # Close the key
waiting = raw_input("Press enter to close")

    

