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


class CartPrice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_cart=None, total_without_tax=None, total_discount=None, total_trial=None, total=None):
        """
        CartPrice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_cart': 'int',
            'total_without_tax': 'float',
            'total_discount': 'float',
            'total_trial': 'float',
            'total': 'float'
        }

        self.attribute_map = {
            'id_cart': 'id_cart',
            'total_without_tax': 'total_without_tax',
            'total_discount': 'total_discount',
            'total_trial': 'total_trial',
            'total': 'total'
        }

        self._id_cart = id_cart
        self._total_without_tax = total_without_tax
        self._total_discount = total_discount
        self._total_trial = total_trial
        self._total = total

    @property
    def id_cart(self):
        """
        Gets the id_cart of this CartPrice.
        

        :return: The id_cart of this CartPrice.
        :rtype: int
        """
        return self._id_cart

    @id_cart.setter
    def id_cart(self, id_cart):
        """
        Sets the id_cart of this CartPrice.
        

        :param id_cart: The id_cart of this CartPrice.
        :type: int
        """

        self._id_cart = id_cart

    @property
    def total_without_tax(self):
        """
        Gets the total_without_tax of this CartPrice.
        

        :return: The total_without_tax of this CartPrice.
        :rtype: float
        """
        return self._total_without_tax

    @total_without_tax.setter
    def total_without_tax(self, total_without_tax):
        """
        Sets the total_without_tax of this CartPrice.
        

        :param total_without_tax: The total_without_tax of this CartPrice.
        :type: float
        """

        self._total_without_tax = total_without_tax

    @property
    def total_discount(self):
        """
        Gets the total_discount of this CartPrice.
        

        :return: The total_discount of this CartPrice.
        :rtype: float
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """
        Sets the total_discount of this CartPrice.
        

        :param total_discount: The total_discount of this CartPrice.
        :type: float
        """

        self._total_discount = total_discount

    @property
    def total_trial(self):
        """
        Gets the total_trial of this CartPrice.
        

        :return: The total_trial of this CartPrice.
        :rtype: float
        """
        return self._total_trial

    @total_trial.setter
    def total_trial(self, total_trial):
        """
        Sets the total_trial of this CartPrice.
        

        :param total_trial: The total_trial of this CartPrice.
        :type: float
        """

        self._total_trial = total_trial

    @property
    def total(self):
        """
        Gets the total of this CartPrice.
        

        :return: The total of this CartPrice.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this CartPrice.
        

        :param total: The total of this CartPrice.
        :type: float
        """

        self._total = total

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
