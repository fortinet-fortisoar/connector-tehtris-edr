# License details
""" Copyright start
  MIT License
  Copyright (c) 2025 Fortinet Inc
  Copyright end """

# Imports
import time
from connectors.core.connector import ConnectorError, get_logger
import json, requests, base64

# Initialize logger
logger = get_logger('tehtris-edr')


# Common function to make external API calls.
def make_api_call(method="GET", endpoint="", config=None, params=None, headers=None, data=None, json_data=None,
                  verify_ssl=False):
    try:
        default_headers = {
            "Authorization": "Basic " + base64.b64encode(('Basic:' + config['password']).encode()).decode(),
            'Content-Type': 'application/json'
        }

        if headers:
            default_headers.update(headers)
        logger.debug("endpoint: " + str(endpoint))
        logger.debug("params: " + str(params))
        logger.debug("method: " + str(method))
        logger.debug("data: " + str(data))
        logger.debug("json_data: " + str(json_data))
        other_params = {}
        endpoint = config.get("server_url") + endpoint
        response = requests.request(method=method, url=endpoint, headers=default_headers, data=data, json=json_data,
                                    params=params, verify=verify_ssl, **other_params)
        if response.ok:
            if response.content:
                response = response.json()
            else:
                response = {"result": "No Data Returned", "status": "success"}
            return response
        else:
            logger.error("Error: {0}".format(response.json()))
            raise ConnectorError('{0}:{1}'.format(response.status_code, response.text))
    except requests.exceptions.SSLError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except requests.exceptions.ConnectionError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))



def get_epoch(date_time):
    try:
        if 'T' in date_time:
            pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
            date_time = int(time.mktime(time.strptime(date_time, pattern)))
            return date_time
        else:
            return date_time
    except Exception as Err:
        logger.error('get_epoch: Exception occurred [{0}]'.format(str(Err)))
        raise ConnectorError('get_epoch: Exception occurred [{0}]'.format(str(Err)))

# Operation definition

def fetch_events(config, params):
    query_params = {
        'fromDate': get_epoch(params.get('fromDate'))
    }
    if params.get('countOnly'):
        query_params['countOnly'] = str(params.get('countOnly')).lower()
    if params.get('byTag'):
        query_params['byTag'] = str(params.get('byTag')).lower()
    if params.get('toDate'):
        query_params['toDate'] = get_epoch(params.get('toDate'))
    if params.get('eventId'):
        query_params['eventId'] = params.get('eventId')
    if params.get('limit'):
        query_params['limit'] = params.get('limit')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')
    if params.get('filterID'):
        query_params['filterID'] = params.get('filterID')
    if params.get('createdOrModified'):
        query_params['createdOrModified'] = params.get('createdOrModified')

    endpoint = '/api/xdr/v1/event'
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def list_folders_and_filters(config, params):
    query_params = {}
    if params.get('name'):
        query_params['name'] = params.get('name')
    if params.get('module'):
        query_params['module'] = params.get('module')
    if params.get('oldFilterId'):
        query_params['oldFilterId'] = params.get('oldFilterId')
    if params.get('filtersOnly'):
        query_params['filtersOnly'] = str(params.get('filtersOnly')).lower()
    if params.get('presetFilters'):
        query_params['presetFilters'] = str(params.get('presetFilters')).lower()

    endpoint = '/api/xdr/v2/filter'
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_filter_by_id(config, params):
    query_params = {}
    if params.get('withHistory'):
        query_params['withHistory'] = str(params.get('withHistory')).lower()

    endpoint = '/api/xdr/v2/filter/filter/' + params.get('filterId')
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def create_filter(config, params):
    json_data = {
        'name': params.get('name'),
        'description': params.get('description'),
        'module': params.get('module')
    }
    json_data['filterQuery'] = {}
    json_data['filterQuery']['module'] = "Endpoint_Active"
    #json_data['filterQuery']['offset'] = 0
    #json_data['filterQuery']['limit'] = 25
    json_data['filterQuery']['timeOrder'] = 'DESC'
    json_data['filterQuery']['columns'] = {}
    json_data['filterQuery']['columns']['lvl'] = {}
    json_data['filterQuery']['columns']['lvl']['searchValue'] = str(params.get('lvlmin')) + "~" + str(
        params.get('lvlmax'))

    endpoint = '/api/xdr/v2/filter/filter'
    return make_api_call(config=config, json_data=json_data, endpoint=endpoint, method="POST")


