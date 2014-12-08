select way,coalesce(('highway_' || highway), ('railway_' ||(case when railway='preserved' and service in ('spur','siding','yard') then 'INT-preserved-ssy'::text when (railway='rail' and service in ('spur','siding','yard'))  then 'INT-spur-siding-yard' when railway in ('light_rail', 'narrow_gauge', 'funicular', 'rail', 'subway', 'tram', 'spur', 'siding', 'monorail', 'platform', 'preserved', 'disused', 'construction', 'miniature', 'turntable') then railway else null end)), ('aeroway_' || aeroway)) as feature, sac_scale, horse, foot, bicycle, tracktype, case when access in ('permissive') then 'permissive'::text when access in ('destination') then 'destination'::text when access in ('no', 'private') then 'no'::text else null end as access, construction, case when service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as service, case when oneway in ('yes', '-1') and highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street','construction') then oneway else null end as oneway, case when layer is null then '0' else layer end as layernotnull from planet_osm_line where (highway in ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'road', 'unclassified', 'service', 'pedestrian', 'living_street', 'raceway', 'bridleway', 'footway', 'cycleway', 'path', 'track', 'steps', 'platform', 'proposed', 'construction')  or aeroway in ('runway','taxiway') or railway in ('light_rail', 'subway', 'narrow_gauge',  'rail', 'spur', 'siding', 'preserved', 'funicular', 'tram', 'monorail', 'platform', 'miniature', 'turntable', 'disused', 'construction')) and bridge in ('yes','true','1','viaduct') and (layer is null or (layer in ('0','1','2','3','4','5'))) order by layernotnull, z_order

