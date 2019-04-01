from jsonschema import validate

schema = {
    "title": "Validate event json",
    "type": "object",
    "required": ["component", "version", "responsible", "status"],
    "additionalProperties": False,
    "properties": {
        "component":{
            "type": "string"
        },
        "version":{
            "type": "string"
        },
        "responsible":{
            "type": "string"
        },
        "status":{
            "type": "string"
        }
    }
}

def validate_event(event_json):
    try:
        validate_response = validate(event_json, schema)
    except Exception as e:
        print(e)
        return False
    return True