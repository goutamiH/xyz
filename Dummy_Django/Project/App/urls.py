from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

  
  
urlpatterns = [  
   path('',views.nope,name='nope'), 
   path('home/',views.home,name='home'), 
   path('register/',views.registerUser,name='register'),
   path('login/',views.LoginUser,name='login'),
    path('logout/', views.logout_request, name= 'logout'),
    path('about-us/',views.About,name="about-us"),
    path('contact-us/',views.Contact,name="contact-us"),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('move',views.move,name='move'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('profile/<str:pk>/',views.userprofile,name='profile'),
    path('update-user/<str:pk>/',views.Update_user,name="update-user"),
    path('topics/',views.Topics_collection,name='topics'),
    path('Recent-Activities/',views.Activity_Page,name='Recent-Activities'),
    path('Dairy-Writing/',views.DairyModule,name="Dairy-Writing"),
    path('<pk>/update_diary/',views.DiaryUpdateView.as_view(),name="update_diary"),
    path('<pk>/delete_diary/',views.DiaryDeleteView.as_view(),name="delete_diary"),
    path('Share-a-story',views.ShareStory,name="Share-a-story"),
]  
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)