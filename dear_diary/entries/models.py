from django.db import models
# what goes into the form 
class Entry (models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # blank her repersents the numbered Id
        return 'Entry #{}'.format(self.id)

        class Meta:
            verbose_name_plural = 'entries'


