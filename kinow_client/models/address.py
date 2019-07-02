# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Address(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_customer=None, id_country=None, id_state=None, company=None, vat_number=None, address1=None, postcode=None, city=None, date_add=None, date_upd=None, firstname=None, lastname=None):
        """
        Address - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_customer': 'int',
            'id_country': 'int',
            'id_state': 'int',
            'company': 'str',
            'vat_number': 'str',
            'address1': 'str',
            'postcode': 'str',
            'city': 'str',
            'date_add': 'str',
            'date_upd': 'str',
            'firstname': 'str',
            'lastname': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_customer': 'id_customer',
            'id_country': 'id_country',
            'id_state': 'id_state',
            'company': 'company',
            'vat_number': 'vat_number',
            'address1': 'address1',
            'postcode': 'postcode',
            'city': 'city',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'firstname': 'firstname',
            'lastname': 'lastname'
        }

        self._id = id
        self._id_customer = id_customer
        self._id_country = id_country
        self._id_state = id_state
        self._company = company
        self._vat_number = vat_number
        self._address1 = address1
        self._postcode = postcode
        self._city = city
        self._date_add = date_add
        self._date_upd = date_upd
        self._firstname = firstname
        self._lastname = lastname

    @property
    def id(self):
        """
        Gets the id of this Address.

        :return: The id of this Address.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Address.

        :param id: The id of this Address.
        :type: int
        """

        self._id = id

    @property
    def id_customer(self):
        """
        Gets the id_customer of this Address.

        :return: The id_customer of this Address.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this Address.

        :param id_customer: The id_customer of this Address.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_country(self):
        """
        Gets the id_country of this Address.

        :return: The id_country of this Address.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this Address.

        :param id_country: The id_country of this Address.
        :type: int
        """

        self._id_country = id_country

    @property
    def id_state(self):
        """
        Gets the id_state of this Address.

        :return: The id_state of this Address.
        :rtype: int
        """
        return self._id_state

    @id_state.setter
    def id_state(self, id_state):
        """
        Sets the id_state of this Address.

        :param id_state: The id_state of this Address.
        :type: int
        """

        self._id_state = id_state

    @property
    def company(self):
        """
        Gets the company of this Address.

        :return: The company of this Address.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Address.

        :param company: The company of this Address.
        :type: str
        """

        self._company = company

    @property
    def vat_number(self):
        """
        Gets the vat_number of this Address.

        :return: The vat_number of this Address.
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """
        Sets the vat_number of this Address.

        :param vat_number: The vat_number of this Address.
        :type: str
        """

        self._vat_number = vat_number

    @property
    def address1(self):
        """
        Gets the address1 of this Address.

        :return: The address1 of this Address.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Address.

        :param address1: The address1 of this Address.
        :type: str
        """

        self._address1 = address1

    @property
    def postcode(self):
        """
        Gets the postcode of this Address.

        :return: The postcode of this Address.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this Address.

        :param postcode: The postcode of this Address.
        :type: str
        """

        self._postcode = postcode

    @property
    def city(self):
        """
        Gets the city of this Address.

        :return: The city of this Address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Address.

        :param city: The city of this Address.
        :type: str
        """

        self._city = city

    @property
    def date_add(self):
        """
        Gets the date_add of this Address.

        :return: The date_add of this Address.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Address.

        :param date_add: The date_add of this Address.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Address.

        :return: The date_upd of this Address.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Address.

        :param date_upd: The date_upd of this Address.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def firstname(self):
        """
        Gets the firstname of this Address.

        :return: The firstname of this Address.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Address.

        :param firstname: The firstname of this Address.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this Address.

        :return: The lastname of this Address.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Address.

        :param lastname: The lastname of this Address.
        :type: str
        """

        self._lastname = lastname

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
