import pytest

from nodes.native_image_sizes import (
    IMAGE_SIZE_PRESETS,
    NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS,
    NativeImageSizesNode,
)


@pytest.mark.parametrize(
    "preset,expected",
    IMAGE_SIZE_PRESETS.items(),
)
def test_native_image_sizes_node_returns_expected_dimensions(preset, expected):
    node = NativeImageSizesNode()
    result = node.select_size(preset, "1")
    assert result == expected


def test_native_image_sizes_node_returns_int_dimensions():
    node = NativeImageSizesNode()
    width, height = node.select_size("16:9", "1")
    assert isinstance(width, int)
    assert isinstance(height, int)


@pytest.mark.parametrize(
    "scale,expected",
    [
        ("0.5", (832, 464)),
        ("1", (1664, 928)),
        ("2", (3328, 1856)),
    ],
)
def test_native_image_sizes_node_applies_scale(scale, expected):
    node = NativeImageSizesNode()
    assert node.select_size("16:9", scale) == expected


def test_node_class_mappings_are_discovered_dynamically():
    assert "NativeImageSizes" in NODE_CLASS_MAPPINGS
    assert NODE_CLASS_MAPPINGS["NativeImageSizes"] is NativeImageSizesNode


def test_node_display_name_mappings_are_discovered_dynamically():
    assert NODE_DISPLAY_NAME_MAPPINGS["NativeImageSizes"] == "NativeImageSizes"
