from rest_framework import serializers
from .models import Delivery, Orderitem, Orders, Wishlist
from django.conf import settings

User = settings.AUTH_USER_MODEL


class DeliverySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Delivery
        exclude = [
            "updated_at",
        ]


class OrderitemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orderitem
        exclude = ["created_at", "created_by", "updated_at", "updated_by"]


class OrdersSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)
    delivery = DeliverySerializer()
    order_items = OrderitemSerializer(source="orderitem_set", many=True)

    class Meta:
        model = Orders
        exclude = [
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        delivery_data = validated_data.pop("delivery", None)
        order_items_data = validated_data.pop("orderitem_set", [])

        # Create or update delivery
        delivery = Delivery.objects.create(**delivery_data) if delivery_data else None
        order = Orders.objects.create(delivery=delivery, **validated_data)

        # Create order items
        for item_data in order_items_data:
            Orderitem.objects.create(order=order, **item_data)

        return order

    def update(self, instance, validated_data):
        delivery_data = validated_data.pop("delivery", None)
        order_items_data = validated_data.pop("orderitem_set", [])

        # Update delivery if provided
        if delivery_data:
            Delivery.objects.update_or_create(
                id=instance.delivery.id, defaults=delivery_data
            )

        # Update order fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update order items
        instance.orderitem_set.all().delete()  # Clear existing items
        for item_data in order_items_data:
            Orderitem.objects.create(order=instance, **item_data)

        return instance


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        exclude = ["created_at", "created_by", "updated_at", "updated_by"]
