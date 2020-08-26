# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.80
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DownloadInformations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, source_url=None, manifest=None, session_id=None):
        """
        DownloadInformations - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'source_url': 'str',
            'manifest': 'object',
            'session_id': 'str'
        }

        self.attribute_map = {
            'source_url': 'source_url',
            'manifest': 'manifest',
            'session_id': 'session_id'
        }

        self._source_url = source_url
        self._manifest = manifest
        self._session_id = session_id

    @property
    def source_url(self):
        """
        Gets the source_url of this DownloadInformations.

        :return: The source_url of this DownloadInformations.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """
        Sets the source_url of this DownloadInformations.

        :param source_url: The source_url of this DownloadInformations.
        :type: str
        """

        self._source_url = source_url

    @property
    def manifest(self):
        """
        Gets the manifest of this DownloadInformations.

        :return: The manifest of this DownloadInformations.
        :rtype: object
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DownloadInformations.

        :param manifest: The manifest of this DownloadInformations.
        :type: object
        """

        self._manifest = manifest

    @property
    def session_id(self):
        """
        Gets the session_id of this DownloadInformations.

        :return: The session_id of this DownloadInformations.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this DownloadInformations.

        :param session_id: The session_id of this DownloadInformations.
        :type: str
        """

        self._session_id = session_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
