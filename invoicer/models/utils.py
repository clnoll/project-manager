def set_model_attr(model, attr, value):
    if hasattr(model, attr):
        setattr(model, attr, value)
