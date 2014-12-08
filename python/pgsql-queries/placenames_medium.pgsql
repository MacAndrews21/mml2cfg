select way,place,name      from planet_osm_point      where place in ('city','town')        and (capital is null or capital != 'yes')      

