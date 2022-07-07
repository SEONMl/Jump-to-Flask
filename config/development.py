# 개발 환경을 담당
from config.default import *

SQLACHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
SQLALCEHMY_TRACK_MODIFICATIONS =False
SECRET_KET='dev'