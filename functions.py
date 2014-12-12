try:
    from Tkinter import Tk
    from tkFileDialog import askopenfilename
    from tkFileDialog import askdirectory
    import glob
    import os
    import simplejson as json
except:
    print 'nope'

def getURL():
    url        = ''
    querie_url = '../TileStache/queries/'
    config_url = '../TileStache/'
    
    if not os.path.exists(querie_url):
        os.makedirs(querie_url)
    else:
        pass

    return url, querie_url, config_url




    
def createFileNameList(folderPath):
    fileNameList = []
    
    for filename in glob.glob(os.path.join(folderPath, '*.pgsql')):
        startIndex = filename.rfind('/') + 1
        endIndex = filename.rfind('.')
        #print filename[startIndex:]
        sql = open(filename)
        lines = sql.readlines()
        sql.close()
        temp = {}
        temp['file'] = filename
        temp['name'] = filename[startIndex:endIndex]
        for line in lines:
            if 'select' in line: 
                temp['query'] = line.strip()
    #print temp
        fileNameList.append(temp)

    return fileNameList

def writeLayerConfig(fileNameList, url):
    fileNameList = createFileNameList(url)
    fileNameList.sort()
    config = open('layer_config.py', 'w')
    config.write('layerList = ( {"aaa_default":{"zoom" : 10}}\n')
    
    for i in fileNameList:
        config.write('              #, {"' + i['name'].replace('-', '_') + '":{"zoom" : 10}}\n')
    config.write(')')
    config.close()


    
def searchLayerList(lL):
    tempList = []
    for i in lL:
        try:
            tempList.append(i.keys()[0])
        except:
            pass
    return tempList

def cleanUp(sql):
        #sql = re.sub('\s+', ' ', sql).strip()
        end = sql.rfind(')')
        sql = sql[:end]
        
        sql = sql.replace(','         ,' , ' )
        sql = sql.replace(' way '     ,' way AS __geometry__ ', 1)        
        sql = sql.replace('select '   , 'SELECT ')
        sql = sql.replace('(SELECT '   , 'SELECT ')
        sql = sql.replace(' from '    , ' FROM ')
        sql = sql.replace('from '    , 'FROM ')
        sql = sql.replace('where '   , 'WHERE ')
        sql = sql.replace(' and '     , ' AND ')
        sql = sql.replace(' is '      , ' IS ')
        sql = sql.replace(' in '      , ' IN ')
        sql = sql.replace(' as '      , ' AS ')
        sql = sql.replace(' not '     , ' NOT ')
        sql = sql.replace(' null '    , ' NULL ')
        sql = sql.replace(' null'     , ' NULL')
        sql = sql.replace(' or '      , ' OR ')
        sql = sql.replace(' order '   , ' ORDER ')
        sql = sql.replace(' by '      , ' BY ')
        sql = sql.replace(' case '    , ' CASE ')
        sql = sql.replace('(case '    , ' (CASE ')
        sql = sql.replace(' when '    , ' WHEN ')
        sql = sql.replace(' then '    , ' THEN ')
        sql = sql.replace(' desc '    , ' DESC ')
        sql = sql.replace(' desc'     , ' DESC')
        sql = sql.replace(' asc '     , ' ASC ')
        sql = sql.replace(' asc'      , ' ASC')
        sql = sql.replace(' coalesce' , ' COALESCE')
        sql = sql.replace(' coalesce ' , ' COALESCE ')
        sql = sql.replace('coalesce ' , 'COALESCE ')
        sql = sql.replace(' union '   , ' UNION ')
        sql = sql.replace(' between ' , ' BETWEEN ')
        return sql