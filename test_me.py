#!/usr/bin/python
# -*- coding: utf-8 -*-

from main import for_tests
import unittest


class AppRuntimeTestCase(unittest.TestCase):
    def testAppRunningIsCorrect(self):
        result = for_tests()
        self.assertEqual(True, result)

if __name__ == "__main__":
    unittest.main()
