select way, highway, name       from planet_osm_line       where highway in ('bridleway', 'footway', 'cycleway', 'path', 'track', 'steps')          and name is not null      

