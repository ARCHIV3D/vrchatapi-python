"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.7.7
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.api_client import ApiClient, Endpoint as _Endpoint
from vrchatapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from vrchatapi.model.add_favorite_request import AddFavoriteRequest
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
from vrchatapi.model.favorite_group import FavoriteGroup
from vrchatapi.model.success import Success
from vrchatapi.model.update_favorite_group_request import UpdateFavoriteGroupRequest


class FavoritesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_favorite_endpoint = _Endpoint(
            settings={
                'response_type': (Favorite,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites',
                'operation_id': 'add_favorite',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'add_favorite_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'add_favorite_request':
                        (AddFavoriteRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'add_favorite_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.clear_favorite_group_endpoint = _Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId}',
                'operation_id': 'clear_favorite_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'required': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'favorite_group_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('favorite_group_type',): {

                        "WORLD": "world",
                        "FRIEND": "friend",
                        "AVATAR": "avatar"
                    },
                },
                'openapi_types': {
                    'favorite_group_type':
                        (str,),
                    'favorite_group_name':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_group_type': 'favoriteGroupType',
                    'favorite_group_name': 'favoriteGroupName',
                    'user_id': 'userId',
                },
                'location_map': {
                    'favorite_group_type': 'path',
                    'favorite_group_name': 'path',
                    'user_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_favorite_endpoint = _Endpoint(
            settings={
                'response_type': (Favorite,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites/{favoriteId}',
                'operation_id': 'get_favorite',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_id',
                ],
                'required': [
                    'favorite_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'favorite_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_id': 'favoriteId',
                },
                'location_map': {
                    'favorite_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_favorite_group_endpoint = _Endpoint(
            settings={
                'response_type': (FavoriteGroup,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId}',
                'operation_id': 'get_favorite_group',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'required': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'favorite_group_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('favorite_group_type',): {

                        "WORLD": "world",
                        "FRIEND": "friend",
                        "AVATAR": "avatar"
                    },
                },
                'openapi_types': {
                    'favorite_group_type':
                        (str,),
                    'favorite_group_name':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_group_type': 'favoriteGroupType',
                    'favorite_group_name': 'favoriteGroupName',
                    'user_id': 'userId',
                },
                'location_map': {
                    'favorite_group_type': 'path',
                    'favorite_group_name': 'path',
                    'user_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_favorite_groups_endpoint = _Endpoint(
            settings={
                'response_type': ([FavoriteGroup],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/groups',
                'operation_id': 'get_favorite_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'n',
                    'offset',
                    'owner_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'n',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('n',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'n':
                        (int,),
                    'offset':
                        (int,),
                    'owner_id':
                        (str,),
                },
                'attribute_map': {
                    'n': 'n',
                    'offset': 'offset',
                    'owner_id': 'ownerId',
                },
                'location_map': {
                    'n': 'query',
                    'offset': 'query',
                    'owner_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_favorites_endpoint = _Endpoint(
            settings={
                'response_type': ([Favorite],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites',
                'operation_id': 'get_favorites',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'n',
                    'offset',
                    'type',
                    'tag',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'n',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('n',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'n':
                        (int,),
                    'offset':
                        (int,),
                    'type':
                        (str,),
                    'tag':
                        (str,),
                },
                'attribute_map': {
                    'n': 'n',
                    'offset': 'offset',
                    'type': 'type',
                    'tag': 'tag',
                },
                'location_map': {
                    'n': 'query',
                    'offset': 'query',
                    'type': 'query',
                    'tag': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.remove_favorite_endpoint = _Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites/{favoriteId}',
                'operation_id': 'remove_favorite',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_id',
                ],
                'required': [
                    'favorite_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'favorite_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_id': 'favoriteId',
                },
                'location_map': {
                    'favorite_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_favorite_group_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId}',
                'operation_id': 'update_favorite_group',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                    'update_favorite_group_request',
                ],
                'required': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'favorite_group_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('favorite_group_type',): {

                        "WORLD": "world",
                        "FRIEND": "friend",
                        "AVATAR": "avatar"
                    },
                },
                'openapi_types': {
                    'favorite_group_type':
                        (str,),
                    'favorite_group_name':
                        (str,),
                    'user_id':
                        (str,),
                    'update_favorite_group_request':
                        (UpdateFavoriteGroupRequest,),
                },
                'attribute_map': {
                    'favorite_group_type': 'favoriteGroupType',
                    'favorite_group_name': 'favoriteGroupName',
                    'user_id': 'userId',
                },
                'location_map': {
                    'favorite_group_type': 'path',
                    'favorite_group_name': 'path',
                    'user_id': 'path',
                    'update_favorite_group_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def add_favorite(
        self,
        **kwargs
    ):
        """Add Favorite  # noqa: E501

        Add a new favorite.  Friend groups are named `group_0` through `group_3`. Avatar and World groups are named `avatars1` to `avatars4` and `worlds1` to `worlds4`.  You cannot add people whom you are not friends with to your friends list. Destroying a friendship removes the person as favorite on both sides.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_favorite(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            add_favorite_request (AddFavoriteRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Favorite
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.add_favorite_endpoint.call_with_http_info(**kwargs)

    def clear_favorite_group(
        self,
        favorite_group_type,
        favorite_group_name,
        user_id,
        **kwargs
    ):
        """Clear Favorite Group  # noqa: E501

        Clear ALL contents of a specific favorite group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_favorite_group(favorite_group_type, favorite_group_name, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            favorite_group_type (str): The type of group to fetch, must be a valid FavoriteType.
            favorite_group_name (str):
            user_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Success
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['favorite_group_type'] = \
            favorite_group_type
        kwargs['favorite_group_name'] = \
            favorite_group_name
        kwargs['user_id'] = \
            user_id
        return self.clear_favorite_group_endpoint.call_with_http_info(**kwargs)

    def get_favorite(
        self,
        favorite_id,
        **kwargs
    ):
        """Show Favorite  # noqa: E501

        Return information about a specific Favorite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_favorite(favorite_id, async_req=True)
        >>> result = thread.get()

        Args:
            favorite_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Favorite
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['favorite_id'] = \
            favorite_id
        return self.get_favorite_endpoint.call_with_http_info(**kwargs)

    def get_favorite_group(
        self,
        favorite_group_type,
        favorite_group_name,
        user_id,
        **kwargs
    ):
        """Show Favorite Group  # noqa: E501

        Fetch information about a specific favorite group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_favorite_group(favorite_group_type, favorite_group_name, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            favorite_group_type (str): The type of group to fetch, must be a valid FavoriteType.
            favorite_group_name (str):
            user_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            FavoriteGroup
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['favorite_group_type'] = \
            favorite_group_type
        kwargs['favorite_group_name'] = \
            favorite_group_name
        kwargs['user_id'] = \
            user_id
        return self.get_favorite_group_endpoint.call_with_http_info(**kwargs)

    def get_favorite_groups(
        self,
        **kwargs
    ):
        """List Favorite Groups  # noqa: E501

        Return a list of favorite groups owned by a user. Returns the same information as `getFavoriteGroups`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_favorite_groups(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
            offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
            owner_id (str): The owner of whoms favorite groups to return. Must be a UserID.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [FavoriteGroup]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_favorite_groups_endpoint.call_with_http_info(**kwargs)

    def get_favorites(
        self,
        **kwargs
    ):
        """List Favorites  # noqa: E501

        Returns a list of favorites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_favorites(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
            offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
            type (str): The type of favorites to return, FavoriteType.. [optional]
            tag (str): Tags to include (comma-separated). Any of the tags needs to be present.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Favorite]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_favorites_endpoint.call_with_http_info(**kwargs)

    def remove_favorite(
        self,
        favorite_id,
        **kwargs
    ):
        """Remove Favorite  # noqa: E501

        Remove a favorite from your favorites list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_favorite(favorite_id, async_req=True)
        >>> result = thread.get()

        Args:
            favorite_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Success
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['favorite_id'] = \
            favorite_id
        return self.remove_favorite_endpoint.call_with_http_info(**kwargs)

    def update_favorite_group(
        self,
        favorite_group_type,
        favorite_group_name,
        user_id,
        **kwargs
    ):
        """Update Favorite Group  # noqa: E501

        Update information about a specific favorite group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_favorite_group(favorite_group_type, favorite_group_name, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            favorite_group_type (str): The type of group to fetch, must be a valid FavoriteType.
            favorite_group_name (str):
            user_id (str):

        Keyword Args:
            update_favorite_group_request (UpdateFavoriteGroupRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['favorite_group_type'] = \
            favorite_group_type
        kwargs['favorite_group_name'] = \
            favorite_group_name
        kwargs['user_id'] = \
            user_id
        return self.update_favorite_group_endpoint.call_with_http_info(**kwargs)

