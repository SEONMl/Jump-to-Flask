import os

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# os.path.dirname을 한 번 더 사용하여 BASE_DIR을 설정한 것이다
# projects/myproject/config/default.py에서 os.path.dirname을 2번 사용했으므로 BASE_DIR에는 projects/myproject가 대입된다.