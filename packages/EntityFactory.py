from packages.Const import WIN_WIDTH;
from packages.Background import Background;

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Level 1":
                list_background = [];
                for i in range(7):
                    list_background.append(Background(f"Level1Bg{i}.png", i))
                    list_background.append(Background(f"Level1Bg{i}.png", i, position=(WIN_WIDTH, 0)))
                return list_background
    
                