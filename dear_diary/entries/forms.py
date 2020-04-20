# creates the form just Like the model Its a python repersenation of your database
from django.forms import ModelForm
# Importing entry model create In models
from .models import Entry
# create a from from the entry model using the field text
# date posted is handeled automatically
# This Is telling model form create a form from the entry modle using the text field
class EntryForm(ModelForm):
    class Meta:
        model = Entry
    # text pass In comma makes it a tuple 
        fields = {'text',}
         
   
        # this init is going to be used as well as the default init thats used in model form
    # all this Is doing is calling the existing init.py
    def __init__(self, *args,**kwags):   
          super().__init__(*args,**kwags)
        #   gets the class attribute textarea from the add.html page 
          self.fields['text'].widget.attrs.update({'class': 'textarea ','placeholder': 'What\'s on your mind?'})

