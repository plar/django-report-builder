from django.conf.urls import url, include
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import routers
from . import views
from .api import views as api_views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'reports', api_views.ReportViewSet)
router.register(r'report', api_views.ReportNestedViewSet)
router.register(r'formats', api_views.FormatViewSet)
router.register(r'filterfields', api_views.FilterFieldViewSet)
router.register(r'contenttypes', api_views.ContentTypeViewSet)

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
   url(r'^report/(?P<pk>\d+)/download_file/$', permission_required('report_builder.view_report')(views.DownloadFileView.as_view()), name="report_download_file"),
    url('^report/(?P<pk>\d+)/download_file/(?P<filetype>.+)/$', permission_required('report_builder.view_report')(views.DownloadFileView.as_view()), name="report_download_file"),
    url('^report/(?P<pk>\d+)/check_status/(?P<task_id>.+)/$', permission_required('report_builder.view_report')(views.check_status), name="report_check_status"),
    url('^report/(?P<pk>\d+)/add_star/$', permission_required('report_builder.view_report')(views.ajax_add_star), name="ajax_add_star"),
    url('^report/(?P<pk>\d+)/toggle_general_report/$', staff_member_required(views.ajax_toggle_general_report), name="ajax_toggle_general_report"),
    url('^report/(?P<pk>\d+)/create_copy/$', permission_required('report_builder.view_report')(views.create_copy), name="create_copy"),
    url('^export_to_report/$', permission_required('report_builder.view_report')(views.ExportToReport.as_view()), name="export_to_report"),
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/related_fields', login_required(api_views.RelatedFieldsView.as_view()), name="related_fields"),
    url(r'^api/fields', login_required(api_views.FieldsView.as_view()), name="fields"),
    url(r'^api/report/(?P<report_id>\w+)/generate/', login_required(api_views.GenerateReport.as_view()), name="generate_report"),
    url('^report/(?P<pk>\d+)/$', views.ReportSPAView.as_view(), name="report_update_view"),
]

if not hasattr(settings, 'REPORT_BUILDER_FRONTEND') or settings.REPORT_BUILDER_FRONTEND:
    urlpatterns += [
        url(r'^', login_required(views.ReportSPAView.as_view()), name="report_builder"),
    ]
