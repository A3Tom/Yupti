#!/bin/bash

SERVER="localhost"
DATABASE="master"
USER="sa"
PASSWORD="ThePopeRunsTheR3m0"

/opt/mssql/bin/sqlservr & sleep 15

for i in {1..50};
do
    /opt/mssql-tools/bin/sqlcmd -S $SERVER -U $USER -P $PASSWORD -Q "SELECT 1" > /dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "SQL Server is ready"
        break
    else
        echo "Not ready yet..."
        sleep 1
    fi
done

for file in $(ls /app/schema/*.sql | sort)
do
    echo "Executing $file"
    /opt/mssql-tools/bin/sqlcmd -S $SERVER -d $DATABASE -U $USER -P $PASSWORD -i $file
done