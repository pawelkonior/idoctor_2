from django.db import models


class NewsletterUser(models.Model):
    email = models.EmailField(unique=True)
    added = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('NewsletterCategory', through='Agreement', related_name='users_categories')

    def __str__(self):
        return self.email


class NewsletterCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    required = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class AgreementLog(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)
    agreement = models.ForeignKey('Agreement', on_delete=models.DO_NOTHING, related_name='log')
    status = models.BooleanField()

    def __str__(self):
        return f'Agreement: {self.agreement}, updated at: {self.updated_at:%d-%m-%y}, status: {self.status}'


class AgreementManager(models.query.QuerySet):
    def update(self, **kwargs):
        super().update(**kwargs)
        AgreementLog.objects.bulk_create([
            AgreementLog(agreement=agreement, status=agreement.agreed) for agreement in self
        ])


class Agreement(models.Model):
    category = models.ForeignKey('NewsletterCategory', on_delete=models.DO_NOTHING, related_name='agreement_category')
    email = models.ForeignKey('NewsletterUser', on_delete=models.DO_NOTHING, related_name='agreement_email')
    agreed = models.BooleanField(default=False)

    objects = AgreementManager.as_manager()

    def __str__(self):
        return f'Email: {self.email}, category: {self.category}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        AgreementLog.objects.create(agreement=self, status=self.agreed)
