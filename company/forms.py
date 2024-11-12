from django import forms
from company.models import Contact, Quotation

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'mobile',
            'email',
            'subject',
            'message'
        ]

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [
            'company_name',
            'contact_person',
            'email',
            'contact_no',
            'address',
            'remark',
            'plan_file'
        ]
    plan_file = forms.FileField(label='Upload Plan Image', required=False)
