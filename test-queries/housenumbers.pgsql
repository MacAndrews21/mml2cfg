      SELECT way AS __geometry__ , "addr:housenumber" FROM planet_osm_polygon WHERE "addr:housenumber" IS NOT NULL AND building IS NOT NULL
       union
       SELECT way , "addr:housenumber" FROM planet_osm_point WHERE "addr:housenumber" IS NOT NULL
      
