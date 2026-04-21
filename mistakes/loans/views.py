# ВИПРАВЛЕНО: Додано IsAuthenticated для захисту ендпоінтів позик
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Loan
from .serializers import LoanSerializer


class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer

    # ВИПРАВЛЕНО: Додано permission — тільки авторизовані користувачі
    permission_classes = [IsAuthenticated]

    # ВИПРАВЛЕНО: Замінено queryset = Loan.objects.all() на get_queryset(),
    # щоб кожен користувач бачив тільки свої позики, а не всі
    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)


@api_view(['GET'])
# ВИПРАВЛЕНО: Додано permission для user_loans_summary
@permission_classes([IsAuthenticated])
def user_loans_summary(request):
    """A custom endpoint that lists current user's loans."""
    # ВИПРАВЛЕНО: Фільтруємо позики по поточному користувачу замість всіх
    loans = Loan.objects.filter(user=request.user)
    # ВИПРАВЛЕНО: Додано many=True, бо loans — це QuerySet (колекція об'єктів)
    data = LoanSerializer(loans, many=True).data
    return Response(data)
