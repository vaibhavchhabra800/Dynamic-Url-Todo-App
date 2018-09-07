from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your Note",
                                    "class": "new-class-name two",
                                    #"id": "my-id-for-textarea",
                                    "rows": 11,
                                    'cols': 126,
                                }
                            )
                        )

    
    class Meta:
        model = Comment
        fields = [

            'description',

        ]


