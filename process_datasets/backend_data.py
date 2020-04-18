#!/usr/env/bin/python3.6.9
from credentials.credentials import USERNAME_DB, PASSWORD_DB, HOSTNAME, DATABASE
import pymysql

# function process data backend with MariaDB Server


def connection_database(username=USERNAME_DB, hostname=HOSTNAME, password=PASSWORD_DB, database=DATABASE):
    try:
        cnx = pymysql.connections.Connection(
            host=hostname,
            user=username,
            password=password,
            database=database,
            port=3306)
        # define cursor
        return cnx
    except pymysql.err.ProgrammingError as err:
        return "Error in connect Database {}".format(err.args)


def queries_data_sql(*args):
    cnx = connection_database()
    cnx_cursor = cnx.cursor()
    for index in args:
        try:
            cnx_cursor.execute(index)
            cnx.commit()
        except pymysql.err.ProgrammingError as err:
            return "Error in execute sql process {}".format(err.args)
    cnx.close()


def response_data_query(sql):
    cnx = connection_database()
    cnx_cursor = cnx.cursor()
    cnx_cursor.execute(sql)
    return cnx_cursor.fetchall()
