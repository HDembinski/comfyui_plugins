# pyright: reportMissingImports=false

from typing import Any

from .nodes.native_image_sizes import NativeImageSizes


async def comfy_entrypoint() -> Any:
	from comfy_api.latest import ComfyExtension, io

	from .nodes.text_encode_qwen_image_edit import (
		TextEncodeQwenImageEditAlt,
		TextEncodeQwenImageEditPlusAlt,
	)

	class PluginExtension(ComfyExtension):
		async def get_node_list(self) -> list[type[io.ComfyNode]]:
			return [
				NativeImageSizes,
				TextEncodeQwenImageEditAlt,
				TextEncodeQwenImageEditPlusAlt,
			]

	return PluginExtension()


__all__ = ["comfy_entrypoint"]
