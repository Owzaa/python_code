import datetime
AWS_ACCESS_KEY_ID = "AKIAXOPGFALJMIP57IGZ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'webfile.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'webfile.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'awsuploadfiles'
S3DIRECT_REGION = 'eu-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
AWS_LOCATION = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = AWS_LOCATION + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}