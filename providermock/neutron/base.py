from abc import abstractmethod
import time


class ResponseBase(object):

    @abstractmethod
    def path(self):
        pass

    @abstractmethod
    def response(self, path, content=None):
        pass

    def generate_id(self):
        return str(int(time.time()))
