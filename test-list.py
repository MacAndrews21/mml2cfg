#testList = ({"roads-fill", 10}, {"roads", 20})

#print testList[0]



className = {}

className = ({ 'roads-fill':    {'zoom' : 10}}
	     ,{'roads':         {'zoom' : 10}}
	     ,{'roads-highway': {'zoom' : 10}}
	     
	     
	     )
#className['roads'] = test #{'zoom', 20}

#print className['roads-fill']['zoom']
string = 'roads-highway'
#print className[string]
for i in className:
    #print className
    try:
        print i[string]['zoom']
        
        print i.keys()[0]
    except:
        pass
        #print 'nope'
        
    #if string in className[i]:
      #print 'yes'
      #print className[string]['zoom']