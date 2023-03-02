from django import forms
from django.core.exceptions import ValidationError

from tracker_app.models.issues import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'types')
        lables = {
            'summary': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'types': 'Тип задачи'
        }

    def clean_title(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return summary