def update_filter(config, params):
    json_data = {}
    if params.get('name'):
        json_data['name'] = params.get('name')
    if params.get('description'):
        json_data['description'] = params.get('description')
    if params.get('module'):
        json_data['module'] = params.get('module')
    if params.get('lvlmin') and params.get('lvlmax'):
        json_data['filterQuery'] = {}
        json_data['filterQuery']['module'] = "Endpoint_Active"
        #json_data['filterQuery']['offset'] = 0
        #json_data['filterQuery']['limit'] = 25
        json_data['filterQuery']['timeOrder'] = 'DESC'
        json_data['filterQuery']['columns'] = {}
        json_data['filterQuery']['columns']['lvl'] = {}
        json_data['filterQuery']['columns']['lvl']['searchValue'] = str(params.get('lvlmin')) + "~" + str(
            params.get('lvlmax'))

    endpoint = '/api/xdr/v2/filter/filter/' + params.get('filterId')
    return make_api_call(config=config, json_data=json_data, endpoint=endpoint, method="PUT")


def delete_filter(config, params):
    endpoint = '/api/xdr/v2/filter/filter/' + params.get('filterId')
    return make_api_call(config=config, endpoint=endpoint, method="DELETE")


def get_all_endpoints(config, params):
    query_params = {}
    if params.get('tags'):
        query_params['tags'] = params.get('tags')
    if params.get('versions'):
        query_params['versions'] = params.get('versions')
    if params.get('configUuid'):
        query_params['configUuid'] = params.get('configUuid')
    if params.get('uuids'):
        query_params['uuids'] = params.get('uuids')
    if params.get('applianceIds'):
        query_params['applianceIds'] = params.get('applianceIds')
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')
    if params.get('hostnameRegex'):
        query_params['hostnameRegex'] = params.get('hostnameRegex')
    if params.get('domain'):
        query_params['domain'] = params.get('domain')
    if params.get('domainRegex'):
        query_params['domainRegex'] = params.get('domainRegex')
    if params.get('network'):
        query_params['network'] = params.get('network')
    if params.get('firstSeenFrom'):
        query_params['firstSeenFrom'] = params.get('firstSeenFrom')
    if params.get('firstSeenTo'):
        query_params['firstSeenTo'] = params.get('firstSeenTo')
    if params.get('lastSeenFrom'):
        query_params['lastSeenFrom'] = params.get('lastSeenFrom')
    if params.get('lastSeenTo'):
        query_params['lastSeenTo'] = params.get('lastSeenTo')
    if params.get('os'):
        query_params['os'] = params.get('os')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    func_headers_dict = {}
    endpoint = "/api/edr/v2/inventory"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, headers=func_headers_dict, method="GET")


def set_event_status(config, params):
    json_data = {
        'status': params.get('status'),
        'oldStatus': params.get('oldStatus')
    }
    endpoint = '/api/xdr/v1/event/status/' + str(params.get('id'))
    return make_api_call(config=config, json_data=json_data, endpoint=endpoint, method="PUT")


