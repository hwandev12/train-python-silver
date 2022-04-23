# In main settings.py we need import some files
from django.contrib import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LogoutView.as_view(), name='login'),
]
# With that way we need to create a template inside registration folder logout template
