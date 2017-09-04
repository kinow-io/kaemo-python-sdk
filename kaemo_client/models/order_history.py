# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrderHistory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_order=None, id_order_state=None, date_add=None):
        """
        OrderHistory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_order': 'int',
            'id_order_state': 'int',
            'date_add': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_order': 'id_order',
            'id_order_state': 'id_order_state',
            'date_add': 'date_add'
        }

        self._id = id
        self._id_order = id_order
        self._id_order_state = id_order_state
        self._date_add = date_add

    @property
    def id(self):
        """
        Gets the id of this OrderHistory.

        :return: The id of this OrderHistory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderHistory.

        :param id: The id of this OrderHistory.
        :type: int
        """

        self._id = id

    @property
    def id_order(self):
        """
        Gets the id_order of this OrderHistory.

        :return: The id_order of this OrderHistory.
        :rtype: int
        """
        return self._id_order

    @id_order.setter
    def id_order(self, id_order):
        """
        Sets the id_order of this OrderHistory.

        :param id_order: The id_order of this OrderHistory.
        :type: int
        """

        self._id_order = id_order

    @property
    def id_order_state(self):
        """
        Gets the id_order_state of this OrderHistory.

        :return: The id_order_state of this OrderHistory.
        :rtype: int
        """
        return self._id_order_state

    @id_order_state.setter
    def id_order_state(self, id_order_state):
        """
        Sets the id_order_state of this OrderHistory.

        :param id_order_state: The id_order_state of this OrderHistory.
        :type: int
        """

        self._id_order_state = id_order_state

    @property
    def date_add(self):
        """
        Gets the date_add of this OrderHistory.

        :return: The date_add of this OrderHistory.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this OrderHistory.

        :param date_add: The date_add of this OrderHistory.
        :type: str
        """

        self._date_add = date_add

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
