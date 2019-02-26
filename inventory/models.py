# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Hosts(models.Model):
    
    group_name = models.CharField(max_length=32, verbose_name="组名")
    host_name = models.GenericIPAddressField(max_length=64, verbose_name="主机名")
    ansible_ssh_user = models.CharField(max_length=32, verbose_name="连接被管理主机的用户", default='root')
    ansible_ssh_pass = models.CharField(max_length=64, verbose_name="连接被管理主机的密码", blank=True, null=True)
    ansible_ssh_port = models.IntegerField(verbose_name="被管理主机的SSH端口号", default=22)
    ansible_sudo = models.CharField(max_length=32, verbose_name="是否启动sudo", blank=True, null=True)
    ansible_sudo_pass = models.CharField(max_length=64, verbose_name="sudo密码", blank=True, null=True)
    ansible_sudo_exe = models.CharField(max_length=128, verbose_name="sudo路径", blank=True, null=True)
    ansible_connection = models.CharField(max_length=32, verbose_name="ssh连接方式", blank=True, null=True)
    ansible_ssh_key = models.CharField(max_length=16, verbose_name="ssh的key名称", blank=True, null=True)
    ansible_shell_type = models.CharField(max_length=16, verbose_name="被管理主机的shell类型", blank=True, null=True)
    ansible_python_interpreter = models.CharField(max_length=128, verbose_name="被被管理主机的python编译器路径", blank=True, null=True)
    ansible_other_interpreter = models.CharField(max_length=128, verbose_name="被管理主机的其他编译器路径，未使用", blank=True, null=True)

    def __unicode__(self):
        return self.host_name

    class Meta:
        verbose_name_plural = 'inventory表'
        db_table = "hosts"
        unique_together = ("group_name", "host_name")


class PrivateKey(models.Model):
    key_name = models.CharField(max_length=16, verbose_name="密钥名", primary_key=True)
    private_key = models.TextField(verbose_name="密钥内容", blank=True, null=True)
    public_key = models.TextField(verbose_name="公钥内容", blank=True, null=True)

    def __unicode__(self):

        return self.key_name

    class Meta:
        verbose_name_plural = 'private_key表'
        db_table = "private_key"
