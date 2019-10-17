# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Feature(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, position=None, name=None, value=None):
        """
        Feature - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'position': 'int',
            'name': 'str',
            'value': 'FeatureValue'
        }

        self.attribute_map = {
            'id': 'id',
            'position': 'position',
            'name': 'name',
            'value': 'value'
        }

        self._id = id
        self._position = position
        self._name = name
        self._value = value

    @property
    def id(self):
        """
        Gets the id of this Feature.
        

        :return: The id of this Feature.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Feature.
        

        :param id: The id of this Feature.
        :type: int
        """

        self._id = id

    @property
    def position(self):
        """
        Gets the position of this Feature.
        

        :return: The position of this Feature.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this Feature.
        

        :param position: The position of this Feature.
        :type: int
        """

        self._position = position

    @property
    def name(self):
        """
        Gets the name of this Feature.
        

        :return: The name of this Feature.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Feature.
        

        :param name: The name of this Feature.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this Feature.

        :return: The value of this Feature.
        :rtype: FeatureValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Feature.

        :param value: The value of this Feature.
        :type: FeatureValue
        """

        self._value = value

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
