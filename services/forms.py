from wtforms import Form, StringField, Field, ValidationError, validators

from models import Customer


def validate_products(form, field):
    if not isinstance(field.data, list):
        raise ValidationError("Products must be a list")
    for entry in field.data:
        if (not isinstance(entry, str)) and (not isinstance(entry, unicode)):
            raise ValidationError("Product id must be a string")

class OrderForm(Form):
    """ Form to validate incoming POST requests """

    customer_id = StringField(validators=[validators.DataRequired(), validators.Length(min=8, max=8)])
    products = Field(validators=[validators.DataRequired(), validate_products])