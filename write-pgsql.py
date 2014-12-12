import project 
import functions as func

""" local & server switch """
url, querie_url, config_url = func.getURL()


""" load project.mml as python dictionary"""
mml = project.project 



p = open('mml/project_temp.txt', 'w')
for i in range(0, len(mml['Layer'])):
    p.write(mml['Layer'][i]['name'])
    queries = open(querie_url + mml['Layer'][i]['name'] + '.pgsql', 'w')
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
fileNameList = func.createFileNameList(querie_url)       
func.writeLayerConfig(fileNameList, querie_url)
        

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
