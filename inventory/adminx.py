import xadmin
from .models import Hosts
from .models import PrivateKey


class HostsAdmin(object):
    list_display = ['group_name', 'host_name', 'ansible_ssh_user', 'ansible_ssh_pass', 'ansible_ssh_port', 'ansible_ssh_key']
    search_fields = ['group_name', 'host_name', 'ansible_ssh_key']
    list_filter = ['group_name', 'host_name', 'ansible_ssh_key', 'ansible_ssh_user', 'ansible_ssh_pass', 'ansible_ssh_port']


class PrivateKeyAdmin(object):
    list_display = ['key_name', 'private_key', 'public_key']
    search_fields = ['key_name']
    list_filter = ['key_name']


xadmin.site.register(Hosts,HostsAdmin)
xadmin.site.register(PrivateKey, PrivateKeyAdmin)

