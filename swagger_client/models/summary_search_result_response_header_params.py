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


class SummarySearchResultResponseHeaderParams(object):
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
        'indent': 'bool',
        'start': 'int',
        'q': 'str',
        'fq': 'str',
        'wt': 'str',
        'rows': 'int'
    }

    attribute_map = {
        'indent': 'indent',
        'start': 'start',
        'q': 'q',
        'fq': 'fq',
        'wt': 'wt',
        'rows': 'rows'
    }

    def __init__(self, indent=None, start=None, q=None, fq=None, wt=None, rows=None):  # noqa: E501
        """SummarySearchResultResponseHeaderParams - a model defined in Swagger"""  # noqa: E501

        self._indent = None
        self._start = None
        self._q = None
        self._fq = None
        self._wt = None
        self._rows = None
        self.discriminator = None

        if indent is not None:
            self.indent = indent
        if start is not None:
            self.start = start
        if q is not None:
            self.q = q
        if fq is not None:
            self.fq = fq
        if wt is not None:
            self.wt = wt
        if rows is not None:
            self.rows = rows

    @property
    def indent(self):
        """Gets the indent of this SummarySearchResultResponseHeaderParams.  # noqa: E501


        :return: The indent of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :rtype: bool
        """
        return self._indent

    @indent.setter
    def indent(self, indent):
        """Sets the indent of this SummarySearchResultResponseHeaderParams.


        :param indent: The indent of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :type: bool
        """

        self._indent = indent

    @property
    def start(self):
        """Gets the start of this SummarySearchResultResponseHeaderParams.  # noqa: E501

        Determines the first row to display (used for paging)  # noqa: E501

        :return: The start of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SummarySearchResultResponseHeaderParams.

        Determines the first row to display (used for paging)  # noqa: E501

        :param start: The start of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def q(self):
        """Gets the q of this SummarySearchResultResponseHeaderParams.  # noqa: E501

        Text that was searched  # noqa: E501

        :return: The q of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this SummarySearchResultResponseHeaderParams.

        Text that was searched  # noqa: E501

        :param q: The q of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def fq(self):
        """Gets the fq of this SummarySearchResultResponseHeaderParams.  # noqa: E501


        :return: The fq of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :rtype: str
        """
        return self._fq

    @fq.setter
    def fq(self, fq):
        """Sets the fq of this SummarySearchResultResponseHeaderParams.


        :param fq: The fq of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :type: str
        """

        self._fq = fq

    @property
    def wt(self):
        """Gets the wt of this SummarySearchResultResponseHeaderParams.  # noqa: E501


        :return: The wt of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :rtype: str
        """
        return self._wt

    @wt.setter
    def wt(self, wt):
        """Sets the wt of this SummarySearchResultResponseHeaderParams.


        :param wt: The wt of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :type: str
        """

        self._wt = wt

    @property
    def rows(self):
        """Gets the rows of this SummarySearchResultResponseHeaderParams.  # noqa: E501

        Number of items per 'page'  # noqa: E501

        :return: The rows of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this SummarySearchResultResponseHeaderParams.

        Number of items per 'page'  # noqa: E501

        :param rows: The rows of this SummarySearchResultResponseHeaderParams.  # noqa: E501
        :type: int
        """

        self._rows = rows

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
        if not isinstance(other, SummarySearchResultResponseHeaderParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other