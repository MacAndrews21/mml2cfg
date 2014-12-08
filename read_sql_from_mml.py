""" 1.  seperate sql queries form project.mml"""
mml = open('Projekte/create_db/python/mml/project.mml')
lines = mml.readlines()
mml.close()

project = open('Projekte/create_db/python/mml/project.txt', 'w')
for line in lines:
    if 'table' in line:
        line = line.replace(r"\n", '')
        line = line.replace(r'\"', '"')
        #project.write("hallo" + '\n')
        asStart = line.rfind(' as ') + len(' as ')
        asEnd = line.rfind('"')
        project.write(line[asStart:asEnd] + '\n')
        
        start = line.find('select')
        end = line.rfind(')')
        temp1 = line[start:end]        
        project.write(temp1 + '\n')        
      
project.close()

""" 2. write queries in *.pgsql files """
txt = open('Projekte/create_db/python/mml/project.txt')
lines = txt.readlines()
txt.close()

for line in lines:
    #print line
    if 'select' not in line:
        #line
        project = open('Projekte/create_db/python/pgsql-queries/' + line.strip() + '.pgsql', 'w')
    if 'select' in line:
        #print 'ok'
        project.write(line + '\n')
        project.close()
    
