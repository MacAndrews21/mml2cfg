select way,"addr:housenumber" from planet_osm_polygon where "addr:housenumber" is not null and building is not null       union       select way,"addr:housenumber" from planet_osm_point where "addr:housenumber" is not null      

