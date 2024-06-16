class StateMachineResponseMixin:
    states = {}

    def finalize_response(self, request, response, *args, **kwargs):
        next_action = self.states.get(self.action)
        if next_action and hasattr(self, next_action):
            response = getattr(self, next_action)(request, *args, **kwargs)
        return super().finalize_response(request, response, *args, **kwargs)


class TemplatesMapMixin:
    templates_map = {}

    def get_template_names(self):
        if self.action not in self.templates_map:
            return []

        return [self.templates_map[self.action]]
