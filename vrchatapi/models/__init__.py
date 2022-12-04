# coding: utf-8

# flake8: noqa
"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.9.1
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from vrchatapi.models.api_config import APIConfig
from vrchatapi.models.api_config_announcement import APIConfigAnnouncement
from vrchatapi.models.api_config_download_url_list import APIConfigDownloadURLList
from vrchatapi.models.api_config_events import APIConfigEvents
from vrchatapi.models.api_health import APIHealth
from vrchatapi.models.add_favorite_request import AddFavoriteRequest
from vrchatapi.models.add_group_gallery_image_request import AddGroupGalleryImageRequest
from vrchatapi.models.avatar import Avatar
from vrchatapi.models.avatar_unity_package_url_object import AvatarUnityPackageUrlObject
from vrchatapi.models.ban_group_member_request import BanGroupMemberRequest
from vrchatapi.models.create_avatar_request import CreateAvatarRequest
from vrchatapi.models.create_file_request import CreateFileRequest
from vrchatapi.models.create_file_version_request import CreateFileVersionRequest
from vrchatapi.models.create_group_announcement_request import CreateGroupAnnouncementRequest
from vrchatapi.models.create_group_gallery_request import CreateGroupGalleryRequest
from vrchatapi.models.create_group_invite_request import CreateGroupInviteRequest
from vrchatapi.models.create_group_request import CreateGroupRequest
from vrchatapi.models.create_group_role_request import CreateGroupRoleRequest
from vrchatapi.models.create_world_request import CreateWorldRequest
from vrchatapi.models.current_user import CurrentUser
from vrchatapi.models.deployment_group import DeploymentGroup
from vrchatapi.models.developer_type import DeveloperType
from vrchatapi.models.dynamic_content_row import DynamicContentRow
from vrchatapi.models.error import Error
from vrchatapi.models.favorite import Favorite
from vrchatapi.models.favorite_group import FavoriteGroup
from vrchatapi.models.favorite_group_visibility import FavoriteGroupVisibility
from vrchatapi.models.favorite_type import FavoriteType
from vrchatapi.models.file import File
from vrchatapi.models.file_data import FileData
from vrchatapi.models.file_status import FileStatus
from vrchatapi.models.file_upload_url import FileUploadURL
from vrchatapi.models.file_version import FileVersion
from vrchatapi.models.file_version_upload_status import FileVersionUploadStatus
from vrchatapi.models.finish_file_data_upload_request import FinishFileDataUploadRequest
from vrchatapi.models.friend_status import FriendStatus
from vrchatapi.models.group import Group
from vrchatapi.models.group_announcement import GroupAnnouncement
from vrchatapi.models.group_audit_log_entry import GroupAuditLogEntry
from vrchatapi.models.group_gallery import GroupGallery
from vrchatapi.models.group_gallery_image import GroupGalleryImage
from vrchatapi.models.group_join_state import GroupJoinState
from vrchatapi.models.group_limited_member import GroupLimitedMember
from vrchatapi.models.group_member import GroupMember
from vrchatapi.models.group_member_limited_user import GroupMemberLimitedUser
from vrchatapi.models.group_member_status import GroupMemberStatus
from vrchatapi.models.group_my_member import GroupMyMember
from vrchatapi.models.group_permission import GroupPermission
from vrchatapi.models.group_privacy import GroupPrivacy
from vrchatapi.models.group_role import GroupRole
from vrchatapi.models.group_role_template import GroupRoleTemplate
from vrchatapi.models.group_user_visibility import GroupUserVisibility
from vrchatapi.models.info_push import InfoPush
from vrchatapi.models.info_push_data import InfoPushData
from vrchatapi.models.info_push_data_article import InfoPushDataArticle
from vrchatapi.models.info_push_data_article_content import InfoPushDataArticleContent
from vrchatapi.models.info_push_data_clickable import InfoPushDataClickable
from vrchatapi.models.instance import Instance
from vrchatapi.models.instance_platforms import InstancePlatforms
from vrchatapi.models.instance_short_name_response import InstanceShortNameResponse
from vrchatapi.models.instance_type import InstanceType
from vrchatapi.models.invite_message import InviteMessage
from vrchatapi.models.invite_message_type import InviteMessageType
from vrchatapi.models.invite_request import InviteRequest
from vrchatapi.models.invite_response import InviteResponse
from vrchatapi.models.license import License
from vrchatapi.models.license_action import LicenseAction
from vrchatapi.models.license_group import LicenseGroup
from vrchatapi.models.license_type import LicenseType
from vrchatapi.models.limited_unity_package import LimitedUnityPackage
from vrchatapi.models.limited_user import LimitedUser
from vrchatapi.models.limited_world import LimitedWorld
from vrchatapi.models.mime_type import MIMEType
from vrchatapi.models.moderate_user_request import ModerateUserRequest
from vrchatapi.models.notification import Notification
from vrchatapi.models.notification_type import NotificationType
from vrchatapi.models.order_option import OrderOption
from vrchatapi.models.paginated_group_audit_log_entry_list import PaginatedGroupAuditLogEntryList
from vrchatapi.models.past_display_name import PastDisplayName
from vrchatapi.models.permission import Permission
from vrchatapi.models.player_moderation import PlayerModeration
from vrchatapi.models.player_moderation_type import PlayerModerationType
from vrchatapi.models.region import Region
from vrchatapi.models.release_status import ReleaseStatus
from vrchatapi.models.request_invite_request import RequestInviteRequest
from vrchatapi.models.respond_group_join_request import RespondGroupJoinRequest
from vrchatapi.models.response import Response
from vrchatapi.models.sent_notification import SentNotification
from vrchatapi.models.sort_option import SortOption
from vrchatapi.models.subscription import Subscription
from vrchatapi.models.subscription_period import SubscriptionPeriod
from vrchatapi.models.success import Success
from vrchatapi.models.transaction import Transaction
from vrchatapi.models.transaction_agreement import TransactionAgreement
from vrchatapi.models.transaction_status import TransactionStatus
from vrchatapi.models.transaction_steam_info import TransactionSteamInfo
from vrchatapi.models.transaction_steam_wallet_info import TransactionSteamWalletInfo
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.unity_package import UnityPackage
from vrchatapi.models.update_avatar_request import UpdateAvatarRequest
from vrchatapi.models.update_favorite_group_request import UpdateFavoriteGroupRequest
from vrchatapi.models.update_group_gallery_request import UpdateGroupGalleryRequest
from vrchatapi.models.update_group_member_request import UpdateGroupMemberRequest
from vrchatapi.models.update_group_request import UpdateGroupRequest
from vrchatapi.models.update_group_role_request import UpdateGroupRoleRequest
from vrchatapi.models.update_invite_message_request import UpdateInviteMessageRequest
from vrchatapi.models.update_user_request import UpdateUserRequest
from vrchatapi.models.update_world_request import UpdateWorldRequest
from vrchatapi.models.user import User
from vrchatapi.models.user_exists import UserExists
from vrchatapi.models.user_state import UserState
from vrchatapi.models.user_status import UserStatus
from vrchatapi.models.user_subscription import UserSubscription
from vrchatapi.models.verify2_fa_result import Verify2FAResult
from vrchatapi.models.verify_auth_token_result import VerifyAuthTokenResult
from vrchatapi.models.world import World
from vrchatapi.models.world_metadata import WorldMetadata
from vrchatapi.models.world_publish_status import WorldPublishStatus
