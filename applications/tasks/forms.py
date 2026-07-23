from django import forms

from .models import Task, CheckList, CheckListItem


class BoardEditForm(forms.Form):
    name = forms.CharField(
        required=True, 
        label="Название доски",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

class ColumnEditForm(forms.Form):
    name = forms.CharField(
        required=True, 
        label="Название колонки",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "color",
            "deadline",
            "is_archived",
        ]
        labels = {
            "title": "Название задачи",
            "description": "Описание",
            "color": "Цвет",
            "deadline": "Дедлайн",
            "is_archived": "Архивирована",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "color": forms.TextInput(
                attrs={
                    "class": "form-control form-control-color",
                    "type": "color",
                }
            ),
            "deadline": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),
            "is_archived": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Чтобы datetime-local корректно отображал существующее значение
        if self.instance and self.instance.deadline:
            self.initial["deadline"] = self.instance.deadline.strftime(
                "%Y-%m-%dT%H:%M"
            )


class ChecklistEditForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = ["task", "name"]
        labels = {
            "task": "",
            "name": "Название"
        }
        widgets = {
            "task": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            )
        }

class ChecklistItemEditForm(forms.ModelForm):
    class Meta:
        model = CheckListItem
        fields = ["checklist", "title", "done"]
        labels = {
            "checklist": "",
            "title": "Название",
            "done": "",
        }
        widgets = {
            "task": forms.HiddenInput(),
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "done": forms.CheckboxInput(
                attrs={"class": "form-control"}
            )
        }