select way,"natural",waterway,landuse,name      from planet_osm_polygon      where (waterway in ('dock','mill_pond','riverbank','canal')         or landuse in ('reservoir','water','basin')         or "natural" in ('lake','water','land','glacier','mud'))         and building is null      order by z_order,way_area desc      

