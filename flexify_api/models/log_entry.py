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

from flexify_api.models.log_event import LogEvent  # noqa: F401,E501


class LogEntry(object):
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
        'endpoint_id': 'int',
        'engine_uuid': 'str',
        'event': 'LogEvent',
        'migration_id': 'int',
        'storage_account_id': 'int',
        'storage_id': 'int',
        'task_uuid': 'str'
    }

    attribute_map = {
        'endpoint_id': 'endpointId',
        'engine_uuid': 'engineUuid',
        'event': 'event',
        'migration_id': 'migrationId',
        'storage_account_id': 'storageAccountId',
        'storage_id': 'storageId',
        'task_uuid': 'taskUuid'
    }

    def __init__(self, endpoint_id=None, engine_uuid=None, event=None, migration_id=None, storage_account_id=None, storage_id=None, task_uuid=None):  # noqa: E501
        """LogEntry - a model defined in Swagger"""  # noqa: E501

        self._endpoint_id = None
        self._engine_uuid = None
        self._event = None
        self._migration_id = None
        self._storage_account_id = None
        self._storage_id = None
        self._task_uuid = None
        self.discriminator = None

        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if engine_uuid is not None:
            self.engine_uuid = engine_uuid
        if event is not None:
            self.event = event
        if migration_id is not None:
            self.migration_id = migration_id
        if storage_account_id is not None:
            self.storage_account_id = storage_account_id
        if storage_id is not None:
            self.storage_id = storage_id
        if task_uuid is not None:
            self.task_uuid = task_uuid

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this LogEntry.  # noqa: E501

        Flexify endpoint related to this event, if any  # noqa: E501

        :return: The endpoint_id of this LogEntry.  # noqa: E501
        :rtype: int
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this LogEntry.

        Flexify endpoint related to this event, if any  # noqa: E501

        :param endpoint_id: The endpoint_id of this LogEntry.  # noqa: E501
        :type: int
        """

        self._endpoint_id = endpoint_id

    @property
    def engine_uuid(self):
        """Gets the engine_uuid of this LogEntry.  # noqa: E501

        Engine with which this endpoint is associated  # noqa: E501

        :return: The engine_uuid of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._engine_uuid

    @engine_uuid.setter
    def engine_uuid(self, engine_uuid):
        """Sets the engine_uuid of this LogEntry.

        Engine with which this endpoint is associated  # noqa: E501

        :param engine_uuid: The engine_uuid of this LogEntry.  # noqa: E501
        :type: str
        """

        self._engine_uuid = engine_uuid

    @property
    def event(self):
        """Gets the event of this LogEntry.  # noqa: E501

        Log event  # noqa: E501

        :return: The event of this LogEntry.  # noqa: E501
        :rtype: LogEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this LogEntry.

        Log event  # noqa: E501

        :param event: The event of this LogEntry.  # noqa: E501
        :type: LogEvent
        """

        self._event = event

    @property
    def migration_id(self):
        """Gets the migration_id of this LogEntry.  # noqa: E501

        Migration related to this event, if any  # noqa: E501

        :return: The migration_id of this LogEntry.  # noqa: E501
        :rtype: int
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """Sets the migration_id of this LogEntry.

        Migration related to this event, if any  # noqa: E501

        :param migration_id: The migration_id of this LogEntry.  # noqa: E501
        :type: int
        """

        self._migration_id = migration_id

    @property
    def storage_account_id(self):
        """Gets the storage_account_id of this LogEntry.  # noqa: E501

        Storage account related to this event, if any  # noqa: E501

        :return: The storage_account_id of this LogEntry.  # noqa: E501
        :rtype: int
        """
        return self._storage_account_id

    @storage_account_id.setter
    def storage_account_id(self, storage_account_id):
        """Sets the storage_account_id of this LogEntry.

        Storage account related to this event, if any  # noqa: E501

        :param storage_account_id: The storage_account_id of this LogEntry.  # noqa: E501
        :type: int
        """

        self._storage_account_id = storage_account_id

    @property
    def storage_id(self):
        """Gets the storage_id of this LogEntry.  # noqa: E501

        Storage related to this event, if any  # noqa: E501

        :return: The storage_id of this LogEntry.  # noqa: E501
        :rtype: int
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this LogEntry.

        Storage related to this event, if any  # noqa: E501

        :param storage_id: The storage_id of this LogEntry.  # noqa: E501
        :type: int
        """

        self._storage_id = storage_id

    @property
    def task_uuid(self):
        """Gets the task_uuid of this LogEntry.  # noqa: E501

        Task UUID related to this event, if any (NOT that the task might be already deleted)  # noqa: E501

        :return: The task_uuid of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._task_uuid

    @task_uuid.setter
    def task_uuid(self, task_uuid):
        """Sets the task_uuid of this LogEntry.

        Task UUID related to this event, if any (NOT that the task might be already deleted)  # noqa: E501

        :param task_uuid: The task_uuid of this LogEntry.  # noqa: E501
        :type: str
        """

        self._task_uuid = task_uuid

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
        if issubclass(LogEntry, dict):
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
        if not isinstance(other, LogEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
