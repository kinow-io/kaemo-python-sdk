# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.81
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.task_factory import TaskFactory


class TestTaskFactory(unittest.TestCase):
    """ TaskFactory unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskFactory(self):
        """
        Test TaskFactory
        """
        model = kinow_client.models.task_factory.TaskFactory()


if __name__ == '__main__':
    unittest.main()
