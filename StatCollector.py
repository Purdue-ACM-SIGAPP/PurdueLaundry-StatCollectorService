#!/usr/bin/python3.6.0
"""Stat Collector
  This module/microservice is used to collect data directly from the Machine Api
  It will then send the data along as an intermediary to the Machine Stats DB
"""
import configparser
import urllib.request
import json
import psycopg2

config = configparser.ConfigParser()
config.read('config')


def create_db_cursor() -> any:
    connection = connect_database()
    return connection.cursor()

def connect_database() -> any:
    db_config = dict(config['DATABASE'])
    connect_str = """host=%(host)s
                        port=%(port)s
                        user=%(user)s
                        password=%(password)s
                        dbname=%(name)s""" % db_config
    return psycopg2.connect(connect_str)

def get_stats() -> dict:
    """Function to retrieve stats from Machine Api
    Args:jj
        None
    Returns:
        dict: dictionary of data from machine api
    """
    with urllib.request.urlopen(config['MACHINES']['HOST'] + "/Laundry/location/all") as response:
        data = json.loads(response.read())
        return data
    return {}



def store_stats(cursor: any, stats: dict) -> bool:
    """Function to send stats from Machine Api to Machine Stats Api
    Args:
        cursor (obj): Postgres cursor that allows us to make queries to the database
        stats (dict): dictionary of stats to be sent to db
    Returns:
        bool:  Returns true if request is a success, false if unsuccessful
    """
    return True

def main():
    """Main function that will be run every minute based on cron job"""
    new_stats = get_stats()
    cursor = create_db_cursor()
    print("done")

if __name__ == "__main__":
    main()



