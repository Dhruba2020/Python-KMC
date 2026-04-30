def log_event(event_type, *args, **kwargs):
    # 1. Check if messages exist
    if not args:
        raise ValueError("At least one message must be provided")

    # 2. Convert messages to list
    messages = list(args)
    

    # 3. Prepare metadata (only allowed keys)
    allowed_keys = {"timestamp", "user", "priority"}
    meta = {}

    for key, value in kwargs.items():
        if key in allowed_keys:
            meta[key] = value

    # 4. Handle priority = high
    if meta.get("priority") == "high":
        meta["alert"] = True

    # 5. Final structured dictionary
    log = {
        "type": event_type,
        "messages": messages,
        "meta": meta
    }

    return log



result = log_event(
    "ERROR",
    "File not found",
    "Invalid path",
    timestamp="2026-04-23 10:00",
    user="admin",
    priority="high"
)

print(result)


{
    'type': 'ERROR',
    'messages': ['File not found', 'Invalid path'],
    'meta': {
        'timestamp': '2026-04-23 10:00',
        'user': 'admin',
        'priority': 'high',
        'alert': True
    }
}


log_event("INFO")