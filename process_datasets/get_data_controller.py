#!/usr/env/bin/python3.6.9
from credentials.credentials import *
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


def get_alarms_aci(method):
    # https://sandboxapicdc.cisco.com/api/node/class/topology/pod-1/faultSummary.json?query-target-filter=and
    # (not(wcard(faultSummary.dn,%22__ui_%22)),and())&order-by=faultSummary.severity|desc&page=0&page-size=15
    #  https://sandboxapicdc.cisco.com/api/node/class/faultSummary.json?query-target-filter=
    #  and(not(wcard(faultSummary.dn,%22__ui_%22)),and())&order-by=faultSummary.severity|desc
    list_response = APIC_OBJECT.get_data_aci(method)
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


def get_data_interface(id_node):
    list_response = APIC_OBJECT.get_data_aci("class/topology/pod-1/node-"+id_node+"/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf&order-by=l1PhysIf.monPolDn|asc")
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


def get_status_interfaces(id_node):
    list_response = APIC_OBJECT.get_data_aci("class/topology/pod-1/node-"+id_node+"/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf&order-by=l1PhysIf.monPolDn|asc")
    result_list = list()
    for index in list_response:
        result_list.append([
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['accessVlan'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['allowedVlans'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['backplaneMac'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['bundleBupId'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['bundleIndex'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['cfgAccessVlan'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['cfgNativeVlan'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['childAction'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['currErrIndex'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['diags'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['encap'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['errDisTimerRunning'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['errVlanStatusHt'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['errVlans'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['hwBdId'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['hwResourceId'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['intfT'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['iod'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['lastErrors'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['lastLinkStChg'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['media'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['modTs'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['monPolDn'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['nativeVlan'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['numOfSI'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operBitset'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operDceMode'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operDuplex'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operEEERxWkTime'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operEEEState'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operEEETxWkTime'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operErrDisQual'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operFecMode'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operFlowCtrl'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operMdix'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operMode'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operModeDetail'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operPhyEnSt'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operRouterMac'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operSpeed'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operSt'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operStQual'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operStQualCode'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operVlans'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['osSum'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['portCfgWaitFlags'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['primaryVlan'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['resetCtr'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['rn'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['siList'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['status'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['txT'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['usage'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['userCfgdFlags'],
            index['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['vdcId']
        ])
    return result_list
