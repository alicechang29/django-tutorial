from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# tell the admin that Question objects have an admin interface.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# “Choice objects are edited on the Question admin page.
# By default, provide enough fields for 3 choices.”


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets are a visual divider between sets of fields
    # The first element of each tuple in fieldsets is the title of the fieldset.
    # Note on field label - Django auto-generates it if no verbose_name is provided wihin Question models
    # fields are displayed in order listed
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": [
         "pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    # use the list_display admin option, which is a list of field names to
    # adds columns on the change list page for the object with values:
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # That adds a “Filter” sidebar that lets people filter the change list by the pub_date field:
    list_filter = ["pub_date"]
    # adds a search bar (uses LIKE query - so limit the fields that are searched)
    search_fields = ["question_text"]


# create a model admin class, then pass it as the second argument to
# admin.site.register() – any time you need to change the admin
# options for a model.
admin.site.register(Question, QuestionAdmin)
