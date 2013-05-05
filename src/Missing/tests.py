import sys
import unittest

if sys.version_info >= (3, ):
    def u(value):
        return str(value, 'utf-8')
else:
    def u(value):
        return unicode(value, 'utf-8')


class ValueTests(object):

    def test_cmp(self):
        value = self._make_one()
        self.assertNotEqual(value, 12)
        self.assertNotEqual(12, value)
        self.assertNotEqual(value, b'abc')
        self.assertNotEqual(b'abc', value)
        self.assertNotEqual(value, u(b'abc'))
        self.assertNotEqual(u(b'abc'), value)

    def test_add(self):
        value = self._make_one()
        self.assertEqual(1 + value, value)
        self.assertEqual(value + 1, value)
        self.assertEqual(value, 1 + value)
        self.assertEqual(value, value + 1)

    def test_class(self):
        value = self._make_one()
        self.assertEqual(repr(value.__class__), "<type 'Missing.Value'>")

    def test_type(self):
        value = self._make_one()
        self.assertEqual(repr(type(value())), "<type 'Missing.Value'>")


class TestValue(ValueTests, unittest.TestCase):

    def _make_one(self):
        from Missing import Value
        return Value


class TestMV(ValueTests, unittest.TestCase):

    def _make_one(self):
        from Missing import MV
        return MV


class TestV(ValueTests, unittest.TestCase):

    def _make_one(self):
        from Missing import V
        return V
