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


def process_data_inventory(file_csv, table):
    if not os.path.isfile(file_csv):
        os.mknod(file_csv)
        os.chown(file_csv, 123, 134)
    data_rows = get_data_inventory()
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' " \
                  "(adSt, address, annotation, apicType, childAction, delayedHeartbeat, dn, extMngdBy, fabricSt, id," \
                  " lastStateModTs, lcOwn, modTs, model, monPolDn, name, nameAlias, nodeType, role, serial, status," \
                  " uid, vendor, version)".format(file_csv, table)
    print("Execute query", sql_execute)
    queries_data_sql(sql_execute)
    os.remove(file_csv)


def process_data_interfaces(file_csv, id_controller, table):
    if not os.path.isfile(file_csv):
        os.mknod(file_csv)
        os.chown(file_csv, 123, 134)
    data_rows = get_data_interface(id_controller)
    for index in data_rows:
        index.append(id_controller)
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' " \
                  "(`adminSt`, `autoNeg`, `brkoutMap`, `bw`, `childAction`, `delay`, `descr`, `dn`," \
                  " `dot1qEtherType`, `ethpmCfgFailedBmp`,`ethpmCfgFailedTs`, `ethpmCfgState`, `fcotChannelNumber`," \
                  " `fecMode`, `id`, `inhBw`, `isReflectiveRelayCfgSupported`, `layer`, `lcOwn`, `linkDebounce`," \
                  " `linkLog`, `mdix`, `medium`, `modTs`, `mode`, `monPolDn`, `mtu`, `name`, `pathSDescr`, `portT`," \
                  " `prioFlowCtrl`, `reflectiveRelayEn`, `routerMac`, `snmpTrapSt`, `spanMode`, `speed`, `status`," \
                  " `switchingSt`,`trunkLog`, `usage`, `idParent`)".format(file_csv, table)
    # print("execute query_sql ...", sql_execute)
    queries_data_sql(sql_execute)
    os.remove(file_csv)


def response_available_id():
    tuple_id = response_data_query("SELECT distinct(id) FROM `aci_inventory`")
    i = 0
    list_id_controller = list()
    while i < len(tuple_id):
        list_id_controller.append(tuple_id[i][0])
        i = i + 1
    return list_id_controller


def execute_function():
    # call inventory
    process_data_inventory(LIST_FILES[0], "aci_inventory")
    # call interfaces id
    for index in response_available_id():
        process_data_interfaces(LIST_FILES[1], str(index), "aci_interfaces")
