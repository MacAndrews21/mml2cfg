select way,name,railway,aerialway,disused      from planet_osm_point      where railway in ('station','halt','tram_stop','subway_entrance')         or aerialway='station'      

