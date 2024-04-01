from rest_framework.permissions import IsAdminUser
from .getWithdrawnView import GetWithdrawnView
from .createWithdrawnView import CreateWithdrawnView
from .listWithdrawnView import ListWithdrawnView

# Define a master viewset that combines multiple user-related viewsets.
class MasterWithdrawnViewSet(
    CreateWithdrawnView,
    ListWithdrawnView,
    GetWithdrawnView
):
    # Define a mapping of view actions to the corresponding permission classes required for each action.
    permission_classes_by_action = {
        "create": [IsAdminUser], 
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser]
    }

    def get_permissions(self):
        # Returns a list of permission classes required for the current action.
        # Tries to retrieve permission classes specific to the current action using 'self.permission_classes_by_action',
        # and falls back to using the default permission classes defined in 'self.permission_classes' if not found.
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except:
            return [permission() for permission in self.permission_classes]
