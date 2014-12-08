#!/bin/bash

# echo "Type in your..."
# echo "Postgres Username:"
# read username
# echo "Host:(for localhost, just press [ENTER])"
# read host
# echo "Database:" 
# read database
# echo "Database Port:" 
# read port
# # echo "/home/user/path/to/your.style.txt:" 
# # read stylePath
# # echo "/home/user/path/to/your.style.txt:"  
# # read dataPath
# # 
# read -s -p "Postgres User Password:" password

username="postgres"
database="gis"
host="localhost"
port="5432"

# stylePath="/home/andreas/Projekte/osm-data/optimapCustom.style.txt"
# dataPath="/home/andreas/Projekte/osm-data/faroe-islands-latest.osm.pbf"

# stylePath="optimapCustom.style.txt"
# dataPath="faroe-islands-latest.osm.pbf"
export PGPASSWORD=$password

# echo "Please type in your postgres user password:"
createdb -U $username -h $host -p $port $database

# echo "Please type in your postgres user password:"
psql -U $username -h $host -p $port -d $database -c 'CREATE EXTENSION IF NOT EXISTS postgis; CREATE EXTENSION IF NOT EXISTS hstore;'

# echo "Please type in your postgres user password:"
# osm2pgsql -c --cache-strategy sparse -C 750 -U $username -H $host -P $port -W -S $stylePath -d $database -k $dataPath 
osm2pgsql -c --cache-strategy sparse -C 750 -U $username -H $host -P $port -S $stylePath -d $database -k $dataPath 