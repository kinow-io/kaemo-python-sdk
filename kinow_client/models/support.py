# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.76
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Support(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_lang=None, id_contact=None, id_customer=None, id_order=None, id_product=None, status=None, email=None, date_add=None, date_upd=None):
        """
        Support - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_lang': 'int',
            'id_contact': 'int',
            'id_customer': 'int',
            'id_order': 'int',
            'id_product': 'int',
            'status': 'str',
            'email': 'str',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_lang': 'id_lang',
            'id_contact': 'id_contact',
            'id_customer': 'id_customer',
            'id_order': 'id_order',
            'id_product': 'id_product',
            'status': 'status',
            'email': 'email',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_lang = id_lang
        self._id_contact = id_contact
        self._id_customer = id_customer
        self._id_order = id_order
        self._id_product = id_product
        self._status = status
        self._email = email
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this Support.

        :return: The id of this Support.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Support.

        :param id: The id of this Support.
        :type: int
        """

        self._id = id

    @property
    def id_lang(self):
        """
        Gets the id_lang of this Support.

        :return: The id_lang of this Support.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this Support.

        :param id_lang: The id_lang of this Support.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def id_contact(self):
        """
        Gets the id_contact of this Support.

        :return: The id_contact of this Support.
        :rtype: int
        """
        return self._id_contact

    @id_contact.setter
    def id_contact(self, id_contact):
        """
        Sets the id_contact of this Support.

        :param id_contact: The id_contact of this Support.
        :type: int
        """

        self._id_contact = id_contact

    @property
    def id_customer(self):
        """
        Gets the id_customer of this Support.

        :return: The id_customer of this Support.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this Support.

        :param id_customer: The id_customer of this Support.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_order(self):
        """
        Gets the id_order of this Support.

        :return: The id_order of this Support.
        :rtype: int
        """
        return self._id_order

    @id_order.setter
    def id_order(self, id_order):
        """
        Sets the id_order of this Support.

        :param id_order: The id_order of this Support.
        :type: int
        """

        self._id_order = id_order

    @property
    def id_product(self):
        """
        Gets the id_product of this Support.

        :return: The id_product of this Support.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this Support.

        :param id_product: The id_product of this Support.
        :type: int
        """

        self._id_product = id_product

    @property
    def status(self):
        """
        Gets the status of this Support.

        :return: The status of this Support.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Support.

        :param status: The status of this Support.
        :type: str
        """

        self._status = status

    @property
    def email(self):
        """
        Gets the email of this Support.

        :return: The email of this Support.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Support.

        :param email: The email of this Support.
        :type: str
        """

        self._email = email

    @property
    def date_add(self):
        """
        Gets the date_add of this Support.

        :return: The date_add of this Support.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Support.

        :param date_add: The date_add of this Support.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Support.

        :return: The date_upd of this Support.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Support.

        :param date_upd: The date_upd of this Support.
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
