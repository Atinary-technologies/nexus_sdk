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


class HealthCheckReport(object):
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
        'generated_at': 'str'
    }

    attribute_map = {
        'generated_at': 'generated_at'
    }

    def __init__(self, generated_at=None, local_vars_configuration=None):  # noqa: E501
        """HealthCheckReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._generated_at = None
        self.discriminator = None

        self.generated_at = generated_at

    @property
    def generated_at(self):
        """Gets the generated_at of this HealthCheckReport.  # noqa: E501

        date-time in ISO8601 format  # noqa: E501

        :return: The generated_at of this HealthCheckReport.  # noqa: E501
        :rtype: str
        """
        return self._generated_at

    @generated_at.setter
    def generated_at(self, generated_at):
        """Sets the generated_at of this HealthCheckReport.

        date-time in ISO8601 format  # noqa: E501

        :param generated_at: The generated_at of this HealthCheckReport.  # noqa: E501
        :type generated_at: str
        """
        if self.local_vars_configuration.client_side_validation and generated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `generated_at`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                generated_at is not None and len(generated_at) > 32):
            raise ValueError("Invalid value for `generated_at`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                generated_at is not None and len(generated_at) < 19):
            raise ValueError("Invalid value for `generated_at`, length must be greater than or equal to `19`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                generated_at is not None and not re.search(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?(\+\d{2}:\d{2}|Z)?$', generated_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `generated_at`, must be a follow pattern or equal to `/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?(\+\d{2}:\d{2}|Z)?$/`")  # noqa: E501

        self._generated_at = generated_at

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
        if not isinstance(other, HealthCheckReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthCheckReport):
            return True

        return self.to_dict() != other.to_dict()
