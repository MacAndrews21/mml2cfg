select way,name,railway,aerialway,disused      from planet_osm_polygon      where railway in ('station','halt','tram_stop')         or aerialway='station'      

