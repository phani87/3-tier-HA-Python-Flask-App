SECRET_KEY = 'CHANGE_ME'
# database connection uri
#SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb/Pass_Word_2018@129.146.166.76:1521/pdb1.sub07182009420.gartnerdemovcn.oraclevcn.com'
#SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb/Pass_Word_2018@mydb'

#SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb:Pass_Word_2018@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=129.146.166.76)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=pdb1.sub07182009420.gartnerdemovcn.oraclevcn.com)))'
#SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb:Pass_Word_2018@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=129.146.37.162)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=pdb1.dbsubnetad1.gartnerdemovcn.oraclevcn.com)))'

SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://appdb:PASS_Gartner_2018@(DESCRIPTION=(FAILOVER=on)(CONNECT_TIMEOUT=5)(RETRY_COUNT=10)(TRANSPORT_CONNECT_TIMEOUT=3)(ADDRESS_LIST=(LOAD_BALANCE=on)(ADDRESS=(PROTOCOL=TCP)(HOST=10.0.4.2)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=10.0.3.2)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.3.2)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=gartner.gartnerdemovcn.oraclevcn.com)))'
STATIC_ROOT = None


