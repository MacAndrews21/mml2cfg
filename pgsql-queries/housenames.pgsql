select way,"addr:housename" from planet_osm_polygon where "addr:housename" is not null and building is not null       union       select way,"addr:housename" from planet_osm_point where "addr:housename" is not null      

