# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.6
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Endpoint(object):
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
        'bucket': 'str',
        'credential': 'str',
        'id': 'int',
        'identity': 'str',
        'protocol': 'str',
        'public_access_read_all_blobs': 'bool'
    }

    attribute_map = {
        'bucket': 'bucket',
        'credential': 'credential',
        'id': 'id',
        'identity': 'identity',
        'protocol': 'protocol',
        'public_access_read_all_blobs': 'publicAccessReadAllBlobs'
    }

    def __init__(self, bucket=None, credential=None, id=None, identity=None, protocol=None, public_access_read_all_blobs=None):  # noqa: E501
        """Endpoint - a model defined in Swagger"""  # noqa: E501

        self._bucket = None
        self._credential = None
        self._id = None
        self._identity = None
        self._protocol = None
        self._public_access_read_all_blobs = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if credential is not None:
            self.credential = credential
        if id is not None:
            self.id = id
        if identity is not None:
            self.identity = identity
        if protocol is not None:
            self.protocol = protocol
        if public_access_read_all_blobs is not None:
            self.public_access_read_all_blobs = public_access_read_all_blobs

    @property
    def bucket(self):
        """Gets the bucket of this Endpoint.  # noqa: E501

        Backet name  # noqa: E501

        :return: The bucket of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this Endpoint.

        Backet name  # noqa: E501

        :param bucket: The bucket of this Endpoint.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def credential(self):
        """Gets the credential of this Endpoint.  # noqa: E501

        Storage Credential (Secret Key)  # noqa: E501

        :return: The credential of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this Endpoint.

        Storage Credential (Secret Key)  # noqa: E501

        :param credential: The credential of this Endpoint.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def id(self):
        """Gets the id of this Endpoint.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this Endpoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Endpoint.

        Id  # noqa: E501

        :param id: The id of this Endpoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identity(self):
        """Gets the identity of this Endpoint.  # noqa: E501

        Storage Identity (Access Key)  # noqa: E501

        :return: The identity of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this Endpoint.

        Storage Identity (Access Key)  # noqa: E501

        :param identity: The identity of this Endpoint.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def protocol(self):
        """Gets the protocol of this Endpoint.  # noqa: E501

        Storage Protocol  # noqa: E501

        :return: The protocol of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Endpoint.

        Storage Protocol  # noqa: E501

        :param protocol: The protocol of this Endpoint.  # noqa: E501
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
    def public_access_read_all_blobs(self):
        """Gets the public_access_read_all_blobs of this Endpoint.  # noqa: E501

        Public read access for all objects  # noqa: E501

        :return: The public_access_read_all_blobs of this Endpoint.  # noqa: E501
        :rtype: bool
        """
        return self._public_access_read_all_blobs

    @public_access_read_all_blobs.setter
    def public_access_read_all_blobs(self, public_access_read_all_blobs):
        """Sets the public_access_read_all_blobs of this Endpoint.

        Public read access for all objects  # noqa: E501

        :param public_access_read_all_blobs: The public_access_read_all_blobs of this Endpoint.  # noqa: E501
        :type: bool
        """

        self._public_access_read_all_blobs = public_access_read_all_blobs

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
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
