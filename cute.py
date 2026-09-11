class EventBus:

    def __init__(self):
        self._listeners = {}

    def subscribe(self, event_type, callback):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        if event_type in self._listeners:
            self._listeners[event_type].remove(callback)

    def publish(self, event_type, data):
        if event_type in self._listeners:
            for callback in self._listeners[event_type]:
                callback(data)


bus = EventBus()

# Event listeners
on_user_login = lambda data: print(f"[Email Notification] Welcome back, {data['user']}!")
on_audit_log = lambda data: print(f"[Audit Log] Event logged for user: {data['user']}")

bus.subscribe("user_login", on_user_login)
bus.subscribe("user_login", on_audit_log)

print("Publishing 'user_login' event:")
bus.publish("user_login", {"user": "Alice"})

bus.unsubscribe("user_login", on_user_login)
print("\nPublishing 'user_login' after unsubscribing email handler:")
bus.publish("user_login", {"user": "Bob"})