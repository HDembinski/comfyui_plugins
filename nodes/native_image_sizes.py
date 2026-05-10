from .registry import build_node_mappings


IMAGE_SIZE_PRESETS: dict[str, tuple[int, int]] = {
    "16:9": (1664, 928),
    "3:2": (1584, 1056),
    "4:3": (1472, 1104),
    "1:1": (1328, 1328),
    "3:4": (1104, 1472),
    "2:3": (1056, 1584),
    "9:16": (928, 1664),
}


class NativeImageSizesNode:
    NODE_KEY: str = "NativeImageSizes"
    DISPLAY_NAME: str = "NativeImageSizes"

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, dict[str, tuple[list[str]]]]:
        return {
            "required": {
                "preset": (list(IMAGE_SIZE_PRESETS.keys()),),
            }
        }

    RETURN_TYPES: tuple[str, str] = ("INT", "INT")
    RETURN_NAMES: tuple[str, str] = ("width", "height")
    FUNCTION: str = "select_size"
    CATEGORY: str = "image/resolution"

    def select_size(self, preset: str) -> tuple[int, int]:
        width, height = IMAGE_SIZE_PRESETS[preset]
        return (width, height)


NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS = build_node_mappings(globals())
