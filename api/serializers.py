from rest_framework import serializers
from products.models import Product , Tag ,Comment
from users.models import Profile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tag
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    skill= serializers.SerializerMethodField()
    class Meta:
        model= Profile
        fields = '__all__'

    def get_skill(self , obj):
        skill=obj.skill_set.all()
        serializer= CommentSerializer(skill , many=True)  

        return serializer.data 

class ProductSerializer(serializers.ModelSerializer):
    owner= ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    comment= serializers.SerializerMethodField()
    class Meta:
        model= Product
        fields = '__all__'

    def get_comment(self , obj):
        comments=obj.comment_set.all()
        serializer= CommentSerializer(comments , many=True)  

        return serializer.data
    


       


