select way,way_area,name,boundary from planet_osm_polygon where (boundary='national_park' or leisure='nature_reserve') and building is null

