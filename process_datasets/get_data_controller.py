#!/usr/env/bin/python3.6.9
from credentials.credentials import USERNAME, PASSWORD, IP_CONTROLLER
from main_apic import *

# ===============================================================
#
#
#
#
#
# ================================================================

# constant
APIC_OBJECT = ApiRestAci(IP_CONTROLLER, USERNAME, PASSWORD)


def get_data_inventory():
    list_response = APIC_OBJECT.get_data_aci("mo/topology/pod-1.json?query-target=children&target-subtree-class=fabricNode&query-target-filter=and(not(wcard(fabricNode.dn,%22__ui_%22)),and(ne(fabricNode.role,\"controller\")))")
    result_list = list()
    for index in list_response:
        result_list.append([
            index['fabricNode']['attributes']['adSt'],
            index['fabricNode']['attributes']['address'],
            index['fabricNode']['attributes']['annotation'],
            index['fabricNode']['attributes']['apicType'],
            index['fabricNode']['attributes']['childAction'],
            index['fabricNode']['attributes']['delayedHeartbeat'],
            index['fabricNode']['attributes']['dn'],
            index['fabricNode']['attributes']['extMngdBy'],
            index['fabricNode']['attributes']['fabricSt'],
            index['fabricNode']['attributes']['id'],
            index['fabricNode']['attributes']['lastStateModTs'],
            index['fabricNode']['attributes']['lcOwn'],
            index['fabricNode']['attributes']['modTs'],
            index['fabricNode']['attributes']['model'],
            index['fabricNode']['attributes']['monPolDn'],
            index['fabricNode']['attributes']['name'],
            index['fabricNode']['attributes']['nameAlias'],
            index['fabricNode']['attributes']['nodeType'],
            index['fabricNode']['attributes']['role'],
            index['fabricNode']['attributes']['serial'],
            index['fabricNode']['attributes']['status'],
            index['fabricNode']['attributes']['uid'],
            index['fabricNode']['attributes']['vendor'],
            index['fabricNode']['attributes']['version']
        ])
    return result_list


def get_data_interface(id_node):
    list_response = APIC_OBJECT.get_data_aci("class/topology/pod-1/node-" + id_node + "/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf&order-by=l1PhysIf.monPolDn|asc&page=0&page-size=100")
    result_list = list()
    for index in list_response:
        result_list.append([
            index['l1PhysIf']['attributes']['adminSt'],
            index['l1PhysIf']['attributes']['autoNeg'],
            index['l1PhysIf']['attributes']['brkoutMap'],
            index['l1PhysIf']['attributes']['bw'],
            index['l1PhysIf']['attributes']['childAction'],
            index['l1PhysIf']['attributes']['delay'],
            index['l1PhysIf']['attributes']['descr'],
            index['l1PhysIf']['attributes']['dn'],
            index['l1PhysIf']['attributes']['dot1qEtherType'],
            index['l1PhysIf']['attributes']['ethpmCfgFailedBmp'],
            index['l1PhysIf']['attributes']['ethpmCfgFailedTs'],
            index['l1PhysIf']['attributes']['ethpmCfgState'],
            index['l1PhysIf']['attributes']['fcotChannelNumber'],
            index['l1PhysIf']['attributes']['fecMode'],
            index['l1PhysIf']['attributes']['id'],
            index['l1PhysIf']['attributes']['inhBw'],
            index['l1PhysIf']['attributes']['isReflectiveRelayCfgSupported'],
            index['l1PhysIf']['attributes']['layer'],
            index['l1PhysIf']['attributes']['lcOwn'],
            index['l1PhysIf']['attributes']['linkDebounce'],
            index['l1PhysIf']['attributes']['linkLog'],
            index['l1PhysIf']['attributes']['mdix'],
            index['l1PhysIf']['attributes']['medium'],
            index['l1PhysIf']['attributes']['modTs'],
            index['l1PhysIf']['attributes']['mode'],
            index['l1PhysIf']['attributes']['monPolDn'],
            index['l1PhysIf']['attributes']['mtu'],
            index['l1PhysIf']['attributes']['name'],
            index['l1PhysIf']['attributes']['pathSDescr'],
            index['l1PhysIf']['attributes']['portT'],
            index['l1PhysIf']['attributes']['prioFlowCtrl'],
            index['l1PhysIf']['attributes']['reflectiveRelayEn'],
            index['l1PhysIf']['attributes']['routerMac'],
            index['l1PhysIf']['attributes']['snmpTrapSt'],
            index['l1PhysIf']['attributes']['spanMode'],
            index['l1PhysIf']['attributes']['speed'],
            index['l1PhysIf']['attributes']['status'],
            index['l1PhysIf']['attributes']['switchingSt'],
            index['l1PhysIf']['attributes']['trunkLog'],
            index['l1PhysIf']['attributes']['usage']
        ])
    return result_list


def get_alarms_aci():
    # https://sandboxapicdc.cisco.com/api/node/class/topology/pod-1/faultSummary.json?query-target-filter=and(not(wcard(faultSummary.dn,%22__ui_%22)),and())&order-by=faultSummary.severity|desc&page=0&page-size=15
    list_response = APIC_OBJECT.get_data_aci("class/topology/pod-1/faultSummary.json?query-target-filter=and(not(wcard(faultSummary.dn,%22__ui_%22)),and())&order-by=faultSummary.severity|desc&page=0&page-size=15")
    result_list = list()
    for index in list_response:
        result_list.append([
            index['faultSummary']['attributes']['cause'],
            index['faultSummary']['attributes']['childAction'],
            index['faultSummary']['attributes']['code'],
            index['faultSummary']['attributes']['count'],
            index['faultSummary']['attributes']['descr'],
            index['faultSummary']['attributes']['dn'],
            index['faultSummary']['attributes']['domain'],
            index['faultSummary']['attributes']['nonAcked'],
            index['faultSummary']['attributes']['nonDelegated'],
            index['faultSummary']['attributes']['nonDelegatedAndNonAcked'],
            index['faultSummary']['attributes']['rule'],
            index['faultSummary']['attributes']['severity'],
            index['faultSummary']['attributes']['status'],
            index['faultSummary']['attributes']['subject'],
            index['faultSummary']['attributes']['type']
        ])
    return result_list
