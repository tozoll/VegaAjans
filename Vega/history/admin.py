from django.contrib import admin
from .models import HistoryHeader,HistoryYears

# Register your models here.

class HistoryHeaderAdmin(admin.ModelAdmin):
  list_display = ('id', 'header', 'content','created','updated','created_by')
  list_display_links = ('id', 'header')
#   list_filter = ('header',)
#   list_editable = ('header','content')
#   search_fields = ('header',)
  list_per_page = 25

class HistoryYearsAdmin(admin.ModelAdmin):
  list_display = ('id', 'year','content','created','updated','created_by')
  list_display_links = ('id', 'year','content')
#   list_filter = ('realtor',)
#   list_editable = ('year','content')
#   search_fields = ('name',)
#   list_per_page = 25

admin.site.register(HistoryHeader, HistoryHeaderAdmin)
admin.site.register(HistoryYears, HistoryYearsAdmin)


