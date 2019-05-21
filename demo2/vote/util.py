from django.shortcuts import redirect, reverse


# 调用流程
# 将index函数作为fun实参传入checklogin 并且执行执行check()
def checklogin(fun):

    def check(request, *args):

        if request.user and request.user.is_authenticated:
            return fun(request, *args)

        else:

            return redirect(reverse('vote:login'))
    return check