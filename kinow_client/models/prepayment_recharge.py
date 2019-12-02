# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.36
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrepaymentRecharge(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_product=None, amount=None, type=None, date_add=None, date_upd=None, active=None):
        """
        PrepaymentRecharge - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_product': 'int',
            'amount': 'float',
            'type': 'str',
            'date_add': 'str',
            'date_upd': 'str',
            'active': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'id_product': 'id_product',
            'amount': 'amount',
            'type': 'type',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'active': 'active'
        }

        self._id = id
        self._id_product = id_product
        self._amount = amount
        self._type = type
        self._date_add = date_add
        self._date_upd = date_upd
        self._active = active

    @property
    def id(self):
        """
        Gets the id of this PrepaymentRecharge.
        

        :return: The id of this PrepaymentRecharge.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrepaymentRecharge.
        

        :param id: The id of this PrepaymentRecharge.
        :type: int
        """

        self._id = id

    @property
    def id_product(self):
        """
        Gets the id_product of this PrepaymentRecharge.
        

        :return: The id_product of this PrepaymentRecharge.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this PrepaymentRecharge.
        

        :param id_product: The id_product of this PrepaymentRecharge.
        :type: int
        """

        self._id_product = id_product

    @property
    def amount(self):
        """
        Gets the amount of this PrepaymentRecharge.
        

        :return: The amount of this PrepaymentRecharge.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PrepaymentRecharge.
        

        :param amount: The amount of this PrepaymentRecharge.
        :type: float
        """

        self._amount = amount

    @property
    def type(self):
        """
        Gets the type of this PrepaymentRecharge.
        

        :return: The type of this PrepaymentRecharge.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PrepaymentRecharge.
        

        :param type: The type of this PrepaymentRecharge.
        :type: str
        """

        self._type = type

    @property
    def date_add(self):
        """
        Gets the date_add of this PrepaymentRecharge.
        

        :return: The date_add of this PrepaymentRecharge.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this PrepaymentRecharge.
        

        :param date_add: The date_add of this PrepaymentRecharge.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this PrepaymentRecharge.
        

        :return: The date_upd of this PrepaymentRecharge.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this PrepaymentRecharge.
        

        :param date_upd: The date_upd of this PrepaymentRecharge.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def active(self):
        """
        Gets the active of this PrepaymentRecharge.
        

        :return: The active of this PrepaymentRecharge.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PrepaymentRecharge.
        

        :param active: The active of this PrepaymentRecharge.
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
