import urllib.request
import io

req=urllib.request.urlopen('https://www.nrc.gov/pmns/mtg')
charset=req.info().get_content_charset()
content=req.read().decode(charset)
first = True
sql = ''

for row in content.split('<tr class='):
    if not first:
        cols = row.split('<td>')
        datetime = " ".join(cols[1].replace('\r', '').replace('\n', '').replace('\t', '').replace("'", "''").split())
        purpose = " ".join(cols[2].replace('\r', '').replace('\n', '').replace('\t', '').replace("'", "''").split())
        location = " ".join(cols[3].replace('\r', '').replace('\n', '').replace('\t', '').replace("'", "''").split())
        contact = " ".join(cols[4].replace('\r', '').replace('\n', '').replace('\t', '').replace("'", "''").split())
        sql += "INSERT INTO PublicMeetingsScheduled VALUES ('" + datetime + "', '" + purpose + "', '" + location + "', '" + contact + "');\n"
        x = 2 + 2
    else:
        first = False

with io.open("C:\\Users\\Steve\\Documents\\insert_events.sql", "w", encoding="utf-8") as f:
    f.write(sql)

