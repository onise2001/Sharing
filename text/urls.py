from django.urls import path
from .views import add_text, show_and_edit_text, edit_text


urlpatterns = [
    path("", add_text),
    path("texts/<int:id>", show_and_edit_text, name="texts"),
    #path("edit_text/<int:id>", edit_text),
]
