#!/usr/env/bin/python3.6.9

# ==============================================================
#          Credentials Controller and Database
#
#
# ==============================================================

# parameters controller authentication
USERNAME = "admin"
PASSWORD = "ciscopsdt"
IP_CONTROLLER = "sandboxapicdc.cisco.com"


# parameters database authentication
USERNAME_DB = "bryan"
PASSWORD_DB = "claro123"
DATABASE = "DATASETS"
HOSTNAME = "127.0.0.1"
UID_MYSQL = 123
GUID_MYSQL = 134


# list_files
LIST_FILES = [
    "/var/lib/mysql/"+DATABASE+"/inventory.csv",
    "/var/lib/mysql/"+DATABASE+"/interfaces.csv",
    "/var/lib/mysql/"+DATABASE+"/alarms.csv",
    "/var/lib/mysql/"+DATABASE+"/status_interfaces.csv"
]

