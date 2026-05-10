# pyright: reportMissingImports=false

from comfy_api.latest import io


IMAGE_SIZE_PRESETS: dict[str, tuple[int, int]] = {
    "16:9": (1664, 928),
    "3:2": (1584, 1056),
    "4:3": (1472, 1104),
    "1:1": (1328, 1328),
    "3:4": (1104, 1472),
    "2:3": (1056, 1584),
    "9:16": (928, 1664),
}

SCALE_PRESETS: tuple[str, str, str] = ("0.5", "1", "2")


class NativeImageSizes(io.ComfyNode):

    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id=cls.__name__,
            category="image/resolution",
            inputs=[
                io.Combo.Input("preset", options=list(IMAGE_SIZE_PRESETS.keys())),
                io.Combo.Input("scale", options=list(SCALE_PRESETS), default="1"),
            ],
            outputs=[
                io.Int.Output(display_name="width"),
                io.Int.Output(display_name="height"),
            ],
        )

    @staticmethod
    def select_size(preset: str, scale: str) -> tuple[int, int]:
        width, height = IMAGE_SIZE_PRESETS[preset]
        factor = float(scale)
        return (round(width * factor), round(height * factor))

    @classmethod
    def execute(cls, preset: str, scale: str):
        width, height = cls.select_size(preset, scale)
        return io.NodeOutput(width, height)
