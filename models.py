from marshmallow import Schema, fields, validate

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort', 'regex')


class RequestSchema(Schema):
    cmd = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value = fields.Str(required=True)


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
