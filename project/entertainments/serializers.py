from rest_framework import serializers
from .models import Entertainments


class ResponseHandling:
    def save_response(self, response_data):
        activity = response_data.get('activity')
        type = response_data.get('type')
        participants = response_data.get('participants')
        price = response_data.get('price')
        link = response_data.get('link')
        key = response_data.get('key')
        accessibility = response_data.get('accessibility')

        request_data = Entertainments(
            category=type,
            entertainment=activity,
            participants=participants,
            price=price,
            accessibility=accessibility,
            entertainment_id=key,
            link=link,
        )

        request_data.save()


class EntertainmentsSerializer(serializers.ModelSerializer, ResponseHandling):
    class Meta:
        model = Entertainments
        fields = ('category',
                  'entertainment',
                  'participants',
                  'price',
                  'accessibility',
                  'entertainment_id',
                  'link',
                  )

    # def create(self, validated_data):
    #     return Entertainments.objects.create(**validated_data)
