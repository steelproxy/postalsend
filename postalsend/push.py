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
    """
    Send a push notification using the Postal API.

    Args:
        subject (str, optional): The subject of the push notification.
        tag (str, optional): The tag of the push notification.
        plain_body (str, optional): The plain body of the push notification.
        html_body (str, optional): The HTML body of the push notification.
        attachments (list, optional): A list of attachments to the push notification.

    Exceptions:
        NoContent: If no plain_body or html_body is provided.
    """

    if not (plain_body or html_body):
        raise NoContent()

    to_address = _get_to_address()
    from_address = _get_from_address()

    send(from_address, to_address, cc=None, bcc=None, sender=None, subject=subject, tag=tag, reply_to=None, plain_body=plain_body, html_body=html_body, attachments=attachments, headers=None, bounce=None)

