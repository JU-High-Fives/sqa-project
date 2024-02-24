from django import forms
from .models import DeliveryRequest

class deliveryRequestForm(forms.ModelForm):
    """
    Form for creating or updating a delivery request.
    """

    class Meta:
        model = DeliveryRequest
        # Specifies the model to use for this form and the fields to include.
        fields = [
            'm_pickup_location',  # Field for entering the pickup location.
            'm_delivery_destination',  # Field for entering the delivery destination.
            'm_size_weight',  # Field for specifying the size and weight of the delivery.
            'm_preferred_delivery_window',  # Field for selecting the preferred delivery window.
            'm_special_instructions',  # Field for providing any special instructions for the delivery.
        ]

    def __init__(self, *args, **kwargs):
        """
        Constructor for the deliveryRequestForm.
        """
        super().__init__(*args, **kwargs)
        # Perform any additional initialization here if needed.