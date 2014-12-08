select way,highway,ref,char_length(ref) as length       from planet_osm_roads       where highway in ('motorway','trunk','primary','secondary')         and ref is not null         and char_length(ref) between 1 and 8      

