_app_to_address = None
_app_from_address = None


def _set_app_name(name: str):
    global _app_name
    _app_name = name

def _set_app_version(version: str):
    global _app_version
    _app_version = version  

def _set_identifier(identifier: str):
    global _app_identifier
    _app_identifier = identifier    

def _set_to_address(to_address: str):
    global _app_to_address
    _app_to_address = to_address

def _set_from_address(from_address: str):
    global _app_from_address
    _app_from_address = from_address

def _get_app_name():
    return _app_name

def _get_app_version():
    return _app_version

def _get_identifier():
    return _app_identifier

def _get_to_address():
    return _app_to_address

def _get_from_address():
    return _app_from_address
