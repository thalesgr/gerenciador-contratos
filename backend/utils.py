def update_model_from_dict(model, data, numeric_fields=None):
    numeric_fields = numeric_fields or []
    
    for key, value in data.items():
        if not hasattr(model, key):
            continue  # ignora campos inexistentes
        if key in numeric_fields:
            try:
                value = float(value)
            except (ValueError, TypeError):
                from errors import InvalidUsage
                raise InvalidUsage(f"Campo '{key}' deve ser um número válido")
        setattr(model, key, value)
