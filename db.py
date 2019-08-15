from weather import weather
import mysql.connector

def saveDb(weathers):
    print('save db')
    cnx = mysql.connector.connect(
        host="localhost",
        user="wangxin",
        passwd="123456",
        auth_plugin='mysql_native_password'
    )

    create_database_sql = 'CREATE DATABASE IF NOT EXISTS db_weather'
    cursor = cnx.cursor(buffered=True)
    cursor.execute(create_database_sql)
    cursor.close()
    cnx.close()

    cnx = mysql.connector.connect(
        host="localhost",
        user="wangxin",
        passwd="123456",
        database="db_weather",
        auth_plugin='mysql_native_password'
    )
    create_table_sql = 'CREATE TABLE IF NOT EXISTS t_weather (province VARCHAR(128), city VARCHAR(128) NOT NULL, date VARCHAR(256) NOT NULL, phenomenon VARCHAR(256), temperature INT, wind_direction VARCHAR(256), wind_power VARCHAR(256), PRIMARY KEY (province, city, date)) ENGINE=InnoDB DEFAULT CHARSET=utf8'
    cursor = cnx.cursor(buffered=True)
    cursor.execute(create_table_sql)

    for w in weathers:
        insert_weather_sql = (
            "INSERT INTO t_weather (province, city, date, phenomenon, temperature, wind_direction, wind_power) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_weather_sql, (w.province, w.city, w.date, w.phenomenon, w.temperature, w.wind_direction, w.wind_power))
        cnx.commit()
        pass
    
    cursor.close()
    cnx.close()
    pass