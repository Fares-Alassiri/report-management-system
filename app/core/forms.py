# from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple, FileField, ModelChoiceField
# from core.models import Report, Attachment, Tag, Group


# class ReportForm(ModelForm):

#     def __init__(self, *args, **kwargs):
#         """ Grants access to the request object so that only members of the current user
#         are given as options"""

#         self.request = kwargs.pop('request')
#         self.pk = kwargs.pop('pk')
#         super(ReportForm, self).__init__(*args, **kwargs)
#         # self.fields['groups'].queryset = Group.objects.filter(
#             # user=self.request.user)
#         self.fields['attachments'].queryset = Attachment.objects.filter(report=self.pk)
#         # self.fields['attachments'].widget = ModelMultipleChoiceField(queryset=Attachment.objects.filter(report=self.pk))
        
#     attachment = FileField()
#     attachments = ModelMultipleChoiceField(queryset= None, widget=CheckboxSelectMultiple(attrs={"checked":""}))


#     class Meta:
#         model = Report
#         fields = [
#             'name', 'tags', 'groups', 'content', 'attachment', 'attachments'
#         ]

#     tags = ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         widget=CheckboxSelectMultiple
#     )

#     groups = ModelMultipleChoiceField(
#         queryset=Group.objects.all(),
#         widget=CheckboxSelectMultiple
#     )