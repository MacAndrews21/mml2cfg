select way,coalesce(('highway_' || highway), ('railway_' ||(case when railway in ('light_rail', 'abandoned', 'spur', 'siding', 'yard', 'narrow_gauge', 'funicular', 'rail', 'subway', 'tram', 'spur', 'siding', 'monorail', 'platform', 'preserved', 'disused', 'construction', 'miniature', 'turntable') then railway else null end)), ('aeroway_' || aeroway)) as feature, sac_scale, horse, foot, bicycle, tracktype, case when access in ('permissive') then 'permissive'::text when access in ('destination') then 'destination'::text when access in ('no', 'private') then 'no'::text else null end as access, construction, case when service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as service, case when oneway in ('yes', '-1') and highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street','construction') then oneway else null end as oneway, case when layer is null then '0' else layer end as layernotnull from planet_osm_line where (highway in ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'road', 'unclassified', 'service', 'pedestrian', 'living_street', 'raceway', 'bridleway', 'footway', 'cycleway', 'path', 'track', 'steps', 'platform', 'proposed', 'construction')  or aeroway in ('runway','taxiway') or railway in ('light_rail', 'abandoned', 'subway', 'narrow_gauge',  'rail', 'spur', 'siding', 'preserved', 'funicular', 'tram', 'monorail', 'platform', 'miniature', 'turntable', 'disused', 'construction')) and (tunnel is null or not tunnel in ('yes','true','1')) and (bridge is null or not bridge in ('yes','true','1','viaduct')) order by z_order

