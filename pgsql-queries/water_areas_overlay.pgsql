select way,"natural"      from planet_osm_polygon      where "natural" in ('marsh','wetland') and building is null      order by z_order,way_area desc      

