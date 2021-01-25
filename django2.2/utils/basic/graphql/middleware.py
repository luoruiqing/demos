
class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        if info.field_name == 'user':
            return None
        return next(root, info, **args)

# def login_required(func):
#     ''' 未登录返回空 '''
#     @functools.wraps(func)
#     def warpper(self, info, args, **kwargs):
#         if not args.context.user.is_authenticated:
#             return None
#         with reversion.create_revision():  # 记录历史
#             result = func(self, info, args, **kwargs) # 执行
#             reversion.set_user(args.context.user)
#             reversion.set_comment(f"[Grap] 变更.")  # 设置版本的标注
#         return result
#     return warpper 
