from django.contrib import admin

# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
