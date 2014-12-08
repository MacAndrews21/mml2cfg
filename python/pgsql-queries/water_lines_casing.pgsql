select way,waterway      from planet_osm_line      where waterway in ('stream','drain','ditch')        and (tunnel is null or tunnel != 'yes')      

