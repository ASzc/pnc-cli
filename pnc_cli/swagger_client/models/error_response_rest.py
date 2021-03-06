# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class ErrorResponseRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'error_type': 'str',
        'error_message': 'str',
        'details': 'object'
    }

    attribute_map = {
        'error_type': 'errorType',
        'error_message': 'errorMessage',
        'details': 'details'
    }

    def __init__(self, error_type=None, error_message=None, details=None):
        """
        ErrorResponseRest - a model defined in Swagger
        """

        self._error_type = None
        self._error_message = None
        self._details = None

        if error_type is not None:
          self.error_type = error_type
        if error_message is not None:
          self.error_message = error_message
        if details is not None:
          self.details = details

    @property
    def error_type(self):
        """
        Gets the error_type of this ErrorResponseRest.

        :return: The error_type of this ErrorResponseRest.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this ErrorResponseRest.

        :param error_type: The error_type of this ErrorResponseRest.
        :type: str
        """

        self._error_type = error_type

    @property
    def error_message(self):
        """
        Gets the error_message of this ErrorResponseRest.

        :return: The error_message of this ErrorResponseRest.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ErrorResponseRest.

        :param error_message: The error_message of this ErrorResponseRest.
        :type: str
        """

        self._error_message = error_message

    @property
    def details(self):
        """
        Gets the details of this ErrorResponseRest.

        :return: The details of this ErrorResponseRest.
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this ErrorResponseRest.

        :param details: The details of this ErrorResponseRest.
        :type: object
        """

        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ErrorResponseRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
