"""
OSEF Runtime

resolver.py

Reference resolution and dependency validation.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from implementation.runtime.errors import ResolutionError
from implementation.runtime.registry import RuntimeRegistry


@dataclass(slots=True)
class ResolutionReport:

    errors: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return len(self.errors) == 0


class RuntimeResolver:

    def __init__(self, registry: RuntimeRegistry):

        self.registry = registry

    def validate(self) -> ResolutionReport:

        report = ResolutionReport()

        self._validate_agents(report)

        self._validate_workflows(report)

        self._validate_capabilities(report)

        self._validate_skills(report)

        return report

    # ---------------------------------------------------------
    # Agents
    # ---------------------------------------------------------

    def _validate_agents(
        self,
        report: ResolutionReport,
    ) -> None:

        for agent in self.registry.agents.values():

            if (
                agent.mission
                and self.registry.get_mission(agent.mission) is None
            ):
                report.errors.append(
                    f"Agent '{agent.id}' references "
                    f"missing mission '{agent.mission}'."
                )

            for workflow_id in agent.workflows:

                if self.registry.get_workflow(workflow_id) is None:

                    report.errors.append(
                        f"Agent '{agent.id}' references "
                        f"missing workflow '{workflow_id}'."
                    )

            for capability_id in agent.capabilities:

                if self.registry.get_capability(capability_id) is None:

                    report.errors.append(
                        f"Agent '{agent.id}' references "
                        f"missing capability '{capability_id}'."
                    )

    # ---------------------------------------------------------
    # Workflows
    # ---------------------------------------------------------

    def _validate_workflows(
        self,
        report: ResolutionReport,
    ) -> None:

        for workflow in self.registry.workflows.values():

            if (
                workflow.mission
                and self.registry.get_mission(workflow.mission) is None
            ):
                report.errors.append(
                    f"Workflow '{workflow.id}' references "
                    f"missing mission '{workflow.mission}'."
                )

            for step in workflow.steps:

                capability_id = step.get("capability")

                if (
                    capability_id
                    and self.registry.get_capability(capability_id) is None
                ):
                    report.errors.append(
                        f"Workflow '{workflow.id}' step "
                        f"references missing capability "
                        f"'{capability_id}'."
                    )

    # ---------------------------------------------------------
    # Capabilities
    # ---------------------------------------------------------

    def _validate_capabilities(
        self,
        report: ResolutionReport,
    ) -> None:

        for capability in self.registry.capabilities.values():

            for skill_id in capability.skills:

                if self.registry.get_skill(skill_id) is None:

                    report.errors.append(
                        f"Capability '{capability.id}' "
                        f"references missing skill "
                        f"'{skill_id}'."
                    )

    # ---------------------------------------------------------
    # Skills
    # ---------------------------------------------------------

    def _validate_skills(
        self,
        report: ResolutionReport,
    ) -> None:

        for skill in self.registry.skills.values():

            for tool_id in skill.tools:

                if self.registry.get_tool(tool_id) is None:

                    report.errors.append(
                        f"Skill '{skill.id}' references "
                        f"missing tool '{tool_id}'."
                    )

            for resource_id in skill.resources:

                if self.registry.get_resource(resource_id) is None:

                    report.errors.append(
                        f"Skill '{skill.id}' references "
                        f"missing resource '{resource_id}'."
                    )

    # ---------------------------------------------------------
    # Strict mode
    # ---------------------------------------------------------

    def resolve_or_raise(self) -> None:

        report = self.validate()

        if not report.valid:

            raise ResolutionError(
                "\n".join(report.errors)
            )
