from unicodedata import name
from django.urls import path 
from .views import AddIssue, ListIssue, IssueDetail, IssueUpdate , IssueDelete


urlpatterns = [ 
    path('listIssue', ListIssue.as_view(), name='listIssue'),
    path('addIssue',AddIssue.as_view(), name='addIssue'),
    path('issueDetail/<int:pk>',IssueDetail.as_view(), name='issueDetail'),
    path('issueUpdate/<int:pk>', IssueUpdate.as_view(), name ='issueUpdate'),
    path('issueDelete/<int:pk>',IssueDelete.as_view(), name = 'issueDelete' )
]