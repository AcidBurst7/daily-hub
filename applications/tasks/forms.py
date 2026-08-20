from django import forms

from .models import Task, Column, CheckList, CheckListItem


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
            "column",
            "color",
            "deadline",
            "is_archived",
        ]
        labels = {
            "title": "Название задачи",
            "column": "Колонка",
            "description": "Описание",
            "color": "Цвет",
            "deadline": "Дедлайн",
            "is_archived": "Архивирована",
        }
        widgets = {
            "title": forms.TextInput( attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control","rows": 4}
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
        board = kwargs.pop("board", None)

        super().__init__(*args, **kwargs)

        self.fields["column"].widget.attrs.update({
            "class": "form-control"
        })

        if self.instance and self.instance.deadline:
            self.initial["deadline"] = self.instance.deadline.strftime(
                "%Y-%m-%dT%H:%M"
            )

        if board:
            self.fields["column"].queryset = Column.objects.\
                filter(board=board, board__user=board.user).all()
            # self.fields["column"].initial = board

        if not self.instance.pk:
            self.fields.pop("column")
            self.fields.pop("is_archived")

class ChecklistEditForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = ["name"]
        labels = {"name": "Название"}
        widgets = {
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