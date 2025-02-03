from .message import send
from ._app import _get_to_address, _get_from_address, _set_to_address, _set_from_address
from .errors import NoContent

def push_setup(to_address: str, from_address: str):
    _set_to_address(to_address)
    _set_from_address(from_address)

def push_send(subject: str = None,
              tag: str = None,
              plain_body: str = None, 
              html_body: str = None, 
              attachments: list = None,
              ):
    
    if not (plain_body or html_body):
        raise NoContent()

    to_address = _get_to_address()
    from_address = _get_from_address()

    send(from_address, to_address, cc=None, bcc=None, sender=None, subject=subject, tag=tag, reply_to=None, plain_body=plain_body, html_body=html_body, attachments=attachments, headers=None, bounce=None)
