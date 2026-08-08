from implementation.runtime.artifact_engine import (
    ArtifactEngine,
)

from implementation.runtime.artifact_record import (
    ArtifactRecord,
)


def test_store_artifact():

    engine = ArtifactEngine()

    engine.store(
        ArtifactRecord(
            id="artifact-1",
            title="Learning Guide",
            content="Kubernetes guide",
            artifact_type="guide",
        )
    )

    assert engine.count() == 1


def test_get_artifact():

    engine = ArtifactEngine()

    engine.store(
        ArtifactRecord(
            id="artifact-1",
            title="Learning Guide",
            content="Kubernetes guide",
            artifact_type="guide",
        )
    )

    artifact = engine.get(
        "artifact-1"
    )

    assert artifact is not None

    assert artifact.title == (
        "Learning Guide"
    )


def test_search_by_tag():

    engine = ArtifactEngine()

    engine.store(
        ArtifactRecord(
            id="artifact-1",
            title="Guide",
            content="...",
            artifact_type="guide",
            tags=["kubernetes"],
        )
    )

    results = engine.search_by_tag(
        "kubernetes"
    )

    assert len(results) == 1


def test_search_by_type():

    engine = ArtifactEngine()

    engine.store(
        ArtifactRecord(
            id="artifact-1",
            title="Guide",
            content="...",
            artifact_type="guide",
        )
    )

    results = engine.search_by_type(
        "guide"
    )

    assert len(results) == 1
