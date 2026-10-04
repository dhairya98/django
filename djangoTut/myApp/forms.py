from django import forms
from .models import FirstModel

class FirstModelForm(forms.Form):
    dataOnForm = forms.ModelChoiceField(
        queryset=FirstModel.objects.all(),
        label='Select Tech Stack',
        widget=forms.Select(attrs={
            'class': 'w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-3 text-slate-100 focus:outline-none focus:border-indigo-500 transition-colors cursor-pointer'
        })
    )
