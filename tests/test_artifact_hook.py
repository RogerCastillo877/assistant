from implementation.runtime.artifact_engine import (
    ArtifactEngine,
)

from implementation.runtime.hooks.artifact_hook import (
    ArtifactHook,
)


def test_artifact_hook():

    engine = ArtifactEngine()

    hook = ArtifactHook(
        artifact_engine=engine,
    )

    hook.execute(
        {
            "workflow_id":
            "learning-workflow"
        }
    )

    assert engine.count() == 1

    artifact = engine.all()[0]

    assert (
        artifact.id
        ==
        "artifact-learning-workflow"
    )

    assert (
        artifact.artifact_type
        ==
        "report"
    )
