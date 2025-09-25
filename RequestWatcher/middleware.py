class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(f"Nouvelle requête → URL: {request.path} | IP: {ip}")
        response = self.get_response(request)
        return response

    class LogMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Récupérer l’adresse IP du visiteur
            ip = request.META.get('REMOTE_ADDR')
            print(f"Nouvelle requête → URL: {request.path} | IP: {ip}")

            # Continuer le processus normal
            response = self.get_response(request)
            return response
