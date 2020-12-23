# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1-dev
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PaymentOptions(object):
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
        'amount_string': 'str',
        'auth_token': 'str',
        'product_id': 'int'
    }

    attribute_map = {
        'amount_string': 'amountString',
        'auth_token': 'authToken',
        'product_id': 'productId'
    }

    def __init__(self, amount_string=None, auth_token=None, product_id=None):  # noqa: E501
        """PaymentOptions - a model defined in Swagger"""  # noqa: E501

        self._amount_string = None
        self._auth_token = None
        self._product_id = None
        self.discriminator = None

        if amount_string is not None:
            self.amount_string = amount_string
        if auth_token is not None:
            self.auth_token = auth_token
        if product_id is not None:
            self.product_id = product_id

    @property
    def amount_string(self):
        """Gets the amount_string of this PaymentOptions.  # noqa: E501


        :return: The amount_string of this PaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._amount_string

    @amount_string.setter
    def amount_string(self, amount_string):
        """Sets the amount_string of this PaymentOptions.


        :param amount_string: The amount_string of this PaymentOptions.  # noqa: E501
        :type: str
        """

        self._amount_string = amount_string

    @property
    def auth_token(self):
        """Gets the auth_token of this PaymentOptions.  # noqa: E501


        :return: The auth_token of this PaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this PaymentOptions.


        :param auth_token: The auth_token of this PaymentOptions.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def product_id(self):
        """Gets the product_id of this PaymentOptions.  # noqa: E501


        :return: The product_id of this PaymentOptions.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PaymentOptions.


        :param product_id: The product_id of this PaymentOptions.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

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
        if issubclass(PaymentOptions, dict):
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
        if not isinstance(other, PaymentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
