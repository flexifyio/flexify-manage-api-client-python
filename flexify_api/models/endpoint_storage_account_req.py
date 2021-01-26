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


class EndpointStorageAccountReq(object):
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
        'settings': 'EndpointStorageAccountSettings',
        'storage_account_id': 'int'
    }

    attribute_map = {
        'settings': 'settings',
        'storage_account_id': 'storageAccountId'
    }

    def __init__(self, settings=None, storage_account_id=None):  # noqa: E501
        """EndpointStorageAccountReq - a model defined in Swagger"""  # noqa: E501

        self._settings = None
        self._storage_account_id = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        if storage_account_id is not None:
            self.storage_account_id = storage_account_id

    @property
    def settings(self):
        """Gets the settings of this EndpointStorageAccountReq.  # noqa: E501

        Attached storage account configuration  # noqa: E501

        :return: The settings of this EndpointStorageAccountReq.  # noqa: E501
        :rtype: EndpointStorageAccountSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this EndpointStorageAccountReq.

        Attached storage account configuration  # noqa: E501

        :param settings: The settings of this EndpointStorageAccountReq.  # noqa: E501
        :type: EndpointStorageAccountSettings
        """

        self._settings = settings

    @property
    def storage_account_id(self):
        """Gets the storage_account_id of this EndpointStorageAccountReq.  # noqa: E501

        Id of attached storage account  # noqa: E501

        :return: The storage_account_id of this EndpointStorageAccountReq.  # noqa: E501
        :rtype: int
        """
        return self._storage_account_id

    @storage_account_id.setter
    def storage_account_id(self, storage_account_id):
        """Sets the storage_account_id of this EndpointStorageAccountReq.

        Id of attached storage account  # noqa: E501

        :param storage_account_id: The storage_account_id of this EndpointStorageAccountReq.  # noqa: E501
        :type: int
        """

        self._storage_account_id = storage_account_id

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
        if issubclass(EndpointStorageAccountReq, dict):
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
        if not isinstance(other, EndpointStorageAccountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
