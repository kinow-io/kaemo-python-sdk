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


class PrepaymentOperation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_customer=None, id_order=None, amount=None, type=None, date_add=None, date_upd=None):
        """
        PrepaymentOperation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_customer': 'int',
            'id_order': 'int',
            'amount': 'float',
            'type': 'str',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_customer': 'id_customer',
            'id_order': 'id_order',
            'amount': 'amount',
            'type': 'type',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_customer = id_customer
        self._id_order = id_order
        self._amount = amount
        self._type = type
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this PrepaymentOperation.

        :return: The id of this PrepaymentOperation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrepaymentOperation.

        :param id: The id of this PrepaymentOperation.
        :type: int
        """

        self._id = id

    @property
    def id_customer(self):
        """
        Gets the id_customer of this PrepaymentOperation.

        :return: The id_customer of this PrepaymentOperation.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this PrepaymentOperation.

        :param id_customer: The id_customer of this PrepaymentOperation.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_order(self):
        """
        Gets the id_order of this PrepaymentOperation.

        :return: The id_order of this PrepaymentOperation.
        :rtype: int
        """
        return self._id_order

    @id_order.setter
    def id_order(self, id_order):
        """
        Sets the id_order of this PrepaymentOperation.

        :param id_order: The id_order of this PrepaymentOperation.
        :type: int
        """

        self._id_order = id_order

    @property
    def amount(self):
        """
        Gets the amount of this PrepaymentOperation.

        :return: The amount of this PrepaymentOperation.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PrepaymentOperation.

        :param amount: The amount of this PrepaymentOperation.
        :type: float
        """

        self._amount = amount

    @property
    def type(self):
        """
        Gets the type of this PrepaymentOperation.

        :return: The type of this PrepaymentOperation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PrepaymentOperation.

        :param type: The type of this PrepaymentOperation.
        :type: str
        """

        self._type = type

    @property
    def date_add(self):
        """
        Gets the date_add of this PrepaymentOperation.

        :return: The date_add of this PrepaymentOperation.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this PrepaymentOperation.

        :param date_add: The date_add of this PrepaymentOperation.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this PrepaymentOperation.

        :return: The date_upd of this PrepaymentOperation.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this PrepaymentOperation.

        :param date_upd: The date_upd of this PrepaymentOperation.
        :type: str
        """

        self._date_upd = date_upd

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
