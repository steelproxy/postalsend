_postal_key = None
_postal_server = None

def _set_server(server):
    global _postal_server
    _postal_server = server

def _get_server():
    return _postal_server

def _set_api_key(key):
    global _postal_key
    _postal_key = key

def _get_api_key():
    return _postal_key