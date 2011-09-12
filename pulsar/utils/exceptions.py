
class PulsarException(Exception):
    '''base class of all Pulsar Exception'''


class PulsarInternetException(PulsarException):
    '''base class of all Pulsar Internet Exception'''
    pass
    
class ActorAlreadyStarted(PulsarException):
    '''A :class:`PulsarException` raised when trying to start an actor already started'''
    
class HaltServer(PulsarInternetException):
    
    def __init__(self, reason, signal=None):
        super(HaltServer,self).__init__(reason)
        self.signal = signal


class ConnectionError(PulsarInternetException):
    pass
    
class AlreadyCalledError(PulsarException):
    '''Raised when a Deferred instance receives more than une callback'''

class AlreadyRegistered(PulsarException):
    pass

class NotRegisteredWithServer(PulsarException):
    pass


class BadHttpRequest(PulsarInternetException):
    status = 500
    def __init__(self, status = None, reason = ''):
        self.status = status or self.status
        super(BadHttpRequest,self).__init__(reason)