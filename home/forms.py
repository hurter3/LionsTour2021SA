from django import forms

class ContactForm(forms.Form):
        
    contact_name = forms.CharField(label='Name',
        required=True
    )
    contact_email = forms.EmailField(label='Email',
        required=True
    )
    contact_message = forms.CharField(
        label='Message',
        required=True,
        widget=forms.Textarea(
            attrs={
                "rows": 5,
            },
        ),
    )
    class Meta:
        fields = [
            'contact_name',
            'contact_email',
            'contact_message',
        ]