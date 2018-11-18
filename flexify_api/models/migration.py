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

from flexify_api.models.mapping import Mapping  # noqa: F401,E501
from flexify_api.models.migration_settings import MigrationSettings  # noqa: F401,E501
from flexify_api.models.migration_stat import MigrationStat  # noqa: F401,E501


class Migration(object):
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
        'hidden': 'bool',
        'id': 'int',
        'mappings': 'list[Mapping]',
        'settings': 'MigrationSettings',
        'stat': 'MigrationStat'
    }

    attribute_map = {
        'hidden': 'hidden',
        'id': 'id',
        'mappings': 'mappings',
        'settings': 'settings',
        'stat': 'stat'
    }

    def __init__(self, hidden=None, id=None, mappings=None, settings=None, stat=None):  # noqa: E501
        """Migration - a model defined in Swagger"""  # noqa: E501

        self._hidden = None
        self._id = None
        self._mappings = None
        self._settings = None
        self._stat = None
        self.discriminator = None

        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if mappings is not None:
            self.mappings = mappings
        if settings is not None:
            self.settings = settings
        if stat is not None:
            self.stat = stat

    @property
    def hidden(self):
        """Gets the hidden of this Migration.  # noqa: E501

        Indicates that his migration should not be show in UI  # noqa: E501

        :return: The hidden of this Migration.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Migration.

        Indicates that his migration should not be show in UI  # noqa: E501

        :param hidden: The hidden of this Migration.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this Migration.  # noqa: E501

        Unique ID  # noqa: E501

        :return: The id of this Migration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Migration.

        Unique ID  # noqa: E501

        :param id: The id of this Migration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mappings(self):
        """Gets the mappings of this Migration.  # noqa: E501

        Source to destination storages mappings  # noqa: E501

        :return: The mappings of this Migration.  # noqa: E501
        :rtype: list[Mapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this Migration.

        Source to destination storages mappings  # noqa: E501

        :param mappings: The mappings of this Migration.  # noqa: E501
        :type: list[Mapping]
        """

        self._mappings = mappings

    @property
    def settings(self):
        """Gets the settings of this Migration.  # noqa: E501

        Migration settings  # noqa: E501

        :return: The settings of this Migration.  # noqa: E501
        :rtype: MigrationSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Migration.

        Migration settings  # noqa: E501

        :param settings: The settings of this Migration.  # noqa: E501
        :type: MigrationSettings
        """

        self._settings = settings

    @property
    def stat(self):
        """Gets the stat of this Migration.  # noqa: E501

        Comulative migration statistics  # noqa: E501

        :return: The stat of this Migration.  # noqa: E501
        :rtype: MigrationStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this Migration.

        Comulative migration statistics  # noqa: E501

        :param stat: The stat of this Migration.  # noqa: E501
        :type: MigrationStat
        """

        self._stat = stat

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
        if not isinstance(other, Migration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
