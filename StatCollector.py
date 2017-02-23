#!/usr/bin/python3.6.0
"""Stat Collector
  This module/microservice is used to collect data directly from the Machine Api
  It will then send the data along as an intermediary to the Machine Stats DB
"""
import configparser
import urllib.request

config = configparser.ConfigParser()
config.read('config')
DATABASE_URL = config['DATABASE']['Host']

MACHINE_URL = config['MACHINES']['Host']

def get_stats() -> dict:
    """Function to retrieve stats from Machine Api
    Args:
        None
    Returns:
        dict: dictionary of data from database
    """
    return {}


def store_stats(stats: dict) -> bool:
    """Function to send stats from Machine Api to database
    Args:
        stats (dict): dictionary of stats to be sent to db
    Returns:
        bool:  Returns true if request is a success, false if unsuccessful
    """
    return True

def main():
    """Main function that will be run every minute based on cron job"""
    store_stats(get_stats)
    print("done")

if __name__ == "__main__":
    main()



