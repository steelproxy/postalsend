from ._server import _get_api_key, _get_server
from .errors import (
    PostalError, ParameterError, NoContent, TooManyToAddresses, TooManyCCAddresses,
    TooManyBCCAddresses, NoRecipients, FromAddressMissing,
    AttachmentMissingName, AttachmentMissingData, UnauthenticatedFromAddress,
    ValidationError
)
import requests
import json

SEND_ENDPOINT = "/api/v1/send/message"

def send(from_address: str, 
         to_address: list[str], 
         cc: list[str] = None, 
         bcc: list[str] = None, 
         sender: str = None, 
         subject: str = None, 
         tag: str = None, 
         reply_to: str = None, 
         plain_body: str = None, 
         html_body: str = None, 
         attachments: list = None, 
         headers: dict = None, 
         bounce: bool = None):
    """
    Send an email using the Postal API.
    
    Args:
        from_address (str): Email address for the From header.
        to_address (list[str]): Recipients email addresses (max 50).
        cc (list[str], optional): CC recipients email addresses (max 50).
        bcc (list[str], optional): BCC recipients email addresses (max 50).
        sender (str, optional): Email address for the Sender header.
        subject (str, optional): Email subject.
        tag (str, optional): Email tag.
        reply_to (str, optional): Reply-to address.
        plain_body (str, optional): Email body in plain text.
        html_body (str, optional): Email body in HTML.
        attachments (list, optional): Array of attachments.
        headers (dict, optional): Additional headers.
        bounce (bool, optional): Whether this message is a bounce.
    
    Returns:
        dict: API response.
        
    Raises:
        NoRecipients: If no recipients are provided.
        FromAddressMissing: If the From address is missing.
        NoContent: If both plain_body and html_body are missing.
        TooManyToAddresses: If more than 50 "To" recipients are provided.
        TooManyCCAddresses: If more than 50 "CC" recipients are provided.
        TooManyBCCAddresses: If more than 50 "BCC" recipients are provided.
        AttachmentMissingName: If an attachment is missing a name.
        AttachmentMissingData: If an attachment is missing data.
        UnauthenticatedFromAddress: If the sender is not authorized to send emails.
        ValidationError: If the API rejects the request due to validation issues.
        PostalError: If an unknown API error occurs.
    """
    server = _get_server()
    api_key = _get_api_key()

    url = f"https://{server}{SEND_ENDPOINT}"
    
    api_headers = {
        'X-Server-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    # Validation checks before making the request
    if not from_address:
        raise FromAddressMissing()

    if not (to_address or cc or bcc):
        raise NoRecipients()

    if len(to_address) > 50:
        raise TooManyToAddresses()
    
    if cc and len(cc) > 50:
        raise TooManyCCAddresses()
    
    if bcc and len(bcc) > 50:
        raise TooManyBCCAddresses()
    
    if not (plain_body or html_body):
        raise NoContent()
    
    if attachments:
        for attachment in attachments:
            if not attachment.get("name"):
                raise AttachmentMissingName()
            if not attachment.get("data"):
                raise AttachmentMissingData()

    payload = {
        'to': to_address,
        'from': from_address,
        'subject': subject,
        **({'cc': cc} if cc else {}),
        **({'bcc': bcc} if bcc else {}),
        **({'sender': sender} if sender else {}),
        **({'tag': tag} if tag else {}),
        **({'reply_to': reply_to} if reply_to else {}),
        **({'plain_body': plain_body} if plain_body else {}),
        **({'html_body': html_body} if html_body else {}),
        **({'attachments': attachments} if attachments else {}),
        **({'headers': headers} if headers else {}),
        **({'bounce': bounce} if bounce is not None else {})
    }
    
    response = requests.post(url, headers=api_headers, json=payload)
    response_data = response.json()

    # Handle API response errors
    if response.status_code == 403:
        raise UnauthenticatedFromAddress()
    
    if response.status_code == 400:
        errors = response_data.get("errors", {})
        raise ValidationError(errors)
    
    # Check for specific API error messages in response
    error_map = {
        "NoRecipients": NoRecipients,
        "NoContent": NoContent,
        "TooManyToAddresses": TooManyToAddresses,
        "TooManyCCAddresses": TooManyCCAddresses,
        "TooManyBCCAddresses": TooManyBCCAddresses,
        "FromAddressMissing": FromAddressMissing,
        "UnauthenticatedFromAddress": UnauthenticatedFromAddress,
        "AttachmentMissingName": AttachmentMissingName,
        "AttachmentMissingData": AttachmentMissingData
    }
    
    error_type = response_data.get("error")
    if error_type in error_map:
        raise error_map[error_type]()
    
    # If the response contains errors not explicitly mapped, raise generic PostalError
    if response.status_code != 200:
        raise PostalError(f"Unexpected API error: {response_data}")

    return response_data

