from django.db import models


# Storing Prompts category in the database
class PromptCategory(models.Model):
    # for avoiding duplicates or inserting duplicate values
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Storing prompts with its categories in the database
class Prompts(models.Model):
    prompts = models.TextField(max_length=3000)
    category = models.ForeignKey(PromptCategory, on_delete=models.CASCADE)

    # for avoiding duplicates or inserting duplicate values
    class Meta:
        unique_together = ('prompts', 'category')

    def __str__(self):
        return self.prompts
