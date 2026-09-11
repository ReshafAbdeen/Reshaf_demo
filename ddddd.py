import inspect


class ValidationRule:

    def __init__(self, field, error_msg):
        self.field = field
        self.error_msg = error_msg

    def validate(self, data):
        raise NotImplementedError


class Required(ValidationRule):

    def validate(self, data):
        val = data.get(self.field)
        return val is not None and str(val).strip() != ""


class MinLength(ValidationRule):

    def __init__(self, field, min_len):
        super().__init__(field, f"Field '{field}' must be at least {min_len} chars")
        self.min_len = min_len

    def validate(self, data):
        val = data.get(self.field, "")
        return len(str(val)) >= self.min_len


class SchemaValidator:

    def __init__(self, rules):
        self.rules = rules

    def validate(self, data):
        errors = []
        for rule in self.rules:
            if not rule.validate(data):
                errors.append(rule.error_msg)
        return len(errors) == 0, errors


validator = SchemaValidator([
    Required("username", "Username is required"),
    MinLength("username", 4),
    Required("email", "Email is required"),
])

data1 = {"username": "abc", "email": ""}
valid, errors = validator.validate(data1)
print(f"Data 1 Valid: {valid} | Errors: {errors}")

data2 = {"username": "alice_dev", "email": "alice@example.com"}
valid, errors = validator.validate(data2)
print(f"Data 2 Valid: {valid} | Errors: {errors}")