# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.52
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAttributeCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, type=None, price=None, active=None):
        """
        ProductAttributeCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'int',
            'type': 'int',
            'price': 'float',
            'active': 'bool'
        }

        self.attribute_map = {
            'product_id': 'product_id',
            'type': 'type',
            'price': 'price',
            'active': 'active'
        }

        self._product_id = product_id
        self._type = type
        self._price = price
        self._active = active

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductAttributeCreateRequest.
        Id of the product to attach this attribute

        :return: The product_id of this ProductAttributeCreateRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductAttributeCreateRequest.
        Id of the product to attach this attribute

        :param product_id: The product_id of this ProductAttributeCreateRequest.
        :type: int
        """

        self._product_id = product_id

    @property
    def type(self):
        """
        Gets the type of this ProductAttributeCreateRequest.
        1: Streaming & Download, 2: Download only, 3: Streaming only

        :return: The type of this ProductAttributeCreateRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductAttributeCreateRequest.
        1: Streaming & Download, 2: Download only, 3: Streaming only

        :param type: The type of this ProductAttributeCreateRequest.
        :type: int
        """

        self._type = type

    @property
    def price(self):
        """
        Gets the price of this ProductAttributeCreateRequest.
        Final price of the product

        :return: The price of this ProductAttributeCreateRequest.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductAttributeCreateRequest.
        Final price of the product

        :param price: The price of this ProductAttributeCreateRequest.
        :type: float
        """

        self._price = price

    @property
    def active(self):
        """
        Gets the active of this ProductAttributeCreateRequest.
        Status of the attribute

        :return: The active of this ProductAttributeCreateRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductAttributeCreateRequest.
        Status of the attribute

        :param active: The active of this ProductAttributeCreateRequest.
        :type: bool
        """

        self._active = active

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
