from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerializer , ProfileSerializer
from products.models import Product , Comment
from users.models import Skill, Profile




@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/products'},
        {'GET':'/api/products/id'}

    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
    products= Product.objects.all()
    serializer= ProductSerializer(products , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request , pk):
    product= Product.objects.get(id=pk)
    serializer= ProductSerializer(product , many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def productVote(request , pk):
    product= Product.objects.get(id=pk)
    user=request.user.profile
    data=request.data

    comment , created = Comment.objects.get_or_create(
        owner=user,
        product=product,
    )
    comment.Value=data['value']
    comment.save()
    product.getVoteCount

    serializer=ProductSerializer(product , many=False)

    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    ##product= Product.objects.get(id=pk)
    profile=request.user.profile
    data=request.data

    skill , created = Skill.objects.get_or_create(
        owner=profile,
    )
    skill.name=data['name']
    skill.save()

    serializer=ProfileSerializer(profile, many=False)

    return Response(serializer.data)