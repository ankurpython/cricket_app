from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from rest.views import *

score = DefaultRouter()
score.register('batting_player_score', BattingPlayerScore, basename='batting_player_score')
score.register('bowling_player_score', BowlingPlayerScore, basename='bowling_player_score')
score.register('match_score', MatchScore, basename='match_score')

urlpatterns = [
    path('', include(score.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token'),

    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # its uses token authentication
    # url(r'^', include('rest_auth.urls'))
]


