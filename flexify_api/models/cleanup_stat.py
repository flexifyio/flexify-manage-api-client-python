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


class CleanupStat(object):
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
        'active_engines': 'int',
        'active_streams': 'int',
        'bytes_failed': 'int',
        'bytes_not_matching_pattern': 'int',
        'bytes_processed': 'int',
        'bytes_removed': 'int',
        'bytes_skipped': 'int',
        'finished': 'datetime',
        'objects_failed': 'int',
        'objects_not_matching_pattern': 'int',
        'objects_processed': 'int',
        'objects_removed': 'int',
        'objects_skipped': 'int',
        'processing_objects_per_second': 'float',
        'removing_objects_per_second': 'float',
        'retried': 'int',
        'started': 'datetime',
        'state': 'str'
    }

    attribute_map = {
        'active_engines': 'activeEngines',
        'active_streams': 'activeStreams',
        'bytes_failed': 'bytesFailed',
        'bytes_not_matching_pattern': 'bytesNotMatchingPattern',
        'bytes_processed': 'bytesProcessed',
        'bytes_removed': 'bytesRemoved',
        'bytes_skipped': 'bytesSkipped',
        'finished': 'finished',
        'objects_failed': 'objectsFailed',
        'objects_not_matching_pattern': 'objectsNotMatchingPattern',
        'objects_processed': 'objectsProcessed',
        'objects_removed': 'objectsRemoved',
        'objects_skipped': 'objectsSkipped',
        'processing_objects_per_second': 'processingObjectsPerSecond',
        'removing_objects_per_second': 'removingObjectsPerSecond',
        'retried': 'retried',
        'started': 'started',
        'state': 'state'
    }

    def __init__(self, active_engines=None, active_streams=None, bytes_failed=None, bytes_not_matching_pattern=None, bytes_processed=None, bytes_removed=None, bytes_skipped=None, finished=None, objects_failed=None, objects_not_matching_pattern=None, objects_processed=None, objects_removed=None, objects_skipped=None, processing_objects_per_second=None, removing_objects_per_second=None, retried=None, started=None, state=None):  # noqa: E501
        """CleanupStat - a model defined in Swagger"""  # noqa: E501

        self._active_engines = None
        self._active_streams = None
        self._bytes_failed = None
        self._bytes_not_matching_pattern = None
        self._bytes_processed = None
        self._bytes_removed = None
        self._bytes_skipped = None
        self._finished = None
        self._objects_failed = None
        self._objects_not_matching_pattern = None
        self._objects_processed = None
        self._objects_removed = None
        self._objects_skipped = None
        self._processing_objects_per_second = None
        self._removing_objects_per_second = None
        self._retried = None
        self._started = None
        self._state = None
        self.discriminator = None

        if active_engines is not None:
            self.active_engines = active_engines
        if active_streams is not None:
            self.active_streams = active_streams
        if bytes_failed is not None:
            self.bytes_failed = bytes_failed
        if bytes_not_matching_pattern is not None:
            self.bytes_not_matching_pattern = bytes_not_matching_pattern
        if bytes_processed is not None:
            self.bytes_processed = bytes_processed
        if bytes_removed is not None:
            self.bytes_removed = bytes_removed
        if bytes_skipped is not None:
            self.bytes_skipped = bytes_skipped
        if finished is not None:
            self.finished = finished
        if objects_failed is not None:
            self.objects_failed = objects_failed
        if objects_not_matching_pattern is not None:
            self.objects_not_matching_pattern = objects_not_matching_pattern
        if objects_processed is not None:
            self.objects_processed = objects_processed
        if objects_removed is not None:
            self.objects_removed = objects_removed
        if objects_skipped is not None:
            self.objects_skipped = objects_skipped
        if processing_objects_per_second is not None:
            self.processing_objects_per_second = processing_objects_per_second
        if removing_objects_per_second is not None:
            self.removing_objects_per_second = removing_objects_per_second
        if retried is not None:
            self.retried = retried
        if started is not None:
            self.started = started
        if state is not None:
            self.state = state

    @property
    def active_engines(self):
        """Gets the active_engines of this CleanupStat.  # noqa: E501

        Number of engines that are busy with this  # noqa: E501

        :return: The active_engines of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._active_engines

    @active_engines.setter
    def active_engines(self, active_engines):
        """Sets the active_engines of this CleanupStat.

        Number of engines that are busy with this  # noqa: E501

        :param active_engines: The active_engines of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._active_engines = active_engines

    @property
    def active_streams(self):
        """Gets the active_streams of this CleanupStat.  # noqa: E501

        Number of currently active streams  # noqa: E501

        :return: The active_streams of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._active_streams

    @active_streams.setter
    def active_streams(self, active_streams):
        """Sets the active_streams of this CleanupStat.

        Number of currently active streams  # noqa: E501

        :param active_streams: The active_streams of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._active_streams = active_streams

    @property
    def bytes_failed(self):
        """Gets the bytes_failed of this CleanupStat.  # noqa: E501


        :return: The bytes_failed of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_failed

    @bytes_failed.setter
    def bytes_failed(self, bytes_failed):
        """Sets the bytes_failed of this CleanupStat.


        :param bytes_failed: The bytes_failed of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._bytes_failed = bytes_failed

    @property
    def bytes_not_matching_pattern(self):
        """Gets the bytes_not_matching_pattern of this CleanupStat.  # noqa: E501


        :return: The bytes_not_matching_pattern of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_not_matching_pattern

    @bytes_not_matching_pattern.setter
    def bytes_not_matching_pattern(self, bytes_not_matching_pattern):
        """Sets the bytes_not_matching_pattern of this CleanupStat.


        :param bytes_not_matching_pattern: The bytes_not_matching_pattern of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._bytes_not_matching_pattern = bytes_not_matching_pattern

    @property
    def bytes_processed(self):
        """Gets the bytes_processed of this CleanupStat.  # noqa: E501


        :return: The bytes_processed of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_processed

    @bytes_processed.setter
    def bytes_processed(self, bytes_processed):
        """Sets the bytes_processed of this CleanupStat.


        :param bytes_processed: The bytes_processed of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._bytes_processed = bytes_processed

    @property
    def bytes_removed(self):
        """Gets the bytes_removed of this CleanupStat.  # noqa: E501


        :return: The bytes_removed of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_removed

    @bytes_removed.setter
    def bytes_removed(self, bytes_removed):
        """Sets the bytes_removed of this CleanupStat.


        :param bytes_removed: The bytes_removed of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._bytes_removed = bytes_removed

    @property
    def bytes_skipped(self):
        """Gets the bytes_skipped of this CleanupStat.  # noqa: E501


        :return: The bytes_skipped of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_skipped

    @bytes_skipped.setter
    def bytes_skipped(self, bytes_skipped):
        """Sets the bytes_skipped of this CleanupStat.


        :param bytes_skipped: The bytes_skipped of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._bytes_skipped = bytes_skipped

    @property
    def finished(self):
        """Gets the finished of this CleanupStat.  # noqa: E501

        Finished time  # noqa: E501

        :return: The finished of this CleanupStat.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this CleanupStat.

        Finished time  # noqa: E501

        :param finished: The finished of this CleanupStat.  # noqa: E501
        :type: datetime
        """

        self._finished = finished

    @property
    def objects_failed(self):
        """Gets the objects_failed of this CleanupStat.  # noqa: E501


        :return: The objects_failed of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_failed

    @objects_failed.setter
    def objects_failed(self, objects_failed):
        """Sets the objects_failed of this CleanupStat.


        :param objects_failed: The objects_failed of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._objects_failed = objects_failed

    @property
    def objects_not_matching_pattern(self):
        """Gets the objects_not_matching_pattern of this CleanupStat.  # noqa: E501


        :return: The objects_not_matching_pattern of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_not_matching_pattern

    @objects_not_matching_pattern.setter
    def objects_not_matching_pattern(self, objects_not_matching_pattern):
        """Sets the objects_not_matching_pattern of this CleanupStat.


        :param objects_not_matching_pattern: The objects_not_matching_pattern of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._objects_not_matching_pattern = objects_not_matching_pattern

    @property
    def objects_processed(self):
        """Gets the objects_processed of this CleanupStat.  # noqa: E501


        :return: The objects_processed of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_processed

    @objects_processed.setter
    def objects_processed(self, objects_processed):
        """Sets the objects_processed of this CleanupStat.


        :param objects_processed: The objects_processed of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._objects_processed = objects_processed

    @property
    def objects_removed(self):
        """Gets the objects_removed of this CleanupStat.  # noqa: E501


        :return: The objects_removed of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_removed

    @objects_removed.setter
    def objects_removed(self, objects_removed):
        """Sets the objects_removed of this CleanupStat.


        :param objects_removed: The objects_removed of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._objects_removed = objects_removed

    @property
    def objects_skipped(self):
        """Gets the objects_skipped of this CleanupStat.  # noqa: E501


        :return: The objects_skipped of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_skipped

    @objects_skipped.setter
    def objects_skipped(self, objects_skipped):
        """Sets the objects_skipped of this CleanupStat.


        :param objects_skipped: The objects_skipped of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._objects_skipped = objects_skipped

    @property
    def processing_objects_per_second(self):
        """Gets the processing_objects_per_second of this CleanupStat.  # noqa: E501

        Objects/second processed  # noqa: E501

        :return: The processing_objects_per_second of this CleanupStat.  # noqa: E501
        :rtype: float
        """
        return self._processing_objects_per_second

    @processing_objects_per_second.setter
    def processing_objects_per_second(self, processing_objects_per_second):
        """Sets the processing_objects_per_second of this CleanupStat.

        Objects/second processed  # noqa: E501

        :param processing_objects_per_second: The processing_objects_per_second of this CleanupStat.  # noqa: E501
        :type: float
        """

        self._processing_objects_per_second = processing_objects_per_second

    @property
    def removing_objects_per_second(self):
        """Gets the removing_objects_per_second of this CleanupStat.  # noqa: E501


        :return: The removing_objects_per_second of this CleanupStat.  # noqa: E501
        :rtype: float
        """
        return self._removing_objects_per_second

    @removing_objects_per_second.setter
    def removing_objects_per_second(self, removing_objects_per_second):
        """Sets the removing_objects_per_second of this CleanupStat.


        :param removing_objects_per_second: The removing_objects_per_second of this CleanupStat.  # noqa: E501
        :type: float
        """

        self._removing_objects_per_second = removing_objects_per_second

    @property
    def retried(self):
        """Gets the retried of this CleanupStat.  # noqa: E501

        Number of retries  # noqa: E501

        :return: The retried of this CleanupStat.  # noqa: E501
        :rtype: int
        """
        return self._retried

    @retried.setter
    def retried(self, retried):
        """Sets the retried of this CleanupStat.

        Number of retries  # noqa: E501

        :param retried: The retried of this CleanupStat.  # noqa: E501
        :type: int
        """

        self._retried = retried

    @property
    def started(self):
        """Gets the started of this CleanupStat.  # noqa: E501

        Started time  # noqa: E501

        :return: The started of this CleanupStat.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this CleanupStat.

        Started time  # noqa: E501

        :param started: The started of this CleanupStat.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def state(self):
        """Gets the state of this CleanupStat.  # noqa: E501

        State of migration on its part  # noqa: E501

        :return: The state of this CleanupStat.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CleanupStat.

        State of migration on its part  # noqa: E501

        :param state: The state of this CleanupStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEPLOYING", "FAILED", "IN_PROGRESS", "NO_CONNECTION_TO_ENGINE", "RESTARTING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "WAITING"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if issubclass(CleanupStat, dict):
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
        if not isinstance(other, CleanupStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
