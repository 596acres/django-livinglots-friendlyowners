from django import forms
from django.utils.translation import ugettext_lazy as _


class FriendlyOwnerFormMixin(forms.ModelForm):

    def clean(self):
        cleaned_data = super(FriendlyOwnerFormMixin, self).clean()
        email = cleaned_data.get('email', None)
        phone = cleaned_data.get('phone', None)
        if not (email or phone):
            raise forms.ValidationError(_('Please enter an email address or '
                                          'phone number'))
        return cleaned_data
