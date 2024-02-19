from rest_framework import serializers

from .models import StaffProfile, PastoralProfile, FirstTimer


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields =('firstname', 'lastname', 'pronouns', 'profilepic', 'role', 'email', 'bio')


class PastorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastoralProfile
        fields = ('firstname', 'lastname', 'pronouns', 'profilepic', 'role', 'email', 'bio')


class FirstTimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstTimer
        fields = ('firstname', 'lastname', 'pronouns', 'email', 'phonenumber', 'streetaddress', 'locality', 'state',
                  'zipcode', 'maritalstatus')
