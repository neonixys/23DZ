from marshmallow import Schema, fields, validates_schema, ValidationError


class RequestParamSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        valid_cmd_commands = {'filter', 'sort', 'map', 'limit', 'unique'}

        if values['cmd'] not in valid_cmd_commands:
            raise ValidationError({'cmd': f'содержится не корректная команда={values["cmd"]}'})
        return values


class RequestParamsListSchema(Schema):
    queries = fields.Nested(RequestParamSchema, many=True)
    filename = fields.Str(required=True)
