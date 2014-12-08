select name, way, way_area from planet_osm_polygon where building is not null  and building not in ('no','station','supermarket')

