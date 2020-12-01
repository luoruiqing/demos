set -e                                                              # 严格模式
cd $(dirname $0) && cd ..                                           # 进入目录
source .venv/bin/activate                                           # 虚拟环境
pip install -i https://pypi.douban.com/simple/ -r ./requirement.txt # 安装依赖
# 测试
python manage.py test
# 启动
python manage.py runserver
# 异步任务
python manage.py celery beat # 定时任务生产者(只启动一个)
python manage.py celery worker # 异步任务消费者