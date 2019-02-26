#--*-- coding:utf8 --*--
from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import DICUSER, Host, Department
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    widgets = [
        [

            {"type": "list", "model": "hosts.host"},
        ],
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"model": Host}, {"model": DICUSER}, {"title": "Zabbix", "url": "http://172.20.0.200/zabbix/zabbix.php?action=dashboard.view"}]},

        ]
    ]




@xadmin.sites.register(DICUSER)
class USERAdmin(object):
    list_display = ("name", "description", "create_time", "telphone", "address", "customer_id")
    list_display_links = ("name",)
    wizard_form_list = [
        ("First's Form", ("name", "description")),
        ("Second Form", ( "telphone", "address")),
        ("Thread Form", ("customer_id",))
    ]
    search_fields = ["name", "description", "telphone", "address"]
    list_filter = [
        "name"
    ]
    list_quick_filter = [{"field": "name", "limit": 10}]

    search_fields = ["name"]
    relfield_style = "fk-select"
    reversion_enable = True

    actions = [BatchChangeAction, ]
    batch_fields = ("description", "address", "customer_id")


@xadmin.sites.register(Host)
class HostAdmin(object):
    def open_web(self, instance):
        return """<a href="http://%s" target="_blank">Open</a>""" % instance.ip

    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True

    list_display = (
        "name", "user", "service_type", "status",
        "description", "ip",
    )
    list_display_links = ("name",)

    raw_id_fields = ("user",)
    style_fields = {"system": "radio-inline"}

    search_fields = ["name", "ip", "description"]
    list_filter = [
        "user",  "status", "brand",  "cpu", "core_num",
        "hard_disk", "memory", (
            "service_type",
            xadmin.filters.MultiSelectFieldListFilter,
        ),
    ]

    list_quick_filter = ["service_type", {"field": "user__name", "limit": 10}]
    # list_quick_filter = ["idc_id"]
    list_bookmarks = [{
        "title": "Need Guarantee",
        "query": {"status__exact": 2},
        "cols": ("brand", "service_type"),
    }]

    show_detail_fields = ("user",)
    list_editable = (
        "name", "user", "service_type", "description", "ip"
    )
    save_as = True

    grid_layouts = ("table", "thumbnails")

    form_layout = (
        Main(
            TabHolder(
                Tab(
                    "Main Infomations",
                    Fieldset(
                        u"绑定管理员", "name", "user",
                        description="some comm fields, required",
                    )
                ),
                Tab(
                    "detail Infomations",
                    Fieldset(
                        "Detailed configuration",
                        "service_type",
                        Row("brand"),
                        Row("cpu", "core_num"),
                        Row(
                            AppendedText("hard_disk", "G"),
                            AppendedText("memory", "G")
                        ),

                    ),
                ),
            ),
        ),
        Side(
            Fieldset("Status data", "status", "ssh_port", "ip"),
        )
    )
    reversion_enable = True

    # data_charts = {
    #     "host_service_type_counts": {'title': u"Host service type count", "x-field": "service_type",
    #                                  "y-field": ("service_type",),
    #                                  "option": {
    #                                      "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
    #                                      "xaxis": {"aggregate": "count", "mode": "categories"},
    #                                  },
    #                                  },}


@xadmin.sites.register(Department)
class DepartmentAdmin(object):
    list_display = ("name", "description")
    list_display_links = ("name",)

    search_fields = ["name"]
    style_fields = {"hosts": "checkbox-inline"}





