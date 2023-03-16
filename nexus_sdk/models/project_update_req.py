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


class ProjectUpdateReq(object):
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
        'new_name': 'str',
        'new_description': 'str',
        'new_owner': 'str'
    }

    attribute_map = {
        'new_name': 'new_name',
        'new_description': 'new_description',
        'new_owner': 'new_owner'
    }

    def __init__(self, new_name=None, new_description='', new_owner=None, local_vars_configuration=None):  # noqa: E501
        """ProjectUpdateReq - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._new_name = None
        self._new_description = None
        self._new_owner = None
        self.discriminator = None

        if new_name is not None:
            self.new_name = new_name
        if new_description is not None:
            self.new_description = new_description
        if new_owner is not None:
            self.new_owner = new_owner

    @property
    def new_name(self):
        """Gets the new_name of this ProjectUpdateReq.  # noqa: E501

        Name assigned to the project  # noqa: E501

        :return: The new_name of this ProjectUpdateReq.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this ProjectUpdateReq.

        Name assigned to the project  # noqa: E501

        :param new_name: The new_name of this ProjectUpdateReq.  # noqa: E501
        :type new_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                new_name is not None and len(new_name) > 50):
            raise ValueError("Invalid value for `new_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_name is not None and len(new_name) < 1):
            raise ValueError("Invalid value for `new_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_name is not None and not re.search(r'^[ -~]+$', new_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `new_name`, must be a follow pattern or equal to `/^[ -~]+$/`")  # noqa: E501

        self._new_name = new_name

    @property
    def new_description(self):
        """Gets the new_description of this ProjectUpdateReq.  # noqa: E501

        Description of the project.  # noqa: E501

        :return: The new_description of this ProjectUpdateReq.  # noqa: E501
        :rtype: str
        """
        return self._new_description

    @new_description.setter
    def new_description(self, new_description):
        """Sets the new_description of this ProjectUpdateReq.

        Description of the project.  # noqa: E501

        :param new_description: The new_description of this ProjectUpdateReq.  # noqa: E501
        :type new_description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                new_description is not None and len(new_description) > 255):
            raise ValueError("Invalid value for `new_description`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_description is not None and not re.search(r'^[ -~]*$', new_description)):  # noqa: E501
            raise ValueError(r"Invalid value for `new_description`, must be a follow pattern or equal to `/^[ -~]*$/`")  # noqa: E501

        self._new_description = new_description

    @property
    def new_owner(self):
        """Gets the new_owner of this ProjectUpdateReq.  # noqa: E501

        User email  # noqa: E501

        :return: The new_owner of this ProjectUpdateReq.  # noqa: E501
        :rtype: str
        """
        return self._new_owner

    @new_owner.setter
    def new_owner(self, new_owner):
        """Sets the new_owner of this ProjectUpdateReq.

        User email  # noqa: E501

        :param new_owner: The new_owner of this ProjectUpdateReq.  # noqa: E501
        :type new_owner: str
        """
        if (self.local_vars_configuration.client_side_validation and
                new_owner is not None and len(new_owner) > 254):
            raise ValueError("Invalid value for `new_owner`, length must be less than or equal to `254`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_owner is not None and len(new_owner) < 4):
            raise ValueError("Invalid value for `new_owner`, length must be greater than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_owner is not None and not re.search(r'^(?=[a-zA-Z0-9][a-zA-Z0-9@._%+-]{5,253}$)[a-zA-Z0-9._%+-]{1,64}@(?:(?=[a-zA-Z0-9-]{1,63}\.)[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*\.){1,8}[a-zA-Z]{2,63}$', new_owner)):  # noqa: E501
            raise ValueError(r"Invalid value for `new_owner`, must be a follow pattern or equal to `/^(?=[a-zA-Z0-9][a-zA-Z0-9@._%+-]{5,253}$)[a-zA-Z0-9._%+-]{1,64}@(?:(?=[a-zA-Z0-9-]{1,63}\.)[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*\.){1,8}[a-zA-Z]{2,63}$/`")  # noqa: E501

        self._new_owner = new_owner

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
        if not isinstance(other, ProjectUpdateReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUpdateReq):
            return True

        return self.to_dict() != other.to_dict()
