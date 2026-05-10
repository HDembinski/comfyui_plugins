"""Utilities for dynamic ComfyUI node registration.

This module inspects a node module's globals, finds classes that look like
ComfyUI nodes, and builds the two dictionaries ComfyUI expects:
NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS.
"""

from collections.abc import Mapping
from typing import Any, TypeAlias


NodeClass: TypeAlias = type
ModuleGlobals: TypeAlias = Mapping[str, Any]


def _is_comfy_node_class(value: Any) -> bool:
    """Return True when a value appears to be a valid ComfyUI node class."""
    if not isinstance(value, type):
        return False
    required_attributes = ("INPUT_TYPES", "RETURN_TYPES", "FUNCTION", "CATEGORY")
    if not all(hasattr(value, attr) for attr in required_attributes):
        return False
    function_name = getattr(value, "FUNCTION", None)
    return isinstance(function_name, str) and hasattr(value, function_name)


def _discover_node_classes(module_globals: ModuleGlobals) -> list[NodeClass]:
    """Collect and stably sort ComfyUI-like classes from a module globals dict."""
    node_classes = []
    for value in module_globals.values():
        if _is_comfy_node_class(value):
            node_classes.append(value)
    node_classes.sort(key=lambda node_class: node_class.__name__)
    return node_classes


def _node_key(node_class: NodeClass) -> str:
    """Resolve the registry key for a node class.

    NODE_KEY is used when present; otherwise the class name is used.
    """
    return getattr(node_class, "NODE_KEY", node_class.__name__)


def _display_name(node_class: NodeClass) -> str:
    """Resolve the display name for a node class.

    DISPLAY_NAME is used when present; otherwise the resolved node key is used.
    """
    return getattr(node_class, "DISPLAY_NAME", _node_key(node_class))


def build_node_mappings(module_globals: ModuleGlobals) -> tuple[dict[str, NodeClass], dict[str, str]]:
    """Build ComfyUI node mapping dictionaries from module globals.

    Args:
        module_globals: The globals() dictionary from a node module.

    Returns:
        A tuple of (NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS).
    """
    node_classes = _discover_node_classes(module_globals)
    class_mappings = {
        _node_key(node_class): node_class
        for node_class in node_classes
    }
    display_name_mappings = {
        _node_key(node_class): _display_name(node_class)
        for node_class in node_classes
    }
    return class_mappings, display_name_mappings
