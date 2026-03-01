from django.shortcuts import redirect
from django.urls import reverse

class RoleBasedAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/agent-admin/'):
            if not request.user.is_authenticated:
                return redirect(f'/agent-admin/login/?next={request.path}')
            if request.user.role != 'agent':
                return redirect('/admin/')
        
        if request.path.startswith('/admin/') and not request.path.startswith('/admin/login'):
            if request.user.is_authenticated and request.user.role == 'agent':
                return redirect('/agent-admin/')
        
        response = self.get_response(request)
        return response
