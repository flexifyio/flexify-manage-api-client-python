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

from swagger_client.io.flexify.apiclient.model.money import Money  # noqa: F401,E501


class Payment(object):
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
        'amount': 'Money',
        'comments': 'str',
        'entry_mode': 'str',
        'method': 'str',
        'payment_date': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'comments': 'comments',
        'entry_mode': 'entryMode',
        'method': 'method',
        'payment_date': 'paymentDate'
    }

    def __init__(self, amount=None, comments=None, entry_mode=None, method=None, payment_date=None):  # noqa: E501
        """Payment - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._comments = None
        self._entry_mode = None
        self._method = None
        self._payment_date = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if comments is not None:
            self.comments = comments
        if entry_mode is not None:
            self.entry_mode = entry_mode
        if method is not None:
            self.method = method
        if payment_date is not None:
            self.payment_date = payment_date

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501

        Payment amount  # noqa: E501

        :return: The amount of this Payment.  # noqa: E501
        :rtype: Money
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.

        Payment amount  # noqa: E501

        :param amount: The amount of this Payment.  # noqa: E501
        :type: Money
        """

        self._amount = amount

    @property
    def comments(self):
        """Gets the comments of this Payment.  # noqa: E501

        Payment comments (will be shown to the customer)  # noqa: E501

        :return: The comments of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Payment.

        Payment comments (will be shown to the customer)  # noqa: E501

        :param comments: The comments of this Payment.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def entry_mode(self):
        """Gets the entry_mode of this Payment.  # noqa: E501

        Payment entry mode (automatic or manual)  # noqa: E501

        :return: The entry_mode of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._entry_mode

    @entry_mode.setter
    def entry_mode(self, entry_mode):
        """Sets the entry_mode of this Payment.

        Payment entry mode (automatic or manual)  # noqa: E501

        :param entry_mode: The entry_mode of this Payment.  # noqa: E501
        :type: str
        """
        allowed_values = ["MANUAL", "AUTOMATIC"]  # noqa: E501
        if entry_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `entry_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(entry_mode, allowed_values)
            )

        self._entry_mode = entry_mode

    @property
    def method(self):
        """Gets the method of this Payment.  # noqa: E501

        Payment method  # noqa: E501

        :return: The method of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Payment.

        Payment method  # noqa: E501

        :param method: The method of this Payment.  # noqa: E501
        :type: str
        """
        allowed_values = ["CASH", "WIRE_TRANSFER", "PAYMENT_GATEWAY", "ADJUSTMENT"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def payment_date(self):
        """Gets the payment_date of this Payment.  # noqa: E501

        Payment date  # noqa: E501

        :return: The payment_date of this Payment.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this Payment.

        Payment date  # noqa: E501

        :param payment_date: The payment_date of this Payment.  # noqa: E501
        :type: datetime
        """

        self._payment_date = payment_date

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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
