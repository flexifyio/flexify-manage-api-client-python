# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Distributor(object):
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
        'name': 'str',
        'pay_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pay_url': 'payUrl'
    }

    def __init__(self, id=None, name=None, pay_url=None):  # noqa: E501
        """Distributor - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._pay_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if pay_url is not None:
            self.pay_url = pay_url

    @property
    def id(self):
        """Gets the id of this Distributor.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this Distributor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Distributor.

        Id  # noqa: E501

        :param id: The id of this Distributor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Distributor.  # noqa: E501

        Name of the distributor  # noqa: E501

        :return: The name of this Distributor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Distributor.

        Name of the distributor  # noqa: E501

        :param name: The name of this Distributor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pay_url(self):
        """Gets the pay_url of this Distributor.  # noqa: E501

        URL where user should be redirected for paymnet  # noqa: E501

        :return: The pay_url of this Distributor.  # noqa: E501
        :rtype: str
        """
        return self._pay_url

    @pay_url.setter
    def pay_url(self, pay_url):
        """Sets the pay_url of this Distributor.

        URL where user should be redirected for paymnet  # noqa: E501

        :param pay_url: The pay_url of this Distributor.  # noqa: E501
        :type: str
        """

        self._pay_url = pay_url

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
        if issubclass(Distributor, dict):
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
        if not isinstance(other, Distributor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
