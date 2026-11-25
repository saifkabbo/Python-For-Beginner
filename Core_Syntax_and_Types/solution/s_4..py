# Safe default. Write coalesce(*values) that returns the first argument that is not None (so 0 and "" are valid results).

def coalesce(*values):
    print(next((v for v in values if v is not None),None))


coalesce(None, 0, 5)