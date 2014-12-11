import project 
import functions as func

mml = project.project 
   
    
    
#print project.keys()
#print project['Layer'][4]['name']
#print project['Layer'][4]['Datasource']
#print project['Layer'][4]['Datasource']['table'] # .keys()
url = "Projekte/mml2cfg/"
p = open(url + 'mml/project_temp.txt', 'w')
for i in range(0, len(mml['Layer'])):
    p.write(mml['Layer'][i]['name'])
    queries = open(url + 'queries/' + mml['Layer'][i]['name'] + '.pgsql', 'w')
    p.write('\n')
    try:
        sql = mml['Layer'][i]['Datasource']['table']
        #line = line
        sql = func.cleanUp(sql)
        p.write(sql)        
        p.write('\n')
        
        queries.write(sql)
        queries.write('\n')
        
    except:
        pass
    try:
        shp = mml['Layer'][i]['Datasource']['file']
        p.write(shp)
        p.write('\n')
        
        queries.write(shp)        
        queries.write('\n')        
    except:
        pass

""" write the layer configuration list in a seperate file """
fileNameList = func.createFileNameList(url + 'queries/')       
func.writeLayerConfig(fileNameList, url)
        

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
