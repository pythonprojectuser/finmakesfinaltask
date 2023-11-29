# forms.py

from django import forms
from .models import Student,Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'department', 'course', 'roll_number']

    # Override __init__ to set up dynamic choices for the department and course fields
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update({'id': 'department-select'})
        self.fields['course'].widget.attrs.update({'id': 'course-select'})
        self.fields['course'].queryset = Course.objects.none()
