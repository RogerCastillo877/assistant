from implementation.runtime.runtime_lifecycle import (
    RuntimeLifecycle,
)


class DummyHook:

    def __init__(self):

        self.executed = False

    def execute(
        self,
        payload: dict,
    ) -> None:

        self.executed = True


def test_runtime_lifecycle():

    lifecycle = RuntimeLifecycle()

    hook = DummyHook()

    lifecycle.register(
        "workflow.completed",
        hook,
    )

    lifecycle.emit(
        "workflow.completed",
        {},
    )

    assert hook.executed is True
