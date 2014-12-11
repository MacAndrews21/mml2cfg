import re
import functions as func

""" local & server switch """
url, querie_url, config_url = func.getURL()

""" 1.  seperate sql queries form project.mml"""
mml = open(url + 'mml/project.mml')
lines = mml.readlines()
mml.close()

project = open(url + 'mml/project.txt', 'w')
for line in lines:
    if 'table' in line:
        line = line.replace(r"\n", ' ')
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
txt = open(url + 'mml/project.txt')
lines = txt.readlines()
txt.close()

for line in lines:
    #print line
    if 'select' not in line:
        #line
        project = open(querie_url + 'queries/' + line.strip() + '.pgsql', 'w')
        
        
    if 'select' in line:
        #print 'ok'
        line = re.sub('\s+', ' ', line).strip()

        line = line.replace(',', ' , ' )
        # line = line.split(' ', 1)
        line = line.replace(' way ', ' way AS __geometry__ ', 1)

        
        line = line.replace('select ', 'SELECT ')
        line = line.replace(' from ', ' \nFROM ')
        line = line.replace(' where ', ' \nWHERE ')
        line = line.replace(' and ', ' \n    AND ')
        line = line.replace(' is ', ' IS ')
        line = line.replace(' in ', ' IN ')
        line = line.replace(' as ', ' AS ')
        line = line.replace(' not ', ' NOT ')
        line = line.replace(' null ', ' NULL ')
        line = line.replace(' null', ' NULL')
        line = line.replace(' or ', ' \n    OR ')
        line = line.replace(' order ', ' \nORDER ')
        line = line.replace(' by ', ' BY ')
        line = line.replace(' case ', ' CASE ')
        line = line.replace('(case ', '\n  (CASE ')
        line = line.replace(' when ', '\n  WHEN ')
        line = line.replace(' then ', '\n  THEN ')
        line = line.replace(' desc ', ' DESC ')
        line = line.replace(' desc', ' DESC')
        line = line.replace(' asc ', ' ASC ')
        line = line.replace(' asc', ' ASC')
        line = line.replace(' coalesce', ' \n  COALESCE')
        
        line = line.replace(' union ', ' \nUNION ')
        line = line.replace(' between ', ' BETWEEN ')
        
 
        project.write(line + '\n')
        project.close()
    
