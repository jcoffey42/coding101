#!/usr/bin/perl
#
# Created on win8 in notepad++
# Mind reading math game in PERL

# Ask the questions one at a time
print "Think of a number, any number.\
\nPress enter when you're ready.";
<STDIN>; # Wait for enter to be pressed
print "\nMultiply that number by 2.\
\nPress enter when you're ready.";
<STDIN>;
print "\nAdd 10 to that number.\
\nPress enter when you're ready.";
<STDIN>;
print "\nDivide that number by 2.\
\nPress enter when you're ready.";
<STDIN>;
print "\nSubtract your original from the last.\
\nPress enter when you're ready.\n";
<STDIN>;
print "Please wait while I read your mind.\n";

#This is a delay loop to add to the tension.
$num = 5; #Set the wait loop count down
while($num--){
    print "\n$num\n"; #Print the count down
    sleep(1); #Sleep for 1 second. The program does nothing for one second.
}
print "The answer is 5!"; #Hazzah the number
<STDIN>; #Used to keep the program window open.
