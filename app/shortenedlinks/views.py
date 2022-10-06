from django.shortcuts import redirect, Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import SLink
from .permissions import IsAdmin, IsOwner
from .serializers import SLinkSerializer, SLinkSerializerAdmin, UserSerializer


def redirecto(request, into):
    try:
        ob = SLink.objects.get(id=into)
        ob.count = ob.count + 1
        ob.save()
        link = ob.link
        return redirect(link)

    except:
        raise Http404("We can not find your link")


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class SLinkCreateView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = SLinkSerializer
    permission_classes = (IsOwner, IsAuthenticated)

    def get_queryset(self):
        return SLink.objects.filter(User=self.request.user.id)


class SLinkView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SLink.objects.all()
    serializer_class = SLinkSerializer
    permission_classes = (IsOwner, IsAuthenticated)


class SLinkCreateViewAdmin(generics.CreateAPIView, generics.ListAPIView):
    queryset = SLink.objects.all()
    serializer_class = SLinkSerializerAdmin
    permission_classes = (IsAdmin,)


class SLinkViewAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = SLink.objects.all()
    serializer_class = SLinkSerializerAdmin
    permission_classes = (IsAdmin,)
