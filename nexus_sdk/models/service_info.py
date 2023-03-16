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


class ServiceInfo(object):
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
        'allowed_extensions': 'list[str]'
    }

    attribute_map = {
        'allowed_extensions': 'allowed_extensions'
    }

    def __init__(self, allowed_extensions=None, local_vars_configuration=None):  # noqa: E501
        """ServiceInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_extensions = None
        self.discriminator = None

        self.allowed_extensions = allowed_extensions

    @property
    def allowed_extensions(self):
        """Gets the allowed_extensions of this ServiceInfo.  # noqa: E501

        A comma separated list of allowed extensions.  # noqa: E501

        :return: The allowed_extensions of this ServiceInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_extensions

    @allowed_extensions.setter
    def allowed_extensions(self, allowed_extensions):
        """Sets the allowed_extensions of this ServiceInfo.

        A comma separated list of allowed extensions.  # noqa: E501

        :param allowed_extensions: The allowed_extensions of this ServiceInfo.  # noqa: E501
        :type allowed_extensions: list[str]
        """
        if self.local_vars_configuration.client_side_validation and allowed_extensions is None:  # noqa: E501
            raise ValueError("Invalid value for `allowed_extensions`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                allowed_extensions is not None and len(allowed_extensions) > 30):
            raise ValueError("Invalid value for `allowed_extensions`, number of items must be less than or equal to `30`")  # noqa: E501

        self._allowed_extensions = allowed_extensions

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
        if not isinstance(other, ServiceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceInfo):
            return True

        return self.to_dict() != other.to_dict()
