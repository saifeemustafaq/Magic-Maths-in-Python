print ""
print "     Please press enter after each step!"
print ""
print '     Think of a number below 10...'
a=raw_input(                )

print '     Double the number you have thought.'
b=raw_input()

c= int(input("     Add something from 1-10 with the getting result and type it here (type only within 1-10):"))
print ""
print '     Half the answer, (that is divide it by 2.)'
d=raw_input()

print '     Take away the number you have thought from the answer\n     that is, (subtract the number you have thought from the answer you have now.)'
e=raw_input()

if c==0 :
    print "Please be honest"
if c==1 :
    print "0.5"
if c==2 :
    print "1"
if c==3 :
    print "1.5"
if c==4 :
    print "2"
if c==5 :
    print "2.5"
if c==6 :
    print "3"
if c==7 :
    print "3.5"
if c==8 :
    print "4"
if c==9 :
    print "4.5"
if c==10 :
    print "5"
