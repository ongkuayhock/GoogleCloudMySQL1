import sqlalchemy
from sqlalchemy import create_engine

# Set the following variables depending on your specific
# connection name and root password from the earlier steps:
connection_name = "lamusic1:us-central1:lamysql"
db_password = "test1234"
db_name = "khproddb"

db_user = "root"
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

"""Responds to any HTTP request.
Args:
    request (flask.Request): HTTP request object.
Returns:
    The response text or any set of values that can be turned into a
    Response object using
    `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
"""

stmt = sqlalchemy.text('select * from khproddb.flights')
db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800
)
try:
    with db.connect() as conn:
        flights = conn.execute(stmt).fetchall()
except Exception as e:
    err1= 'Error: {}'.format(str(e))

print (err1)
print ("Ended")
print (flights)

#    flights = db.execute("SELECT * FROM flights").fetchall()
