from apps.utils.mixins import StateMachineResponseMixin, TemplatesMapMixin
from apps.utils.renderer import TemplateHTMLRendererWithSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class HTMLViewSet(StateMachineResponseMixin, TemplatesMapMixin, ModelViewSet):
    many_objects_context_name = 'objects'
    single_object_context_name = 'object'
    renderer_classes = [TemplateHTMLRendererWithSerializer]

    def list(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            return Response({self.many_objects_context_name: page, 'paginator': self.paginator})

        return Response({self.many_objects_context_name: queryset})

    def retrieve(self, *args, **kwargs):
        instance = self.get_object()
        return Response({'serializer': self.get_serializer(instance), self.single_object_context_name: instance})
