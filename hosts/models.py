# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, u"正常"),
    (1, u"关机"),
    (2, u"无法连接"),
    (3, u"异常"),
)
SERVICE_TYPES = (
    ('moniter', u"监控主机"),
    ('cluster', u"集群"),
    ('db', u"数据库"),
    ('office', u"办公"),
    ('test', u"开发测试"),
    ('storge', u"存储"),
    ('web', u"WEB服务"),
    ('email', u"Email服务器"),
    ('mix', u"综合"),
)


@python_2_unicode_compatible
class DICUSER(models.Model):
    name = models.CharField(max_length=64, verbose_name=u"姓名")
    telphone = models.CharField(max_length=32, verbose_name="联系电话", blank=True, null=True)
    address = models.CharField(max_length=128, verbose_name="联系地址", blank=True, null=True)
    customer_id = models.CharField(max_length=128, verbose_name='员工id', blank=True, null=True)
    description = models.TextField(verbose_name="描述", blank=True, null=True)


    create_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"管理员信息表"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Host(models.Model):
    user = models.ForeignKey(DICUSER, verbose_name='管理员')
    name = models.CharField(max_length=64, verbose_name='主机名')
    ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='虚拟机IP')
    internal_ip = models.GenericIPAddressField(blank=True, null=True)
    usename = models.CharField(max_length=64, default="root", blank=True, null=True, verbose_name='管理员用户名')
    password = models.CharField(max_length=128, verbose_name='管理员密码')
    ssh_port = models.IntegerField(blank=True, null=True, default=22, verbose_name='端口号')
    status = models.SmallIntegerField(choices=SERVER_STATUS, default=0, verbose_name='使用状态')
    brand = models.CharField(max_length=64, choices=[(i, i) for i in (u"DELL", u"HP", u"虚拟机", u"Other")], default=u"虚拟机",  verbose_name='品牌')
    cpu = models.CharField(max_length=64, verbose_name='cpu数')
    core_num = models.SmallIntegerField(choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)], verbose_name='核心数')
    hard_disk = models.IntegerField(verbose_name='硬盘容量')
    memory = models.IntegerField(verbose_name='内存容量')
    system = models.CharField( max_length=32, choices=[(i, i) for i in (u"CentOS", u"FreeBSD", u"Ubuntu")], verbose_name='系统名称')
    system_version = models.CharField(max_length=32, choices=[(i, i) for i in (u"CentOS 7.2", u"FreeBSD", u"Ubuntu")], default=u"CentOS 7.2", verbose_name='系统版本')
    system_arch = models.CharField(max_length=32, choices=[(i, i) for i in (u"x86_64", u"i386")], verbose_name='系统位数')
    create_time = models.DateField(verbose_name='创建时间')
    service_type = models.CharField(max_length=32, choices=SERVICE_TYPES, verbose_name='服务类型')
    description = models.TextField(verbose_name='描述(用途)', blank=True, null=True)
    remark = models.TextField(verbose_name='备注', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"主机资产表"
        verbose_name_plural = verbose_name





@python_2_unicode_compatible
class Department(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    hosts = models.ManyToManyField(
        Host, verbose_name=u'Hosts', blank=True, related_name='departments')

    class Meta:
        verbose_name = u"部门信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



