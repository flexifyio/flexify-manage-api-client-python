# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.7-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.models.money import Money  # noqa: F401,E501
from flexify_api.models.price_list_entry import PriceListEntry  # noqa: F401,E501


class CostDetails(object):
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
        'cost': 'Money',
        'price_list_entry': 'PriceListEntry',
        'usage': 'int',
        'username': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'price_list_entry': 'priceListEntry',
        'usage': 'usage',
        'username': 'username'
    }

    def __init__(self, cost=None, price_list_entry=None, usage=None, username=None):  # noqa: E501
        """CostDetails - a model defined in Swagger"""  # noqa: E501

        self._cost = None
        self._price_list_entry = None
        self._usage = None
        self._username = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if price_list_entry is not None:
            self.price_list_entry = price_list_entry
        if usage is not None:
            self.usage = usage
        if username is not None:
            self.username = username

    @property
    def cost(self):
        """Gets the cost of this CostDetails.  # noqa: E501

        Cost  # noqa: E501

        :return: The cost of this CostDetails.  # noqa: E501
        :rtype: Money
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this CostDetails.

        Cost  # noqa: E501

        :param cost: The cost of this CostDetails.  # noqa: E501
        :type: Money
        """

        self._cost = cost

    @property
    def price_list_entry(self):
        """Gets the price_list_entry of this CostDetails.  # noqa: E501

        Price List Entry  # noqa: E501

        :return: The price_list_entry of this CostDetails.  # noqa: E501
        :rtype: PriceListEntry
        """
        return self._price_list_entry

    @price_list_entry.setter
    def price_list_entry(self, price_list_entry):
        """Sets the price_list_entry of this CostDetails.

        Price List Entry  # noqa: E501

        :param price_list_entry: The price_list_entry of this CostDetails.  # noqa: E501
        :type: PriceListEntry
        """

        self._price_list_entry = price_list_entry

    @property
    def usage(self):
        """Gets the usage of this CostDetails.  # noqa: E501

        Usage in bytes  # noqa: E501

        :return: The usage of this CostDetails.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this CostDetails.

        Usage in bytes  # noqa: E501

        :param usage: The usage of this CostDetails.  # noqa: E501
        :type: int
        """

        self._usage = usage

    @property
    def username(self):
        """Gets the username of this CostDetails.  # noqa: E501

        Username  # noqa: E501

        :return: The username of this CostDetails.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CostDetails.

        Username  # noqa: E501

        :param username: The username of this CostDetails.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, CostDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
