import glob
import os
def createFileNameList(folderPath):
    
    for filename in glob.glob(os.path.join(folderPath, '*.pgsql')):
        pgsql = open(filename)
        lines = pgsql.readlines()
        pgsql.close()
        
        for line in lines:
	    if '"' in line: 
	        print filename


createFileNameList('Projekte/vector-datasource/queries/')
