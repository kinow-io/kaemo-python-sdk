# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.60
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SessionVideoStat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, customer_id=None, video_id=None, date=None, iso_code=None, watched_time=None, watched_number=None, played_number=None):
        """
        SessionVideoStat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'customer_id': 'int',
            'video_id': 'int',
            'date': 'str',
            'iso_code': 'str',
            'watched_time': 'float',
            'watched_number': 'int',
            'played_number': 'int'
        }

        self.attribute_map = {
            'customer_id': 'customer_id',
            'video_id': 'video_id',
            'date': 'date',
            'iso_code': 'iso_code',
            'watched_time': 'watched_time',
            'watched_number': 'watched_number',
            'played_number': 'played_number'
        }

        self._customer_id = customer_id
        self._video_id = video_id
        self._date = date
        self._iso_code = iso_code
        self._watched_time = watched_time
        self._watched_number = watched_number
        self._played_number = played_number

    @property
    def customer_id(self):
        """
        Gets the customer_id of this SessionVideoStat.
        

        :return: The customer_id of this SessionVideoStat.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this SessionVideoStat.
        

        :param customer_id: The customer_id of this SessionVideoStat.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def video_id(self):
        """
        Gets the video_id of this SessionVideoStat.
        

        :return: The video_id of this SessionVideoStat.
        :rtype: int
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this SessionVideoStat.
        

        :param video_id: The video_id of this SessionVideoStat.
        :type: int
        """

        self._video_id = video_id

    @property
    def date(self):
        """
        Gets the date of this SessionVideoStat.
        

        :return: The date of this SessionVideoStat.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this SessionVideoStat.
        

        :param date: The date of this SessionVideoStat.
        :type: str
        """

        self._date = date

    @property
    def iso_code(self):
        """
        Gets the iso_code of this SessionVideoStat.
        

        :return: The iso_code of this SessionVideoStat.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this SessionVideoStat.
        

        :param iso_code: The iso_code of this SessionVideoStat.
        :type: str
        """

        self._iso_code = iso_code

    @property
    def watched_time(self):
        """
        Gets the watched_time of this SessionVideoStat.
        

        :return: The watched_time of this SessionVideoStat.
        :rtype: float
        """
        return self._watched_time

    @watched_time.setter
    def watched_time(self, watched_time):
        """
        Sets the watched_time of this SessionVideoStat.
        

        :param watched_time: The watched_time of this SessionVideoStat.
        :type: float
        """

        self._watched_time = watched_time

    @property
    def watched_number(self):
        """
        Gets the watched_number of this SessionVideoStat.
        

        :return: The watched_number of this SessionVideoStat.
        :rtype: int
        """
        return self._watched_number

    @watched_number.setter
    def watched_number(self, watched_number):
        """
        Sets the watched_number of this SessionVideoStat.
        

        :param watched_number: The watched_number of this SessionVideoStat.
        :type: int
        """

        self._watched_number = watched_number

    @property
    def played_number(self):
        """
        Gets the played_number of this SessionVideoStat.
        

        :return: The played_number of this SessionVideoStat.
        :rtype: int
        """
        return self._played_number

    @played_number.setter
    def played_number(self, played_number):
        """
        Sets the played_number of this SessionVideoStat.
        

        :param played_number: The played_number of this SessionVideoStat.
        :type: int
        """

        self._played_number = played_number

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
