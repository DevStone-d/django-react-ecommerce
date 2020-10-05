from rest_framework import serializers

from account.models import Account



class RegistrationSerializer(serializers.ModelSerializer):
    confirmationPass    = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Account
        fields = [
            "email",  
            "first_name",
            "last_name",
            "password",
            "confirmationPass",
        ]
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def save(self):
        account = Account(
                        email       = self.validated_data['email'],
                        first_name  = self.validated_data['first_name'],
                        last_name   = self.validated_data['last_name']
        )

        #parola ve dogrulama parolasi kontrolu
        password = self.validated_data['password']
        confirmationPass = self.validated_data['confirmationPass']

        if password != confirmationPass:
            raise serializers.ValidationError({'password': 'Parolalar uyusmak zorunda'})

        account.set_password(password)
        account.save()

        return account
