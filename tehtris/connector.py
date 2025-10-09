# License details
""" Copyright start
  MIT License
  Copyright (c) 2025 Fortinet Inc
  Copyright end """

# Imports
from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations_map, make_api_call

# Initialise logger
logger = get_logger('tehtris')

# Class Definition
class Tehtris(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations_map.get(operation)
        return action(config, params)

    def check_health(self, config):
        try:
            json_data = {}
            query_params = {}
            func_headers_dict = {}
            from .operations import get_tags
            return get_tags(config, params={})
        except Exception as err:
            logger.error("Check Health Failed. Error: {0}".format(str(err)))
            raise ConnectorError(str(err))