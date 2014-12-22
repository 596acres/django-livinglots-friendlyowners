from django.contrib import admin


class FriendlyOwnerAdminMixin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone', 'notes', 'parcels', 'lot', 'added',)
    list_display = ('name', 'email', 'phone', 'lot', 'added',)
    readonly_fields = ('added', 'lot', 'parcels',)
