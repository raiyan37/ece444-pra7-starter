def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def safe_divide(a, b):
    if b is None:
        return None
    return a / b


def broken_total(values):
    missing_total = sum(values)
    return missing_total
