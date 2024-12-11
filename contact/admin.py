from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'recieved_at', 'anwser', 'anwsered', 'anwsered_at')
    date_hierarchy = 'recieved_at'
    search_fields = ('name', 'email', 'phone', 'message', 'recieved_at')
    list_filter = ('anwsered', 'recieved_at')
    actions = ['mark_as_answered', ]

    def contact_today(self, obj):
        return obj.recieved_at.date() == now().date()
    
    contact_today.short_description = "Recebido hoje?"
    contact_today.boolean = True

    def mark_as_answered(self, request, queryset):
        count = queryset.update(anwsered=True, anwsered_at=now())

        for contact in queryset:
            if contact.anwser:
                send_mail(
                    f"Resposta ao seu contato - {contact.name}",
                    contact.anwser, 
                    settings.DEFAULT_FROM_EMAIL,
                    [contact.email, settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )

        self.message_user(request, f'{count} contato(s) foi(ram) marcado(s) como respondido(s).')

    mark_as_answered.short_description = 'Marcar como respondido'

    def save_model(self, request, obj, form, change):
        if obj.anwser:
            obj.anwsered = True
            obj.anwsered_at = now()

        super().save_model(request, obj, form, change)

admin.site.register(Contact, ContactModelAdmin)
