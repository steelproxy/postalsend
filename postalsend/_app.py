_app_data = {
    "name": None,
    "version": None,
    "identifier": None,
    "to_address": None,
    "from_address": None,
    "server": None,
    "api_key": None
}

def _set_app_name(name: str):
    _app_data["name"] = name

def _get_app_name():
    return _app_data["name"]

def _set_app_version(version: str):
    _app_data["version"] = version

def _get_app_version():
    return _app_data["version"]

def _set_identifier(identifier: str):
    _app_data["identifier"] = identifier

def _get_identifier():
    return _app_data["identifier"]

def _set_to_address(to_address: str):
    _app_data["to_address"] = to_address

def _get_to_address():
    return _app_data["to_address"]

def _set_from_address(from_address: str):
    _app_data["from_address"] = from_address

def _get_from_address():
    return _app_data["from_address"]

def _set_server(server: str):
    _app_data["server"] = server

def _get_server():
    return _app_data["server"]

def _set_api_key(api_key: str):
    _app_data["api_key"] = api_key

def _get_api_key():
    return _app_data["api_key"]
