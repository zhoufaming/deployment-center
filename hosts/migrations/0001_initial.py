# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '\u90e8\u95e8\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u90e8\u95e8\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='DICUSER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('telphone', models.CharField(blank=True, max_length=32, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe5\x9c\xb0\xe5\x9d\x80')),
                ('customer_id', models.CharField(blank=True, max_length=128, null=True, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5id')),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('create_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7ba1\u7406\u5458\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7ba1\u7406\u5458\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name=b'\xe8\x99\x9a\xe6\x8b\x9f\xe6\x9c\xbaIP')),
                ('internal_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('usename', models.CharField(blank=True, default=b'root', max_length=64, null=True, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=128, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe5\xaf\x86\xe7\xa0\x81')),
                ('ssh_port', models.IntegerField(blank=True, default=22, null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x8f\xb7')),
                ('status', models.SmallIntegerField(choices=[(0, '\u6b63\u5e38'), (1, '\u5173\u673a'), (2, '\u65e0\u6cd5\u8fde\u63a5'), (3, '\u5f02\u5e38')], default=0, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8a\xb6\xe6\x80\x81')),
                ('brand', models.CharField(choices=[('DELL', 'DELL'), ('HP', 'HP'), ('\u865a\u62df\u673a', '\u865a\u62df\u673a'), ('Other', 'Other')], default='\u865a\u62df\u673a', max_length=64, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('cpu', models.CharField(max_length=64, verbose_name=b'cpu\xe6\x95\xb0')),
                ('core_num', models.SmallIntegerField(choices=[(2, b'2 Cores'), (4, b'4 Cores'), (6, b'6 Cores'), (8, b'8 Cores'), (10, b'10 Cores'), (12, b'12 Cores'), (14, b'14 Cores'), (16, b'16 Cores'), (18, b'18 Cores'), (20, b'20 Cores'), (22, b'22 Cores'), (24, b'24 Cores'), (26, b'26 Cores'), (28, b'28 Cores')], verbose_name=b'\xe6\xa0\xb8\xe5\xbf\x83\xe6\x95\xb0')),
                ('hard_disk', models.IntegerField(verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe5\xae\xb9\xe9\x87\x8f')),
                ('memory', models.IntegerField(verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xae\xb9\xe9\x87\x8f')),
                ('system', models.CharField(choices=[('CentOS', 'CentOS'), ('FreeBSD', 'FreeBSD'), ('Ubuntu', 'Ubuntu')], max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
                ('system_version', models.CharField(choices=[('CentOS 7.2', 'CentOS 7.2'), ('FreeBSD', 'FreeBSD'), ('Ubuntu', 'Ubuntu')], default='CentOS 7.2', max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\x89\x88\xe6\x9c\xac')),
                ('system_arch', models.CharField(choices=[('x86_64', 'x86_64'), ('i386', 'i386')], max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe4\xbd\x8d\xe6\x95\xb0')),
                ('create_time', models.DateField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('service_type', models.CharField(choices=[(b'moniter', '\u76d1\u63a7\u4e3b\u673a'), (b'cluster', '\u96c6\u7fa4'), (b'db', '\u6570\u636e\u5e93'), (b'office', '\u529e\u516c'), (b'test', '\u5f00\u53d1\u6d4b\u8bd5'), (b'storge', '\u5b58\u50a8'), (b'web', 'WEB\u670d\u52a1'), (b'email', 'Email\u670d\u52a1\u5668'), (b'mix', '\u7efc\u5408')], max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0(\xe7\x94\xa8\xe9\x80\x94)')),
                ('remark', models.TextField(blank=True, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosts.DICUSER')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u8d44\u4ea7\u8868',
                'verbose_name_plural': '\u4e3b\u673a\u8d44\u4ea7\u8868',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='hosts',
            field=models.ManyToManyField(blank=True, related_name='departments', to='hosts.Host', verbose_name='Hosts'),
        ),
    ]
