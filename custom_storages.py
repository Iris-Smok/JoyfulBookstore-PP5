"""custom storages"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """static custom storages"""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """media custom storages"""
    location = settings.MEDIAFILES_LOCATION
