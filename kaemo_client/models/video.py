# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Video(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_product=None, id_language=None, language_filter=None, id_media_source=None, name=None, description=None, duration=None, filename=None, position=None, subscription=None, free=None, download=None, active=None, date_add=None, date_upd=None):
        """
        Video - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_product': 'int',
            'id_language': 'int',
            'language_filter': 'int',
            'id_media_source': 'int',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'duration': 'int',
            'filename': 'str',
            'position': 'int',
            'subscription': 'int',
            'free': 'int',
            'download': 'int',
            'active': 'bool',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_product': 'id_product',
            'id_language': 'id_language',
            'language_filter': 'language_filter',
            'id_media_source': 'id_media_source',
            'name': 'name',
            'description': 'description',
            'duration': 'duration',
            'filename': 'filename',
            'position': 'position',
            'subscription': 'subscription',
            'free': 'free',
            'download': 'download',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_product = id_product
        self._id_language = id_language
        self._language_filter = language_filter
        self._id_media_source = id_media_source
        self._name = name
        self._description = description
        self._duration = duration
        self._filename = filename
        self._position = position
        self._subscription = subscription
        self._free = free
        self._download = download
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this Video.

        :return: The id of this Video.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Video.

        :param id: The id of this Video.
        :type: int
        """

        self._id = id

    @property
    def id_product(self):
        """
        Gets the id_product of this Video.

        :return: The id_product of this Video.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this Video.

        :param id_product: The id_product of this Video.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_language(self):
        """
        Gets the id_language of this Video.

        :return: The id_language of this Video.
        :rtype: int
        """
        return self._id_language

    @id_language.setter
    def id_language(self, id_language):
        """
        Sets the id_language of this Video.

        :param id_language: The id_language of this Video.
        :type: int
        """

        self._id_language = id_language

    @property
    def language_filter(self):
        """
        Gets the language_filter of this Video.

        :return: The language_filter of this Video.
        :rtype: int
        """
        return self._language_filter

    @language_filter.setter
    def language_filter(self, language_filter):
        """
        Sets the language_filter of this Video.

        :param language_filter: The language_filter of this Video.
        :type: int
        """

        self._language_filter = language_filter

    @property
    def id_media_source(self):
        """
        Gets the id_media_source of this Video.

        :return: The id_media_source of this Video.
        :rtype: int
        """
        return self._id_media_source

    @id_media_source.setter
    def id_media_source(self, id_media_source):
        """
        Sets the id_media_source of this Video.

        :param id_media_source: The id_media_source of this Video.
        :type: int
        """

        self._id_media_source = id_media_source

    @property
    def name(self):
        """
        Gets the name of this Video.

        :return: The name of this Video.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Video.

        :param name: The name of this Video.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Video.

        :return: The description of this Video.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Video.

        :param description: The description of this Video.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def duration(self):
        """
        Gets the duration of this Video.

        :return: The duration of this Video.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this Video.

        :param duration: The duration of this Video.
        :type: int
        """

        self._duration = duration

    @property
    def filename(self):
        """
        Gets the filename of this Video.

        :return: The filename of this Video.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this Video.

        :param filename: The filename of this Video.
        :type: str
        """

        self._filename = filename

    @property
    def position(self):
        """
        Gets the position of this Video.

        :return: The position of this Video.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this Video.

        :param position: The position of this Video.
        :type: int
        """

        self._position = position

    @property
    def subscription(self):
        """
        Gets the subscription of this Video.

        :return: The subscription of this Video.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this Video.

        :param subscription: The subscription of this Video.
        :type: int
        """

        self._subscription = subscription

    @property
    def free(self):
        """
        Gets the free of this Video.

        :return: The free of this Video.
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """
        Sets the free of this Video.

        :param free: The free of this Video.
        :type: int
        """

        self._free = free

    @property
    def download(self):
        """
        Gets the download of this Video.

        :return: The download of this Video.
        :rtype: int
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this Video.

        :param download: The download of this Video.
        :type: int
        """

        self._download = download

    @property
    def active(self):
        """
        Gets the active of this Video.

        :return: The active of this Video.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Video.

        :param active: The active of this Video.
        :type: bool
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this Video.

        :return: The date_add of this Video.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Video.

        :param date_add: The date_add of this Video.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Video.

        :return: The date_upd of this Video.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Video.

        :param date_upd: The date_upd of this Video.
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
