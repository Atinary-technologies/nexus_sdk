# coding: utf-8

"""
    Atinary™ Nexus

    As part of Atinary™ Nexus, we offer a downloadable software development kit (SDK) client, which facilitates the access to the application programming interface (API) entry point. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Atinary™ Nexus account. You can generate your `API KEY` on your [account information page](https://home.atinary.com/user).  # noqa: E501

    The version of the OpenAPI document: 0.13.0
    Contact: support@atinary.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nexus_sdk.configuration import Configuration


class ProjectSubscribeReq(object):
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
        'email_list': 'list[str]'
    }

    attribute_map = {
        'email_list': 'email_list'
    }

    def __init__(self, email_list=None, local_vars_configuration=None):  # noqa: E501
        """ProjectSubscribeReq - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_list = None
        self.discriminator = None

        self.email_list = email_list

    @property
    def email_list(self):
        """Gets the email_list of this ProjectSubscribeReq.  # noqa: E501

        A comma separated list of user emails.  # noqa: E501

        :return: The email_list of this ProjectSubscribeReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_list

    @email_list.setter
    def email_list(self, email_list):
        """Sets the email_list of this ProjectSubscribeReq.

        A comma separated list of user emails.  # noqa: E501

        :param email_list: The email_list of this ProjectSubscribeReq.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_list is None:  # noqa: E501
            raise ValueError("Invalid value for `email_list`, must not be `None`")  # noqa: E501

        self._email_list = email_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, ProjectSubscribeReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectSubscribeReq):
            return True

        return self.to_dict() != other.to_dict()
