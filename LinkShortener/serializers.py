from dataclasses import field
from rest_framework import serializers
from .models import Link
from django.core.validators import URLValidator
from .models import Link
import pyshorteners

class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Link
       
        fields = ['main_url', 'shorten_url','created_at','valid','expired_date']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'valid': {'read_only': True},
            'shorten_url' :{'read_only':True}
        }
    def validate(self, attrs):
        main_url = attrs.get('main_url', '')
        val = URLValidator()
        try:
            val(main_url)
            print('ok')
        except:
            print('worng')
            raise serializers.ValidationError('Url Not valid')
        return attrs

        

    