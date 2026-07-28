"""
OSEF Runtime

errors.py

Common exceptions used by runtime validators.
"""


class OSEFError(Exception):
    """Base OSEF runtime exception."""


class ValidationError(OSEFError):
    """Base validation error."""


class ProjectError(ValidationError):
    """Project validation failed."""


class SchemaError(ValidationError):
    """Schema validation failed."""


class ReferenceError(ValidationError):
    """Reference validation failed."""


class TraceabilityError(ValidationError):
    """Traceability validation failed."""


class PolicyError(ValidationError):
    """Policy validation failed."""


class RuntimeError(OSEFError):
    """Runtime execution failed."""


class ReleaseError(OSEFError):
    """Release validation failed."""
