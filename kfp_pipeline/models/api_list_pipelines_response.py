# coding: utf-8

"""
    backend/api/pipeline.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kfp_pipeline.models.api_pipeline import ApiPipeline  # noqa: F401,E501


class ApiListPipelinesResponse(object):
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
        'pipelines': 'list[ApiPipeline]',
        'total_size': 'int',
        'next_page_token': 'str'
    }

    attribute_map = {
        'pipelines': 'pipelines',
        'total_size': 'total_size',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, pipelines=None, total_size=None, next_page_token=None):  # noqa: E501
        """ApiListPipelinesResponse - a model defined in Swagger"""  # noqa: E501

        self._pipelines = None
        self._total_size = None
        self._next_page_token = None
        self.discriminator = None

        if pipelines is not None:
            self.pipelines = pipelines
        if total_size is not None:
            self.total_size = total_size
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def pipelines(self):
        """Gets the pipelines of this ApiListPipelinesResponse.  # noqa: E501


        :return: The pipelines of this ApiListPipelinesResponse.  # noqa: E501
        :rtype: list[ApiPipeline]
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        """Sets the pipelines of this ApiListPipelinesResponse.


        :param pipelines: The pipelines of this ApiListPipelinesResponse.  # noqa: E501
        :type: list[ApiPipeline]
        """

        self._pipelines = pipelines

    @property
    def total_size(self):
        """Gets the total_size of this ApiListPipelinesResponse.  # noqa: E501


        :return: The total_size of this ApiListPipelinesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this ApiListPipelinesResponse.


        :param total_size: The total_size of this ApiListPipelinesResponse.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ApiListPipelinesResponse.  # noqa: E501


        :return: The next_page_token of this ApiListPipelinesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ApiListPipelinesResponse.


        :param next_page_token: The next_page_token of this ApiListPipelinesResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

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
        if issubclass(ApiListPipelinesResponse, dict):
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
        if not isinstance(other, ApiListPipelinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