def get_isolation_status(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/isolation"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def send_isolation_action(config, params):
    query_params = {
        'isolationAction': params.get('isolationAction').lower()
    }
    if params.get('power'):
        query_params['power'] = params.get('power').lower()
    if params.get('persist'):
        query_params['persist'] = str(params.get('persist')).lower()

    json_data = {}
    if len(params.get('toWhitelist')) > 0:
        json_data['toWhitelist'] = params.get('toWhitelist')

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/isolation"
    return make_api_call(config=config, json_data=json_data, params=query_params, endpoint=endpoint, method="POST")


def get_all_global_policies(config, params):
    endpoint = '/api/edr/v2/policies/global/list'
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def create_new_global_policies(config, params):
    json_data = params.get('policyData')
    endpoint = '/api/edr/v2/policies/global'
    return make_api_call(config=config, json_data=json_data, endpoint=endpoint, method=params.get('position'))


def get_tags(config, params):
    endpoint = "/api/edr/v2/inventory/tags"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def update_endpoints_tags(config, params):
    json_data = {}
    if len(params.get('edrUuidList')) > 0:
        json_data['edrUuidList'] = params.get('edrUuidList')
    if params.get('tags'):
        json_data['tags'] = params.get('tags')

    endpoint = "/api/edr/v2/inventory/tags"
    return make_api_call(config=config, json_data=json_data, endpoint=endpoint, method="PUT")


def get_accesslogs(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')
    if params.get('logonEventTimeFrom'):
        query_params['logonEventTimeFrom'] = params.get('logonEventTimeFrom')
    if params.get('logonEventTimeTo'):
        query_params['logonEventTimeTo'] = params.get('logonEventTimeTo')
    if params.get('admin'):
        query_params['admin'] = str(params.get('admin')).lower()
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/accesslogs"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_users_connected(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/users"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_network_infos(config, params):
    query_params = {}
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/network"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_history_of_processes(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if len(params.get('pids')) > 0:
        query_params['pids'] = params.get('pids')
    if len(params.get('ppids')) > 0:
        query_params['ppids'] = params.get('ppids')
    if len(params.get('logonIds')) > 0:
        query_params['logonIds'] = params.get('logonIds')
    if params.get('userIdentifier'):
        query_params['userIdentifier'] = params.get('userIdentifier')
    if params.get('username'):
        query_params['username'] = params.get('username')
    if params.get('domainName'):
        query_params['domainName'] = params.get('domainName')
    if params.get('localTime'):
        query_params['localTime'] = str(params.get('localTime')).lower()
    if params.get('timeFilter'):
        query_params['timeFilter'] = params.get('timeFilter').lower()
    if params.get('timeFrom'):
        query_params['timeFrom'] = params.get('timeFrom')
    if params.get('timeTo'):
        query_params['timeTo'] = params.get('timeTo')
    if params.get('sha256'):
        query_params['sha256'] = params.get('sha256')
    if params.get('sha1'):
        query_params['sha1'] = params.get('sha1')
    if params.get('md5'):
        query_params['md5'] = params.get('md5')
    if params.get('path'):
        query_params['path'] = params.get('path')
    if params.get('cmdline'):
        query_params['cmdline'] = params.get('cmdline')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/processes"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_process_tree(config, params):
    query_params = {
        'pid': params.get('pid'),
        'createTime': params.get('createTime'),
        'nbParents': params.get('nbParents'),
        'limit': params.get('limit')
    }
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/processes/tree"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_persistence_entries(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('localTime'):
        query_params['localTime'] = str(params.get('localTime')).lower()
    if params.get('t'):
        query_params['t'] = params.get('t')
    if params.get('persistence_path'):
        query_params['persistence_path'] = params.get('persistence_path')
    if params.get('persistence_type'):
        query_params['persistence_type'] = params.get('persistence_type')
    if params.get('name'):
        query_params['name'] = params.get('name')
    if params.get('sha256'):
        query_params['sha256'] = params.get('sha256')
    if params.get('sha1'):
        query_params['sha1'] = params.get('sha1')
    if params.get('md5'):
        query_params['md5'] = params.get('md5')
    if params.get('path'):
        query_params['path'] = params.get('path')
    if params.get('cmdline'):
        query_params['cmdline'] = params.get('cmdline')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/autostart"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_usb_history(config, params):
    query_params = {}
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/usb"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_browser_security(config, params):
    query_params = {}
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')

    endpoint = "/api/edr/v2/data/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/browsers"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_software_list(config, params):
    query_params = {}
    if params.get('persist'):
        query_params['persist'] = str(params.get('persist')).lower()

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/software"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def fetch_info_about_endpoint(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/systemInfo"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def get_last_offline_forensic_report(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/tof/lastReport"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def get_offline_forensic_status(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/tof"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def start_offline_forensic(config, params):
    query_params = {}
    if params.get('persist'):
        query_params['persist'] = str(params.get('persist')).lower()

    json_data = {}
    if params.get('processes'):
        json_data['processes'] = params.get('processes')
    if params.get('startup'):
        json_data['startup'] = params.get('startup')
    if params.get('disk'):
        json_data['disk'] = params.get('disk')
    if len(params.get('diskPaths')) > 0:
        json_data['diskPaths'] = params.get('diskPaths')
    if len(params.get('extensions')) > 0:
        json_data['extensions'] = params.get('extensions')
    if params.get('privacy'):
        json_data['privacy'] = params.get('privacy')
    if params.get('advanced'):
        json_data['advanced'] = params.get('advanced')
    if params.get('commands'):
        json_data['commands'] = params.get('commands')
    if params.get('yara'):
        json_data['yara'] = params.get('yara')
    if params.get('forensic'):
        json_data['forensic'] = params.get('forensic')

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/tof"
    return make_api_call(config=config, params=query_params, json_data=json_data, endpoint=endpoint, method="POST")


def stop_offline_forensic(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/tof"
    return make_api_call(config=config, endpoint=endpoint, method="DELETE")


def search_binaries(config, params):
    query_params = {}
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')
    if params.get('hostnameRegex'):
        query_params['hostnameRegex'] = params.get('hostnameRegex')
    if params.get('sha256'):
        query_params['sha256'] = params.get('sha256')
    if params.get('sha1'):
        query_params['sha1'] = params.get('sha1')
    if params.get('md5'):
        query_params['md5'] = params.get('md5')
    if params.get('path'):
        query_params['path'] = params.get('path')
    if params.get('pathRegex'):
        query_params['pathRegex'] = params.get('pathRegex')
    if params.get('signatureCn'):
        query_params['signatureCn'] = params.get('signatureCn')
    if params.get('signatureCnRegex'):
        query_params['signatureCnRegex'] = params.get('signatureCnRegex')
    if params.get('lastSeenFrom'):
        query_params['lastSeenFrom'] = params.get('lastSeenFrom')
    if params.get('lastSeenTo'):
        query_params['lastSeenTo'] = params.get('lastSeenTo')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/search/" + str(params.get("applianceId")) + "/binaries"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def search_user_accesslogs(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('username'):
        query_params['username'] = params.get('username')
    if params.get('usernameRegex'):
        query_params['usernameRegex'] = params.get('usernameRegex')
    if params.get('logonEventTimeFrom'):
        query_params['logonEventTimeFrom'] = params.get('logonEventTimeFrom')
    if params.get('logonEventTimeTo'):
        query_params['logonEventTimeTo'] = params.get('logonEventTimeTo')
    if params.get('logoffEventTimeFrom'):
        query_params['logoffEventTimeFrom'] = params.get('logoffEventTimeFrom')
    if params.get('logoffEventTimeTo'):
        query_params['logoffEventTimeTo'] = params.get('logoffEventTimeTo')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/search/" + str(params.get("applianceId")) + "/accesslogs"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def search_persistent_entries_category(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')
    if params.get('hostnameRegex'):
        query_params['hostnameRegex'] = params.get('hostnameRegex')
    if params.get('pathRegex'):
        query_params['pathRegex'] = params.get('pathRegex')
    if params.get('cmdlineRegex'):
        query_params['cmdlineRegex'] = params.get('cmdlineRegex')
    if params.get('signatureCn'):
        query_params['signatureCn'] = params.get('signatureCn')
    if params.get('signatureCnRegex'):
        query_params['signatureCnRegex'] = params.get('signatureCnRegex')
    if params.get('persistencePath'):
        query_params['persistencePath'] = params.get('persistencePath')
    if params.get('persistencePathRegex'):
        query_params['persistencePathRegex'] = params.get('persistencePathRegex')
    if params.get('persistenceType'):
        query_params['persistenceType'] = params.get('persistenceType')
    if params.get('persistenceTypeRegex'):
        query_params['persistenceTypeRegex'] = params.get('persistenceTypeRegex')
    if params.get('name'):
        query_params['name'] = params.get('name')
    if params.get('nameRegex'):
        query_params['nameRegex'] = params.get('nameRegex')
    if params.get('sha256'):
        query_params['sha256'] = params.get('sha256')
    if params.get('sha1'):
        query_params['sha1'] = params.get('sha1')
    if params.get('md5'):
        query_params['md5'] = params.get('md5')
    if params.get('path'):
        query_params['path'] = params.get('path')
    if params.get('cmdline'):
        query_params['cmdline'] = params.get('cmdline')
    if params.get('createdFrom'):
        query_params['createdFrom'] = params.get('createdFrom')
    if params.get('createdTo'):
        query_params['createdTo'] = params.get('createdTo')
    if params.get('deletedFrom'):
        query_params['deletedFrom'] = params.get('deletedFrom')
    if params.get('deletedTo'):
        query_params['deletedTo'] = params.get('deletedTo')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/search/" + str(params.get("applianceId")) + "/autostart/" + str(
        params.get("category").lower())
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def search_persistent_entries(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('hostname'):
        query_params['hostname'] = params.get('hostname')
    if params.get('hostnameRegex'):
        query_params['hostnameRegex'] = params.get('hostnameRegex')
    if params.get('pathRegex'):
        query_params['pathRegex'] = params.get('pathRegex')
    if params.get('cmdlineRegex'):
        query_params['cmdlineRegex'] = params.get('cmdlineRegex')
    if params.get('signatureCn'):
        query_params['signatureCn'] = params.get('signatureCn')
    if params.get('signatureCnRegex'):
        query_params['signatureCnRegex'] = params.get('signatureCnRegex')
    if params.get('persistencePath'):
        query_params['persistencePath'] = params.get('persistencePath')
    if params.get('persistencePathRegex'):
        query_params['persistencePathRegex'] = params.get('persistencePathRegex')
    if params.get('persistenceType'):
        query_params['persistenceType'] = params.get('persistenceType')
    if params.get('persistenceTypeRegex'):
        query_params['persistenceTypeRegex'] = params.get('persistenceTypeRegex')
    if params.get('name'):
        query_params['name'] = params.get('name')
    if params.get('nameRegex'):
        query_params['nameRegex'] = params.get('nameRegex')
    if params.get('sha256'):
        query_params['sha256'] = params.get('sha256')
    if params.get('sha1'):
        query_params['sha1'] = params.get('sha1')
    if params.get('md5'):
        query_params['md5'] = params.get('md5')
    if params.get('path'):
        query_params['path'] = params.get('path')
    if params.get('cmdline'):
        query_params['cmdline'] = params.get('cmdline')
    if params.get('createdFrom'):
        query_params['createdFrom'] = params.get('createdFrom')
    if params.get('createdTo'):
        query_params['createdTo'] = params.get('createdTo')
    if params.get('deletedFrom'):
        query_params['deletedFrom'] = params.get('deletedFrom')
    if params.get('deletedTo'):
        query_params['deletedTo'] = params.get('deletedTo')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/search/" + str(params.get("applianceId")) + "/autostart"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def get_disk_scan_status(config, params):
    query_params = {}
    if params.get('scanId'):
        query_params['scanId'] = params.get('scanId')

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/scan-disk"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def launch_disk_scan(config, params):
    query_params = {}
    if params.get('persist'):
        query_params['persist'] = str(params.get('persist')).lower()

    json_data = {}
    if params.get('scanADS'):
        json_data['scanADS'] = params.get('scanADS')
    if params.get('scanWhitelistPaths'):
        json_data['scanWhitelistPaths'] = params.get('scanWhitelistPaths')
    if params.get('startFolders'):
        json_data['startFolders'] = params.get('startFolders')

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/scan-disk"
    return make_api_call(config=config, params=query_params, json_data=json_data, endpoint=endpoint, method="POST")


def get_current_scan_status(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/scan-disk/current"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def stop_current_scan(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get("edrUuid") + "/scan-disk/current"
    return make_api_call(config=config, endpoint=endpoint, method="DELETE")


def list_quarantine_files(config, params):
    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get(
        "edrUuid") + "/remediation/quarantine"
    return make_api_call(config=config, endpoint=endpoint, method="GET")


def quarantine_file(config, params):
    query_params = {
        'path': params.get('path')
    }
    if params.get('persist'):
        query_params['persist'] = str(params.get('persist')).lower()
    if params.get('notification'):
        query_params['notification'] = params.get('notification')

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get(
        "edrUuid") + "/remediation/quarantine"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="POST")


def restore_file_from_quarantine(config, params):
    query_params = {
        'path': params.get('path')
    }
    if params.get('persist'):
        query_params['persist'] = str(params.get('persist')).lower()

    endpoint = "/api/edr/v2/live/" + str(params.get("applianceId")) + "/" + params.get(
        "edrUuid") + "/remediation/quarantine"
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="PATCH")


def get_unmanaged_hosts(config, params):
    query_params = {
        'limit': params.get('limit')
    }
    if params.get('lastSeenFrom'):
        query_params['lastSeenFrom'] = params.get('lastSeenFrom')
    if params.get('lastSeenTo'):
        query_params['lastSeenTo'] = params.get('lastSeenTo')
    if params.get('offset'):
        query_params['offset'] = params.get('offset')

    endpoint = "/api/edr/v2/discovery/" + str(params.get("applianceId"))
    return make_api_call(config=config, params=query_params, endpoint=endpoint, method="GET")


def execute_an_api_call(config, params):
    endpoint = params.get("endpoint")
    http_method = params.get("method")
    query_params = params.get("query_params") if params.get("query_params") else {}
    payload = params.get("payload") if params.get("payload") else {}
    logger.debug("Payload: {0}".format(payload))
    response = make_api_call(config=config, endpoint=endpoint, method=http_method, params=query_params,
                             json_data=payload)
    return response


operations_map = {
    'fetch_events': fetch_events,
    'get_all_endpoints': get_all_endpoints,
    'set_event_status': set_event_status,
    'list_folders_and_filters': list_folders_and_filters,
    'get_filter_by_id': get_filter_by_id,
    'create_filter': create_filter,
    'update_filter': update_filter,
    'delete_filter': delete_filter,
    'get_isolation_status': get_isolation_status,
    'send_isolation_action': send_isolation_action,
    'get_all_global_policies': get_all_global_policies,
    'create_new_global_policies': create_new_global_policies,
    'get_tags': get_tags,
    'update_endpoints_tags': update_endpoints_tags,
    'get_accesslogs': get_accesslogs,
    'get_users_connected': get_users_connected,
    'get_network_infos': get_network_infos,
    'get_history_of_processes': get_history_of_processes,
    'get_process_tree': get_process_tree,
    'get_persistence_entries': get_persistence_entries,
    'get_usb_history': get_usb_history,
    'get_browser_security': get_browser_security,
    'get_software_list': get_software_list,
    'fetch_info_about_endpoint': fetch_info_about_endpoint,
    'get_last_offline_forensic_report': get_last_offline_forensic_report,
    'get_offline_forensic_status': get_offline_forensic_status,
    'start_offline_forensic': start_offline_forensic,
    'stop_offline_forensic': stop_offline_forensic,
    'search_binaries': search_binaries,
    'search_user_accesslogs': search_user_accesslogs,
    'search_persistent_entries_category': search_persistent_entries_category,
    'search_persistent_entries': search_persistent_entries,
    'get_disk_scan_status': get_disk_scan_status,
    'launch_disk_scan': launch_disk_scan,
    'get_current_scan_status': get_current_scan_status,
    'stop_current_scan': stop_current_scan,
    'list_quarantine_files': list_quarantine_files,
    'quarantine_file': quarantine_file,
    'restore_file_from_quarantine': restore_file_from_quarantine,
    'get_unmanaged_hosts': get_unmanaged_hosts,
    'execute_an_api_call': execute_an_api_call
}
