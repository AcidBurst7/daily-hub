from django import forms


class BoardEditForm(forms.Form):
    name = forms.CharField(
        required=True, 
        label="Название доски",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )