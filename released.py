from types import MethodType


class Method(object):

    def __init__(self, method):
        self._method = method

    def __get__(self, obj, objtype):
        return self._method if obj is None else MethodType(self._method, obj,
                                                           objtype)


class ReleasedMetaClass(type):

    def __init__(cls, name, bases, attrs):
        for key, value in attrs.iteritems():
            if callable(value):
                setattr(cls, key, Method(value))


class object(object):

    __metaclass__ = ReleasedMetaClass
