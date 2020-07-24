# coding: utf-8

"""
    Post-it digitalization API

    Post-it digitalization API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: muellerobin95@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Coordinate(object):
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
        'pos_x': 'float',
        'pos_y': 'float'
    }

    attribute_map = {
        'pos_x': 'posX',
        'pos_y': 'posY'
    }

    def __init__(self, pos_x=None, pos_y=None):  # noqa: E501
        """Coordinate - a model defined in Swagger"""  # noqa: E501
        self._pos_x = None
        self._pos_y = None
        self.discriminator = None
        self.pos_x = pos_x
        self.pos_y = pos_y

    @property
    def pos_x(self):
        """Gets the pos_x of this Coordinate.  # noqa: E501


        :return: The pos_x of this Coordinate.  # noqa: E501
        :rtype: float
        """
        return self._pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        """Sets the pos_x of this Coordinate.


        :param pos_x: The pos_x of this Coordinate.  # noqa: E501
        :type: float
        """
        if pos_x is None:
            raise ValueError("Invalid value for `pos_x`, must not be `None`")  # noqa: E501

        self._pos_x = pos_x

    @property
    def pos_y(self):
        """Gets the pos_y of this Coordinate.  # noqa: E501


        :return: The pos_y of this Coordinate.  # noqa: E501
        :rtype: float
        """
        return self._pos_y

    @pos_y.setter
    def pos_y(self, pos_y):
        """Sets the pos_y of this Coordinate.


        :param pos_y: The pos_y of this Coordinate.  # noqa: E501
        :type: float
        """
        if pos_y is None:
            raise ValueError("Invalid value for `pos_y`, must not be `None`")  # noqa: E501

        self._pos_y = pos_y

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
        if issubclass(Coordinate, dict):
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
        if not isinstance(other, Coordinate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other