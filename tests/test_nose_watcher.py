# -*- coding: utf-8 -*-
import unittest

from mock import Mock

from nose_watcher.nose_watcher import WatcherPlugin


class TestNoseWatcher(unittest.TestCase):

    def setUp(self):
        self.plugin = WatcherPlugin()
        self.plugin.call = Mock()

    def test_file_types_py(self):
        self.assertTrue(self.plugin.check_files({'test.py'}))

    def test_file_types_pyx(self):
        self.assertTrue(self.plugin.check_files({'test.pyx'}))

    def test_file_types_pyc(self):
        self.assertFalse(self.plugin.check_files({'test.pyc'}))

    def test_file_types_py_and_pyc(self):
        self.assertTrue(self.plugin.check_files({'test.py', 'test.pyc'}))

    def test_file_types_pyc_and_txt(self):
        self.assertFalse(self.plugin.check_files({'test.txt', 'test.pyc'}))
