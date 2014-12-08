select *      from planet_osm_point      where aeroway in ('aerodrome','helipad')         or barrier in ('bollard','gate','lift_gate','block')         or highway in ('mini_roundabout','gate')         or man_made in ('lighthouse','power_wind','windmill','mast')         or (power='generator' and ("generator:source"='wind' or power_source='wind'))         or "natural" in ('peak','volcano','spring','tree','cave_entrance')         or railway='level_crossing'      

