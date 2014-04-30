# Created on a win system with IDLE
# Practice python script project 2014-003b.py
print """
# A script to pull in an output file with pipe delimited values, with a varied number
# of items per Title record.
# list of titles to create a smaller list of titles with the format
#  Publication Year | Call#  | Title
# Here is an example of your file locations
# filein = "c:\data\catalog.txt"
# fileout = "c:\data\export.txt"
"""

filein = raw_input("Where is your input file:") # Location of the input file
fileout = raw_input("Where is your output file:") # Location of the output file




# Open file for read only access, change the filename to your needs
record = open(filein, "r")

# Open a file for output, write access, change the filename to your needs
output = open(fileout,"w")

# Setup the empty lists

Title = [] # The Title of the item(s)

T = int(0) # A counter for the end

Item = [] # The item ID of the item(s)

Callnumber = [] # The Call Number of the items(s)

C = int(0) # A counter for the Call numbers

Pubyear = [] # The Publication Year of the Title

Finished = [] # Used to put together the data for export

Working = [] # The entire input from one file read, split by "|"

# Setup loop to read through entire file for processing
# Loads a line of text from the object record into lineuntil the file end

for Line in record:
        
# Split the record into a list called working by the pipe symbol
        Working = Line.split("|")
        #print "line input"
        #print Working
         

# Find the location of ITEM tags, not used at this time
        for x in range(0,len(Working)):
              if Working[x] == "ITEM>":
                  Item.append(x)  

# Find the location of the Call number tags         
        for x in range(0,len(Working)):
              #print x,"c"
              if Working[x] == "CALLNUM>":
                 Callnumber.append(Working[x+1])# Load the Call number
                 C=C+1 # Totaling the call numbers
                 #print "call", Callnumber
# Find the location of the Title tag
        for x in range(0,len(Working)):
              #print x,"t"
              if Working[x] == "Title":
                  Title.append(Working[x+1])# Load the Title
                  Pubyear.append(Working[x-2])# load the Publication year
                  T= T+1 # Totaling the titles
                  #print "title", Title
# Pack the finished list for each Callnumber in the record, may be one or more        
        for x in range(0,len(Callnumber)):
              #print x,"write"
              Finished.append(Pubyear)
              Finished.append(Callnumber[x])
              Finished.append(Title)
              
      # Prepare the final output string for wrting 
              export = str("{}|{}|{}|\n").format(Finished[0],Finished[1],Finished[2])
              output.write(export)# Write the one item to the files
              print "Processed title #",T, "Callnumber",x+1 # To indicate work is being done

        Finished = []# Clear the list for the next item
        Title = []# Clear the Title list
        Pubyear = []# Clear the Publication year list
        Callnumber = []# Clear the Call Number list
        
# Indicate count of processed records for quality control

print T," Titles processed"
print C," Call Numbers processed"

# Close the files and end

output.close()
record.close()

raw_input() # To keep the window open on gui systems
