select way,waterway,lock,name,tunnel      from planet_osm_line      where waterway in ('weir','river','canal','derelict_canal','stream','drain','ditch','wadi')       order by z_order      

