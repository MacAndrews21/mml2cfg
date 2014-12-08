select way,leisure,case when leisure='pitch' then 2  when leisure='track' then 1  else 0 end as prio  from planet_osm_polygon  where leisure in ('sports_centre','stadium','pitch','track')  order by z_order,prio,way_area desc

