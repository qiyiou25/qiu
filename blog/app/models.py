from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    password = models.CharField(max_length=255, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'users'


class UserTicket(models.Model):
    user = models.ForeignKey(Users)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'user_ticket'


class TextUpload(models.Model):
    title = models.CharField(max_length=15, unique=True, verbose_name='标题')
    content = models.CharField(max_length=255, unique=True, verbose_name='内容')
    keywords = models.CharField(max_length=20, unique=True, verbose_name='关键字')
    describe = models.CharField(max_length=30, unique=True, verbose_name='描述')

    class Meta:
        db_table = 'text_upload'