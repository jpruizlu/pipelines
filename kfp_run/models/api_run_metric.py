# coding: utf-8

"""
    backend/api/run.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kfp_run.models.run_metric_format import RunMetricFormat  # noqa: F401,E501


class ApiRunMetric(object):
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
        'name': 'str',
        'node_id': 'str',
        'number_value': 'float',
        'format': 'RunMetricFormat'
    }

    attribute_map = {
        'name': 'name',
        'node_id': 'node_id',
        'number_value': 'number_value',
        'format': 'format'
    }

    def __init__(self, name=None, node_id=None, number_value=None, format=None):  # noqa: E501
        """ApiRunMetric - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._node_id = None
        self._number_value = None
        self._format = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if number_value is not None:
            self.number_value = number_value
        if format is not None:
            self.format = format

    @property
    def name(self):
        """Gets the name of this ApiRunMetric.  # noqa: E501

        Required. The user defined name of the metric. It must between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.  # noqa: E501

        :return: The name of this ApiRunMetric.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiRunMetric.

        Required. The user defined name of the metric. It must between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.  # noqa: E501

        :param name: The name of this ApiRunMetric.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_id(self):
        """Gets the node_id of this ApiRunMetric.  # noqa: E501

        Required. The runtime node ID which reports the metric. The node ID can be found in the RunDetail.workflow.Status. Metric with same (node_id, name) are considerd as duplicate. Only the first reporting will be recorded. Max length is 128.  # noqa: E501

        :return: The node_id of this ApiRunMetric.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ApiRunMetric.

        Required. The runtime node ID which reports the metric. The node ID can be found in the RunDetail.workflow.Status. Metric with same (node_id, name) are considerd as duplicate. Only the first reporting will be recorded. Max length is 128.  # noqa: E501

        :param node_id: The node_id of this ApiRunMetric.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def number_value(self):
        """Gets the number_value of this ApiRunMetric.  # noqa: E501

        The number value of the metric.  # noqa: E501

        :return: The number_value of this ApiRunMetric.  # noqa: E501
        :rtype: float
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this ApiRunMetric.

        The number value of the metric.  # noqa: E501

        :param number_value: The number_value of this ApiRunMetric.  # noqa: E501
        :type: float
        """

        self._number_value = number_value

    @property
    def format(self):
        """Gets the format of this ApiRunMetric.  # noqa: E501

        The display format of metric.  # noqa: E501

        :return: The format of this ApiRunMetric.  # noqa: E501
        :rtype: RunMetricFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ApiRunMetric.

        The display format of metric.  # noqa: E501

        :param format: The format of this ApiRunMetric.  # noqa: E501
        :type: RunMetricFormat
        """

        self._format = format

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
        if issubclass(ApiRunMetric, dict):
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
        if not isinstance(other, ApiRunMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
