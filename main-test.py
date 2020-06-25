# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_cloudsql_mysql]
import os

from flask import Flask
import pymysql

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

db_user = "root"
db_password = "test1234"
db_name = "khproddb"
db_connection_name =  "lamusic1:us-central1:lamysql"

print( db_user )

cnx = pymysql.connect(user=db_user, password=db_password,
                        host=host, db=db_name)

with cnx.cursor() as cursor:
    cursor.execute('SELECT * from khproddb.flights;')
    result1 = cursor.fetchall()
    
cnx.close()
print('My SQL query result')
print (result1)
return (result1)
# [END gae_python37_cloudsql_mysql]
