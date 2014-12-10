import psycopg2 as pg

try:
    con = pg.connect(database='gis4',  user='postgres', password='postgres', host='localhost', port='5432')
    print 'YEAH!'
except:
    print 'nope'
    

try:    
    cur = con.cursor()
    cur.execute('SELECT way AS __geometry__ FROM planet_osm_line')
    
    version = cur.fetchone()
    print version
except:
    print 'none'

#finally:
    #if con:
        #con.close()


