from wtforms import Form, StringField, validators, IntegerField


class PaymentForm(Form):
    name = StringField("Name", [validators.Length(min=1, max=150)])
    creditcard = StringField("Card Number", [validators.Length(min=1, max=150)])
    expirydate = StringField("Expiry Date", [validators.Length(min=1, max=20)])
    cvc = IntegerField("CVC", [validators.NumberRange(max=999)])
