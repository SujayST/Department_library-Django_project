from django import forms


class addForm(forms.Form):
    USN = forms.CharField()
    Name = forms.CharField()
    Semester = forms.CharField()
    phone_no = forms.CharField()


class lendForm(forms.Form):
    book_id = forms.CharField()
    USN = forms.CharField()
    issue = forms.DateField()
    due = forms.DateField()


class transfer(forms.Form):
    trnid = forms.IntegerField()
    return_date = forms.DateField()
