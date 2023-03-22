from typing import Optional
from flask_wtf import FlaskForm
from wtforms import ValidationError, Field, IntegerField
from wtforms.validators import InputRequired

class NumberLength:
    def __init__(self, min=None, max=None, message=None):
        self.message = message
        self.min = min
        self.max = max
    def __call__(self, form: FlaskForm, field: Field):
        data = field.data
        if len(str(data)) > self.max or len(str(data)) < self.min:
            raise ValidationError(message=self.message)

def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        data = field.data
        if len(str(data)) > max or len(str(data)) < min:
            raise ValidationError(message=message)
    return _number_length


number = IntegerField(validators=[InputRequired(), NumberLength()])