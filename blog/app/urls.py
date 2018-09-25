from django.conf.urls import url

from app import views


urlpatterns = [
    # 注册
    url(r'^register/', views.register,name='register'),
    # 登录
    url(r'^login/', views.login,name='login'),
    # 主界面
    url(r'^index/', views.index,name='index'),
    # 文章
    url(r'^article/', views.article, name='article'),
    # 公告
    url(r'^notice/', views.notice, name='notice'),
    # 评论
    url(r'^comment/', views.comment, name='comment'),
    # 栏目
    url(r'^category/', views.category, name='category'),
    # 友情链接
    url(r'^flink/', views.flink, name='flink'),
    # 访问记录
    url(r'^loginlog/', views.loginlog, name='loginlog'),
    # 管理用户
    url(r'^manage_user/', views.manage_user, name='manage-user'),
    # 基本设置
    url(r'^setting/', views.setting, name='setting'),
    # 用户设置
    url(r'^readset/', views.readset, name='readset'),
    # 添加文章
    url(r'^add_article/', views.add_article, name='add-article'),
    # 添加栏目
    url(r'^add_category/', views.add_category, name='add-category'),
    # 添加友情链接
    url(r'^add_flink/', views.add_flink, name='add-flink'),
    # 添加公告
    url(r'^add_notice/', views.add_notice, name='add-notice'),
    # 修改文章
    url(r'^update_article/(?P<num>\d+)', views.update_article, name='update_article'),
    # 修改栏目
    url(r'^update_category/', views.update_category, name='update-category'),
    # 修改友情链接
    url(r'^update_flink/', views.update_flink, name='update-flink'),
    # 删除文章
    url(r'^delete_article/(?P<num>\d+)',views.delete_article,name='delete_article'),
    # 展示页面
    url(r'^webindex/',views.webindex,name='webindex')
]