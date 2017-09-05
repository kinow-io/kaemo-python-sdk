# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FeatureValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_feature=None, custom=None, value=None):
        """
        FeatureValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_feature': 'int',
            'custom': 'bool',
            'value': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_feature': 'id_feature',
            'custom': 'custom',
            'value': 'value'
        }

        self._id = id
        self._id_feature = id_feature
        self._custom = custom
        self._value = value

    @property
    def id(self):
        """
        Gets the id of this FeatureValue.

        :return: The id of this FeatureValue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FeatureValue.

        :param id: The id of this FeatureValue.
        :type: int
        """

        self._id = id

    @property
    def id_feature(self):
        """
        Gets the id_feature of this FeatureValue.

        :return: The id_feature of this FeatureValue.
        :rtype: int
        """
        return self._id_feature

    @id_feature.setter
    def id_feature(self, id_feature):
        """
        Sets the id_feature of this FeatureValue.

        :param id_feature: The id_feature of this FeatureValue.
        :type: int
        """

        self._id_feature = id_feature

    @property
    def custom(self):
        """
        Gets the custom of this FeatureValue.

        :return: The custom of this FeatureValue.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this FeatureValue.

        :param custom: The custom of this FeatureValue.
        :type: bool
        """

        self._custom = custom

    @property
    def value(self):
        """
        Gets the value of this FeatureValue.

        :return: The value of this FeatureValue.
        :rtype: list[I18nField]
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this FeatureValue.

        :param value: The value of this FeatureValue.
        :type: list[I18nField]
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
