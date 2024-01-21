import pyotp
username='A54248437'
password='1212'
apikey='cXj9f8yW'
tok = "SPP2QWLVG6X44EBESSVS7BJKPM"
totp=pyotp.TOTP(tok).now()
feed_token=None
token_map=None      