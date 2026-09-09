class StateMachine:

    def __init__(self, initial_state):
        self.state = initial_state
        self.transitions = {}

    def add_transition(self, trigger, source, target):
        self.transitions[(trigger, source)] = target

    def trigger(self, action):
        key = (action, self.state)
        if key in self.transitions:
            old_state = self.state
            self.state = self.transitions[key]
            print(f"Action '{action}': {old_state} -> {self.state}")
            return True
        print(f"Invalid transition '{action}' from '{self.state}'")
        return False


fsm = StateMachine("Draft")
fsm.add_transition("submit", "Draft", "In Review")
fsm.add_transition("approve", "In Review", "Published")
fsm.add_transition("reject", "In Review", "Draft")

fsm.trigger("submit")
fsm.trigger("reject")
fsm.trigger("approve")
fsm.trigger("submit")
fsm.trigger("approve")import inspect


class DependencyContainer:

    def __init__(self):
        self._services = {}

    def register(self, interface, implementation):
        self._services[interface] = implementation

    def resolve(self, interface):
        impl = self._services.get(interface, interface)
        if not callable(impl):
            return impl

        constructor = getattr(impl, "__init__", None)
        if not constructor or constructor == object.__init__:
            return impl()

        params = inspect.signature(constructor).parameters
        dependencies = {
            name: self.resolve(param.annotation)
            for name, param in params.items()
            if param.annotation != inspect.Parameter.empty
        }
        return impl(**dependencies)


class Logger:
    def log(self, msg):
        print(f"LOG: {msg}")


class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def create(self, name):
        self.logger.log(f"Created user {name}")


container = DependencyContainer()
container.register(Logger, Logger)
user_service = container.resolve(UserService)
user_service.create("Alice")