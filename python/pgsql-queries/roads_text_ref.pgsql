select way,coalesce(highway,aeroway) as highway,ref,char_length(ref) as length,       case when bridge in ('yes','true','1') then 'yes'::text else 'no'::text end as bridge       from planet_osm_line       where (highway is not null or aeroway is not null)         and ref is not null         and char_length(ref) between 1 and 8      

