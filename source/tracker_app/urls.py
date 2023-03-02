from django.urls import path
from tracker_app.views.base import IndexView

from tracker_app.views.issues_view import IssueAddView, IssueDetail, IssueUpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexView.as_view(), name='index'),
    path('issue/add/', IssueAddView.as_view(), name='add_issue'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='update_issue'),
    path('issue/<int:pk>/delete', DeleteView.as_view(), name='delete_issue'),

]
