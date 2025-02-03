class PostalError(Exception):
    """Base exception class for Postal errors"""
    pass

class ValidationError(PostalError):
    """The provided data was not sufficient to send an email"""
    def __init__(self, errors=None):
        self.errors = errors
        super().__init__("The provided data was not sufficient to send an email")

class NoRecipients(PostalError):
    """There are no recipients defined to received this message"""
    def __init__(self):
        super().__init__("There are no recipients defined to received this message")

class NoContent(PostalError):
    """There is no content defined for this e-mail"""
    def __init__(self):
        super().__init__("There is no content defined for this e-mail")

class TooManyToAddresses(PostalError):
    """The maximum number of To addresses has been reached (maximum 50)"""
    def __init__(self):
        super().__init__("The maximum number of To addresses has been reached (maximum 50)")

class TooManyCCAddresses(PostalError):
    """The maximum number of CC addresses has been reached (maximum 50)"""
    def __init__(self):
        super().__init__("The maximum number of CC addresses has been reached (maximum 50)")

class TooManyBCCAddresses(PostalError):
    """The maximum number of BCC addresses has been reached (maximum 50)"""
    def __init__(self):
        super().__init__("The maximum number of BCC addresses has been reached (maximum 50)")

class FromAddressMissing(PostalError):
    """The From address is missing and is required"""
    def __init__(self):
        super().__init__("The From address is missing and is required")

class UnauthenticatedFromAddress(PostalError):
    """The From address is not authorised to send mail from this server"""
    def __init__(self):
        super().__init__("The From address is not authorised to send mail from this server")

class AttachmentMissingName(PostalError):
    """An attachment is missing a name"""
    def __init__(self):
        super().__init__("An attachment is missing a name")

class AttachmentMissingData(PostalError):
    """An attachment is missing data"""
    def __init__(self):
        super().__init__("An attachment is missing data")

class ParameterError(PostalError):
    """Generic error for invalid parameters"""
    pass
