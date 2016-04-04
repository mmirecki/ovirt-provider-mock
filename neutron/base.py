from abc import abstractmethod
import time


class ResponseBase(object):

    @abstractmethod
    def path(self):
        pass

    @abstractmethod
    def response(self, path):
        pass


class PostResponseBase(object):

    @abstractmethod
    def path(self):
        pass

    @abstractmethod
    def response(self, path, content):
        pass

    def generate_id(self):
        return str(int(time.time()))
