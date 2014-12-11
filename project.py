project = {
    "interactivity": {
        "fields": []
    },
    "Layer": [
        {
            "status": "off",
            "name": "world",
            "srs-name": "900913",
            "geometry": "polygon",
            "class": "",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "type": "shape",
                "id": "world",
                "file": "data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp"
            },
            "extent": [
                -179.99999692067183,
                -85.051,
                179.99999692067183,
                83.66933299999998
            ],
            "id": "world",
            "advanced": {}
        },
        {
            "status": "off",
            "name": "coast-poly",
            "srs-name": "900913",
            "geometry": "polygon",
            "class": "",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "type": "shape",
                "file": "data/land-polygons-split-3857/land_polygons.shp"
            },
            "extent": [
                -179.99999692067183,
                -85.051,
                179.99999692067183,
                83.66933299999998
            ],
            "id": "coast-poly",
            "advanced": {}
        },
        {
            "status": "off",
            "name": "builtup",
            "srs-name": "mercator",
            "geometry": "polygon",
            "class": "",
            "srs": "+proj=merc +datum=WGS84 +over",
            "Datasource": {
                "project": "github",
                "srs": "+proj=merc +datum=WGS84 +over",
                "type": "shape",
                "id": "builtup",
                "file": "data/world_boundaries/builtup_area.shp"
            },
            "extent": [
                -179.12960815429688,
                -52.982724914179855,
                178.4432525634766,
                70.87402746981634
            ],
            "id": "builtup",
            "advanced": {}
        },
        {
            "status": "off",
            "name": "necountries",
            "srs-name": "WGS84",
            "geometry": "linestring",
            "class": "",
            "srs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs",
            "Datasource": {
                "project": "github",
                "srs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs",
                "type": "shape",
                "id": "necountries",
                "file": "data/ne_110m_admin_0_boundary_lines_land/ne_110m_admin_0_boundary_lines_land.shp"
            },
            "extent": [
                -140.99778,
                -54.89681,
                141.03385176001382,
                70.16419
            ],
            "id": "necountries",
            "advanced": {}
        },
        {
            "name": "landcover",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "landcover",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "landcover",
                "table": "(select way, religion,\ncoalesce (aeroway, amenity, landuse, leisure, military, \"natural\", power, tourism, highway) as feature from (\nselect way,\n('aeroway_' || (case when aeroway in ('apron', 'aerodrome') then aeroway else null end)) as aeroway,\n('amenity_' || (case when amenity in ('parking', 'university', 'college', 'school', 'hospital', 'kindergarten', 'grave_yard') then amenity else null end)) as amenity,\n('landuse_' || (case when landuse in ('quarry', 'vineyard', 'orchard', 'cemetery', 'grave_yard', 'residential', 'garages', 'field', 'meadow', 'grass', 'allotments', 'forest', 'farmyard', 'farm', 'farmland', 'recreation_ground', 'conservation', 'village_green', 'retail', 'industrial', 'railway', 'commercial', 'brownfield', 'landfill', 'greenfield', 'construction') then landuse else null end)) as landuse,\n('leisure_' || (case when leisure in ('swimming_pool', 'playground', 'park', 'recreation_ground', 'common', 'garden', 'golf_course', 'picnic_table') then leisure else null end)) as leisure,\n('military_' || (case when military in ('barracks', 'danger_area') then military else null end)) as military,\n('natural_' || (case when \"natural\" in ('field','beach','desert','heath','mud','grassland','wood','sand','scrub') then \"natural\" else null end)) as \"natural\",\n('power_' || (case when power in ('station','sub_station','substation','generator') then power else null end)) as power,\n('tourism_' || (case when  tourism in ('attraction', 'camp_site', 'caravan_site', 'picnic_site', 'zoo') then tourism else null end)) as tourism,\n('highway_' || (case when highway in ('services', 'rest_area') then highway else null end)) as highway,\ncase when religion in ('christian','jewish') then religion else 'INT-generic'::text end as religion\n       from planet_osm_polygon\n       where landuse is not null\n          or leisure is not null\n          or aeroway in ('apron','aerodrome')\n          or amenity in ('parking','university','college','school','hospital','kindergarten','grave_yard')\n          or military in ('barracks','danger_area')\n          or \"natural\" in ('field','beach','desert','heath','mud','grassland','wood','sand','scrub')\n          or power in ('station','sub_station','generator')\n          or tourism in ('attraction','camp_site','caravan_site','picnic_site','zoo')\n          or highway in ('services','rest_area')\n       order by z_order,way_area desc\n      ) as landcover\n) as features",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "landcover-line",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "landcover-line",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way\nfrom planet_osm_line\nwhere man_made='cutline'\n) as landcover_line",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "sports-grounds",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "sports-grounds",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,leisure,\ncase when leisure='pitch' then 2\n  when leisure='track' then 1\n  else 0 end as prio\n  from planet_osm_polygon\n  where leisure in ('sports_centre','stadium','pitch','track')\n  order by z_order,prio,way_area desc\n) as sports_grounds",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "water-lines-casing",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "water-lines-casing",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,waterway\n      from planet_osm_line\n      where waterway in ('stream','drain','ditch')\n        and (tunnel is null or tunnel != 'yes')\n      ) as water_lines_casing",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "water-lines-low-zoom",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "water-lines-low-zoom",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,waterway\n      from planet_osm_line\n      where waterway='river'\n      ) as water_lines_low_zoom",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "water-areas",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "water-areas",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "water-areas",
                "table": "      (select way,\"natural\",waterway,landuse,name\n      from planet_osm_polygon\n      where (waterway in ('dock','mill_pond','riverbank','canal')\n         or landuse in ('reservoir','water','basin')\n         or \"natural\" in ('lake','water','land','glacier','mud'))\n         and building is null\n      order by z_order,way_area desc\n      ) as water_areas",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "water-areas-overlay",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "water-areas-overlay",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,\"natural\"\n      from planet_osm_polygon\n      where \"natural\" in ('marsh','wetland') and building is null\n      order by z_order,way_area desc\n      ) as water_areas_overlay",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "water-lines",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "water-lines",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,waterway,lock,name,tunnel\n      from planet_osm_line\n      where waterway in ('weir','river','canal','derelict_canal','stream','drain','ditch','wadi')\n        and (bridge is null or bridge not in ('yes','true','1','aqueduct'))\n      order by z_order\n      ) as water_lines",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "dam",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "dam",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,name from planet_osm_line where waterway='dam') as dam",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "marinas-area",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "marinas-area",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "marinas-area",
                "table": "(select way from planet_osm_polygon where leisure ='marina') as marinas_area",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "piers-area",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "piers-area",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,man_made from planet_osm_polygon where man_made in ('pier','breakwater','groyne')) as piers_area",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "piers",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "piers",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,man_made from planet_osm_line where man_made in ('pier','breakwater','groyne')) as piers",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "locks",
            "srs-name": "900913",
            "geometry": "point",
            "id": "locks",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,waterway from planet_osm_point where waterway='lock_gate') as locks",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "properties": {
                "group-by": "layernotnull"
            },
            "name": "tunnels",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "tunnels",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,coalesce(('highway_' || highway), ('railway_' ||(case when railway='preserved' and service in ('spur','siding','yard') then 'INT-preserved-ssy'::text when (railway='rail' and service in ('spur','siding','yard'))  then 'INT-spur-siding-yard' when railway in ('light_rail', 'narrow_gauge', 'funicular', 'rail', 'subway', 'tram', 'spur', 'siding', 'monorail', 'platform', 'preserved', 'disused', 'construction', 'miniature', 'turntable') then railway else null end)), ('aeroway_' || aeroway)) as feature, sac_scale, horse, foot, bicycle, tracktype, case when access in ('permissive') then 'permissive'::text when access in ('destination') then 'destination'::text when access in ('no', 'private') then 'no'::text else null end as access, construction, case when service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as service, case when oneway in ('yes', '-1') and highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street','construction') then oneway else null end as oneway, case when layer is null then '0' else layer end as layernotnull from planet_osm_line where (highway in ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'road', 'unclassified', 'service', 'pedestrian', 'living_street', 'raceway', 'bridleway', 'footway', 'cycleway', 'path', 'track', 'steps', 'platform', 'proposed', 'construction')  or aeroway in ('runway','taxiway') or railway in ('light_rail', 'subway', 'narrow_gauge',  'rail', 'spur', 'siding', 'preserved', 'funicular', 'tram', 'monorail', 'platform', 'miniature', 'turntable', 'disused', 'construction')) and (tunnel='yes' or tunnel='building_passage' or covered='yes') order by z_order) as tunnels",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "tunnels-fill tunnels-casing access directions",
            "advanced": {}
        },
        {
            "name": "citywalls",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "citywalls",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where \"historic\"='citywalls') as citywalls",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "castlewalls",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "castlewalls",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where \"historic\"='castle_walls') as castlewalls",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "castlewalls",
            "advanced": {}
        },
        {
            "name": "castlewalls-poly",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "castlewalls-poly",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_polygon where \"historic\"='castle_walls') as castlewalls_poly",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "castlewalls",
            "advanced": {}
        },
        {
            "name": "landuse-overlay",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "landuse-overlay",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "landuse-overlay",
                "table": "(select way,landuse,leisure\n       from planet_osm_polygon\n       where (landuse = 'military') and building is null\n      ) as landuse_overlay",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "line-barriers",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "line-barriers",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "line-barriers",
                "table": "(select way, barrier from planet_osm_line where barrier is not null) as line_barriers",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "barriers",
            "advanced": {}
        },
        {
            "name": "cliffs",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "cliffs",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,\"natural\",man_made from planet_osm_line where \"natural\" = 'cliff' or man_made = 'embankment') as cliffs",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "area-barriers",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "area-barriers",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,barrier from planet_osm_polygon where barrier is not null) as area_barriers",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "barriers",
            "advanced": {}
        },
        {
            "name": "ferry-routes",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "ferry-routes",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where route='ferry' ) as ferry_routes",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "turning-circle-casing",
            "srs-name": "900913",
            "geometry": "point",
            "id": "turning-circle-casing",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select distinct on (p.way) p.way as way,l.highway as int_tc_type,case when l.service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as int_tc_service\n       from planet_osm_point p\n       join planet_osm_line l\n        on ST_DWithin(p.way,l.way,0.1)\n       join (values\n        ('tertiary',1),\n        ('unclassified',2),\n        ('residential',3),\n        ('living_street',4),\n        ('service',5)\n       ) as v (highway,prio)\n        on v.highway=l.highway\n       where p.highway='turning_circle'\n       order by p.way,v.prio\n      ) as turning_circle_casing",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-casing",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "roads-casing",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,coalesce(('highway_' || highway), ('railway_' ||(case when railway in ('light_rail', 'abandoned', 'spur', 'siding', 'yard', 'narrow_gauge', 'funicular', 'rail', 'subway', 'tram', 'spur', 'siding', 'monorail', 'platform', 'preserved', 'disused', 'construction', 'miniature', 'turntable') then railway else null end)), ('aeroway_' || aeroway)) as feature, horse, foot, bicycle, tracktype, case when access in ('permissive') then 'permissive'::text when access in ('destination') then 'destination'::text when access in ('no', 'private') then 'no'::text else null end as access, construction, case when service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as service, case when oneway in ('yes', '-1') and highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street','construction') then oneway else null end as oneway, case when layer is null then '0' else layer end as layernotnull from planet_osm_line where (highway in ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'road', 'unclassified', 'service', 'pedestrian', 'living_street', 'raceway', 'bridleway', 'footway', 'cycleway', 'path', 'track', 'steps', 'platform', 'proposed', 'construction')  or aeroway in ('runway','taxiway') or railway in ('light_rail', 'abandoned', 'subway', 'narrow_gauge',  'rail', 'spur', 'siding', 'preserved', 'funicular', 'tram', 'monorail', 'platform', 'miniature', 'turntable', 'disused', 'construction')) and (tunnel is null or not tunnel in ('yes','true','1')) and (bridge is null or not bridge in ('yes','true','1','viaduct')) order by z_order)  as roads",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "roads-casing",
            "advanced": {}
        },
        {
            "name": "highway-area-fill",
            "srs-name": "900913",
            "id": "highway-area-fill",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "highway-area-fill",
                "table": "(select way,coalesce(('highway_' || (case when highway in ('cycleway','living_street','services') then 'cycleway' else null end)), ('highway_' || (case when highway in ('pedestrian') then 'pedestrian' else null end)), ('highway_' || (case when highway in ('service') then 'service' else null end)), ('highway_' || (case when highway in ('residential') then 'residential' else null end)),  ('highway_' || (case when highway in ('unclassified') then 'unclassified' else null end)), ('highway_' || (case when highway in ('footway') then 'footway'else null end)), ('highway_' || (case when highway in ('path') then 'path'else null end)), ('highway_' || (case when highway in ('track') then 'track' else null end)), ('highway_' || (case when highway in ('platform') then 'platform' else null end)), ('railway_' || (case when railway in ('platform') then 'platform' else null end)), ('aeroway_' || (case when aeroway in ('runway') then 'runway' else null end)), ('aeroway_' || (case when aeroway in ('helipad') then 'helipad' else null end)), ('aeroway_' || (case when aeroway in ('aeroway') then 'aeroway' else null end))) as feature from planet_osm_polygon\n       where highway in ('residential','unclassified','pedestrian','service','footway','living_street','track','path','platform','services')\n          or railway in ('platform')\n          or aeroway in ('runway','taxiway','helipad')\n       order by z_order,way_area desc) as highway_area_fill",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "buildings-lz",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "buildings-lz",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,building,railway,amenity from planet_osm_polygon\n       where railway='station'\n          or building in ('station','supermarket')\n          or amenity='place_of_worship'\n       order by z_order,way_area desc) as buildings_lz",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "highway-area-casing",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "highway-area-casing",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "highway-area-casing",
                "table": "(select way,coalesce(('highway_' || (case when highway in ('cycleway') then 'cycleway' else null end)),  ('highway_' || (case when highway in ('pedestrian') then 'pedestrian' else null end)),  ('highway_' || (case when highway in ('service') then 'service' else null end)),  ('highway_' || (case when highway in ('residential') then 'residential' else null end)), ('highway_' || (case when highway in ('unclassified') then 'unclassified' else null end)), ('highway_' || (case when highway in ('footway') then 'footway'else null end)), ('highway_' || (case when highway in ('path') then 'path'else null end)), ('highway_' || (case when highway in ('track') then 'track' else null end)), ('highway_' || (case when highway in ('platform') then 'platform' else null end)), ('railway_' || (case when railway in ('platform') then 'platform' else null end))) as feature from planet_osm_polygon\n       where highway in ('residential','unclassified','pedestrian','service','footway','track','path','platform')\n          or railway in ('platform')\n       order by z_order,way_area desc) as highway_area_casing",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "buildings",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "buildings",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,aeroway,\n        case\n         when building in ('garage','roof','garages','service','shed','shelter','cabin','storage_tank','tank','support','glasshouse','greenhouse','mobile_home','kiosk','silo','canopy','tent') then 'INT-light'::text\n         else building\n        end as building\n       from planet_osm_polygon\n       where (building is not null\n         and building not in ('no','station','supermarket','planned')\n         and (railway is null or railway != 'station')\n         and (amenity is null or amenity != 'place_of_worship'))\n          or aeroway = 'terminal'\n       order by z_order,way_area desc) as buildings",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-fill",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "roads-fill",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "roads-fill",
                "table": "      (select way,coalesce(('highway_' || highway), ('railway_' ||(case when railway in ('light_rail', 'abandoned', 'spur', 'siding', 'yard', 'narrow_gauge', 'funicular', 'rail', 'subway', 'tram', 'spur', 'siding', 'monorail', 'platform', 'preserved', 'disused', 'construction', 'miniature', 'turntable') then railway else null end)), ('aeroway_' || aeroway)) as feature, sac_scale, horse, foot, bicycle, tracktype, case when access in ('permissive') then 'permissive'::text when access in ('destination') then 'destination'::text when access in ('no', 'private') then 'no'::text else null end as access, construction, case when service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as service, case when oneway in ('yes', '-1') and highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street','construction') then oneway else null end as oneway, case when layer is null then '0' else layer end as layernotnull from planet_osm_line where (highway in ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'road', 'unclassified', 'service', 'pedestrian', 'living_street', 'raceway', 'bridleway', 'footway', 'cycleway', 'path', 'track', 'steps', 'platform', 'proposed', 'construction')  or aeroway in ('runway','taxiway') or railway in ('light_rail', 'abandoned', 'subway', 'narrow_gauge',  'rail', 'spur', 'siding', 'preserved', 'funicular', 'tram', 'monorail', 'platform', 'miniature', 'turntable', 'disused', 'construction')) and (tunnel is null or not tunnel in ('yes','true','1')) and (bridge is null or not bridge in ('yes','true','1','viaduct')) order by z_order)  as roads_fill",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "roads-fill access directions",
            "advanced": {}
        },
        {
            "name": "turning-circle-fill",
            "srs-name": "900913",
            "geometry": "point",
            "id": "turning-circle-fill",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select distinct on (p.way) p.way as way,l.highway as int_tc_type,case when l.service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as int_tc_service\n       from planet_osm_point p\n       join planet_osm_line l\n        on ST_DWithin(p.way,l.way,0.1)\n       join (values\n        ('tertiary',1),\n        ('unclassified',2),\n        ('residential',3),\n        ('living_street',4),\n        ('service',5)\n       ) as v (highway,prio)\n        on v.highway=l.highway\n       where p.highway='turning_circle'\n       order by p.way,v.prio\n      ) as turning_circle_fill",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "aerialways",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "aerialways",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,aerialway from planet_osm_line where aerialway is not null) as aerialways",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-low-zoom",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "roads-low-zoom",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,coalesce(('highway_' || (case when highway is not null then highway else null end)), ('railway_' || (case when (railway='rail' and service in ('spur','siding','yard'))  then 'INT-spur-siding-yard' when railway in ('rail','tram','light_rail','funicular','narrow_gauge') then railway else null end))) as feature,tunnel\n       from planet_osm_roads\n       where highway is not null\n          or (railway is not null and railway!='preserved' and (service is null or service not in ('spur','siding','yard')))\n       order by z_order\n      ) as roads_low_zoom",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "waterway-bridges",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "waterway-bridges",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,name from planet_osm_line where waterway='canal' and bridge in ('yes','true','1','aqueduct') order by z_order) as waterway_bridges",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "properties": {
                "group-by": "layernotnull"
            },
            "name": "bridges",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "bridges",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "bridges",
                "table": "(select way,coalesce(('highway_' || highway), ('railway_' ||(case when railway='preserved' and service in ('spur','siding','yard') then 'INT-preserved-ssy'::text when (railway='rail' and service in ('spur','siding','yard'))  then 'INT-spur-siding-yard' when railway in ('light_rail', 'narrow_gauge', 'funicular', 'rail', 'subway', 'tram', 'spur', 'siding', 'monorail', 'platform', 'preserved', 'disused', 'construction', 'miniature', 'turntable') then railway else null end)), ('aeroway_' || aeroway)) as feature, sac_scale, horse, foot, bicycle, tracktype, case when access in ('permissive') then 'permissive'::text when access in ('destination') then 'destination'::text when access in ('no', 'private') then 'no'::text else null end as access, construction, case when service in ('parking_aisle','drive-through','driveway') then 'INT-minor'::text else 'INT-normal'::text end as service, case when oneway in ('yes', '-1') and highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street','construction') then oneway else null end as oneway, case when layer is null then '0' else layer end as layernotnull from planet_osm_line where (highway in ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'road', 'unclassified', 'service', 'pedestrian', 'living_street', 'raceway', 'bridleway', 'footway', 'cycleway', 'path', 'track', 'steps', 'platform', 'proposed', 'construction')  or aeroway in ('runway','taxiway') or railway in ('light_rail', 'subway', 'narrow_gauge',  'rail', 'spur', 'siding', 'preserved', 'funicular', 'tram', 'monorail', 'platform', 'miniature', 'turntable', 'disused', 'construction')) and bridge in ('yes','true','1','viaduct') and (layer is null or (layer in ('0','1','2','3','4','5'))) order by layernotnull, z_order) as bridges",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "bridges-fill bridges-casing access directions",
            "advanced": {}
        },
        {
            "name": "trams",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "trams",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,railway,bridge from planet_osm_line where railway='tram' and (tunnel is null or tunnel != 'yes')) as trams",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "guideways",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "guideways",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where highway='bus_guideway' and (tunnel is null or tunnel != 'yes')) as guideways",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "admin-01234",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "admin-01234",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way,admin_level\n       from planet_osm_roads\n       where \"boundary\"='administrative'\n         and admin_level in ('0','1','2','3','4')\n       ) as admin_01234",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "admin-5678",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "admin-5678",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "admin-5678",
                "table": "(select way,admin_level\n       from planet_osm_roads\n       where \"boundary\"='administrative'\n         and admin_level in ('5','6','7','8')\n       ) as admin_5678",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "admin-other",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "admin-other",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "admin-other",
                "table": "(select way,admin_level\n       from planet_osm_roads\n       where \"boundary\"='administrative'\n         and admin_level in ('9', '10')\n       ) as admin_other",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "power-minorline",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "power-minorline",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where \"power\"='minor_line') as power_minorline",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "power-line",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "power-line",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where \"power\"='line') as power_line",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "nepopulated",
            "srs-name": "WGS84",
            "geometry": "point",
            "class": "",
            "srs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs",
            "Datasource": {
                "encoding": "LATIN1",
                "project": "github",
                "srs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs",
                "file": "data/ne_10m_populated_places/ne_10m_populated_places_orderBy_POP_MAX.shp",
                "type": "shape",
                "id": "nepopulated"
            },
            "extent": [
                -179.58997888396897,
                -85.051,
                179.38330358817018,
                82.48332318035943
            ],
            "id": "nepopulated",
            "advanced": {
                "encoding": "LATIN1"
            }
        },
        {
            "name": "placenames-large",
            "srs-name": "900913",
            "geometry": "point",
            "id": "placenames-large",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "placenames-large",
                "table": "(select way,place,name,ref\n       from planet_osm_point\n       where place in ('country','state')\n      ) as placenames_large",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "country state",
            "advanced": {}
        },
        {
            "name": "placenames-capital",
            "srs-name": "900913",
            "geometry": "point",
            "id": "placenames-capital",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "placenames-capital",
                "table": "(select way,place,name,ref\n       from planet_osm_point\n       where place in ('city','town') and capital='yes'\n      ) as placenames_capital",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "placenames-medium",
            "srs-name": "900913",
            "geometry": "point",
            "id": "placenames-medium",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "placenames-medium",
                "table": "(select way,place,name\n      from planet_osm_point\n      where place in ('city','town')\n        and (capital is null or capital != 'yes')\n      ) as placenames_medium",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "placenames-small",
            "srs-name": "900913",
            "geometry": "point",
            "id": "placenames-small",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "placenames-small",
                "table": "(select way,place,name\n      from planet_osm_point\n      where place in ('suburb','village','hamlet','neighbourhood','locality','isolated_dwelling','farm')\n      ) as placenames_small",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "stations",
            "srs-name": "900913",
            "geometry": "point",
            "id": "stations",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,name,railway,aerialway,disused\n      from planet_osm_point\n      where railway in ('station','halt','tram_stop','subway_entrance')\n         or aerialway='station'\n      ) as stations",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "stations",
            "advanced": {}
        },
        {
            "name": "stations-poly",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "stations-poly",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,name,railway,aerialway,disused\n      from planet_osm_polygon\n      where railway in ('station','halt','tram_stop')\n         or aerialway='station'\n      ) as stations_poly",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "stations",
            "advanced": {}
        },
        {
            "name": "glaciers-text",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "glaciers-text",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "glaciers-text",
                "table": "      (select way,name,way_area\n      from planet_osm_polygon\n      where \"natural\"='glacier' and building is null\n      order by way_area desc\n      ) as glaciers_text",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "amenity-symbols",
            "srs-name": "900913",
            "geometry": "point",
            "id": "amenity-symbols",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "amenity-symbols",
                "table": "(select *\n      from planet_osm_point\n      where aeroway in ('aerodrome','helipad')\n         or barrier in ('bollard','gate','lift_gate','block')\n         or highway in ('mini_roundabout','gate')\n         or man_made in ('lighthouse','power_wind','windmill','mast')\n         or (power='generator' and (\"generator:source\"='wind' or power_source='wind'))\n         or \"natural\" in ('peak','volcano','spring','tree','cave_entrance')\n         or railway='level_crossing'\n      ) as amenity_symbols",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "symbols",
            "advanced": {}
        },
        {
            "name": "amenity-symbols-poly",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "amenity-symbols-poly",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "amenity-symbols-poly",
                "table": "(select *\n      from planet_osm_polygon\n      where aeroway in ('aerodrome','helipad')\n         or barrier in ('bollard','gate','lift_gate','block')\n         or highway in ('mini_roundabout','gate')\n         or man_made in ('lighthouse','power_wind','windmill','mast')\n         or (power='generator' and (\"generator:source\"='wind' or power_source='wind'))\n         or \"natural\" in ('peak','volcano','spring','tree')\n         or railway='level_crossing'\n      ) as amenity_symbols_poly",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "symbols",
            "advanced": {}
        },
        {
            "name": "amenity-points",
            "srs-name": "900913",
            "geometry": "point",
            "id": "amenity-points",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "amenity-points",
                "table": "(select way,amenity,shop,tourism,highway,man_made,access,religion,waterway,lock,historic,leisure\n      from planet_osm_point\n      where amenity is not null\n         or shop is not null\n         or tourism in ('alpine_hut','camp_site','picnic_site','caravan_site','guest_house','hostel','hotel','motel','museum','viewpoint','bed_and_breakfast','information','chalet')\n         or highway in ('bus_stop','traffic_signals','ford')\n         or man_made in ('mast','water_tower')\n         or historic in ('memorial','archaeological_site')\n         or waterway='lock'\n         or lock='yes'\n         or leisure in ('playground','slipway','picnic_table')\n      ) as amenity_points",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "points",
            "advanced": {}
        },
        {
            "name": "amenity-points-poly",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "amenity-points-poly",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "amenity-points-poly",
                "table": "(select way,amenity,shop,tourism,highway,man_made,access,religion,waterway,lock,historic,leisure\n      from planet_osm_polygon\n      where amenity is not null\n         or shop is not null\n         or tourism in ('alpine_hut','camp_site','picnic_site','caravan_site','guest_house','hostel','hotel','motel','museum','viewpoint','bed_and_breakfast','information','chalet')\n         or highway in ('bus_stop','traffic_signals')\n         or man_made in ('mast','water_tower')\n         or historic in ('memorial','archaeological_site')\n         or leisure in ('playground', 'picnic_table')\n      ) as amenity_points_poly",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "points",
            "advanced": {}
        },
        {
            "name": "power-towers",
            "srs-name": "900913",
            "geometry": "point",
            "id": "power-towers",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_point where power='tower') as power_towers",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "power-poles",
            "srs-name": "900913",
            "geometry": "point",
            "id": "power-poles",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_point where power='pole') as power_poles",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-text-ref-low-zoom",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "roads-text-ref-low-zoom",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,highway,ref,char_length(ref) as length\n       from planet_osm_roads\n       where highway in ('motorway','trunk','primary','secondary')\n         and ref is not null\n         and char_length(ref) between 1 and 8\n      ) as roads_text_ref_low_zoom",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "highway-junctions",
            "srs-name": "900913",
            "geometry": "point",
            "id": "highway-junctions",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "     (select way,ref,name\n      from planet_osm_point\n      where highway='motorway_junction'\n     ) as highway_junctions",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-text-ref",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "roads-text-ref",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,coalesce(highway,aeroway) as highway,ref,char_length(ref) as length,\n       case when bridge in ('yes','true','1') then 'yes'::text else 'no'::text end as bridge\n       from planet_osm_line\n       where (highway is not null or aeroway is not null)\n         and ref is not null\n         and char_length(ref) between 1 and 8\n      ) as roads_text_ref",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-area-text-name",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "roads-area-text-name",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way, highway, name\n       from planet_osm_polygon\n       where highway='pedestrian'\n         and name is not null\n      ) as roads_area_text_name",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "roads-text-name",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "roads-text-name",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "roads-text-name",
                "table": "      (select way, highway, name\n       from planet_osm_line\n       where highway in ('motorway','motorway_link','trunk','trunk_link','primary','primary_link','secondary','secondary_link','tertiary','tertiary_link','residential','unclassified','road','service','pedestrian','raceway','living_street', 'construction','proposed','road', 'minor', 'living street', 'unsurfaced', 'track', 'byway', 'footway', 'bridleway', 'path', 'cycleway') \n         and name is not null\n      ) as roads_text_name",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "paths-text-name",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "paths-text-name",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way, highway, name\n       from planet_osm_line\n       where highway in ('bridleway', 'footway', 'cycleway', 'path', 'track', 'steps') \n         and name is not null\n      ) as paths_text_name",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "text",
            "srs-name": "900913",
            "geometry": "point",
            "id": "text",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "text",
                "table": "      (select way,amenity,shop,access,leisure,landuse,man_made,\"natural\",place,tourism,ele,name,ref,military,aeroway,waterway,historic,NULL as way_area\n       from planet_osm_point\n       where amenity is not null\n          or shop in ('supermarket','bakery','clothes','fashion','convenience','doityourself','hairdresser','department_store','butcher','car','car_repair','bicycle','florist')\n          or leisure is not null\n          or landuse is not null\n          or tourism is not null\n          or \"natural\" is not null\n          or man_made in ('lighthouse','windmill')\n          or place='island'\n          or military='danger_area'\n          or aeroway='gate'\n          or waterway='lock'\n          or historic in ('memorial','archaeological_site')\n      ) as text",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "text",
            "advanced": {}
        },
        {
            "name": "text-poly",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "text-poly",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "text-poly",
                "table": "(select way,aeroway,shop,access,amenity,leisure,landuse,man_made,\"natural\",place,tourism,NULL as ele,name,ref,military,waterway,historic,way_area\n       from planet_osm_polygon\n       where amenity is not null\n          or shop in ('supermarket','bakery','clothes','fashion','convenience','doityourself','hairdresser','department_store', 'butcher','car','car_repair','bicycle')\n          or leisure is not null\n          or landuse is not null\n          or tourism is not null\n          or \"natural\" is not null\n          or man_made in ('lighthouse','windmill')\n          or place='island'\n          or military='danger_area'\n          or historic in ('memorial','archaeological_site')\n      ) as text_poly",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "text",
            "advanced": {}
        },
        {
            "name": "building-text",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "building-text",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "building-text",
                "table": "(select name, way, way_area from planet_osm_polygon where building is not null  and building not in ('no','station','supermarket')) as building_text",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "interpolation",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "interpolation",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "(select way from planet_osm_line where \"addr:interpolation\" is not null) as interpolation",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "housenumbers",
            "srs-name": "900913",
            "geometry": "point",
            "id": "housenumbers",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,\"addr:housenumber\" from planet_osm_polygon where \"addr:housenumber\" is not null and building is not null\n       union\n       select way,\"addr:housenumber\" from planet_osm_point where \"addr:housenumber\" is not null\n      ) as housenumbers",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "housenames",
            "srs-name": "900913",
            "geometry": "point",
            "id": "housenames",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "GitLab_Austausch",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "housenames",
                "table": "(select way,\"addr:housename\" from planet_osm_polygon where \"addr:housename\" is not null and building is not null\n       union\n       select way,\"addr:housename\" from planet_osm_point where \"addr:housename\" is not null\n      ) as housenames",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "water-lines-text",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "water-lines-text",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "table": "      (select way,waterway,lock,name,tunnel\n      from planet_osm_line\n      where waterway in ('weir','river','canal','derelict_canal','stream','drain','ditch','wadi')\n       order by z_order\n      ) as water_lines_text",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "admin-text",
            "srs-name": "900913",
            "geometry": "linestring",
            "id": "admin-text",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "custom",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "admin-text",
                "table": "(select way, name, admin_level from planet_osm_polygon where \"boundary\" = 'administrative' and admin_level in ('0','1','2','3','4','5','6','7','8','9','10')) as admin_text",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "nature-reserve-boundaries",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "nature-reserve-boundaries",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "nature-reserve-boundaries",
                "table": "(select way,way_area,name,boundary from planet_osm_polygon where (boundary='national_park' or leisure='nature_reserve') and building is null) as national_park_boundaries",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        },
        {
            "name": "theme-park",
            "srs-name": "900913",
            "geometry": "polygon",
            "id": "theme-park",
            "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
            "Datasource": {
                "project": "github",
                "extent_cache": "auto",
                "geometry_field": "way",
                "dbname": "osm_lux",
                "port": "5432",
                "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
                "host": "localhost",
                "user": "postgres",
                "extent": "-20037508,-19929239,20037508,19929239",
                "id": "theme-park",
                "table": "(select way,name,tourism from planet_osm_polygon where tourism='theme_park') as theme_park",
                "password": "postgres",
                "type": "postgis",
                "key_field": ""
            },
            "extent": [
                -179.99999692067183,
                -84.96651228427099,
                179.99999692067183,
                84.96651228427098
            ],
            "class": "",
            "advanced": {}
        }
    ],
    "scale": 1,
    "attribution": "",
    "center": [
        7.4085,
        52.4247,
        3
    ],
    "format": "png",
    "description": "A faithful reimplementation of the standard komoot style",
    "metatile": 2,
    "bounds": [
        11.385,
        47.2499,
        11.4698,
        47.2935
    ],
    "Stylesheet": [
        "style.mss",
        "landcover.mss",
        "water.mss",
        "water-features.mss",
        "roads.mss",
        "power.mss",
        "citywalls.mss",
        "buildings.mss",
        "placenames.mss",
        "amenity-symbols.mss",
        "stations.mss",
        "amenity-points.mss",
        "ferry-routes.mss",
        "aerialways.mss",
        "admin.mss",
        "addressing.mss",
        "colors.mss"
    ],
    "srs": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over",
    "minzoom": 0,
    "maxzoom": 17,
    "legend": "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=utf-8 />\n<title>Legend</title>\n<meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />\n<script src='https://api.tiles.mapbox.com/mapbox.js/v2.1.4/mapbox.js'></script>\n<link href='https://api.tiles.mapbox.com/mapbox.js/v2.1.4/mapbox.css' rel='stylesheet' />\n<style>\n  body { margin:0; padding:0; }\n  #map { position:absolute; top:0; bottom:0; width:100%; }\n</style>\n</head>\n<body>\n<div id='map'></div>\n\n<script>\nL.mapbox.accessToken = 'pk.eyJ1Ijoia210IiwiYSI6IktWWXhIVVUifQ.K6cG0NyrkkN5rbscptd3Qg';\n  L.mapbox.map('map', 'examples.map-zmy97flj');\n</script>\n</body>\n</html>",
    "name": "komoot-carto"
}