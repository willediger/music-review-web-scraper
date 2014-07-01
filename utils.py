import sqlite3
import scraper

sqlite_file = 'D:\\test\\album_list.sqlite'
grabbed_albums_tbl = 'grabbed_albums'
new_albums_tbl = 'new_albums'
artist_field = 'artist_name'
album_field = 'album_name'
field_type = 'text'

def create_album_table(table_name):
    # c.execute('drop table if exists {tn}'.format(tn=table_name))
    c.execute('create table {tn} ({nf} {ft}, {nf2} {ft}, primary key({nf}, {nf2}))'
          .format(tn=table_name, nf=artist_field, ft=field_type, nf2=album_field))
    return True

def drop_table(table_name):
    c.execute('drop table {tn}'.format(tn=table_name))
    return True

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

drop_table(grabbed_albums_tbl)
drop_table(new_albums_tbl)

#creates album tables with composite key of artist & album names, given table_name

create_album_table(grabbed_albums_tbl)
create_album_table(new_albums_tbl)

albums = scraper.good_albums()

c.executemany('insert into {t} values (?,?)'.format(t=new_albums_tbl), albums)
conn.commit()