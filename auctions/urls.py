from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listing>", views.listing, name="listing"),
    path("create", views.create, name="create"),
    path("create_new", views.create_new, name="create_new"),
    path("close/<str:listing>", views.close_bids, name="close_bids"),
    path("my_watchlist", views.my_watchlist, name="my_watchlist"),
    path("add_to_wl/<str:listing>", views.add_to_wl, name="add_to_wl"),
    path("comment", views.comment, name="comment"),
    path("place_bid/<str:listing>", views.place_bid, name="place_bid")
]
