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
except:
    print 'nope'


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

local_url = 'Projekte/mml2cfg/'
server_url = 'Projekte/mml2cfg/'

url = local_url
#url = server_url
#fileNameList = createFileNameList('vector/TileStache/queries/')
fileNameList = createFileNameList(url + 'queries/')

""" 
    this list define the layers in the tilestache.cfg
    if the line is commented, the layer is not shown
    # the 'default' string is important, because 
    # elsewise  the layerList is a list of characters, not a list of 'stringchains'
"""
layerList = ( 
              # "admin_01234"
              #, "admin_5678"
              #, "admin_other"
              #, "admin_text"
              #, "aerialways"
              #, "amenity_points"
              #, "amenity_points_poly"
              #, "amenity_symbols"
              #, "amenity_symbols_poly"
              #, "area_barriers"
              #, "bridges"
              #, "building_text"
              #, "buildings"
              #, "buildings_lz"
              #, "castlewalls"
              #, "castlewalls_poly"
              #, "citywalls"
              #, "cliffs"
              #, "dam"
              #, "features"
              #, "ferry_routes"
              #, "glaciers_text"
              #, "guideways"
              #, "highway_area_casing"
              #, "highway_area_fill"
              #, "highway_junctions"
              #, "housenames"
              #, "housenumbers"
              #, "interpolation"
              #, "landcover_line"
              #, "landuse_overlay"
              #, "line_barriers"
              #, "locks"
              #, "marinas_area"
              #, "national_park_boundaries"
              #, "paths_text_name"
              #, "piers"
              #, "piers_area"
              #, "placenames_capital"
              #, "placenames_large"
              #, "placenames_medium"
              #, "placenames_small"
              #, "power_line"
              #, "power_minorline"
              #, "power_poles"
              #, "power_towers"
              #, "roads"
              #, "roads_area_text_name"
               "roads_fill"
              #, "roads_low_zoom"
              #, "roads_text_name"
              # , "roads_text_ref"
              #, "roads_text_ref_low_zoom"
              #, "sports_grounds"
              #, "stations"
              #, "stations_poly"
              #, "text"
              #, "text_poly"
              #, "theme_park"
              #, "trams"
              #, "tunnels"
              #, "turning_circle_casing"
              #, "turning_circle_fill"
              #, "water_areas"
              #, "water_areas_overlay"
              #, "water_lines"
              #, "water_lines_casing"
              #, "water_lines_low_zoom"
              #, "water_lines_text"
              #, "waterway_bridges"
              , "default"
             )

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
for i in fileNameList:
    if i['name'] in layerList:
        cfg.write('"' + i['name'] + '"')
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
    if i['name'] in layerList:
        # for n in range(0, len(layerList)):
            # print layerList[n], n
            # if len(i['name']) == len(layerList[n]):

        # cfg.write(',')
       
        
        cfg.write('"' + i['name'] + '": {')
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
        for x in range(0,12):
            cfg.write('null,')
            # cfg.write(', ')
    
        for z in range(0,6):
            cfg.write('"queries/' + i['name'] + '.pgsql",')
            # cfg.write(', ')
        cfg.write('"queries/' + i['name'] + '.pgsql"')
        cfg.write(']')
        # cfg.write('"queries": ["' + i['query'] + '"]')
        # cfg.write(',')
        # cfg.write('"geometry_types": ["Polygon", "MultiPolygon"]')
        cfg.write('}')
        cfg.write('}')
        cfg.write('}')
        
        #print countObjects, 'count'
	#print len(layerList), 'len'
        if 2 <= countObjects < len(layerList) :
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
json.dump(inputJson, outputFile, sort_keys = False, indent = 4)
outputFile.close()


