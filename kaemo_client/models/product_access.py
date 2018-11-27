# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.63
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAccess(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_customer=None, id_product=None, id_product_attribute=None, type=None, date_add=None, date_exp=None, cancel=None, recurring=None, active=None, message=None, id_order=None):
        """
        ProductAccess - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_customer': 'int',
            'id_product': 'int',
            'id_product_attribute': 'int',
            'type': 'str',
            'date_add': 'str',
            'date_exp': 'str',
            'cancel': 'int',
            'recurring': 'int',
            'active': 'int',
            'message': 'str',
            'id_order': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'id_customer': 'id_customer',
            'id_product': 'id_product',
            'id_product_attribute': 'id_product_attribute',
            'type': 'type',
            'date_add': 'date_add',
            'date_exp': 'date_exp',
            'cancel': 'cancel',
            'recurring': 'recurring',
            'active': 'active',
            'message': 'message',
            'id_order': 'id_order'
        }

        self._id = id
        self._id_customer = id_customer
        self._id_product = id_product
        self._id_product_attribute = id_product_attribute
        self._type = type
        self._date_add = date_add
        self._date_exp = date_exp
        self._cancel = cancel
        self._recurring = recurring
        self._active = active
        self._message = message
        self._id_order = id_order

    @property
    def id(self):
        """
        Gets the id of this ProductAccess.

        :return: The id of this ProductAccess.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductAccess.

        :param id: The id of this ProductAccess.
        :type: int
        """

        self._id = id

    @property
    def id_customer(self):
        """
        Gets the id_customer of this ProductAccess.

        :return: The id_customer of this ProductAccess.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this ProductAccess.

        :param id_customer: The id_customer of this ProductAccess.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_product(self):
        """
        Gets the id_product of this ProductAccess.

        :return: The id_product of this ProductAccess.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this ProductAccess.

        :param id_product: The id_product of this ProductAccess.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this ProductAccess.

        :return: The id_product_attribute of this ProductAccess.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this ProductAccess.

        :param id_product_attribute: The id_product_attribute of this ProductAccess.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def type(self):
        """
        Gets the type of this ProductAccess.

        :return: The type of this ProductAccess.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductAccess.

        :param type: The type of this ProductAccess.
        :type: str
        """

        self._type = type

    @property
    def date_add(self):
        """
        Gets the date_add of this ProductAccess.

        :return: The date_add of this ProductAccess.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this ProductAccess.

        :param date_add: The date_add of this ProductAccess.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_exp(self):
        """
        Gets the date_exp of this ProductAccess.

        :return: The date_exp of this ProductAccess.
        :rtype: str
        """
        return self._date_exp

    @date_exp.setter
    def date_exp(self, date_exp):
        """
        Sets the date_exp of this ProductAccess.

        :param date_exp: The date_exp of this ProductAccess.
        :type: str
        """

        self._date_exp = date_exp

    @property
    def cancel(self):
        """
        Gets the cancel of this ProductAccess.

        :return: The cancel of this ProductAccess.
        :rtype: int
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """
        Sets the cancel of this ProductAccess.

        :param cancel: The cancel of this ProductAccess.
        :type: int
        """

        self._cancel = cancel

    @property
    def recurring(self):
        """
        Gets the recurring of this ProductAccess.

        :return: The recurring of this ProductAccess.
        :rtype: int
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """
        Sets the recurring of this ProductAccess.

        :param recurring: The recurring of this ProductAccess.
        :type: int
        """

        self._recurring = recurring

    @property
    def active(self):
        """
        Gets the active of this ProductAccess.

        :return: The active of this ProductAccess.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductAccess.

        :param active: The active of this ProductAccess.
        :type: int
        """

        self._active = active

    @property
    def message(self):
        """
        Gets the message of this ProductAccess.

        :return: The message of this ProductAccess.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ProductAccess.

        :param message: The message of this ProductAccess.
        :type: str
        """

        self._message = message

    @property
    def id_order(self):
        """
        Gets the id_order of this ProductAccess.

        :return: The id_order of this ProductAccess.
        :rtype: int
        """
        return self._id_order

    @id_order.setter
    def id_order(self, id_order):
        """
        Sets the id_order of this ProductAccess.

        :param id_order: The id_order of this ProductAccess.
        :type: int
        """

        self._id_order = id_order

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
