# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductPricePrices(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_attribute=None, price=None, price_noreduc=None):
        """
        ProductPricePrices - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_attribute': 'float',
            'price': 'float',
            'price_noreduc': 'float'
        }

        self.attribute_map = {
            'id_attribute': 'id_attribute',
            'price': 'price',
            'price_noreduc': 'price_noreduc'
        }

        self._id_attribute = id_attribute
        self._price = price
        self._price_noreduc = price_noreduc

    @property
    def id_attribute(self):
        """
        Gets the id_attribute of this ProductPricePrices.

        :return: The id_attribute of this ProductPricePrices.
        :rtype: float
        """
        return self._id_attribute

    @id_attribute.setter
    def id_attribute(self, id_attribute):
        """
        Sets the id_attribute of this ProductPricePrices.

        :param id_attribute: The id_attribute of this ProductPricePrices.
        :type: float
        """

        self._id_attribute = id_attribute

    @property
    def price(self):
        """
        Gets the price of this ProductPricePrices.

        :return: The price of this ProductPricePrices.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductPricePrices.

        :param price: The price of this ProductPricePrices.
        :type: float
        """

        self._price = price

    @property
    def price_noreduc(self):
        """
        Gets the price_noreduc of this ProductPricePrices.

        :return: The price_noreduc of this ProductPricePrices.
        :rtype: float
        """
        return self._price_noreduc

    @price_noreduc.setter
    def price_noreduc(self, price_noreduc):
        """
        Sets the price_noreduc of this ProductPricePrices.

        :param price_noreduc: The price_noreduc of this ProductPricePrices.
        :type: float
        """

        self._price_noreduc = price_noreduc

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