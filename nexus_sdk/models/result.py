# coding: utf-8

"""
    Atinary™ Nexus

    As part of Atinary™ Nexus, we offer a downloadable software development kit (SDK) client, which facilitates the access to the application programming interface (API) entry point. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Atinary™ Nexus account. You can generate your `API KEY` on your [account information page](https://home.atinary.com/user).  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: support@atinary.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from nexus_sdk.configuration import Configuration


class Result(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'int',
        'message': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'resource': 'resource'
    }

    def __init__(self, code=None, message=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """Result - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._message = None
        self._resource = None
        self.discriminator = None

        self.code = code
        if message is not None:
            self.message = message
        if resource is not None:
            self.resource = resource

    @property
    def code(self):
        """Gets the code of this Result.  # noqa: E501

        Operation result  # noqa: E501

        :return: The code of this Result.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Result.

        Operation result  # noqa: E501

        :param code: The code of this Result.  # noqa: E501
        :type code: int
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and code > 9999):  # noqa: E501
            raise ValueError("Invalid value for `code`, must be a value less than or equal to `9999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and code < 0):  # noqa: E501
            raise ValueError("Invalid value for `code`, must be a value greater than or equal to `0`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this Result.  # noqa: E501

        String explanation.  # noqa: E501

        :return: The message of this Result.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Result.

        String explanation.  # noqa: E501

        :param message: The message of this Result.  # noqa: E501
        :type message: str
        """
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) > 255):
            raise ValueError("Invalid value for `message`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and not re.search(r'^[ -~]+$', message)):  # noqa: E501
            raise ValueError(r"Invalid value for `message`, must be a follow pattern or equal to `/^[ -~]+$/`")  # noqa: E501

        self._message = message

    @property
    def resource(self):
        """Gets the resource of this Result.  # noqa: E501

        The object that is involved in the error.  # noqa: E501

        :return: The resource of this Result.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Result.

        The object that is involved in the error.  # noqa: E501

        :param resource: The resource of this Result.  # noqa: E501
        :type resource: str
        """
        if (self.local_vars_configuration.client_side_validation and
                resource is not None and len(resource) > 255):
            raise ValueError("Invalid value for `resource`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                resource is not None and not re.search(r'^[ -~]+$', resource)):  # noqa: E501
            raise ValueError(r"Invalid value for `resource`, must be a follow pattern or equal to `/^[ -~]+$/`")  # noqa: E501

        self._resource = resource

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Result):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Result):
            return True

        return self.to_dict() != other.to_dict()
