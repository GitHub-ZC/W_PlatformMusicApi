import os

# HOST = 'iecoxe.top'
# PORT = '3306'
# DATABASE = 'Blog'
# USERNAME = 'test'
# PASSWORD = 'Zheng123.'
#
# DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)


DEBUG=True
BASE_URL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库配置
# SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = False

# 邮箱配置
# MAIL_SERVER = 'smtp.163.com'
# MAIL_PORT = 994
# MAIL_USE_SSL = True
# MAIL_USE_TLS = False
# MAIL_USERNAME = 'i153140965@163.com'
# MAIL_PASSWORD = 'YGFXZKVOAOINAAZC'


# 缓存
# CACHE_TYPE = 'simple'
# CACHE_REDIS_HOST = 'iecoxe.top'
# CACHE_REDIS_PORT = '6379'