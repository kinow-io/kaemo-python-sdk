# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.65
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CustomerVideoStat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, customer_id=None, played=None, duration=None, views=None):
        """
        CustomerVideoStat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'customer_id': 'int',
            'played': 'int',
            'duration': 'float',
            'views': 'int'
        }

        self.attribute_map = {
            'customer_id': 'customer_id',
            'played': 'played',
            'duration': 'duration',
            'views': 'views'
        }

        self._customer_id = customer_id
        self._played = played
        self._duration = duration
        self._views = views

    @property
    def customer_id(self):
        """
        Gets the customer_id of this CustomerVideoStat.

        :return: The customer_id of this CustomerVideoStat.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this CustomerVideoStat.

        :param customer_id: The customer_id of this CustomerVideoStat.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def played(self):
        """
        Gets the played of this CustomerVideoStat.

        :return: The played of this CustomerVideoStat.
        :rtype: int
        """
        return self._played

    @played.setter
    def played(self, played):
        """
        Sets the played of this CustomerVideoStat.

        :param played: The played of this CustomerVideoStat.
        :type: int
        """

        self._played = played

    @property
    def duration(self):
        """
        Gets the duration of this CustomerVideoStat.

        :return: The duration of this CustomerVideoStat.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this CustomerVideoStat.

        :param duration: The duration of this CustomerVideoStat.
        :type: float
        """

        self._duration = duration

    @property
    def views(self):
        """
        Gets the views of this CustomerVideoStat.

        :return: The views of this CustomerVideoStat.
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this CustomerVideoStat.

        :param views: The views of this CustomerVideoStat.
        :type: int
        """

        self._views = views

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
