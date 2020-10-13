# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartRuleRestrictionGroupItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, id_item=None):
        """
        CartRuleRestrictionGroupItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'id_item': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'id_item': 'id_item'
        }

        self._type = type
        self._id_item = id_item

    @property
    def type(self):
        """
        Gets the type of this CartRuleRestrictionGroupItem.
        Can be: product, subscription, category, actor or director

        :return: The type of this CartRuleRestrictionGroupItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CartRuleRestrictionGroupItem.
        Can be: product, subscription, category, actor or director

        :param type: The type of this CartRuleRestrictionGroupItem.
        :type: str
        """

        self._type = type

    @property
    def id_item(self):
        """
        Gets the id_item of this CartRuleRestrictionGroupItem.
        Item ID to restrict

        :return: The id_item of this CartRuleRestrictionGroupItem.
        :rtype: int
        """
        return self._id_item

    @id_item.setter
    def id_item(self, id_item):
        """
        Sets the id_item of this CartRuleRestrictionGroupItem.
        Item ID to restrict

        :param id_item: The id_item of this CartRuleRestrictionGroupItem.
        :type: int
        """

        self._id_item = id_item

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
