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


class StorageProvider(object):
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
        'disabled_as_destination': 'bool',
        'endpoint': 'str',
        'id': 'int',
        'name': 'str',
        'port_http': 'int',
        'port_https': 'int',
        'product_name': 'str',
        'protocol': 'str',
        'supports_http': 'bool',
        'supports_https': 'bool'
    }

    attribute_map = {
        'disabled_as_destination': 'disabledAsDestination',
        'endpoint': 'endpoint',
        'id': 'id',
        'name': 'name',
        'port_http': 'portHttp',
        'port_https': 'portHttps',
        'product_name': 'productName',
        'protocol': 'protocol',
        'supports_http': 'supportsHttp',
        'supports_https': 'supportsHttps'
    }

    def __init__(self, disabled_as_destination=None, endpoint=None, id=None, name=None, port_http=None, port_https=None, product_name=None, protocol=None, supports_http=None, supports_https=None):  # noqa: E501
        """StorageProvider - a model defined in Swagger"""  # noqa: E501

        self._disabled_as_destination = None
        self._endpoint = None
        self._id = None
        self._name = None
        self._port_http = None
        self._port_https = None
        self._product_name = None
        self._protocol = None
        self._supports_http = None
        self._supports_https = None
        self.discriminator = None

        if disabled_as_destination is not None:
            self.disabled_as_destination = disabled_as_destination
        if endpoint is not None:
            self.endpoint = endpoint
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if port_http is not None:
            self.port_http = port_http
        if port_https is not None:
            self.port_https = port_https
        if product_name is not None:
            self.product_name = product_name
        if protocol is not None:
            self.protocol = protocol
        if supports_http is not None:
            self.supports_http = supports_http
        if supports_https is not None:
            self.supports_https = supports_https

    @property
    def disabled_as_destination(self):
        """Gets the disabled_as_destination of this StorageProvider.  # noqa: E501

        Storage is not allowed to be used as a default storage in endpoint or as a migration destination)  # noqa: E501

        :return: The disabled_as_destination of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._disabled_as_destination

    @disabled_as_destination.setter
    def disabled_as_destination(self, disabled_as_destination):
        """Sets the disabled_as_destination of this StorageProvider.

        Storage is not allowed to be used as a default storage in endpoint or as a migration destination)  # noqa: E501

        :param disabled_as_destination: The disabled_as_destination of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._disabled_as_destination = disabled_as_destination

    @property
    def endpoint(self):
        """Gets the endpoint of this StorageProvider.  # noqa: E501

        Endpoint to access this provider or null for custom providers  # noqa: E501

        :return: The endpoint of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this StorageProvider.

        Endpoint to access this provider or null for custom providers  # noqa: E501

        :param endpoint: The endpoint of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def id(self):
        """Gets the id of this StorageProvider.  # noqa: E501

        Id of the provider in the system  # noqa: E501

        :return: The id of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageProvider.

        Id of the provider in the system  # noqa: E501

        :param id: The id of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StorageProvider.  # noqa: E501

        Name of the provider  # noqa: E501

        :return: The name of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageProvider.

        Name of the provider  # noqa: E501

        :param name: The name of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port_http(self):
        """Gets the port_http of this StorageProvider.  # noqa: E501

        Port for HTTP request (null for default 80)  # noqa: E501

        :return: The port_http of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._port_http

    @port_http.setter
    def port_http(self, port_http):
        """Sets the port_http of this StorageProvider.

        Port for HTTP request (null for default 80)  # noqa: E501

        :param port_http: The port_http of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._port_http = port_http

    @property
    def port_https(self):
        """Gets the port_https of this StorageProvider.  # noqa: E501

        Port for HTTPS request (null for default 443)  # noqa: E501

        :return: The port_https of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._port_https

    @port_https.setter
    def port_https(self, port_https):
        """Sets the port_https of this StorageProvider.

        Port for HTTPS request (null for default 443)  # noqa: E501

        :param port_https: The port_https of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._port_https = port_https

    @property
    def product_name(self):
        """Gets the product_name of this StorageProvider.  # noqa: E501

        Name of product/region for this provider  # noqa: E501

        :return: The product_name of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this StorageProvider.

        Name of product/region for this provider  # noqa: E501

        :param product_name: The product_name of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def protocol(self):
        """Gets the protocol of this StorageProvider.  # noqa: E501

        Storage protocol this provider uses  # noqa: E501

        :return: The protocol of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this StorageProvider.

        Storage protocol this provider uses  # noqa: E501

        :param protocol: The protocol of this StorageProvider.  # noqa: E501
        :type: str
        """
        allowed_values = ["S3", "AZURE", "GOOGLE", "OPENSTACK", "RACKSPACE"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def supports_http(self):
        """Gets the supports_http of this StorageProvider.  # noqa: E501

        Indicates that HTTP is supported  # noqa: E501

        :return: The supports_http of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_http

    @supports_http.setter
    def supports_http(self, supports_http):
        """Sets the supports_http of this StorageProvider.

        Indicates that HTTP is supported  # noqa: E501

        :param supports_http: The supports_http of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_http = supports_http

    @property
    def supports_https(self):
        """Gets the supports_https of this StorageProvider.  # noqa: E501

        Indicates that HTTPS (SSL) is supported  # noqa: E501

        :return: The supports_https of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_https

    @supports_https.setter
    def supports_https(self, supports_https):
        """Sets the supports_https of this StorageProvider.

        Indicates that HTTPS (SSL) is supported  # noqa: E501

        :param supports_https: The supports_https of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_https = supports_https

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
        if not isinstance(other, StorageProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
