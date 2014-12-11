try:
    from Tkinter import Tk
    from tkFileDialog import askopenfilename
    from tkFileDialog import askdirectory
    import glob
    import os
    import simplejson as json
    import functions as func
except:
    print 'nope'
    
def zoomSteps(name):
    # x is the zoomlevel where the data should be displayed
    zl = 18
    for index in layerList:
        try:
            if name == index.keys()[0]:
                x = index[name]['zoom']
        except:
            pass
      
    for n in range(0, (x - 1)):
        cfg.write('null,')
    
    for m in range(0, (zl - x )):
        cfg.write('"queries/' + i['name'] + '.pgsql",')
    cfg.write('"queries/' + i['name'] + '.pgsql"')
    

local_url = 'Projekte/mml2cfg/'
server_url = 'Projekte/mml2cfg/'

#url = local_url
url = server_url
#fileNameList = createFileNameList('vector/TileStache/queries/')
fileNameList = func.createFileNameList(url + 'queries/')
 
""" 
    this list define the layers in the tilestache.cfg
    if the line is commented, the layer is not shown
    # the 'default' string is important, because 
    # elsewise  the layerList is a list of characters, not a list of 'stringchains'
"""
import layer_config as lc
layerList = lc.layerList

cfg = open(url + 'tilestache.cfg', 'w')

# start cfg
cfg.write('{')

# write cache
cfg.write('"cache": {')
cfg.write('"name": "Test",')
cfg.write('"dirs": "quadtile",')
cfg.write('"umask": "0000",')
cfg.write('"path": "cache",')
cfg.write('"gzip": ["txt", "text", "json", "xml", "topojson", "geojson", "oscimap"]')
# end write cache
cfg.write('},')

# write layers
cfg.write('"layers": {')
cfg.write('"all": {')
cfg.write('"allowed origin": "*",')
cfg.write('"provider": {')
cfg.write('"class": "TileStache.Goodies.VecTiles:MultiProvider",')
cfg.write('"kwargs": {')

# write layer names
cfg.write('"names": [')
countNames = 2
layerNameList = func.searchLayerList(layerList)

for i in fileNameList:
    name = i['name'].replace('-','_')
    if name in layerNameList:
        cfg.write('"' + name + '"')
        print name
        if 2 <= countNames < len(layerList) :
	    #print ','
	    cfg.write(',')
	countNames += 1

# end write layer names
cfg.write(']')


cfg.write('}')
cfg.write('}')
cfg.write('},')
# write custom style layer
  
countObjects = 2
for i in fileNameList:
    name = i['name'].replace('-','_')
    if name in layerNameList:
        cfg.write('"' + name + '": {')
        cfg.write('"allowed origin": "*",')
        cfg.write('"provider": {')
        cfg.write('"class": "TileStache.Goodies.VecTiles:Provider",')
        cfg.write('"kwargs": {')
        cfg.write('"dbinfo": {')
        cfg.write('"host": "localhost",')
        cfg.write('"port": 5432,')
        cfg.write('"user": "postgres",')
        cfg.write('"database": "gis"')
        cfg.write('},')
        
        cfg.write('"queries": [')
        zoomSteps(name)
        cfg.write(']')

        cfg.write('}')
        cfg.write('}')
        cfg.write('}')
        
        if 2 <= countObjects < len(layerList):

        cfg.write(',')
 
        
        countObjects += 1
        
        
  

  



# end write layers
cfg.write('}')

# end cfg
cfg.write('}')
cfg.close()

inputFile = open(url + 'tilestache.cfg')
inputJson = json.load(inputFile) 
inputFile.close()

outputFile = open(url + 'tilestache.cfg', 'w')
json.dump(inputJson, outputFile, sort_keys = True, indent = 4)
outputFile.close()


