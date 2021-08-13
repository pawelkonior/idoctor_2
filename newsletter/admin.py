from django.contrib import admin

# Register your models here.
from newsletter.models import NewsletterUser, NewsletterCategory, AgreementLog, Agreement


class NewsletterUserInline(admin.TabularInline):
    model = Agreement
    extra = 2


class NewsletterUserAdmin(admin.ModelAdmin):
    inlines = (NewsletterUserInline,)


admin.site.register(NewsletterUser, NewsletterUserAdmin)
admin.site.register(NewsletterCategory)
admin.site.register(AgreementLog)
admin.site.register(Agreement)
