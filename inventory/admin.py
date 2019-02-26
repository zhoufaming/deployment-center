# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hosts
from .models import PrivateKey

class HostAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'host_name', 'ansible_ssh_user', 'ansible_ssh_pass', 'ansible_ssh_port', 'ansible_ssh_key',)


# admin.site.register(Program)
admin.site.register(PrivateKey)
admin.site.register(Hosts, HostAdmin)

# Register your models here.
