from django.contrib import admin
from leagues.models import *

class LeagueAdmin(admin.ModelAdmin):
  list_display = ('name',)

class PlayerAdmin(admin.ModelAdmin):
  list_display = ('name','account','rating','league',)

class GameAdmin(admin.ModelAdmin):
  list_display = ('league','date_created')

class RankAdmin(admin.ModelAdmin):
  list_display = ('game','player','rank',)

admin.site.register(League, LeagueAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Rank, RankAdmin)