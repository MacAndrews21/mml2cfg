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
fileNameList = createFileNameList('Projekte/create_db/python/pgsql-queries/')

""" 
    this list define the layers in the tilestache.cfg
    if the line is commented, the layer is shown
"""
layerList = ( 
             "admin_01234"
             # , "landuse_overlay"
              #, "highway_junctions"
              #, "features"
              #, "buildings_lz"
              #, "text"
              #, "turning_circle_fill"
              #, "cliffs"
              #, "highway_area_casing"
              #, "building_text"
              #, "admin_5678"
              #, "admin_other"
              #, "national_park_boundaries"
              #, "text_poly"
              #, "water_areas_overlay"
              #, "water_areas"
              #, "stations"
              #, "roads_area_text_name"
              #, "area_barriers"
              #, "water_lines"
              #, "tunnels"
              #, "piers_area"
              #, "roads_fill"
              #, "placenames_large"
              #, "citywalls"
              #, "water_lines_casing"
              #, "ferry_routes"
              #, "landcover_line"
              #, "water_lines_text"
              #, "castlewalls_poly"
              #, "locks"
              #, "glaciers_text"
              #, "piers"
              #, "roads_text_name"
              #, "roads"
              #, "trams"
              #, "roads_low_zoom"
              #, "theme_park"
              #, "water_lines_low_zoom"
              #, "housenames"
              #, "roads_text_ref"
              #, "turning_circle_casing"
              #, "interpolation"
              #, "admin_text"
              #, "power_towers"
              #, "dam"
              #, "amenity_symbols_poly"
              #, "sports_grounds"
              #, "line_barriers"
              #, "waterway_bridges"
              #, "placenames_medium"
              #, "amenity_points_poly"
              #, "castlewalls"
              #, "highway_area_fill"
              #, "amenity_points"
              #, "power_minorline"
              #, "buildings"
              #, "power_line"
              #, "power_poles"
              #, "bridges"
              #, "marinas_area"
              #, "placenames_capital"
              #, "roads_text_ref_low_zoom"
              #, "aerialways"
              #, "paths_text_name"
              #, "placenames_small"
              #, "amenity_symbols"
              #, "housenumbers"
              #, "guideways"
              #, "stations_poly"
             )

cfg = open('Projekte/create_db/python/cfg/tilstache__.cfg', 'w')
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
cfg.write('"custom"')
for i in fileNameList:
    if i['name'] in layerList:
        cfg.write(',"' + i['name'] + '"')
# end write layer names
cfg.write(']')


cfg.write('}')
cfg.write('}')
cfg.write('},')
# write custom style layer
cfg.write('"custom": {')
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
cfg.write('"queries": ["SELECT name,way_area::bigint AS area, military AS class, way AS __geometry__ FROM planet_osm_polygon WHERE military = \'barracks\'"],')
cfg.write('"geometry_types": ["Polygon", "MultiPolygon"]')
cfg.write('}')
cfg.write('}')
cfg.write('}')
# write loop
for i in fileNameList:
    if i['name'] in layerList:
        cfg.write(',')
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
        cfg.write('"queries": ["' + i['name'] + '.pgsql' + '"],')
        cfg.write('"geometry_types": ["Polygon", "MultiPolygon"]')
        cfg.write('}')
        cfg.write('}')
        cfg.write('}')
  
  

  



# end write layers
cfg.write('}')

# end cfg
cfg.write('}')
cfg.close()

inputFile = open('Projekte/create_db/python/cfg/tilstache__.cfg')
#inputFile = open('sftp://komoot@komoot.koding.io/home/komoot/vector/tilestache__.cfg')
inputJson = json.load(inputFile) 
inputFile.close()

outputFile = open('Projekte/create_db/python/cfg/tilstache_pretty_json.cfg', 'w')
#outputFile = open('sftp://komoot@komoot.koding.io/home/komoot/vector/tilestache__.cfg', 'w')
json.dump(inputJson, outputFile, sort_keys = False, indent = 4)
outputFile.close()


