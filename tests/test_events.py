from implementation.runtime.events import (
    EventStore,
)


def test_emit_event():

    store = EventStore()

    store.emit(
        "workflow.started",
        {
            "workflow": "learning-workflow"
        }
    )

    assert store.count() == 1

    event = store.events[0]

    assert event.event_type == "workflow.started"


def test_filter_by_type():

    store = EventStore()

    store.emit("workflow.started")

    store.emit("workflow.completed")

    store.emit("workflow.started")

    started = store.by_type(
        "workflow.started"
    )

    assert len(started) == 2


def test_clear_events():

    store = EventStore()

    store.emit("a")

    store.emit("b")

    assert store.count() == 2

    store.clear()

    assert store.count() == 0
