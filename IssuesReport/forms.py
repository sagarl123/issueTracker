from django import forms 
from .models import Issue 

issues = (('Checkout problem at evening','Checkout problem at evening'),('Takes multiple attempt to checkout','Takes multiple attempt to checkout'),('Face model trained but models does not recognize','Face model trained but models does not recognize'))
class IssueForm(forms.ModelForm):
    # issues = forms.MultipleChoiceField(choices = issues, widget = forms.CheckboxSelectMultiple())
    # issues = forms.ChoiceField(choices = issues)

    class Meta:
        model =  Issue 
        fields = ('employeeId','issue')

    # def __init__(self) -> None:
    #     self.fields = 
