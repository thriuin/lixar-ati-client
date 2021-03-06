# coding: utf-8

"""
    ATIP AI Search API

    This API provides AI search functionalities: summary search and department recommendation.    Use the following code to authorize: ` nTsVPfUb89Ize/1DVSx2xKjLltOagND80lEfHaVB3fGT8CQEF7e9Lw== `  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: atip-support@lixar.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import pprint
import re  # noqa: F401

import six

from swagger_client.models.summary_search_result_response_header_params import SummarySearchResultResponseHeaderParams  # noqa: F401,E501


class SummarySearchResultResponseHeader(object):
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
        'status': 'str',
        'q_time': 'str',
        'params': 'SummarySearchResultResponseHeaderParams'
    }

    attribute_map = {
        'status': 'status',
        'q_time': 'QTime',
        'params': 'params'
    }

    def __init__(self, status=None, q_time=None, params=None):  # noqa: E501
        """SummarySearchResultResponseHeader - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._q_time = None
        self._params = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if q_time is not None:
            self.q_time = q_time
        if params is not None:
            self.params = params

    @property
    def status(self):
        """Gets the status of this SummarySearchResultResponseHeader.  # noqa: E501


        :return: The status of this SummarySearchResultResponseHeader.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SummarySearchResultResponseHeader.


        :param status: The status of this SummarySearchResultResponseHeader.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def q_time(self):
        """Gets the q_time of this SummarySearchResultResponseHeader.  # noqa: E501


        :return: The q_time of this SummarySearchResultResponseHeader.  # noqa: E501
        :rtype: str
        """
        return self._q_time

    @q_time.setter
    def q_time(self, q_time):
        """Sets the q_time of this SummarySearchResultResponseHeader.


        :param q_time: The q_time of this SummarySearchResultResponseHeader.  # noqa: E501
        :type: str
        """

        self._q_time = q_time

    @property
    def params(self):
        """Gets the params of this SummarySearchResultResponseHeader.  # noqa: E501


        :return: The params of this SummarySearchResultResponseHeader.  # noqa: E501
        :rtype: SummarySearchResultResponseHeaderParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this SummarySearchResultResponseHeader.


        :param params: The params of this SummarySearchResultResponseHeader.  # noqa: E501
        :type: SummarySearchResultResponseHeaderParams
        """

        self._params = params

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
        if not isinstance(other, SummarySearchResultResponseHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
