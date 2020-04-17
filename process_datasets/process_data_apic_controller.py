#!/usr/env/bin/python3.6.9
from process_datasets.get_data_controller import *
from process_datasets.backend_data import *
import csv
import os

# list_files
LIST_FILES = [
    "/var/lib/mysql/DATASETS/inventory.csv",
    "/var/lib/mysql/DATASETS/interfaces.csv"
]


def process_data_inventory(file_csv):
    data_rows = get_data_inventory()
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' (adSt, address, annotation, apicType, childAction, delayedHeartbeat, dn, extMngdBy, fabricSt, id, lastStateModTs, lcOwn, modTs, model, monPolDn, name, nameAlias, nodeType, role, serial, status, uid, vendor, version)".format(file_csv, "aci_inventory")
    print("Execute query", sql_execute)
    queries_data_sql(sql_execute)


def process_data_interfaces(file_csv, id):
    data_rows = get_data_interface(id)
    for index in data_rows:
        index.append(id)
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' (`adminSt`, `autoNeg`, `brkoutMap`, `bw`, `childAction`, `delay`, `descr`, `dn`, `dot1qEtherType`, `ethpmCfgFailedBmp`,`ethpmCfgFailedTs`, `ethpmCfgState`, `fcotChannelNumber`, `fecMode`, `id`, `inhBw`, `isReflectiveRelayCfgSupported`, `layer`, `lcOwn`, `linkDebounce`, `linkLog`, `mdix`, `medium`, `modTs`, `mode`, `monPolDn`, `mtu`, `name`, `pathSDescr`, `portT`, `prioFlowCtrl`, `reflectiveRelayEn`, `routerMac`, `snmpTrapSt`, `spanMode`, `speed`, `status`, `switchingSt`,`trunkLog`, `usage`, `idParent`)".format(file_csv, "aci_interfaces")
    # print("execute query_sql ...", sql_execute)
    queries_data_sql(sql_execute)


# create files
def create_files(files_csv):
    for index in files_csv:
        if not os.path.isfile(index):
            os.mknod(index)
            # uid and guid mariaDB ...
            os.chown(index, 123, 134)


# delete files
def remove_files(files_csv):
    for index in files_csv:
        os.remove(index)


def execute_function():
    create_files(LIST_FILES)
    process_data_inventory(LIST_FILES[0])
    process_data_interfaces(LIST_FILES[1],"101")
    #remove_files(LIST_FILES)
