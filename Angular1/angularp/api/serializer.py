from rest_framework import serializers
from .models import Plato




class PlatoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plato
		fields = ('idP','titulo', 'tipo', 'precio', 'cantidad', 'distancia','valorNutricional','imagen','valoracion')

		idP = serializers.IntegerField()
		titulo = serializers.CharField()
		cantidad = serializers.IntegerField()
		distancia = serializers.FloatField()
		valorNutricional = serializers.FloatField()
		tipo = serializers.CharField()
		precio = serializers.FloatField()
		imagen = serializers.CharField()
		valoracion = serializers.IntegerField()

		def create(self, validated_data):
			return Platillo.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.idP = validated_data.get('idP', instance.idP)
			instance.titulo = validated_data.get('titulo', instance.titulo)
			instance.tipo = validated_data.get('tipo', instance.tipo)
			instance.precio = validated_data.get('precio', instance.precio)
			instance.cantidad = validated_data.get('cantidad', instance.cantidad)
			instance.distancia = validated_data.get('distancia', instance.distancia)
			instance.valorNutricional = validated_data.get('valorNutricional', instance.valorNutricional)
			instance.imagen = validated_data.get('imagen', instance.imagen)
			instance.valoracion = validated_data.get('valoracion', instance.valoracion)
			instance.save()
			return instance