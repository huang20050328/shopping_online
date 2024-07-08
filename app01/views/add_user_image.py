from utils.uploads import getNewName
import os
from app01.models import user_info
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404


def add_user_image(request):
    return render(request, 'add_user_image.html')


def upload_handle(request):
    # 获取一个文件管理器对象
    file = request.FILES['pic']

    # 保存文件
    new_name = getNewName('avatar')  # 具体实现在自己写的uploads.py下
    print(settings.MEDIA_ROOT)
    print(settings.BASE_DIR)
    # 将要保存的地址和文件名称
    where = '%s/img/%s' % (settings.MEDIA_ROOT, new_name)
    # 分块保存image
    content = file.chunks()
    with open(where, 'wb') as f:
        for i in content:
            f.write(i)

    # 上传文件名称到数据库
    user_info.objects.filter(name='用户1').update(image=new_name)
    # 返回的httpresponse
    return HttpResponse('ok')


def show_avatar(request):
    user = user_info.objects.filter(name='用户1')[0]
    avatarName = str(user.image)
    # avatarUrl = '%s/users/%s' % (settings.MEDIA_URL, avatarName) # 另一种写法
    avatarUrl = os.path.join(settings.MEDIA_URL, 'img', avatarName)
    avatar_info = {'userName': '用户1', 'avatarUrl': avatarUrl}
    return render(request, 'show_avatar.html', {'avatar_info': avatar_info})
