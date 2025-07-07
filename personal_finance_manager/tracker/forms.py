from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError("Please enter a positive amount.")
        return amount
        
class TransactionFilterForm(forms.Form):
    TRANSACTION_TYPE_CHOICES = [
        ('', 'All'),
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPE_CHOICES, required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    search = forms.CharField(required=False)
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']