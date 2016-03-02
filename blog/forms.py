from django import forms

from .models import Comment

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.help_text,
                    'required': 'required',
                    'spellcheck': 'true'
                })
    class Meta:
        model = Comment
        fields = ('autor', 'comment_name', 'comment_text',)
        help_texts = {
            'autor': 'Автор',
            'comment_name': 'Заголовок',
            'comment_text': 'Текст комментария...',
        }