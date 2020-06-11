# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.73
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoAccessInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_video=None, streaming=None, download=None, maximum_watched=None, maximum_viewing=None, quality_hd=None, quality_sd=None, expires=None, play_duration=None):
        """
        VideoAccessInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_video': 'float',
            'streaming': 'bool',
            'download': 'bool',
            'maximum_watched': 'bool',
            'maximum_viewing': 'bool',
            'quality_hd': 'bool',
            'quality_sd': 'bool',
            'expires': 'str',
            'play_duration': 'float'
        }

        self.attribute_map = {
            'id_video': 'id_video',
            'streaming': 'streaming',
            'download': 'download',
            'maximum_watched': 'maximum_watched',
            'maximum_viewing': 'maximum_viewing',
            'quality_hd': 'quality_hd',
            'quality_sd': 'quality_sd',
            'expires': 'expires',
            'play_duration': 'play_duration'
        }

        self._id_video = id_video
        self._streaming = streaming
        self._download = download
        self._maximum_watched = maximum_watched
        self._maximum_viewing = maximum_viewing
        self._quality_hd = quality_hd
        self._quality_sd = quality_sd
        self._expires = expires
        self._play_duration = play_duration

    @property
    def id_video(self):
        """
        Gets the id_video of this VideoAccessInfo.
        

        :return: The id_video of this VideoAccessInfo.
        :rtype: float
        """
        return self._id_video

    @id_video.setter
    def id_video(self, id_video):
        """
        Sets the id_video of this VideoAccessInfo.
        

        :param id_video: The id_video of this VideoAccessInfo.
        :type: float
        """

        self._id_video = id_video

    @property
    def streaming(self):
        """
        Gets the streaming of this VideoAccessInfo.
        

        :return: The streaming of this VideoAccessInfo.
        :rtype: bool
        """
        return self._streaming

    @streaming.setter
    def streaming(self, streaming):
        """
        Sets the streaming of this VideoAccessInfo.
        

        :param streaming: The streaming of this VideoAccessInfo.
        :type: bool
        """

        self._streaming = streaming

    @property
    def download(self):
        """
        Gets the download of this VideoAccessInfo.
        

        :return: The download of this VideoAccessInfo.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this VideoAccessInfo.
        

        :param download: The download of this VideoAccessInfo.
        :type: bool
        """

        self._download = download

    @property
    def maximum_watched(self):
        """
        Gets the maximum_watched of this VideoAccessInfo.
        

        :return: The maximum_watched of this VideoAccessInfo.
        :rtype: bool
        """
        return self._maximum_watched

    @maximum_watched.setter
    def maximum_watched(self, maximum_watched):
        """
        Sets the maximum_watched of this VideoAccessInfo.
        

        :param maximum_watched: The maximum_watched of this VideoAccessInfo.
        :type: bool
        """

        self._maximum_watched = maximum_watched

    @property
    def maximum_viewing(self):
        """
        Gets the maximum_viewing of this VideoAccessInfo.
        

        :return: The maximum_viewing of this VideoAccessInfo.
        :rtype: bool
        """
        return self._maximum_viewing

    @maximum_viewing.setter
    def maximum_viewing(self, maximum_viewing):
        """
        Sets the maximum_viewing of this VideoAccessInfo.
        

        :param maximum_viewing: The maximum_viewing of this VideoAccessInfo.
        :type: bool
        """

        self._maximum_viewing = maximum_viewing

    @property
    def quality_hd(self):
        """
        Gets the quality_hd of this VideoAccessInfo.
        

        :return: The quality_hd of this VideoAccessInfo.
        :rtype: bool
        """
        return self._quality_hd

    @quality_hd.setter
    def quality_hd(self, quality_hd):
        """
        Sets the quality_hd of this VideoAccessInfo.
        

        :param quality_hd: The quality_hd of this VideoAccessInfo.
        :type: bool
        """

        self._quality_hd = quality_hd

    @property
    def quality_sd(self):
        """
        Gets the quality_sd of this VideoAccessInfo.
        

        :return: The quality_sd of this VideoAccessInfo.
        :rtype: bool
        """
        return self._quality_sd

    @quality_sd.setter
    def quality_sd(self, quality_sd):
        """
        Sets the quality_sd of this VideoAccessInfo.
        

        :param quality_sd: The quality_sd of this VideoAccessInfo.
        :type: bool
        """

        self._quality_sd = quality_sd

    @property
    def expires(self):
        """
        Gets the expires of this VideoAccessInfo.
        

        :return: The expires of this VideoAccessInfo.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this VideoAccessInfo.
        

        :param expires: The expires of this VideoAccessInfo.
        :type: str
        """

        self._expires = expires

    @property
    def play_duration(self):
        """
        Gets the play_duration of this VideoAccessInfo.
        

        :return: The play_duration of this VideoAccessInfo.
        :rtype: float
        """
        return self._play_duration

    @play_duration.setter
    def play_duration(self, play_duration):
        """
        Sets the play_duration of this VideoAccessInfo.
        

        :param play_duration: The play_duration of this VideoAccessInfo.
        :type: float
        """

        self._play_duration = play_duration

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
