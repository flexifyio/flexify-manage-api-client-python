# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VirtualBucket(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'settings': 'VirtualBucketSettings',
        'storages': 'list[VirtualBucketStorageRes]'
    }

    attribute_map = {
        'settings': 'settings',
        'storages': 'storages'
    }

    def __init__(self, settings=None, storages=None):  # noqa: E501
        """VirtualBucket - a model defined in Swagger"""  # noqa: E501

        self._settings = None
        self._storages = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        self.storages = storages

    @property
    def settings(self):
        """Gets the settings of this VirtualBucket.  # noqa: E501

        Settings of the virtual bucket (name, etc.)  # noqa: E501

        :return: The settings of this VirtualBucket.  # noqa: E501
        :rtype: VirtualBucketSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this VirtualBucket.

        Settings of the virtual bucket (name, etc.)  # noqa: E501

        :param settings: The settings of this VirtualBucket.  # noqa: E501
        :type: VirtualBucketSettings
        """

        self._settings = settings

    @property
    def storages(self):
        """Gets the storages of this VirtualBucket.  # noqa: E501

        List of storages mapped to this virtual bucket  # noqa: E501

        :return: The storages of this VirtualBucket.  # noqa: E501
        :rtype: list[VirtualBucketStorageRes]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """Sets the storages of this VirtualBucket.

        List of storages mapped to this virtual bucket  # noqa: E501

        :param storages: The storages of this VirtualBucket.  # noqa: E501
        :type: list[VirtualBucketStorageRes]
        """
        if storages is None:
            raise ValueError("Invalid value for `storages`, must not be `None`")  # noqa: E501

        self._storages = storages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(VirtualBucket, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VirtualBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
