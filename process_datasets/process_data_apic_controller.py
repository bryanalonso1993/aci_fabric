#!/usr/env/bin/python3.6.9
from process_datasets.get_data_controller import *
from process_datasets.backend_data import *
import csv
import os


# process data inventory
def process_data_inventory(file_csv, table):
    data_rows = get_data_inventory()
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' " \
                  "(adSt, address, annotation, apicType, childAction, delayedHeartbeat, dn, extMngdBy, fabricSt, id," \
                  " lastStateModTs, lcOwn, modTs, model, monPolDn, name, nameAlias, nodeType, role, serial, status," \
                  " uid, vendor, version)".format(file_csv, table)
    queries_data_sql(sql_execute)


def process_data_partitions_controller(file_csv, table):
    data_rows = get_data_partitions_controller()
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' " \
                  "(`available`, `blocks`, `capUtilized`, `childAction`, `device`, `dn`, `failReason`, " \
                  "`fileSystem`, `firmwareVersion`, `lcOwn`, `mediaWearout`, `modTs`, `model`, `monPolDn`, `mount`," \
                  " `name`, `nameAlias`, `operSt`, `serial`, `status`, `used`)".format(file_csv, table)
    queries_data_sql(sql_execute)


# process interfaces all nods
def process_data_interfaces(file_csv, id_controller, table):
    data_rows = get_data_interface(id_controller)
    for index in data_rows:
        index.append(id_controller)
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' " \
                  " (`adminSt`, `autoNeg`, `brkoutMap`, `bw`, `childAction`, `delay`, `descr`, `dn`," \
                  " `dot1qEtherType`, `ethpmCfgFailedBmp`,`ethpmCfgFailedTs`, `ethpmCfgState`, `fcotChannelNumber`," \
                  " `fecMode`, `id`, `inhBw`, `isReflectiveRelayCfgSupported`, `layer`, `lcOwn`, `linkDebounce`," \
                  " `linkLog`, `mdix`, `medium`, `modTs`, `mode`, `monPolDn`, `mtu`, `name`, `pathSDescr`, `portT`," \
                  " `prioFlowCtrl`, `reflectiveRelayEn`, `routerMac`, `snmpTrapSt`, `spanMode`, `speed`, `status`," \
                  " `switchingSt`,`trunkLog`, `usage`, `idParent` )".format(file_csv, table)
    queries_data_sql(sql_execute)


# view status interfaces ...
def process_data_status_interfaces(file_csv, id_controller, table):
    data_rows = get_status_interfaces(id_controller)
    for index in data_rows:
        index.append(id_controller)
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' " \
                  " (`id`, `accessVlan`, `allowedVlans`, `backplaneMac`, `bundleBupId`, `bundleIndex`, `cfgAccessVlan`," \
                  " `cfgNativeVlan`, `childAction`, `currErrIndex`, `diags`, `encap`, `errDisTimerRunning`, " \
                  " `errVlanStatusHt`, `errVlans`, `hwBdId`, `hwResourceId`, `intfT`, `iod`, `lastErrors`, " \
                  " `lastLinkStChg`, `media`, `modTs`,`monPolDn`,`nativeVlan`, `numOfSI`,`operBitset`, `operDceMode`," \
                  " `operDuplex`, `operEEERxWkTime`, `operEEEState`, `operEEETxWkTime`, `operErrDisQual`," \
                  " `operFecMode`, `operFlowCtrl`, `operMdix`, `operMode`, `operModeDetail`,`operPhyEnSt`," \
                  " `operRouterMac`, `operSpeed`, `operSt`, `operStQual`,`operStQualCode`, `operVlans`,`osSum`, " \
                  " `portCfgWaitFlags`, `primaryVlan`, `resetCtr`, `rn`, `siList`, `status`, `txT`, `usage`," \
                  " `userCfgdFlags`, `vdcId`, `idParent`)".format(file_csv, table)
    queries_data_sql(sql_execute)


# search id in aci_inventory
def response_available_id():
    tuple_id = response_data_query("SELECT distinct(id) FROM `aci_inventory`")
    i = 0
    list_id_controller = list()
    while i < len(tuple_id):
        list_id_controller.append(tuple_id[i][0])
        i = i + 1
    return list_id_controller


# process alarms ACI
def process_data_alarms(file_csv, table, method):
    data_rows = get_alarms_aci(method)
    with open(file_csv, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='|')
        for row in data_rows:
            spam_writer.writerow(row)
    sql_execute = "LOAD DATA INFILE \'{}\' INTO TABLE {} FIELDS TERMINATED BY '|' LINES TERMINATED BY \'\\n\' (" \
                  "`cause`, `childAction`, `code`, `count`, `descr`, `dn`, `domain`, `nonAcked`, `nonDelegated`," \
                  " `nonDelegatedAndNonAcked`, `rule`, `severity`, `status`, `subject`, `type`)".format(file_csv, table)
    queries_data_sql(sql_execute)


# create files csv
def create_files_csv(*args):
    for index in args:
        if not os.path.isfile(index):
            os.mknod(index)
        os.chown(index, UID_MYSQL, GUID_MYSQL)


# remove files csv
def remove_files_csv(*args):
    for index in args:
        os.remove(index)


def execute_function():
    # create files
    create_files_csv(*LIST_FILES)
    # call inventory
    process_data_inventory(LIST_FILES[0], "aci_inventory")
    # call interfaces ids
    # id_available = response_available_id()
    id_available = [101, 102, 201]
    for index in id_available:
        process_data_interfaces(LIST_FILES[1], str(index), "aci_interfaces")
        process_data_status_interfaces(LIST_FILES[3], str(index), "aci_status_interfaces")
    process_data_alarms(LIST_FILES[2], "aci_alarms_topology", "class/topology/pod-1/faultSummary.json?query-target-filter=and(not(wcard(faultSummary.dn,%22__ui_%22)),and())&order-by=faultSummary.severity|desc")
    process_data_alarms(LIST_FILES[2], "aci_alarms_topology", "class/faultSummary.json?query-target-filter=and(not(wcard(faultSummary.dn,%22__ui_%22)),and())&order-by=faultSummary.severity|desc")
    process_data_partitions_controller(LIST_FILES[4], "aci_partitions_controller")
    remove_files_csv(*LIST_FILES)
