# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoFreeAccess(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, has_streaming=None, has_download=None):
        """
        VideoFreeAccess - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'has_streaming': 'bool',
            'has_download': 'bool'
        }

        self.attribute_map = {
            'has_streaming': 'hasStreaming',
            'has_download': 'hasDownload'
        }

        self._has_streaming = has_streaming
        self._has_download = has_download

    @property
    def has_streaming(self):
        """
        Gets the has_streaming of this VideoFreeAccess.

        :return: The has_streaming of this VideoFreeAccess.
        :rtype: bool
        """
        return self._has_streaming

    @has_streaming.setter
    def has_streaming(self, has_streaming):
        """
        Sets the has_streaming of this VideoFreeAccess.

        :param has_streaming: The has_streaming of this VideoFreeAccess.
        :type: bool
        """

        self._has_streaming = has_streaming

    @property
    def has_download(self):
        """
        Gets the has_download of this VideoFreeAccess.

        :return: The has_download of this VideoFreeAccess.
        :rtype: bool
        """
        return self._has_download

    @has_download.setter
    def has_download(self, has_download):
        """
        Sets the has_download of this VideoFreeAccess.

        :param has_download: The has_download of this VideoFreeAccess.
        :type: bool
        """

        self._has_download = has_download

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
