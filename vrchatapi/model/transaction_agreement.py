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



class TransactionAgreement(ModelNormal):
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
        ('agreement_id',): {
            'min_length': 1,
        },
        ('status',): {
            'min_length': 1,
        },
        ('period',): {
            'min_length': 1,
        },
        ('billing_type',): {
            'min_length': 1,
        },
        ('start_date',): {
            'min_length': 1,
        },
        ('end_date',): {
            'min_length': 1,
        },
        ('currency',): {
            'min_length': 1,
        },
        ('time_created',): {
            'min_length': 1,
        },
        ('next_payment',): {
            'min_length': 1,
        },
        ('last_payment',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'agreement_id': (str,),  # noqa: E501
            'item_id': (float,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'period': (str,),  # noqa: E501
            'frequency': (float,),  # noqa: E501
            'billing_type': (str,),  # noqa: E501
            'start_date': (str,),  # noqa: E501
            'end_date': (str,),  # noqa: E501
            'recurring_amt': (float,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'time_created': (str,),  # noqa: E501
            'next_payment': (str,),  # noqa: E501
            'last_payment': (str,),  # noqa: E501
            'last_amount': (float,),  # noqa: E501
            'last_amount_vat': (float,),  # noqa: E501
            'outstanding': (float,),  # noqa: E501
            'failed_attempts': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'agreement_id': 'agreementId',  # noqa: E501
        'item_id': 'itemId',  # noqa: E501
        'status': 'status',  # noqa: E501
        'period': 'period',  # noqa: E501
        'frequency': 'frequency',  # noqa: E501
        'billing_type': 'billingType',  # noqa: E501
        'start_date': 'startDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'recurring_amt': 'recurringAmt',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'time_created': 'timeCreated',  # noqa: E501
        'next_payment': 'nextPayment',  # noqa: E501
        'last_payment': 'lastPayment',  # noqa: E501
        'last_amount': 'lastAmount',  # noqa: E501
        'last_amount_vat': 'lastAmountVat',  # noqa: E501
        'outstanding': 'outstanding',  # noqa: E501
        'failed_attempts': 'failedAttempts',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, agreement_id, item_id, status, period, frequency, billing_type, start_date, end_date, recurring_amt, currency, time_created, next_payment, last_payment, last_amount, last_amount_vat, outstanding, failed_attempts, *args, **kwargs):  # noqa: E501
        """TransactionAgreement - a model defined in OpenAPI

        Args:
            agreement_id (str):
            item_id (float):
            status (str): This is NOT TransactionStatus, but whatever Steam return.
            period (str):
            frequency (float):
            billing_type (str):
            start_date (str):
            end_date (str):
            recurring_amt (float):
            currency (str):
            time_created (str):
            next_payment (str):
            last_payment (str):
            last_amount (float):
            last_amount_vat (float):
            outstanding (float):
            failed_attempts (float):

        Keyword Args:
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
        """

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

        self.agreement_id = agreement_id
        self.item_id = item_id
        self.status = status
        self.period = period
        self.frequency = frequency
        self.billing_type = billing_type
        self.start_date = start_date
        self.end_date = end_date
        self.recurring_amt = recurring_amt
        self.currency = currency
        self.time_created = time_created
        self.next_payment = next_payment
        self.last_payment = last_payment
        self.last_amount = last_amount
        self.last_amount_vat = last_amount_vat
        self.outstanding = outstanding
        self.failed_attempts = failed_attempts
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
    def __init__(self, agreement_id, item_id, status, period, frequency, billing_type, start_date, end_date, recurring_amt, currency, time_created, next_payment, last_payment, last_amount, last_amount_vat, outstanding, failed_attempts, *args, **kwargs):  # noqa: E501
        """TransactionAgreement - a model defined in OpenAPI

        Args:
            agreement_id (str):
            item_id (float):
            status (str): This is NOT TransactionStatus, but whatever Steam return.
            period (str):
            frequency (float):
            billing_type (str):
            start_date (str):
            end_date (str):
            recurring_amt (float):
            currency (str):
            time_created (str):
            next_payment (str):
            last_payment (str):
            last_amount (float):
            last_amount_vat (float):
            outstanding (float):
            failed_attempts (float):

        Keyword Args:
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
        """

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

        self.agreement_id = agreement_id
        self.item_id = item_id
        self.status = status
        self.period = period
        self.frequency = frequency
        self.billing_type = billing_type
        self.start_date = start_date
        self.end_date = end_date
        self.recurring_amt = recurring_amt
        self.currency = currency
        self.time_created = time_created
        self.next_payment = next_payment
        self.last_payment = last_payment
        self.last_amount = last_amount
        self.last_amount_vat = last_amount_vat
        self.outstanding = outstanding
        self.failed_attempts = failed_attempts
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
