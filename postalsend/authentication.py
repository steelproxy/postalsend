from ._app import _set_api_key, _set_server

def login(server, key):
    _set_server(server)
    _set_api_key(key)