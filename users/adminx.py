import xadmin
from .models import EmailVerifyRecord
from .models import UserProfile
from .models import Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class UserProfileAdmin(object):
    list_display = ['name', 'gender', 'adress', 'mobile' ]
    search_fields = ['name', 'gender', 'adress', 'mobile' ]
    list_filter= ['name', 'gender', 'adress', 'mobile' ]



class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)


