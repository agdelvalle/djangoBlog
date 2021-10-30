from django import forms
from django.forms import widgets
from .models import blogEntry, comment

class newEntry(forms.ModelForm):
	class Meta:
		model = blogEntry
		fields = "__all__"

class newComment(forms.ModelForm):
	class Meta:
		model = comment
		fields = "__all__"