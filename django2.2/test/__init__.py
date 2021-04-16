from .base import main


if __name__ == "__main__":
    main()  # 全部测试
    # ./manage.py test <文件夹>.<文件>  # 单文件测试 
    # ./manage.py test <文件夹>.<文件>.<类名>  # 类测试 
    # ./manage.py test <文件夹>.<文件>.<类名>.<方法>  # 方法测试 
    
    #  ./manage.py test test.base.logger  # 例子
