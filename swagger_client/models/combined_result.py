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

from swagger_client.models.department_recommendation_result import DepartmentRecommendationResult  # noqa: F401,E501
from swagger_client.models.summary_search_result import SummarySearchResult  # noqa: F401,E501


class CombinedResult(object):
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
        'result_departments_json': 'DepartmentRecommendationResult',
        'result_summary_json': 'SummarySearchResult'
    }

    attribute_map = {
        'result_departments_json': 'resultDepartmentsJson',
        'result_summary_json': 'resultSummaryJson'
    }

    def __init__(self, result_departments_json=None, result_summary_json=None):  # noqa: E501
        """CombinedResult - a model defined in Swagger"""  # noqa: E501

        self._result_departments_json = None
        self._result_summary_json = None
        self.discriminator = None

        if result_departments_json is not None:
            self.result_departments_json = result_departments_json
        if result_summary_json is not None:
            self.result_summary_json = result_summary_json

    @property
    def result_departments_json(self):
        """Gets the result_departments_json of this CombinedResult.  # noqa: E501


        :return: The result_departments_json of this CombinedResult.  # noqa: E501
        :rtype: DepartmentRecommendationResult
        """
        return self._result_departments_json

    @result_departments_json.setter
    def result_departments_json(self, result_departments_json):
        """Sets the result_departments_json of this CombinedResult.


        :param result_departments_json: The result_departments_json of this CombinedResult.  # noqa: E501
        :type: DepartmentRecommendationResult
        """

        self._result_departments_json = result_departments_json

    @property
    def result_summary_json(self):
        """Gets the result_summary_json of this CombinedResult.  # noqa: E501


        :return: The result_summary_json of this CombinedResult.  # noqa: E501
        :rtype: SummarySearchResult
        """
        return self._result_summary_json

    @result_summary_json.setter
    def result_summary_json(self, result_summary_json):
        """Sets the result_summary_json of this CombinedResult.


        :param result_summary_json: The result_summary_json of this CombinedResult.  # noqa: E501
        :type: SummarySearchResult
        """

        self._result_summary_json = result_summary_json

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
        if not isinstance(other, CombinedResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
