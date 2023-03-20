from django.urls import path
from .views import (
    PositionListView, 
    SkillListView,
    ApplicationCreateView,
    ApplicationListView,
    ApplicationDetailRetrieveView,
    ApplicationStatusUnreadUpdateView,
    ApplicationStatusReadUpdateView,
    ApplicationStatusInterview1UpdateView,
    ApplicationStatusInterview2UpdateView,
    ApplicationStatusInterview3UpdateView,
    ApplicationStatusAcceptedUpdateView,
    ApplicationStatusArchivedUpdateView,
    ApplicationStatusRejectedUpdateView
)

# paths
app_name = 'application'

urlpatterns = [
    # public
    path('positions/', PositionListView.as_view(), name="position-list-view"),
    path('skills/', SkillListView.as_view(), name='skill-list-view'),
    path('apply/', ApplicationCreateView.as_view(), name='application-create-view'),

    # private
    path('applications/', ApplicationListView.as_view(), name='application-list-view'),
    path('applications/<int:application_id>/', ApplicationDetailRetrieveView.as_view(), name='application-detail-retrieve-view'),
    path('applications/<int:application_id>/status/unread', ApplicationStatusUnreadUpdateView.as_view(), name='application-status-unread-update-view'),
    path('applications/<int:application_id>/status/read', ApplicationStatusReadUpdateView.as_view(), name='application-status-read-update-view'),
    path('applications/<int:application_id>/status/interview-1', ApplicationStatusInterview1UpdateView.as_view(), name='application-status-interview-1-update-view'),
    path('applications/<int:application_id>/status/interview-2', ApplicationStatusInterview2UpdateView.as_view(), name='application-status-interview-2-update-view'),
    path('applications/<int:application_id>/status/interview-3', ApplicationStatusInterview3UpdateView.as_view(), name='application-status-interview-3-update-view'),
    path('applications/<int:application_id>/status/accepted', ApplicationStatusAcceptedUpdateView.as_view(), name='application-status-accepted-update-view'),
    path('applications/<int:application_id>/status/rejected', ApplicationStatusRejectedUpdateView.as_view(), name='application-status-rejected-update-view'),
    path('applications/<int:application_id>/status/archived', ApplicationStatusArchivedUpdateView.as_view(), name='application-status-archived-update-view'),







]