select way from planet_osm_line where highway='bus_guideway' and (tunnel is null or tunnel != 'yes')

