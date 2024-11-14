from django.db import models

class DocumentComparison(models.Model):
    document1 = models.TextField(null=True, blank=True)  
    document2 = models.TextField(null=True, blank=True)  
    similarity_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comparison on {self.created_at}"
