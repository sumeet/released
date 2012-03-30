import doctest
import unittest

from expecter import expect
from mock import Mock

from released import Method, object as object_


class MethodDescriptorTest(unittest.TestCase):

    class MyClass(object):
        my_method = Method(lambda self: self)

    def test_acts_like_a_normal_method(self):
        value = Mock(name='value')
        expect(self.MyClass.my_method(value)) == value

    def test_acts_like_an_instance_method(self):
        my_instance = self.MyClass()
        expect(my_instance.my_method()) == my_instance


class objectTest(unittest.TestCase):

    class MyClass(object_):
        def my_method(self):
            return self

    def test_my_method_acts_like_an_instance_method(self):
        my_instance = self.MyClass()
        expect(my_instance.my_method()) == my_instance

    def test_my_method_acts_like_an_unbound_method(self):
        value = Mock()
        expect(self.MyClass.my_method(value)) == value


class ReadmeTest(unittest.TestCase):

    def setUp(self):
        optionflags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
        self.test_results = doctest.testfile('README.markdown',
                                             optionflags=optionflags)

    def test_contains_tests(self):
        expect(self.test_results.attempted) > 0

    def test_does_not_fail(self):
        expect(self.test_results.failed) == 0


if __name__ == '__main__':
    unittest.main()
