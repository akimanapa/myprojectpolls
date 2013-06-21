from django.contrib import admin

from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
	 
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)
#from polls.models import Poll

#class PollAdmin(admin.ModelAdmin):
     #fieldsets = [
        #(None,               {'fields': ['question']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]

#admin.site.register(Poll, PollAdmin)




