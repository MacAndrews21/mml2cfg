select way,railway,bridge from planet_osm_line where railway='tram' and (tunnel is null or tunnel != 'yes')

