#Created on a win8.1 system with Notepad++
#Practice perl script 


#I take the entry of the first three numbers off a resistor and return it's value.
# Use () rather than [] for the array container
# This is a list for the tens digit of the resistor
@Tens = (0,10,20,30,40,50,60,70,80,90);

# This is a list for the colors on the resistor
@Color = ("Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White");

#This list is the multipliers for the resistor
@Mult = (1,10,100,1000,10000,100000,1000000,10000000,100000000,100000000,1000000000);


#print the basic information

print "Lets see what that resistor value is\
\nFor starters here is what number each color represents:\
\nBlack:0         Green:5\
\nBrown:1         Blue:6\
\nRed:2           Violet:7\
\nOrange:3        Gray:8\
\nYellow:4        White:9";
print" \n";
print "Hold the resistor with this orientation\
\n--------------------\
\n|    c  c  c        |\
\n|    o  o  o        |\
\n|    1  2  3        |\
\n--------------------\n";

print "What number is represented by co1? \n";
$co1 = <>; # Gets the first digit from STDIN ( you could also use <STDIN> )
print "What number is represented by co2? \n";
$co2 = <>; # Gets the second digit from STDIN
print "What number is represented by co3? \n";
$co3 = <>; # Gets the multiplier from STDIN

$value = $co2 + $Tens[$co1]; #Assembling the value of the first two digits, notice that you use $ instaed of @ to reference the arrays
$multiplier = $Mult[$co3]; #Getting the multiplier
$final = $value * $multiplier; # Calculate the value of the resistor for printing

print " ";
print "You input :\n";
print "$Color[$co1], $co1"; #print the color band and number
print "$Color[$co2], $co2"; #print the color band and number
print "$Color[$co3], $co3"; #print the color band and number
print " \n";
print "You have a $final ohm resistor"; # Use  $final for printing as perl cannot do math when printed this way. 

$wait = <>; # keep the window open
