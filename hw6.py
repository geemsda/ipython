import re

fhand = open('myreged')

for lines in fhand:
    # print lines
   
    fe = \
       re.search \
         ('([0-9])\s([A-Z][a-z\sA-Za-z]+)\s\|\s([W|T|L]\s[0-4])\s\|\s([W|T|L]\s[0-4])\s\|\s([W|T|L]\s[0-4])', lines)
            

    if fe:
        

        print "Rank: ", fe.group(1)
        print ("Country: "), fe.group(2)
        print ("Results:")     
        print fe.group(3)
        print fe.group(4)
        print fe.group(5)
