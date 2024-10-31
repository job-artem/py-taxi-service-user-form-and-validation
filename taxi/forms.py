from django.contrib.auth.forms import UserCreationForm
from taxi.models import Driver
from django import forms


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            'license_number',
            'first_name',
            'last_name',
        )


class DriverUpdateLicenceForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('license_number',)
