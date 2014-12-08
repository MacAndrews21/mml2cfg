select way,waterway,lock,name,tunnel      from planet_osm_line      where waterway in ('weir','river','canal','derelict_canal','stream','drain','ditch','wadi')        and (bridge is null or bridge not in ('yes','true','1','aqueduct'))      order by z_order      

