"""
OSEF Runtime

errors.py

Common exceptions used by runtime validators.
"""


class OSEFError(Exception):
    """Base OSEF runtime exception."""
    pass


class ValidationError(OSEFError):
    """Base validation error."""
    pass


class ProjectError(ValidationError):
    """Project validation failed."""
    pass


class SchemaError(ValidationError):
    """Schema validation failed."""
    pass


class ReferenceError(ValidationError):
    """Reference validation failed."""
    pass


class TraceabilityError(ValidationError):
    """Traceability validation failed."""
    pass


class PolicyError(ValidationError):
    """Policy validation failed."""
    pass


class RuntimeError(OSEFError):
    """Runtime execution failed."""
    pass


class ReleaseError(OSEFError):
    """Release validation failed."""
    pass

class ResolutionError(OSEFError):
    """Dependency resolution failed."""
    pass
