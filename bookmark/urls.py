from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # bookmark:list
    path('add/', BookmarkCreateView.as_view(), name='add'),  # bookmark:add
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),   # bookmark:detail
    path('edit/<int:pk>/', BookmarkUpdateView.as_view(), name='edit'),      # bookmark:edit
]