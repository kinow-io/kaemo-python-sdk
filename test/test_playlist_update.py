# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.playlist_update import PlaylistUpdate


class TestPlaylistUpdate(unittest.TestCase):
    """ PlaylistUpdate unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlaylistUpdate(self):
        """
        Test PlaylistUpdate
        """
        model = kinow_client.models.playlist_update.PlaylistUpdate()


if __name__ == '__main__':
    unittest.main()
