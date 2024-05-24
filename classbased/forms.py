from django import forms
from crud.models import ClassRoom, Student

class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'class name'}))

class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name"]  # "__all__" is used to add all fields

class StudentModelForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=14)
    bio = forms.CharField(widget=forms.TextInput(attrs={"rows": 4}))
    profile_picture = forms.FileField(required=False)

    class meta:
        model = Student
        fields = ["name", "age", "email", "address", "classroom"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({"class": "form-control"})