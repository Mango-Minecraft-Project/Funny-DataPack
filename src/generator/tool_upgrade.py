import json
import os

TOOLS_TYPE = "axe, hoe, pickaxe, shovel, sword".split(", ")
MATERIALS = "wooden, stone, iron, golden, diamond, netherite".split(", ")
INGREDIENTS = "cobblestone, iron_ingot, gold_ingot, diamond, netherite_ingot".split(
    ", "
)

for type in TOOLS_TYPE:
    for index, material in enumerate(MATERIALS[1:], start=1):
        with open(
            f"./src/datapacks/老玩家的回忆/data/funny_datapack_01/recipes/tool_upgrade/{material}_{type}.json",
            "w",
        ) as file_ref:
            json.dump(
                {
                    "type": "crafting_shapeless",
                    "ingredients": [
                        {"item": f"minecraft:{MATERIALS[index-1]}_{type}"},
                        {"item": f"minecraft:{INGREDIENTS[index-1]}"},
                    ],
                    "result": {"item": f"minecraft:{material}_{type}"},
                },
                file_ref,
                indent=2,
            )
