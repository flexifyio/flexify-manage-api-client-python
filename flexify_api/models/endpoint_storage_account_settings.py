# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1.h1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EndpointStorageAccountSettings(object):
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
        'create_new_buckets_in': 'str',
        'put_objects': 'bool'
    }

    attribute_map = {
        'create_new_buckets_in': 'createNewBucketsIn',
        'put_objects': 'putObjects'
    }

    def __init__(self, create_new_buckets_in=None, put_objects=None):  # noqa: E501
        """EndpointStorageAccountSettings - a model defined in Swagger"""  # noqa: E501

        self._create_new_buckets_in = None
        self._put_objects = None
        self.discriminator = None

        if create_new_buckets_in is not None:
            self.create_new_buckets_in = create_new_buckets_in
        if put_objects is not None:
            self.put_objects = put_objects

    @property
    def create_new_buckets_in(self):
        """Gets the create_new_buckets_in of this EndpointStorageAccountSettings.  # noqa: E501

        Region where new buckets will be created if not specified in request. Set to null to create new buckets in a default region.  # noqa: E501

        :return: The create_new_buckets_in of this EndpointStorageAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._create_new_buckets_in

    @create_new_buckets_in.setter
    def create_new_buckets_in(self, create_new_buckets_in):
        """Sets the create_new_buckets_in of this EndpointStorageAccountSettings.

        Region where new buckets will be created if not specified in request. Set to null to create new buckets in a default region.  # noqa: E501

        :param create_new_buckets_in: The create_new_buckets_in of this EndpointStorageAccountSettings.  # noqa: E501
        :type: str
        """

        self._create_new_buckets_in = create_new_buckets_in

    @property
    def put_objects(self):
        """Gets the put_objects of this EndpointStorageAccountSettings.  # noqa: E501

        Save new data to this storage account  # noqa: E501

        :return: The put_objects of this EndpointStorageAccountSettings.  # noqa: E501
        :rtype: bool
        """
        return self._put_objects

    @put_objects.setter
    def put_objects(self, put_objects):
        """Sets the put_objects of this EndpointStorageAccountSettings.

        Save new data to this storage account  # noqa: E501

        :param put_objects: The put_objects of this EndpointStorageAccountSettings.  # noqa: E501
        :type: bool
        """

        self._put_objects = put_objects

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
        if issubclass(EndpointStorageAccountSettings, dict):
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
        if not isinstance(other, EndpointStorageAccountSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
