from django.db import models
import uuid
#create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.category_name
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name = 'category',on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.question
    def get_answers(self):
        answer_objs = Answer.objects.filter(question = self)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'uid' : answer_obj.uid,
                'answer' : answer_obj.answer,
            })
        return data
class Answer(BaseModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, related_name= 'question_answer',on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.answer
