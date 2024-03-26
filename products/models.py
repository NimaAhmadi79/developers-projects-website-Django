from django.db import models
import uuid
from users.models import Profile



class Product(models.Model):

    title = models.CharField(max_length=200)
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    featured_image=models.ImageField(null=True,blank=True,default="IMG_20201113_230341.jpg")
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created']



    @property
    def reviewers(self):
        queryset=self.comment_set.all().values_list('owner__id',flat=True)    
        return queryset

    @property
    def getVoteCount(self):
        comments= self.comment_set.all()
        upVotes=comments.filter(Value='up').count()
        totalVotes=comments.count()

        ratio=(upVotes/totalVotes) * 100
        self.vote_total=totalVotes
        self.vote_ratio=ratio

        self.save()




class Comment(models.Model):
    VOTE_TYPE = (
        ('up', 'up vote'),
        ('down', 'down vote'),


    )
    owner=models.ForeignKey(Profile , on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    Value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    class Meta:
        unique_together=[['owner','product']]

    def __str__(self):
        return self.Value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name



   