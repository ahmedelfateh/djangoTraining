from django import forms
from frist_app.models import Topic, Webpage, AccessRecord, user
from django.core import validators

def check_for_z(value):
    if value[0].lower() !="z":
        raise forms.ValidationError("start with z")

##########################
class formName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    # verify_email = forms.EmailField(label="mail again")
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
def claen(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vemail = all_clean_data['verify_email']
    if email != vmail:
        raise formes.ValidationError("Verify email need to be like Email")
##############################

# def clean_botcatcher(self):
#     botcatcher = self.cleaned_data['botcatcher']
#     if len(botcatcher) > 0:
#         raise forms.ValidationError("error")
#     return botcatcher

#for to get the users data on langing page
class newUserForm(forms.ModelForm):
    class Meta():
        model = user
        fields = "__all__"
