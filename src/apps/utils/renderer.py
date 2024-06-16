from rest_framework.renderers import TemplateHTMLRenderer


class TemplateHTMLRendererWithSerializer(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        result = super().get_template_context(data, renderer_context)
        result = result or {}
        if 'serializer' not in result:
            result['serializer'] = renderer_context['view'].serializer_class()
        return result
