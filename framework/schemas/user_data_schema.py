
_ISO_UTC = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$"

USER_DATA_SCHEMA = {
    "type": "object",
    "required": ["payload", "user"],
    "additionalProperties": False,
    "properties": {
        "payload": {"type": "string"},
        "user": {
            "type": "object",
            "required": ["_id", "firstName", "lastName", "email", "role", "createdAt", "updatedAt"],
            "additionalProperties": False,
            "properties": {
                "_id": {"type": "string", "pattern": "^[a-f0-9]{24}$"},
                "firstName": {"type": "string", "minLength": 1},
                "lastName": {"type": "string", "minLength": 1},
                "email": {"type": "string", "pattern": "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"},
                "role": {"type": "string", "enum": ["user", "admin", "organizer"]},
                "createdAt": {"type": "string", "pattern": _ISO_UTC},
                "updatedAt": {"type": "string", "pattern": _ISO_UTC},
            },
        },
    },
}
