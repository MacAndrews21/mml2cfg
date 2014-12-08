select way,building,railway,amenity from planet_osm_polygon       where railway='station'          or building in ('station','supermarket')          or amenity='place_of_worship'       order by z_order,way_area desc

