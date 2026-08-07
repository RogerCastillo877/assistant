from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from implementation.runtime.project import Project


@dataclass(slots=True)
class RuntimeRegistry:

    missions: dict[str, Any] = field(default_factory=dict)

    policies: dict[str, Any] = field(default_factory=dict)

    agents: dict[str, Any] = field(default_factory=dict)

    workflows: dict[str, Any] = field(default_factory=dict)

    capabilities: dict[str, Any] = field(default_factory=dict)

    skills: dict[str, Any] = field(default_factory=dict)

    tools: dict[str, Any] = field(default_factory=dict)

    resources: dict[str, Any] = field(default_factory=dict)

    memory: dict[str, Any] = field(default_factory=dict)

    knowledge: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def build(cls, project: Project) -> "RuntimeRegistry":

        registry = cls()

        registry.missions = {
            item.id: item
            for item in project.missions
        }

        registry.policies = {
            item.id: item
            for item in project.policies
        }

        registry.agents = {
            item.id: item
            for item in project.agents
        }

        registry.workflows = {
            item.id: item
            for item in project.workflows
        }

        registry.capabilities = {
            item.id: item
            for item in project.capabilities
        }

        registry.skills = {
            item.id: item
            for item in project.skills
        }

        registry.tools = {
            item.id: item
            for item in project.tools
        }

        registry.resources = {
            item.id: item
            for item in project.resources
        }

        registry.memory = {
            item.id: item
            for item in project.memory
        }

        registry.knowledge = {
            item.id: item
            for item in project.knowledge
        }

        return registry

    def get_agent(self, agent_id: str):
        return self.agents.get(agent_id)

    def get_workflow(self, workflow_id: str):
        return self.workflows.get(workflow_id)

    def get_capability(self, capability_id: str):
        return self.capabilities.get(capability_id)

    def get_skill(self, skill_id: str):
        return self.skills.get(skill_id)

    def get_tool(self, tool_id: str):
        return self.tools.get(tool_id)

    def get_resource(self, resource_id: str):
        return self.resources.get(resource_id)

    def get_policy(self, policy_id: str):
        return self.policies.get(policy_id)

    def get_mission(self, mission_id: str):
        return self.missions.get(mission_id)

    def get_memory(self, memory_id: str):
        return self.memory.get(memory_id)

    def get_knowledge(self, knowledge_id: str):
        return self.knowledge.get(knowledge_id)
