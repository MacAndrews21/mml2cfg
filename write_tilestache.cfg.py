#txt = open('Projekte/create_db/project__.txt')
#lines = txt.readlines()
#txt.close()
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

url = local_url
#url = server_url
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

#print layerList  
#layerList = ( 'default'
              #, {"admin_01234":              {'zoom' : 10}}
              #, {"admin_5678":               {'zoom' : 10}}
              #, {"admin_other":              {'zoom' : 10}}
              #, {"admin_text":               {'zoom' : 10}}
              #, {"aerialways":               {'zoom' : 10}}
              #, {"amenity_points":           {'zoom' : 10}}
              #, {"amenity_points_poly":      {'zoom' : 10}}
              #, {"amenity_symbols":          {'zoom' : 10}}
              #, {"amenity_symbols_poly":     {'zoom' : 10}}
              #, {"area_barriers":            {'zoom' : 10}}
              #, {"bridges":                  {'zoom' : 10}}
              #, {"building_text":            {'zoom' : 10}}
              #, {"buildings":                {'zoom' : 10}}
              #, {"buildings_lz":             {'zoom' : 10}}
              #, {"castlewalls":              {'zoom' : 10}}
              #, {"castlewalls_poly":         {'zoom' : 10}}
              #, {"citywalls":                {'zoom' : 10}}
              #, {"cliffs":                   {'zoom' : 10}}
              #, {"dam":                      {'zoom' : 10}}
              #, {"features":                 {'zoom' : 10}}
              #, {"ferry_routes":             {'zoom' : 10}}
              #, {"glaciers_text":            {'zoom' : 10}}
              #, {"guideways":                {'zoom' : 10}}
              #, {"highway_area_casing":      {'zoom' : 10}}
              #, {"highway_area_fill":        {'zoom' : 10}}
              #, {"highway_junctions":        {'zoom' : 10}}
              #, {"housenames":               {'zoom' : 10}}
              #, {"housenumbers":             {'zoom' : 10}}
              #, {"interpolation":            {'zoom' : 10}}
              #, {"landcover_line":           {'zoom' : 10}}
              #, {"landuse_overlay":          {'zoom' : 10}}
              #, {"line_barriers":            {'zoom' : 10}}
              #, {"locks":                    {'zoom' : 10}}
              #, {"marinas_area":             {'zoom' : 10}}
              #, {"national_park_boundaries": {'zoom' : 10}}
              #, {"paths_text_name":          {'zoom' : 10}}
              #, {"piers":                    {'zoom' : 10}}
              #, {"piers_area":               {'zoom' : 10}}
              #, {"placenames_capital":       {'zoom' : 10}}
              #, {"placenames_large":         {'zoom' : 10}}
              #, {"placenames_medium":        {'zoom' : 10}}
              #, {"placenames_small":         {'zoom' : 10}}
              #, {"power_line":               {'zoom' : 10}}
              #, {"power_minorline":          {'zoom' : 10}}
              #, {"power_poles":              {'zoom' : 10}}
              #, {"power_towers":             {'zoom' : 10}}
              #, {"roads":                    {'zoom' : 10}}
              #, {"roads_area_text_name":     {'zoom' : 10}}
              #, {"roads_fill":               {'zoom' : 10}}
              #, {"roads_low_zoom":           {'zoom' : 10}}
              #, {"roads_text_name":          {'zoom' : 10}}
              #, {"roads_text_ref":           {'zoom' : 10}}
              #, {"roads_text_ref_low_zoom":  {'zoom' : 10}}
              #, {"sports_grounds":           {'zoom' : 10}}
              #, {"stations":                 {'zoom' : 10}}
              #, {"stations_poly":            {'zoom' : 10}}
              #, {"text":                     {'zoom' : 10}}
              #, {"text_poly":                {'zoom' : 10}}
              #, {"theme_park":               {'zoom' : 10}}
              #, {"trams":                    {'zoom' : 10}}
              #, {"tunnels":                  {'zoom' : 10}}
              #, {"turning_circle_casing":    {'zoom' : 10}}
              #, {"turning_circle_fill":      {'zoom' : 10}}
              #, {"water_areas":              {'zoom' : 10}}
              #, {"water_areas_overlay":      {'zoom' : 10}}
              #, {"water_lines":              {'zoom' : 10}}
              #, {"water_lines_casing":       {'zoom' : 10}}
              #, {"water_lines_low_zoom":     {'zoom' : 10}}
              #, {"water_lines_text":         {'zoom' : 10}}
              #, {"waterway_bridges":         {'zoom' : 10}}
              
             #)

cfg = open(url + 'tilestache.cfg', 'w')
#cfg = open('sftp://komoot@komoot.koding.io/home/komoot/vector/tilestache__.cfg', 'w')
 
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
#for ...
# cfg.write('"custom"')
countNames = 2
layerNameList = func.searchLayerList(layerList)
#print layerNameList 
#for i in fileNameList:
    #print i['name'].replace('-','_')
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
# cfg.write('"custom": {')
# cfg.write('"allowed origin": "*",')
# cfg.write('"provider": {')
# cfg.write('"class": "TileStache.Goodies.VecTiles:Provider",')
# cfg.write('"kwargs": {')
# cfg.write('"dbinfo": {')
# cfg.write('"host": "localhost",')
# cfg.write('"port": 5432,')
# cfg.write('"user": "postgres",')
# cfg.write('"database": "gis"')
# cfg.write('},')
# cfg.write('"queries": ["SELECT name,way_area::bigint AS area, military AS class, way AS __geometry__ FROM planet_osm_polygon WHERE military = \'barracks\'"]')

# cfg.write('}')
# cfg.write('}')
# cfg.write('}')
# write loop

    
  
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
        #for x in range(0,12):
            #cfg.write('null,')
    
        #for z in range(0,6):
            #cfg.write('"queries/' + i['name'] + '.pgsql",')
            ## cfg.write(', ')
        #cfg.write('"queries/' + i['name'] + '.pgsql"')
        zoomSteps(name)
        cfg.write(']')
        # cfg.write('"queries": ["' + i['query'] + '"]')
        # cfg.write(',')
        # cfg.write('"geometry_types": ["Polygon", "MultiPolygon"]')
        cfg.write('}')
        cfg.write('}')
        cfg.write('}')
        
        #print countObjects, 'count'
	#print len(layerList), 'len'
        if 2 <= countObjects < len(layerList):
	    #print ','
	    cfg.write(',')
	    
        
        countObjects += 1
        
        
  

  



# end write layers
cfg.write('}')

# end cfg
cfg.write('}')
cfg.close()

inputFile = open(url + 'tilestache.cfg')
#inputFile = open('sftp://komoot@komoot.koding.io/home/komoot/vector/tilestache__.cfg')
inputJson = json.load(inputFile) 
inputFile.close()

outputFile = open(url + 'tilestache.cfg', 'w')
#outputFile = open('sftp://komoot@komoot.koding.io/home/komoot/vector/tilestache__.cfg', 'w')
json.dump(inputJson, outputFile, sort_keys = True, indent = 4)
outputFile.close()


