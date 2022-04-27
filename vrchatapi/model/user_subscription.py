"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.7.1
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from vrchatapi.exceptions import ApiAttributeError


def lazy_import():
    from vrchatapi.model.license_group_id import LicenseGroupID
    from vrchatapi.model.subscription_period import SubscriptionPeriod
    from vrchatapi.model.transaction_id import TransactionID
    from vrchatapi.model.transaction_status import TransactionStatus
    globals()['LicenseGroupID'] = LicenseGroupID
    globals()['SubscriptionPeriod'] = SubscriptionPeriod
    globals()['TransactionID'] = TransactionID
    globals()['TransactionStatus'] = TransactionStatus


class UserSubscription(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('id',): {
            'min_length': 1,
        },
        ('store',): {
            'min_length': 1,
        },
        ('steam_item_id',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'transaction_id': (TransactionID,),  # noqa: E501
            'store': (str,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'period': (SubscriptionPeriod,),  # noqa: E501
            'tier': (float,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'status': (TransactionStatus,),  # noqa: E501
            'expires': (datetime,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'license_groups': ([LicenseGroupID],),  # noqa: E501
            'is_gift': (bool,),  # noqa: E501
            'steam_item_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'transaction_id': 'transactionId',  # noqa: E501
        'store': 'store',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'description': 'description',  # noqa: E501
        'period': 'period',  # noqa: E501
        'tier': 'tier',  # noqa: E501
        'active': 'active',  # noqa: E501
        'status': 'status',  # noqa: E501
        'expires': 'expires',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'license_groups': 'licenseGroups',  # noqa: E501
        'is_gift': 'isGift',  # noqa: E501
        'steam_item_id': 'steamItemId',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, transaction_id, store, amount, description, period, tier, status, expires, created_at, updated_at, license_groups, *args, **kwargs):  # noqa: E501
        """UserSubscription - a model defined in OpenAPI

        Args:
            id (str):
            transaction_id (TransactionID):
            store (str): Which \"Store\" it came from. Right now only Stores are \"Steam\" and \"Admin\".
            amount (float):
            description (str):
            period (SubscriptionPeriod):
            tier (float):
            status (TransactionStatus):
            expires (datetime):
            created_at (datetime):
            updated_at (datetime):
            license_groups ([LicenseGroupID]):

        Keyword Args:
            active (bool): defaults to True  # noqa: E501
            is_gift (bool): defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            steam_item_id (str): [optional]  # noqa: E501
        """

        active = kwargs.get('active', True)
        is_gift = kwargs.get('is_gift', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.transaction_id = transaction_id
        self.store = store
        self.amount = amount
        self.description = description
        self.period = period
        self.tier = tier
        self.active = active
        self.status = status
        self.expires = expires
        self.created_at = created_at
        self.updated_at = updated_at
        self.license_groups = license_groups
        self.is_gift = is_gift
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, transaction_id, store, amount, description, period, tier, status, expires, created_at, updated_at, license_groups, *args, **kwargs):  # noqa: E501
        """UserSubscription - a model defined in OpenAPI

        Args:
            id (str):
            transaction_id (TransactionID):
            store (str): Which \"Store\" it came from. Right now only Stores are \"Steam\" and \"Admin\".
            amount (float):
            description (str):
            period (SubscriptionPeriod):
            tier (float):
            status (TransactionStatus):
            expires (datetime):
            created_at (datetime):
            updated_at (datetime):
            license_groups ([LicenseGroupID]):

        Keyword Args:
            active (bool): defaults to True  # noqa: E501
            is_gift (bool): defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            steam_item_id (str): [optional]  # noqa: E501
        """

        active = kwargs.get('active', True)
        is_gift = kwargs.get('is_gift', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.transaction_id = transaction_id
        self.store = store
        self.amount = amount
        self.description = description
        self.period = period
        self.tier = tier
        self.active = active
        self.status = status
        self.expires = expires
        self.created_at = created_at
        self.updated_at = updated_at
        self.license_groups = license_groups
        self.is_gift = is_gift
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
