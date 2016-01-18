from abc import abstractmethod


class ResponseBase(object):

    @abstractmethod
    def path(self):
        pass

    @abstractmethod
    def response(self, path):
        pass
