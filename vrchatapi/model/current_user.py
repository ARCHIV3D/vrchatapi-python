"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.1.2
    Contact: me@ruby.js.org
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
    from vrchatapi.model.avatar_id import AvatarID
    from vrchatapi.model.developer_type import DeveloperType
    from vrchatapi.model.past_display_name import PastDisplayName
    from vrchatapi.model.platform import Platform
    from vrchatapi.model.tag import Tag
    from vrchatapi.model.user_state import UserState
    from vrchatapi.model.user_status import UserStatus
    from vrchatapi.model.world_id import WorldID
    globals()['AvatarID'] = AvatarID
    globals()['DeveloperType'] = DeveloperType
    globals()['PastDisplayName'] = PastDisplayName
    globals()['Platform'] = Platform
    globals()['Tag'] = Tag
    globals()['UserState'] = UserState
    globals()['UserStatus'] = UserStatus
    globals()['WorldID'] = WorldID


class CurrentUser(ModelNormal):
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
            'username': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'user_icon': (str,),  # noqa: E501
            'bio': (str,),  # noqa: E501
            'bio_links': ([str],),  # noqa: E501
            'profile_pic_override': (str,),  # noqa: E501
            'status_description': (str,),  # noqa: E501
            'past_display_names': ([PastDisplayName],),  # noqa: E501
            'has_email': (bool,),  # noqa: E501
            'has_pending_email': (bool,),  # noqa: E501
            'obfuscated_email': (str,),  # noqa: E501
            'obfuscated_pending_email': (str,),  # noqa: E501
            'email_verified': (bool,),  # noqa: E501
            'has_birthday': (bool,),  # noqa: E501
            'unsubscribe': (bool,),  # noqa: E501
            'status_history': ([str],),  # noqa: E501
            'status_first_time': (bool,),  # noqa: E501
            'friends': ([str],),  # noqa: E501
            'friend_group_names': ([str],),  # noqa: E501
            'current_avatar_image_url': (str,),  # noqa: E501
            'current_avatar_thumbnail_image_url': (str,),  # noqa: E501
            'fallback_avatar': (AvatarID,),  # noqa: E501
            'current_avatar': (AvatarID,),  # noqa: E501
            'current_avatar_asset_url': (str,),  # noqa: E501
            'accepted_tos_version': (float,),  # noqa: E501
            'steam_id': (str,),  # noqa: E501
            'steam_details': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'oculus_id': (str,),  # noqa: E501
            'has_logged_in_from_client': (bool,),  # noqa: E501
            'home_location': (WorldID,),  # noqa: E501
            'two_factor_auth_enabled': (bool,),  # noqa: E501
            'state': (UserState,),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
            'developer_type': (DeveloperType,),  # noqa: E501
            'last_login': (datetime,),  # noqa: E501
            'last_platform': (Platform,),  # noqa: E501
            'allow_avatar_copying': (bool,),  # noqa: E501
            'status': (UserStatus,),  # noqa: E501
            'date_joined': (date,),  # noqa: E501
            'is_friend': (bool,),  # noqa: E501
            'friend_key': (str,),  # noqa: E501
            'account_deletion_date': (date, none_type,),  # noqa: E501
            'online_friends': ([str],),  # noqa: E501
            'active_friends': ([str],),  # noqa: E501
            'offline_friends': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'username': 'username',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'user_icon': 'userIcon',  # noqa: E501
        'bio': 'bio',  # noqa: E501
        'bio_links': 'bioLinks',  # noqa: E501
        'profile_pic_override': 'profilePicOverride',  # noqa: E501
        'status_description': 'statusDescription',  # noqa: E501
        'past_display_names': 'pastDisplayNames',  # noqa: E501
        'has_email': 'hasEmail',  # noqa: E501
        'has_pending_email': 'hasPendingEmail',  # noqa: E501
        'obfuscated_email': 'obfuscatedEmail',  # noqa: E501
        'obfuscated_pending_email': 'obfuscatedPendingEmail',  # noqa: E501
        'email_verified': 'emailVerified',  # noqa: E501
        'has_birthday': 'hasBirthday',  # noqa: E501
        'unsubscribe': 'unsubscribe',  # noqa: E501
        'status_history': 'statusHistory',  # noqa: E501
        'status_first_time': 'statusFirstTime',  # noqa: E501
        'friends': 'friends',  # noqa: E501
        'friend_group_names': 'friendGroupNames',  # noqa: E501
        'current_avatar_image_url': 'currentAvatarImageUrl',  # noqa: E501
        'current_avatar_thumbnail_image_url': 'currentAvatarThumbnailImageUrl',  # noqa: E501
        'fallback_avatar': 'fallbackAvatar',  # noqa: E501
        'current_avatar': 'currentAvatar',  # noqa: E501
        'current_avatar_asset_url': 'currentAvatarAssetUrl',  # noqa: E501
        'accepted_tos_version': 'acceptedTOSVersion',  # noqa: E501
        'steam_id': 'steamId',  # noqa: E501
        'steam_details': 'steamDetails',  # noqa: E501
        'oculus_id': 'oculusId',  # noqa: E501
        'has_logged_in_from_client': 'hasLoggedInFromClient',  # noqa: E501
        'home_location': 'homeLocation',  # noqa: E501
        'two_factor_auth_enabled': 'twoFactorAuthEnabled',  # noqa: E501
        'state': 'state',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'developer_type': 'developerType',  # noqa: E501
        'last_login': 'last_login',  # noqa: E501
        'last_platform': 'last_platform',  # noqa: E501
        'allow_avatar_copying': 'allowAvatarCopying',  # noqa: E501
        'status': 'status',  # noqa: E501
        'date_joined': 'date_joined',  # noqa: E501
        'is_friend': 'isFriend',  # noqa: E501
        'friend_key': 'friendKey',  # noqa: E501
        'account_deletion_date': 'accountDeletionDate',  # noqa: E501
        'online_friends': 'onlineFriends',  # noqa: E501
        'active_friends': 'activeFriends',  # noqa: E501
        'offline_friends': 'offlineFriends',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'date_joined',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, username, display_name, user_icon, bio, bio_links, profile_pic_override, status_description, past_display_names, has_email, has_pending_email, obfuscated_email, obfuscated_pending_email, email_verified, has_birthday, unsubscribe, status_history, status_first_time, friends, friend_group_names, current_avatar_image_url, current_avatar_thumbnail_image_url, fallback_avatar, current_avatar, current_avatar_asset_url, accepted_tos_version, steam_id, steam_details, oculus_id, has_logged_in_from_client, home_location, two_factor_auth_enabled, state, tags, developer_type, last_login, last_platform, allow_avatar_copying, status, date_joined, friend_key, *args, **kwargs):  # noqa: E501
        """CurrentUser - a model defined in OpenAPI

        Args:
            id (str):
            username (str):
            display_name (str):
            user_icon (str):
            bio (str):
            bio_links ([str]):
            profile_pic_override (str):
            status_description (str):
            past_display_names ([PastDisplayName]):
            has_email (bool):
            has_pending_email (bool):
            obfuscated_email (str):
            obfuscated_pending_email (str):
            email_verified (bool):
            has_birthday (bool):
            unsubscribe (bool):
            status_history ([str]):
            status_first_time (bool):
            friends ([str]):
            friend_group_names ([str]): Always empty array.
            current_avatar_image_url (str):
            current_avatar_thumbnail_image_url (str):
            fallback_avatar (AvatarID):
            current_avatar (AvatarID):
            current_avatar_asset_url (str):
            accepted_tos_version (float):
            steam_id (str):
            steam_details ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            oculus_id (str):
            has_logged_in_from_client (bool):
            home_location (WorldID):
            two_factor_auth_enabled (bool):
            state (UserState):
            tags ([Tag]):
            developer_type (DeveloperType):
            last_login (datetime):
            last_platform (Platform):
            allow_avatar_copying (bool):
            status (UserStatus):
            date_joined (date):
            friend_key (str):

        Keyword Args:
            is_friend (bool): defaults to False  # noqa: E501
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
            account_deletion_date (date, none_type): [optional]  # noqa: E501
            online_friends ([str]): [optional]  # noqa: E501
            active_friends ([str]): [optional]  # noqa: E501
            offline_friends ([str]): [optional]  # noqa: E501
        """

        is_friend = kwargs.get('is_friend', False)
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
        self.username = username
        self.display_name = display_name
        self.user_icon = user_icon
        self.bio = bio
        self.bio_links = bio_links
        self.profile_pic_override = profile_pic_override
        self.status_description = status_description
        self.past_display_names = past_display_names
        self.has_email = has_email
        self.has_pending_email = has_pending_email
        self.obfuscated_email = obfuscated_email
        self.obfuscated_pending_email = obfuscated_pending_email
        self.email_verified = email_verified
        self.has_birthday = has_birthday
        self.unsubscribe = unsubscribe
        self.status_history = status_history
        self.status_first_time = status_first_time
        self.friends = friends
        self.friend_group_names = friend_group_names
        self.current_avatar_image_url = current_avatar_image_url
        self.current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url
        self.fallback_avatar = fallback_avatar
        self.current_avatar = current_avatar
        self.current_avatar_asset_url = current_avatar_asset_url
        self.accepted_tos_version = accepted_tos_version
        self.steam_id = steam_id
        self.steam_details = steam_details
        self.oculus_id = oculus_id
        self.has_logged_in_from_client = has_logged_in_from_client
        self.home_location = home_location
        self.two_factor_auth_enabled = two_factor_auth_enabled
        self.state = state
        self.tags = tags
        self.developer_type = developer_type
        self.last_login = last_login
        self.last_platform = last_platform
        self.allow_avatar_copying = allow_avatar_copying
        self.status = status
        self.date_joined = date_joined
        self.is_friend = is_friend
        self.friend_key = friend_key
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
    def __init__(self, username, display_name, user_icon, bio, bio_links, profile_pic_override, status_description, past_display_names, has_email, has_pending_email, obfuscated_email, obfuscated_pending_email, email_verified, has_birthday, unsubscribe, status_history, status_first_time, friends, friend_group_names, current_avatar_image_url, current_avatar_thumbnail_image_url, fallback_avatar, current_avatar, current_avatar_asset_url, accepted_tos_version, steam_id, steam_details, oculus_id, has_logged_in_from_client, home_location, two_factor_auth_enabled, state, tags, developer_type, last_login, last_platform, allow_avatar_copying, status, friend_key, *args, **kwargs):  # noqa: E501
        """CurrentUser - a model defined in OpenAPI

            username (str):
            display_name (str):
            user_icon (str):
            bio (str):
            bio_links ([str]):
            profile_pic_override (str):
            status_description (str):
            past_display_names ([PastDisplayName]):
            has_email (bool):
            has_pending_email (bool):
            obfuscated_email (str):
            obfuscated_pending_email (str):
            email_verified (bool):
            has_birthday (bool):
            unsubscribe (bool):
            status_history ([str]):
            status_first_time (bool):
            friends ([str]):
            friend_group_names ([str]): Always empty array.
            current_avatar_image_url (str):
            current_avatar_thumbnail_image_url (str):
            fallback_avatar (AvatarID):
            current_avatar (AvatarID):
            current_avatar_asset_url (str):
            accepted_tos_version (float):
            steam_id (str):
            steam_details ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            oculus_id (str):
            has_logged_in_from_client (bool):
            home_location (WorldID):
            two_factor_auth_enabled (bool):
            state (UserState):
            tags ([Tag]):
            developer_type (DeveloperType):
            last_login (datetime):
            last_platform (Platform):
            allow_avatar_copying (bool):
            status (UserStatus):
            friend_key (str):

        Keyword Args:
            is_friend (bool): defaults to False  # noqa: E501
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
            account_deletion_date (date, none_type): [optional]  # noqa: E501
            online_friends ([str]): [optional]  # noqa: E501
            active_friends ([str]): [optional]  # noqa: E501
            offline_friends ([str]): [optional]  # noqa: E501
        """

        is_friend = kwargs.get('is_friend', False)
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

        self.username = username
        self.display_name = display_name
        self.user_icon = user_icon
        self.bio = bio
        self.bio_links = bio_links
        self.profile_pic_override = profile_pic_override
        self.status_description = status_description
        self.past_display_names = past_display_names
        self.has_email = has_email
        self.has_pending_email = has_pending_email
        self.obfuscated_email = obfuscated_email
        self.obfuscated_pending_email = obfuscated_pending_email
        self.email_verified = email_verified
        self.has_birthday = has_birthday
        self.unsubscribe = unsubscribe
        self.status_history = status_history
        self.status_first_time = status_first_time
        self.friends = friends
        self.friend_group_names = friend_group_names
        self.current_avatar_image_url = current_avatar_image_url
        self.current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url
        self.fallback_avatar = fallback_avatar
        self.current_avatar = current_avatar
        self.current_avatar_asset_url = current_avatar_asset_url
        self.accepted_tos_version = accepted_tos_version
        self.steam_id = steam_id
        self.steam_details = steam_details
        self.oculus_id = oculus_id
        self.has_logged_in_from_client = has_logged_in_from_client
        self.home_location = home_location
        self.two_factor_auth_enabled = two_factor_auth_enabled
        self.state = state
        self.tags = tags
        self.developer_type = developer_type
        self.last_login = last_login
        self.last_platform = last_platform
        self.allow_avatar_copying = allow_avatar_copying
        self.status = status
        self.is_friend = is_friend
        self.friend_key = friend_key
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
