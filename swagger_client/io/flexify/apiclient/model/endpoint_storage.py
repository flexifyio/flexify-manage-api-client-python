# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.4.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EndpointStorage(object):
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
        'id': 'int',
        'is_default': 'bool',
        'storage_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'is_default': 'isDefault',
        'storage_id': 'storageId'
    }

    def __init__(self, id=None, is_default=None, storage_id=None):  # noqa: E501
        """EndpointStorage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._is_default = None
        self._storage_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if storage_id is not None:
            self.storage_id = storage_id

    @property
    def id(self):
        """Gets the id of this EndpointStorage.  # noqa: E501

        Endpoint Storage Id  # noqa: E501

        :return: The id of this EndpointStorage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointStorage.

        Endpoint Storage Id  # noqa: E501

        :param id: The id of this EndpointStorage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_default(self):
        """Gets the is_default of this EndpointStorage.  # noqa: E501

        Default storage for endpoint  # noqa: E501

        :return: The is_default of this EndpointStorage.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this EndpointStorage.

        Default storage for endpoint  # noqa: E501

        :param is_default: The is_default of this EndpointStorage.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def storage_id(self):
        """Gets the storage_id of this EndpointStorage.  # noqa: E501

        Storage Id  # noqa: E501

        :return: The storage_id of this EndpointStorage.  # noqa: E501
        :rtype: int
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this EndpointStorage.

        Storage Id  # noqa: E501

        :param storage_id: The storage_id of this EndpointStorage.  # noqa: E501
        :type: int
        """

        self._storage_id = storage_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EndpointStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
