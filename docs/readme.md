## About the connector
TEHTRIS EDR (Endpoint Detection and Response) is designed to detect, analyze, and respond to security incidents on endpoints (such as computers, servers, and mobile devices) in real time.
<p>This document provides information about the TEHTRIS EDR Connector, which facilitates automated interactions, with a TEHTRIS EDR server using FortiSOAR&trade; playbooks. Add the TEHTRIS EDR Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with TEHTRIS EDR.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet SE

Contributor: ArnaudN

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 6.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-tehtris-edr`

## Prerequisites to configuring the connector
- You must have the URL of TEHTRIS EDR server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the TEHTRIS EDR server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>TEHTRIS EDR</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the TEHTRIS EDR server to connect and perform automated operations.<br>
<tr><td>Password<br></td><td>Specify the password to connect to the endpoint and perform automated operations<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 6.0.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Fetch Events<br></td><td>Fetch events from the TEHTRIS EDR based on the filter criteria that you have specified.<br></td><td>fetch_events <br/>Utilities<br></td></tr>
<tr><td>List Folders and Filters<br></td><td>Retrieve a list of all folders and all filters the user has access to (as owner, editor or viewer) from TEHTRIS EDR based on the filter criteria that you have specified.<br></td><td>list_folders_and_filters <br/>Utilities<br></td></tr>
<tr><td>Get Filter by ID<br></td><td>Retrieve a filter by its unique ID from the TEHTRIS EDR platform.<br></td><td>get_filter_by_id <br/>Utilities<br></td></tr>
<tr><td>Create Filter<br></td><td>Create a new filter in the TEHTRIS EDR platform based on specified parameters.<br></td><td>create_filter <br/>Utilities<br></td></tr>
<tr><td>Update Filter<br></td><td>Update an existing filter in the TEHTRIS EDR platform by modifying its parameters or attributes.<br></td><td>update_filter <br/>Utilities<br></td></tr>
<tr><td>Delete Filter<br></td><td>Delete an existing filter from the TEHTRIS EDR platform using its unique identifier.<br></td><td>delete_filter <br/>Utilities<br></td></tr>
<tr><td>Set an event status<br></td><td>Update the status of a specific event in the TEHTRIS EDR platform. The "Old Status" field can optionally be used to verify the current status before updating, or set to null to skip verification.<br></td><td>set_event_status <br/>Utilities<br></td></tr>
<tr><td>Get All Endpoints<br></td><td>Retrieve all endpoints managed by the TEHTRIS EDR platform, with optional filters such as tags, hostnames, domains, IP ranges, OS versions, and time-based parameters.<br></td><td>get_all_endpoints <br/>Utilities<br></td></tr>
<tr><td>Get Isolation Status<br></td><td>Retrieve the current network isolation status of a specific endpoint from the TEHTRIS EDR platform.<br></td><td>get_isolation_status <br/>Utilities<br></td></tr>
<tr><td>Send Isolation Action<br></td><td>Send a network isolation command to a specific endpoint through the TEHTRIS EDR platform. This allows enabling, disabling, or whitelisting isolation rules on managed endpoints.<br></td><td>send_isolation_action <br/>Utilities<br></td></tr>
<tr><td>Get All Global Policies<br></td><td>Retrieve all global policies from the TEHTRIS EDR platform.<br></td><td>get_all_global_policies <br/>Utilities<br></td></tr>
<tr><td>Create New Global Policies<br></td><td>Create or update global policies within the TEHTRIS EDR platform. This operation supports both upsert and downsert actions, depending on the selected method.<br></td><td>create_new_global_policies <br/>Utilities<br></td></tr>
<tr><td>Get Tags<br></td><td>Retrieve all tags from the TEHTRIS EDR platform.<br></td><td>get_tags <br/>Utilities<br></td></tr>
<tr><td>Update Endpoints Tags<br></td><td>Update or assign specific tags to one or multiple endpoints managed by the TEHTRIS EDR platform.<br></td><td>update_endpoints_tags <br/>Utilities<br></td></tr>
<tr><td>Get Access Logs<br></td><td>Create a cursor and fetch the first batch of access log data from the TEHTRIS EDR platform. Access logs are displayed from the most recent to the least recent by default.<br></td><td>get_accesslogs <br/>Utilities<br></td></tr>
<tr><td>Get Users Connected<br></td><td>Retrieve a list of users who have connected to a specified endpoint within the last 6 months using the TEHTRIS EDr platform.<br></td><td>get_users_connected <br/>Utilities<br></td></tr>
<tr><td>Get Network Information<br></td><td>Retrieve detailed network information for a specified endpoint using the TEHTRIS EDR platform.<br></td><td>get_network_infos <br/>Utilities<br></td></tr>
<tr><td>Get Processes History<br></td><td>Retrieve the historical list of processes executed on a specific endpoint within a defined time interval using the TEHTRIS EDR platform.<br></td><td>get_history_of_processes <br/>Utilities<br></td></tr>
<tr><td>Get Process Tree<br></td><td>Retrieve the hierarchical process tree for a given process on a specific endpoint using the TEHTRIS EDR platform.<br></td><td>get_process_tree <br/>Utilities<br></td></tr>
<tr><td>Get Persistence Entries<br></td><td>Retrieve persistence mechanisms (such as services, startup scripts, cron jobs, or configuration-based auto-start entries) detected on a specified Linux endpoint.<br></td><td>get_persistence_entries <br/>Utilities<br></td></tr>
<tr><td>Get USB History<br></td><td>Retrieve the history of USB device connections for a specified endpoint from TEHTRIS EDR platform.<br></td><td>get_usb_history <br/>Utilities<br></td></tr>
<tr><td>Get Browser Security<br></td><td>Retrieve detailed browser security information for a specified endpoint from TEHTRIS EDR platform.<br></td><td>get_browser_security <br/>Utilities<br></td></tr>
<tr><td>Get Software List<br></td><td>Retrieve a comprehensive list of software installed on a specified endpoint from TEHTRIS EDR platform.<br></td><td>get_software_list <br/>Utilities<br></td></tr>
<tr><td>Fetch Endpoint Details<br></td><td>Retrieve detailed system information about a specified endpoint, including hardware and user-related data from TEHTRIS EDR platform.<br></td><td>fetch_info_about_endpoint <br/>Utilities<br></td></tr>
<tr><td>Get Last Offline Forensic Report<br></td><td>Retrieve the most recent TEHTRIS Offline Forensic report generated for a specified endpoint from TEHTRIS EDR platform.<br></td><td>get_last_offline_forensic_report <br/>Utilities<br></td></tr>
<tr><td>Get Offline Forensic Status<br></td><td>Retrieve the current status of the TEHTRIS Offline Forensic module for a specified endpoint.<br></td><td>get_offline_forensic_status <br/>Utilities<br></td></tr>
<tr><td>Start Offline Forensic<br></td><td>Initiate a TEHTRIS Offline Forensic analysis on a specified endpoint.<br></td><td>start_offline_forensic <br/>Utilities<br></td></tr>
<tr><td>Stop Offline Forensic<br></td><td>Terminate an ongoing TEHTRIS Offline Forensic analysis on a specified endpoint.<br></td><td>stop_offline_forensic <br/>Utilities<br></td></tr>
<tr><td>Search Binaries<br></td><td>Search and retrieve information about binaries detected by TEHTRIS EDR across endpoints managed by the specified appliance.<br></td><td>search_binaries <br/>Utilities<br></td></tr>
<tr><td>Search User Access Logs<br></td><td>Retrieve and filter user access logs collected by TEHTRIS EDR for the specified appliance. Supports detailed filtering based on username, login/logout timestamps, and regex-based pattern matching.<br></td><td>search_user_accesslogs <br/>Utilities<br></td></tr>
<tr><td>Search Persistent Entries by Category<br></td><td>Search persistent entries on endpoints using filters across different persistence categories (Files, Keys, Services, or Tasks). Supports regex-based and substring filtering for multiple attributes.<br></td><td>search_persistent_entries_category <br/>Utilities<br></td></tr>
<tr><td>Search Persistent Entries<br></td><td>Search persistent entries across endpoints using flexible filters.<br></td><td>search_persistent_entries <br/>Utilities<br></td></tr>
<tr><td>Get Disk Scan Status<br></td><td>Retrieve the current status of a disk scan for a specified endpoint.<br></td><td>get_disk_scan_status <br/>Utilities<br></td></tr>
<tr><td>Launch Disk Scan<br></td><td>Initiate a disk scan on a specified endpoint to detect potential threats or anomalies.<br></td><td>launch_disk_scan <br/>Utilities<br></td></tr>
<tr><td>Get Current Scan Status<br></td><td>Retrieve the current scan status for a specific endpoint.<br></td><td>get_current_scan_status <br/>Utilities<br></td></tr>
<tr><td>Stop Current Scan<br></td><td>Terminate an active disk scan for a specified endpoint.<br></td><td>stop_current_scan <br/>Utilities<br></td></tr>
<tr><td>Get All Quarantine Files<br></td><td>Retrieve the complete list of quarantined files detected on a specific endpoint.<br></td><td>list_quarantine_files <br/>Utilities<br></td></tr>
<tr><td>Quarantine a File<br></td><td>Remotely quarantine a specific file on an endpoint.<br></td><td>quarantine_file <br/>Utilities<br></td></tr>
<tr><td>Restore File from Quarantine<br></td><td>Restore a previously quarantined file on a given endpoint.<br></td><td>restore_file_from_quarantine <br/>Utilities<br></td></tr>
<tr><td>Get Unmanaged Hosts<br></td><td>Retrieve a list of unmanaged hosts discovered on a specified appliance.<br></td><td>get_unmanaged_hosts <br/>Utilities<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>execute_an_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Fetch Events
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>From Date<br></td><td>Specify the timestamp (in seconds since EPOCH) to define the starting point for fetching events.<br>
</td></tr><tr><td>To Date<br></td><td>Specify the timestamp (in seconds since EPOCH) to define the end point for fetching events.<br>
</td></tr><tr><td>Event ID<br></td><td>Specify the unique event ID to fetch details for a specific event.<br>
</td></tr><tr><td>Count Only<br></td><td>Select whether to count alerts only instead of retrieving the full list of events.<br>
</td></tr><tr><td>By Tag<br></td><td>Select whether to count alerts by their associated tags when count Only is enabled.<br>
</td></tr><tr><td>Filter ID<br></td><td>Specify the filter ID to use for retrieving events. If none is provided, the first filter associated with the API key will be used.<br>
</td></tr><tr><td>Created or Modified<br></td><td>Select whether to fetch events based on their creation time or last modification time.<br>
</td></tr><tr><td>Offset<br></td><td>Specify the number of events to skip before starting to retrieve results, useful for pagination.<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of events to fetch, up to a limit of 1000.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: List Folders and Filters
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Name<br></td><td>Specify the name or partial name to filter and return only folders and filters that contain this value.<br>
</td></tr><tr><td>Module<br></td><td>Specify the module name to return only filters related to that specific module.<br>
</td></tr><tr><td>Old Filter ID<br></td><td>Specify the old filter ID to search for filters that were migrated from releases prior to version 10.1.<br>
</td></tr><tr><td>Filters Only<br></td><td>Select whether to return only filters, leaving the folder list empty.<br>
</td></tr><tr><td>Preset Filters<br></td><td>Select whether to include preset filters in addition to the user’s own filters.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Filter by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter ID<br></td><td>Specify the unique filter ID to retrieve the corresponding filter details.<br>
</td></tr><tr><td>With History<br></td><td>Select whether to retrieve the filter along with its historical versions and changes.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Name<br></td><td>Specify the name for the new filter. The name should clearly describe the purpose or scope of the filter.<br>
</td></tr><tr><td>Minimum Severity Level<br></td><td>Specify the minimum severity level that this filter should capture, where 0 represents the least severe and 9 the most severe.<br>
</td></tr><tr><td>Maximum Severity Level<br></td><td>Specify the maximum severity level that this filter should capture, where 0 represents the least severe and 9 the most severe.<br>
</td></tr><tr><td>Description<br></td><td>Specify the description for the filter.<br>
</td></tr><tr><td>Module<br></td><td>Specify the module to which this filter applies.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Update Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter ID<br></td><td>Specify the unique filter ID for the filter you want to update.<br>
</td></tr><tr><td>Name<br></td><td>Specify the updated name for the filter. The name should clearly represent the filter’s purpose.<br>
</td></tr><tr><td>Minimum Severity Level<br></td><td>Specify the minimum severity level that the filter should capture, where 0 is the least severe and 9 is the most severe.<br>
</td></tr><tr><td>Maximum Severity Level<br></td><td>Specify the maximum severity level that this filter should capture, where 0 represents the least severe and 9 the most severe.<br>
</td></tr><tr><td>Description<br></td><td>Specify the updated description for the filter to provide context about its purpose or criteria.<br>
</td></tr><tr><td>Tag<br></td><td>Specify the tag associated with the filter to update.<br>
</td></tr><tr><td>Device Name<br></td><td>Specify the name of the device associated with this filter to update.<br>
</td></tr><tr><td>Path<br></td><td>Specify the relevant file path if applicable to update the filter.<br>
</td></tr><tr><td>CMD Line<br></td><td>Specify the command line value associated with this filter to update.<br>
</td></tr><tr><td>SHA256<br></td><td>Specify the SHA-256 hash that may be tied to the filter for identification or verification purposes.<br>
</td></tr><tr><td>Event Name<br></td><td>Specify the event name related to the filter to update.<br>
</td></tr><tr><td>EG Knowledge Base ID<br></td><td>Specify the EG knowledge base ID associated with the filter to update.<br>
</td></tr><tr><td>Module<br></td><td>Select the applicable module for the filter. By default, it is set to "Endpoint".<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Delete Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter ID<br></td><td>Specify the filter ID corresponding to the filter that should be removed from the system.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Set an event status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Event ID<br></td><td>Specify the event ID corresponding to the event you want to update in the Tehtris EDR platform.<br>
</td></tr><tr><td>New Status<br></td><td>Select the new status to assign to the event. Possible values include 'checked', 'false positive', 'incident', 'on going', 'pending', and 'resolved'.<br>
</td></tr><tr><td>Old Status<br></td><td>Specify the current status of the event to verify before updating. Use null to bypass the old status check.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Endpoints
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Tags<br></td><td>Provide the list of tags to filter endpoints. Example: ["ABC_TEST", "DEF_TEST"].<br>
</td></tr><tr><td>Hostname<br></td><td>Specify the hostname of the endpoint to filter results.<br>
</td></tr><tr><td>Hostname Regex<br></td><td>Specify a regular expression to match endpoint hostnames.<br>
</td></tr><tr><td>Domain<br></td><td>Specify the domain name to filter endpoints.<br>
</td></tr><tr><td>Domain Regex<br></td><td>Specify a regular expression to match endpoint domains.<br>
</td></tr><tr><td>Network<br></td><td>Specify the local or remote IP address or network subnet to filter endpoints.<br>
</td></tr><tr><td>Versions<br></td><td>Provide the list of EDR versions to filter endpoints. Example: ["1.0.2", "1.1.0"].<br>
</td></tr><tr><td>Config UUIDs<br></td><td>Provide the list of configuration UUIDs to filter endpoints. Example: ["uuid-123", "uuid-456"].<br>
</td></tr><tr><td>UUIDs<br></td><td>Provide the list of endpoint UUIDs to filter results. Example: ["uuid-abc", "uuid-def"].<br>
</td></tr><tr><td>Appliance IDs<br></td><td>Provide the list of appliance IDs to filter endpoints. If not specified, defaults to appliances where the user has access rights.<br>
</td></tr><tr><td>First Seen From<br></td><td>Specify the start date-time for filtering endpoints based on when they were first seen.<br>
</td></tr><tr><td>First Seen To<br></td><td>Specify the end date-time for filtering endpoints based on when they were first seen.<br>
</td></tr><tr><td>Last Seen From<br></td><td>Specify the start date-time for filtering endpoints based on when they were last seen.<br>
</td></tr><tr><td>Last Seen To<br></td><td>Specify the end date-time for filtering endpoints based on when they were last seen.<br>
</td></tr><tr><td>OS<br></td><td>Provide the operating system filter in dictionary format. Example: {"windows": ["10", "8"], "linux": ["Ubuntu 18.04 bionic"]}.<br>
</td></tr><tr><td>Offset<br></td><td>Specify the offset value for pagination. The default value is 0.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Isolation Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Appliance ID<br></td><td>Specify the appliance ID that manages the endpoint whose isolation status is being retrieved.<br>
</td></tr><tr><td>EDR UUID<br></td><td>Specify the EDR UUID corresponding to the endpoint whose isolation status you want to retrieve.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Send Isolation Action
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Appliance ID<br></td><td>Specify the appliance ID that manages the endpoint on which the isolation action will be performed.<br>
</td></tr><tr><td>EDR UUID<br></td><td>Specify the EDR UUID corresponding to the endpoint targeted for the isolation command.<br>
</td></tr><tr><td>Isolation Action<br></td><td>Select the type of isolation action to perform — Enable, Disable, or Whitelist — based on the required isolation state of the endpoint.<br>
</td></tr><tr><td>WhiteList<br></td><td>Specify the whitelist ruleset to apply during isolation, allowing specific connections or policies when soft isolation is active.<br>
</td></tr><tr><td>Power<br></td><td>Select whether to use Soft isolation (policy-based) or Hard isolation (immediate enforcement without configuration).<br>
</td></tr><tr><td>Persist<br></td><td>Select whether to queue the isolation action until the endpoint reconnects, ensuring execution even when the endpoint is temporarily disconnected.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Global Policies
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Create New Global Policies
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Upsert/Downsert<br></td><td>Select the HTTP method to define how the policy should be processed — "POST", to create a new policy (downsert) or "PUT" to update an existing one (upsert).<br>
</td></tr><tr><td>Policy Data<br></td><td>Specify the complete JSON data defining the global policy, including configurations, parameters, and applicable rules.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Tags
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Update Endpoints Tags
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID List<br></td><td>Specify the list of EDR UUIDs representing the endpoints that will receive the new or updated tags.<br>
</td></tr><tr><td>Tags<br></td><td>Specify the tag value to assign to the endpoints. The tag must follow the format 'XXX_tags', where 'XXX' is a trigram identifier.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Access Logs
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>Specify the UUID of the EDR endpoint from which access logs will be fetched.<br>
</td></tr><tr><td>Appliance ID<br></td><td>Specify the ID of the appliance that manages the target endpoint.<br>
</td></tr><tr><td>Hostname<br></td><td>Specify the hostname filter for access logs. If omitted, the most recent hostname will be used.<br>
</td></tr><tr><td>Admin<br></td><td>Select whether to return only the count of alerts (True) or the full list of access logs (False).<br>
</td></tr><tr><td>Logon Event Time From<br></td><td>Specify the start timestamp for filtering access logs based on logon event time.<br>
</td></tr><tr><td>Logon Event Time To<br></td><td>Specify the end timestamp for filtering access logs based on logon event time. Must be later than "Logon Event Time From".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of access log entries to fetch in a single query. The value cannot exceed 1000.<br>
</td></tr><tr><td>Offset<br></td><td>Specify the number of records to skip before starting to retrieve access log results, for pagination purposes.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Users Connected
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>Specify the UUID of the EDR endpoint from which to retrieve connected user information.<br>
</td></tr><tr><td>Appliance ID<br></td><td>Specify the unique identifier of the appliance managing the endpoint.<br>
</td></tr><tr><td>Hostname<br></td><td>Specify the hostname to filter connected users. If omitted, the latest known hostname will be used.<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of connected user records to retrieve in a single query. The limit cannot exceed 1000.<br>
</td></tr><tr><td>Offset<br></td><td>Specify the number of connected user entries to skip before returning results, for pagination purposes.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Network Information
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>Specify the UUID of the EDR endpoint for which to collect detailed network data.<br>
</td></tr><tr><td>Appliance ID<br></td><td>Specify the unique appliance ID associated with the endpoint to retrieve its network details.<br>
</td></tr><tr><td>Hostname<br></td><td>Specify the hostname to refine the network information query. Defaults to the latest hostname if omitted.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Processes History
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier of the endpoint (EDR) whose process history is being queried.<br>
</td></tr><tr><td>Appliance ID<br></td><td>Specify the ID of the appliance managing the specified endpoint.<br>
</td></tr><tr><td>Process IDs<br></td><td>Filter for specific process IDs (PID list).<br>
</td></tr><tr><td>Parent Process IDs<br></td><td>Filter for specific parent process IDs (PPID list).<br>
</td></tr><tr><td>Logon IDs<br></td><td>Filter for logon session identifiers linked to processes.<br>
</td></tr><tr><td>User Identifier<br></td><td>Filter by user identifier (SID on Windows, UID on Linux). Supports substring matching.<br>
</td></tr><tr><td>Username<br></td><td>Filter results by username associated with the process.<br>
</td></tr><tr><td>Domain Name<br></td><td>Filter processes based on the domain name. Supports substring matching.<br>
</td></tr><tr><td>Local Time<br></td><td>If set to True, converts timestamps to the endpoint’s local time. Defaults to UTC.<br>
</td></tr><tr><td>Time Filter<br></td><td>Select which process lifecycle timestamp to filter by — Alive, Created, or Stopped.<br>
</td></tr><tr><td>Time From<br></td><td>Start of the time range for retrieving process history. Format: 2025-09-26T14:40:22.924Z.<br>
</td></tr><tr><td>Time To<br></td><td>End of the time range for retrieving process history. Format: 2025-09-26T14:40:22.924Z.<br>
</td></tr><tr><td>SHA256<br></td><td>Filter processes by their executable file’s SHA256 hash.<br>
</td></tr><tr><td>SHA1<br></td><td>Filter processes by their executable file’s SHA1 hash.<br>
</td></tr><tr><td>MD5<br></td><td>Filter processes by their executable file’s MD5 hash.<br>
</td></tr><tr><td>Path<br></td><td>Filter processes based on the executable file path. Supports substring matching.<br>
</td></tr><tr><td>CMD Line<br></td><td>Filter processes by the command line arguments used when launching the process.<br>
</td></tr><tr><td>Limit<br></td><td>Maximum number of records to return. Value cannot exceed 1000.<br>
</td></tr><tr><td>Offset<br></td><td>Number of records to skip before beginning to return results (for pagination).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Process Tree
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier of the endpoint (EDR) from which the process tree will be retrieved.<br>
</td></tr><tr><td>Appliance ID<br></td><td>Specify the identifier of the appliance managing the target endpoint.<br>
</td></tr><tr><td>Process ID<br></td><td>The process ID (PID) used as the root of the process tree to be retrieved.<br>
</td></tr><tr><td>Created Time<br></td><td>The local creation time of the process, used to identify it precisely. Format: 2025-09-26T14:40:22.924Z.<br>
</td></tr><tr><td>Number of Parents<br></td><td>Specifies how many parent processes should be included in the returned process tree hierarchy.<br>
</td></tr><tr><td>Limit<br></td><td>Maximum number of processes to retrieve in the tree. Cannot exceed 1000.<br>
</td></tr><tr><td>Offset<br></td><td>Pagination offset for results. This parameter is deprecated and fixed to 0.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Persistence Entries
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>Specify the unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>Specify the numeric identifier of the TEHTRIS EDR appliance managing the specified endpoint.<br>
</td></tr><tr><td>Local Time<br></td><td>Specify whether the time filter should use the endpoint’s local time or the server time.<br>
</td></tr><tr><td>Time<br></td><td>A timestamp to filter persistence entries that existed at a specific point in time.<br>
</td></tr><tr><td>Persistence Path<br></td><td>Filter results based on the file path where the persistence mechanism is defined (e.g., configuration file or startup script).<br>
</td></tr><tr><td>Persistence Type<br></td><td>Filter persistence entries by their type or category (e.g., SystemD service, cron job, startup script).<br>
</td></tr><tr><td>Name<br></td><td>Filter by the name associated with the persistence mechanism.<br>
</td></tr><tr><td>SHA256<br></td><td>Filter persistence entries associated with files that have the specified SHA-256 hash value.<br>
</td></tr><tr><td>SHA1<br></td><td>Filter persistence entries associated with files that have the specified SHA-1 hash value.<br>
</td></tr><tr><td>MD5<br></td><td>Filter persistence entries associated with files that have the specified MD5 hash value.<br>
</td></tr><tr><td>Path<br></td><td>Filter based on the file path of the executable or component involved in the persistence mechanism.<br>
</td></tr><tr><td>CMD Line<br></td><td>Filter persistence entries based on command-line arguments or execution parameters.<br>
</td></tr><tr><td>Limit<br></td><td>The maximum number of persistence entries to return in the result set.<br>
</td></tr><tr><td>Offset<br></td><td>The number of entries to skip before starting to collect the result set.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get USB History
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr><tr><td>Hostname<br></td><td>Filter results by the hostname of the endpoint associated with the USB activity.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Browser Security
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr><tr><td>Hostname<br></td><td>Filter results by the hostname of the endpoint associated with the browser security information.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Software List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr><tr><td>Persist<br></td><td>Specify whether the task should persist until completion if the endpoint is currently offline.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Fetch Endpoint Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Last Offline Forensic Report
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Offline Forensic Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Start Offline Forensic
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr><tr><td>Persist<br></td><td>Specify whether the forensic task should persist until it can be executed if the endpoint is currently offline.<br>
</td></tr><tr><td>Processes<br></td><td>Perform analysis of active and historical processes running on the endpoint.<br>
</td></tr><tr><td>Startup<br></td><td>Scan for persistence mechanisms and startup items configured on the endpoint.<br>
</td></tr><tr><td>Disk<br></td><td>Perform disk-level forensic analysis for specified directories and file extensions.<br>
</td></tr><tr><td>Disk Paths<br></td><td>Specify target directories to include in the disk forensic scan. Required only if disk scanning is enabled.<br>
</td></tr><tr><td>Extensions<br></td><td>Specify file extensions to target during disk forensic analysis. Required only if disk scanning is enabled.<br>
</td></tr><tr><td>Privacy<br></td><td>Perform privacy-related forensic checks, such as identifying sensitive data exposure or user information artifacts.<br>
</td></tr><tr><td>Advanced<br></td><td>Execute extended forensic scans including system logs, configurations, and advanced OS artifacts.<br>
</td></tr><tr><td>Commands<br></td><td>Run a set of pre-defined forensic commands to collect detailed endpoint data.<br>
</td></tr><tr><td>Yara<br></td><td>Apply YARA rules during analysis to detect potential malware or suspicious patterns.<br>
</td></tr><tr><td>Forensic<br></td><td>Trigger a comprehensive offline forensic analysis, encompassing all enabled modules.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Stop Offline Forensic
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the appliance managing the specified endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search Binaries
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Appliance ID<br></td><td>The numeric identifier of the TEHTRIS appliance managing the endpoints to be searched.<br>
</td></tr><tr><td>Hostname<br></td><td>Filter results to include binaries found on endpoints with the specified hostname.<br>
</td></tr><tr><td>Hostname Regex<br></td><td>Apply a regular expression filter to match hostnames more flexibly.<br>
</td></tr><tr><td>SHA256<br></td><td>Filter results by the binary’s SHA256 cryptographic hash.<br>
</td></tr><tr><td>SHA1<br></td><td>Filter results by the binary’s SHA1 hash value.<br>
</td></tr><tr><td>MD5<br></td><td>Filter results by the binary’s MD5 hash value.<br>
</td></tr><tr><td>Path<br></td><td>Filter binaries by their file path. This filter matches any part of the path (substring-compatible).<br>
</td></tr><tr><td>Path Regex<br></td><td>Apply a regular expression filter on file paths for flexible matching.<br>
</td></tr><tr><td>Signature CN<br></td><td>Filter binaries by the Common Name (CN) field in their digital signature. This is substring-compatible.<br>
</td></tr><tr><td>Signature CN Regex<br></td><td>Apply a regex-based filter to the Common Name (CN) of binary signatures.<br>
</td></tr><tr><td>Last Seen From<br></td><td>Filter binaries last seen on or after this timestamp. Useful for tracking binaries detected in a specific timeframe.<br>
</td></tr><tr><td>Last Seen To<br></td><td>Filter binaries last seen before this timestamp. Must be greater than 'Last Seen From' if both are provided.<br>
</td></tr><tr><td>Offset<br></td><td>Specify the number of results to skip before returning data. Used for pagination when results exceed 10,000 entries.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search User Access Logs
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Appliance ID<br></td><td>The numeric identifier of the TEHTRIS appliance managing the endpoints where access logs are collected.<br>
</td></tr><tr><td>Username<br></td><td>Filter results to include logs corresponding to a specific username. This filter supports partial (substring) matches.<br>
</td></tr><tr><td>Username Regex<br></td><td>Filter access logs by username using a regular expression for flexible pattern-based matching.<br>
</td></tr><tr><td>Logon Event Time From<br></td><td>Retrieve logs for user logon events that occurred on or after the specified timestamp.<br>
</td></tr><tr><td>Logon Event Time To<br></td><td>Retrieve logs for user logon events that occurred before the specified timestamp. Must be greater than 'Logon Event Time From' if both are specified.<br>
</td></tr><tr><td>Logoff Event Time From<br></td><td>Retrieve logs for user logoff events that occurred on or after the specified timestamp.<br>
</td></tr><tr><td>Logoff Event Time To<br></td><td>Retrieve logs for user logoff events that occurred before the specified timestamp. Must be greater than 'Logoff Event Time From' if both are specified.<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results to return per query. Must not exceed 10,000 entries.<br>
</td></tr><tr><td>Offset<br></td><td>Define the number of records to skip before starting to return results. Used for pagination when results exceed the specified limit.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search Persistent Entries by Category
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Category<br></td><td>Select the persistence entry category to search within. Available options include Files, Keys, Services, and Tasks.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the TEHTRIS appliance that manages the persistence data for endpoints.<br>
</td></tr><tr><td>Hostname<br></td><td>Filter persistence entries based on the endpoint hostname (substring match).<br>
</td></tr><tr><td>Hostname Regex<br></td><td>Filter hostnames using a regular expression pattern for flexible matching.<br>
</td></tr><tr><td>Path Regex<br></td><td>Filter persistence entries by path using a regular expression.<br>
</td></tr><tr><td>CMD Line Regex<br></td><td>Filter entries based on command line content using a regular expression.<br>
</td></tr><tr><td>Signature CN<br></td><td>Filter entries based on the certificate Common Name (CN) used to sign the file (substring match).<br>
</td></tr><tr><td>Signature CN Regex<br></td><td>Filter file signatures using a regular expression for Common Name (CN).<br>
</td></tr><tr><td>Persistence Path<br></td><td>Filter entries by the path of the configuration or source file that defines the persistence mechanism (substring match).<br>
</td></tr><tr><td>Persistence Path Regex<br></td><td>Filter entries by persistence source file path using a regex expression.<br>
</td></tr><tr><td>Persistence Type<br></td><td>Filter entries by type of persistence (e.g., service, task, registry key, or file).<br>
</td></tr><tr><td>Persistence Type Regex<br></td><td>Filter entries by persistence type using a regular expression.<br>
</td></tr><tr><td>Name<br></td><td>Filter entries by name. Depending on category, this corresponds to file path, registry key, service name, or task name.<br>
</td></tr><tr><td>Name Regex<br></td><td>Filter entries by name using a regular expression.<br>
</td></tr><tr><td>SHA256<br></td><td>Filter entries by SHA256 hash value.<br>
</td></tr><tr><td>SHA1<br></td><td>Filter entries by SHA1 hash value.<br>
</td></tr><tr><td>MD5<br></td><td>Filter entries by MD5 hash value.<br>
</td></tr><tr><td>Path<br></td><td>Filter persistence entries based on the file or executable path (substring match).<br>
</td></tr><tr><td>CMD Line<br></td><td>Filter persistence entries based on command-line arguments or execution strings (substring match).<br>
</td></tr><tr><td>Created From<br></td><td>Filter entries created after a specified timestamp (inclusive).<br>
</td></tr><tr><td>Created To<br></td><td>Filter entries created before a specified timestamp (inclusive).<br>
</td></tr><tr><td>Deleted From<br></td><td>Filter entries deleted after a specified timestamp (inclusive).<br>
</td></tr><tr><td>Deleted To<br></td><td>Filter entries deleted before a specified timestamp (inclusive).<br>
</td></tr><tr><td>Limit<br></td><td>The maximum number of results to return in a single response.<br>
</td></tr><tr><td>Offset<br></td><td>The number of results to skip before starting to return data, used for pagination.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search Persistent Entries
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Appliance ID<br></td><td>The numeric identifier of the TEHTRIS appliance managing persistence data for endpoints.<br>
</td></tr><tr><td>Hostname<br></td><td>Filter entries based on the endpoint hostname (substring match).<br>
</td></tr><tr><td>Hostname Regex<br></td><td>Filter hostnames using a regular expression for advanced pattern matching.<br>
</td></tr><tr><td>Path<br></td><td>Filter entries based on file or registry path (substring match).<br>
</td></tr><tr><td>Path Regex<br></td><td>Filter entries by file or registry path using a regular expression.<br>
</td></tr><tr><td>CMD Line<br></td><td>Filter entries based on command line content (substring match).<br>
</td></tr><tr><td>CMD Line Regex<br></td><td>Filter entries by command line using a regular expression.<br>
</td></tr><tr><td>Signature CN<br></td><td>Filter entries by the Common Name (CN) from the file signature (substring match).<br>
</td></tr><tr><td>Signature CN Regex<br></td><td>Filter file signatures using a regular expression for Common Name (CN).<br>
</td></tr><tr><td>Persistence Path<br></td><td>Filter entries by the source or configuration file path that defines persistence (substring match).<br>
</td></tr><tr><td>Persistence Path Regex<br></td><td>Filter entries by persistence source path using a regular expression.<br>
</td></tr><tr><td>Persistence Type<br></td><td>Filter entries based on the type of persistence mechanism (substring match).<br>
</td></tr><tr><td>Persistence Type Regex<br></td><td>Filter entries by persistence type using a regular expression.<br>
</td></tr><tr><td>Name<br></td><td>Filter entries by name. Depending on the category, this may represent a file path, registry key, service name, or scheduled task name.<br>
</td></tr><tr><td>Name Regex<br></td><td>Filter entries by name using a regular expression.<br>
</td></tr><tr><td>SHA256<br></td><td>Filter entries by SHA256 file hash value.<br>
</td></tr><tr><td>SHA1<br></td><td>Filter entries by SHA1 file hash value.<br>
</td></tr><tr><td>MD5<br></td><td>Filter entries by MD5 file hash value.<br>
</td></tr><tr><td>Created From<br></td><td>Return entries created after this date and time.<br>
</td></tr><tr><td>Created To<br></td><td>Return entries created before this date and time.<br>
</td></tr><tr><td>Deleted From<br></td><td>Return entries deleted after this date and time.<br>
</td></tr><tr><td>Deleted To<br></td><td>Return entries deleted before this date and time.<br>
</td></tr><tr><td>Limit<br></td><td>Maximum number of results to return (must be less than or equal to 10,000).<br>
</td></tr><tr><td>Offset<br></td><td>Result offset for pagination. Increment by 10,000 to fetch additional results.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Disk Scan Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the endpoint.<br>
</td></tr><tr><td>Scan ID<br></td><td>The unique identifier of the specific disk scan. If not provided, the API returns the status of the most recent or scheduled scan for the endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Launch Disk Scan
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the specified endpoint.<br>
</td></tr><tr><td>Persist<br></td><td>Specify whether the task should remain pending until execution if the endpoint is currently offline.<br>
</td></tr><tr><td>Scan ADS<br></td><td>Enable scanning of Alternate Data Streams (ADS) on Windows systems.<br>
</td></tr><tr><td>Scan White List Paths<br></td><td>List of directory paths to exclude from the scan (whitelisted).<br>
</td></tr><tr><td>Start Folders<br></td><td>Define specific folders or drives where the scan should begin.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Current Scan Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint as registered in the TEHTRIS EDR system.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the specified endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Stop Current Scan
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint where the scan is running.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the EDR appliance managing the specified endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Quarantine Files
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier (UUID) of the endpoint from which to retrieve quarantined files.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the appliance managing the specified endpoint.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Quarantine a File
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier of the endpoint on which the file quarantine operation will be executed.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the appliance managing the target endpoint.<br>
</td></tr><tr><td>Path<br></td><td>The full path to the file that should be quarantined on the endpoint.<br>
</td></tr><tr><td>Persist<br></td><td>Defines whether the task should be queued and executed when the endpoint reconnects if it is currently offline.<br>
</td></tr><tr><td>Notification<br></td><td>Custom message to display on the endpoint when the file is quarantined (Windows only).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Restore File from Quarantine
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>EDR UUID<br></td><td>The unique identifier of the endpoint where the quarantined file should be restored.<br>
</td></tr><tr><td>Appliance ID<br></td><td>The numeric identifier of the TEHTRIS appliance managing the target endpoint.<br>
</td></tr><tr><td>Path<br></td><td>The full path of the quarantined file to restore.<br>
</td></tr><tr><td>Persist<br></td><td>Defines whether the restore task should be queued and executed when the endpoint reconnects if it is currently offline.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Unmanaged Hosts
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Appliance ID<br></td><td>The unique numeric identifier of the TEHTRIS appliance responsible for host discovery and management.<br>
</td></tr><tr><td>Last Seen From<br></td><td>Return unmanaged hosts that were last seen on or after this timestamp. Useful for time-based filtering of discovery results.<br>
</td></tr><tr><td>Last Seen To<br></td><td>Return unmanaged hosts that were last seen on or before this timestamp. The value must be later than 'Last Seen From' if both are provided.<br>
</td></tr><tr><td>Limit<br></td><td>The maximum number of results to return per request. The value must not exceed 10,000.<br>
</td></tr><tr><td>Offset<br></td><td>The number of records to skip before starting to collect the result set. Used for pagination when more than 10,000 results are available.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE 

GET 

PATCH 

POST 

PUT <br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be /images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - TEHTRIS EDR - 1.0.0` playbook collection comes bundled with the TEHTRIS EDR connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the TEHTRIS EDR connector.

- 00 - Endpoint Isolation Management
- Tehtris > Create
- Tehtris > Fetch
- Tehtris > Fetch > FilterId
- Create Filter Severity Based
- Create New Global Policies
- Delete Filter
- Execute an API Request
- Fetch Events
- Fetch Info About Endpoint
- Get Access Logs
- Get All Endpoints
- Get All Global Policies
- Get Browser Security
- Get Current Scan Status
- Get Disk Scan Status
- Get Filter by ID
- Get History of Processes
- Get Isolation Status
- Get Last Offline Forensic Report
- Get Network Information
- Get Offline Forensic Report
- Get Persistence Entries
- Get Process Tree
- Get Software List
- Get Tags
- Get USB History
- Get Unmanaged Hosts
- Get Users Connected
- Launch Disk Scan
- List Folders and Filters
- List Quarantine Files
- Quarantine File
- Restore File From Quarantine
- Search Binaries
- Search Persistent Entries Using Category
- Search Persistent Entries Using Filters
- Search User Access Logs
- Send Isolation Action
- Set an Event Status
- Start Offline Forensic Analysis
- Stop Current Scan
- Stop Offline Forensic Analysis
- Tehtris > Ingest
- Update Endpoints Tags
- Update Filter

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling events/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.