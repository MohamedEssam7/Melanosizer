from marshmallow import Schema, fields

class PredictionSchema(Schema):
    image = fields.Raw(type='file')

class ResultSchema(Schema):
    result = fields.Str()

class ErrorSchema(Schema):
    message = fields.Str()