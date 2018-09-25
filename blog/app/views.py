from audioop import reverse

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,reverse

from app.forms import UserForm, UserLoginForm ,TextFrom


# 注册
from app.models import TextUpload


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        #校验页面中传递的参数，是否填写完整

        form = UserForm(request.POST)
        #is_valid():判断表单是否验证通过
        if form.is_valid():
            #获取校验后的用户名和密码
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #创建普通用户create_user,超级用户create_superuser
            User.objects.create_user(username=username,password=password)
            #实现跳转
            return render(request,'register.html')
        else:
            return render(request,'register.html',{'form':form})


# 登录
def login(request):
    if request.method == 'GET':
        return  render(request,'login.html')

    if request.method == 'POST':
            #表单验证,用户名和密码是否填写，校验用户名是否注册
        form = UserLoginForm(request.POST)
        # is_valid():判断表单是否验证通过
        if form.is_valid():
            #检验用户名和密码，判断返回的对象是否为空
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user:
                #用户名和密码是正确的登录
                auth.login(request,user)
                return render(request,'index.html')
            else:
                #密码不正确
                pass
                return render(request,'login.html',{'error':'密码错误'})


        else:
            return render(request,'login.html',{'form':form})


# 主界面
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')


# 文章
def article(request):
    if request.method == 'GET':
        text=TextUpload.objects.all()
        return render(request,'article.html',{'textupload':text})


# 添加文章
def add_article(request):
    if request.method == 'GET':
        return render(request,'add-article.html')
    if request.method == 'POST':
        text = TextFrom(request.POST)
        if text.is_valid():
            #获取文本类容
            title = text.cleaned_data['title']
            content = text.cleaned_data['content']
            keywords = text.cleaned_data['keywords']
            describe = text.cleaned_data['describe']
            TextUpload.objects.create(title=title,keywords=keywords,describe=describe,content=content)
            return render(request,'article.html')


# 修改文章
def update_article(request,num):
    if request.method == 'GET':
        return render(request,'update-article.html')


# 公告
def notice(request):
    if request.method == 'GET':
        return render(request,'notice.html')


# 添加公告
def add_notice(request):
    if request.method == 'GET':
        return render(request,'add-notice.html')


# 评论
def comment(request):
    if request.method == 'GET':
        return render(request,'comment.html')


# 栏目
def category(request):
    if request.method == 'GET':
        return render(request,'category.html')


# 添加栏目
def add_category(request):
    if request.method == 'GET':
        return render(request,'add-category.html')


# 修改栏目
def update_category(request):
    if request.method == 'GET':
        return render(request,'update-article.html')


# 友情链接
def flink(request):
    if request.method == 'GET':
        return render(request,'flink.html')


# 添加友情链接
def add_flink(request):
    if request.method == 'GET':
        return render(request,'add-flink.html')


# 修改友情链接
def update_flink(request):
    if request.method == 'GET':
        return render(request,'update-flink.html')


# 访问记录
def loginlog(request):
    if request.method == 'GET':
        return render(request,'loginlog.html')


# 管理用户
def manage_user(request):
    if request.method == 'GET':
        return render(request,'manage-user.html')


# 基本设置
def setting(request):
    if request.method == 'GET':
        return render(request,'setting.html')


# 用户设置
def readset(request):
    if request.method == 'GET':
        return render(request,'readset.html')


# 展示页面
def webindex(request):
    if request.method == 'GET':
        text = TextUpload.objects.all()
        return render(request,'webindex.html',{'textupload':text})


# 删除
def delete_article(request,num):
    if request.method == 'GET':
        TextUpload.objects.filter(id=num).delete()
        return render(request,'article.html')
