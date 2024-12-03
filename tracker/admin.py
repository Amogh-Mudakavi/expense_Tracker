from django.contrib import admin
from tracker.models import *



class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "amount" , 
        "current_balance",
        "expense_type",
        "description",
        "created_at",
        "display_age"
    ]
  
    search_fields = [
        'expense_type',
        'description'
    ]

    def display_age(self , obj):
        return "this is a field"

    ordering = ['-expense_type']
    list_filter = ['expense_type']


admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory , TrackingHistoryAdmin)