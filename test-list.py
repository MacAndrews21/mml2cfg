#testList = ({"roads-fill", 10}, {"roads", 20})

#print testList[0]



className = {}

className = ('default'
	     ,{'roads-fill':    {'zoom' : 10}}
	     #,{'roads':         {'zoom' : 10}}
	     #,{'roads-highway': {'zoom' : 10}}
	     
	     
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
print 'length', len(className)
    #if string in className[i]:
      #print 'yes'
      #print className[string]['zoom']

def test(li):
    temp = []
    for i in li:
        print i
        try:                    
            temp.append(i.keys()[0]) 
        except:
            pass #temp.append('test')
     
    return temp

t = test(className)
print  len(t) , t[0]

print className["roads-fill"]['zoom']