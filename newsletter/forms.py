from django import forms

from newsletter.models import NewsletterUser, NewsletterCategory, Agreement


class NewsletterUserForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ('email', 'categories')

    query = NewsletterCategory.objects.all
    categories = forms.ModelMultipleChoiceField(queryset=query(),
                                                widget=forms.CheckboxSelectMultiple)

    def save(self, commit=True):
        obj = super().save(commit=True)
        agreements = Agreement.objects.filter(email=obj).update(agreed=True)

        return obj
