# Game categories
CATEGORIES = {
    "rpg": "🎭 RPG и открытый мир",
    "strategy": "🎯 Стратегии и симуляторы",
    "competitive": "⚔️ Соревновательные игры",
    "indie": "🎨 Инди и платформеры",
    "sandbox": "🏗️ Песочницы и крафтинг",
    "souls": "⚔️ Сложные игры",
    "management": "📊 Симуляторы управления",
    "survival": "🏕️ Выживание",
    "puzzle": "🧩 Головоломки",
    "space": "🚀 Космос",
    "narrative": "📖 Сюжетные игры",
    "action": "🎯 Экшен игры",
    "mmo": "🌐 MMO и онлайн игры"
}

# Games and their corresponding IT professions
GAMES_PROFESSIONS = {
    # RPG и открытый мир
    "witcher3": {
        "name": "The Witcher 3: Wild Hunt",
        "category": "rpg",
        "professions": ["Гейм-дизайнер", "Технический художник", "Сценарист игр", "Разработчик игровых механик"]
    },
    "skyrim": {
        "name": "The Elder Scrolls V: Skyrim",
        "category": "rpg",
        "professions": ["3D Моделлер", "Дизайнер уровней", "Разработчик игровых механик", "Технический художник"]
    },
    "cyberpunk": {
        "name": "Cyberpunk 2077",
        "category": "rpg",
        "professions": ["3D Моделлер", "Технический художник", "Разработчик шейдеров", "UI/UX дизайнер"]
    },
    "masseffect": {
        "name": "Mass Effect Legendary Edition",
        "category": "rpg",
        "professions": ["Сценарист игр", "Дизайнер диалогов", "3D Моделлер", "Технический художник"]
    },
    "dragonage": {
        "name": "Dragon Age: Inquisition",
        "category": "rpg",
        "professions": ["Сценарист игр", "Дизайнер диалогов", "Разработчик игровых механик"]
    },

    # Стратегии и симуляторы
    "civilization": {
        "name": "Civilization VI",
        "category": "strategy",
        "professions": ["AI инженер", "Аналитик данных", "Разработчик игровой логики"]
    },
    "aoe4": {
        "name": "Age of Empires IV",
        "category": "strategy",
        "professions": ["AI программист", "Разработчик игровой логики", "Специалист по балансу"]
    },
    "xcom2": {
        "name": "XCOM 2",
        "category": "strategy",
        "professions": ["AI программист", "Разработчик тактических систем", "Специалист по балансу"]
    },
    "totalwar": {
        "name": "Total War: Warhammer III",
        "category": "strategy",
        "professions": ["AI программист", "Разработчик боевых систем", "Технический художник"]
    },

    # Соревновательные игры
    "dota2": {
        "name": "Dota 2",
        "category": "competitive",
        "professions": ["Разработчик сетевого кода", "Специалист по балансу", "Backend разработчик"]
    },
    "csgo": {
        "name": "Counter-Strike: Global Offensive",
        "category": "competitive",
        "professions": ["Разработчик сетевого кода", "Специалист по античиту", "Разработчик физического движка"]
    },
    "valorant": {
        "name": "Valorant",
        "category": "competitive",
        "professions": ["Разработчик сетевого кода", "Специалист по античиту", "Разработчик игровых механик"]
    },
    "lol": {
        "name": "League of Legends",
        "category": "competitive",
        "professions": ["Разработчик сетевого кода", "Специалист по балансу", "Backend разработчик"]
    },
    "overwatch": {
        "name": "Overwatch",
        "category": "competitive",
        "professions": ["Разработчик сетевого кода", "Специалист по балансу", "3D аниматор"]
    },

    # Инди и платформеры
    "hollow": {
        "name": "Hollow Knight",
        "category": "indie",
        "professions": ["2D художник", "Геймплей-программист", "Разработчик физического движка"]
    },
    "celeste": {
        "name": "Celeste",
        "category": "indie",
        "professions": ["2D художник", "Разработчик платформеров", "Гейм-дизайнер"]
    },
    "gris": {
        "name": "Gris",
        "category": "indie",
        "professions": ["2D художник", "Технический художник", "Композитор"]
    },
    "journey": {
        "name": "Journey",
        "category": "indie",
        "professions": ["3D художник", "Технический художник", "Композитор"]
    },

    # Песочницы и крафтинг
    "minecraft": {
        "name": "Minecraft",
        "category": "sandbox",
        "professions": ["Java разработчик", "Разработчик процедурной генерации", "Специалист по оптимизации"]
    },
    "terraria": {
        "name": "Terraria",
        "category": "sandbox",
        "professions": ["2D художник", "Разработчик игровых механик", "Специалист по процедурной генерации"]
    },
    "satisfactory": {
        "name": "Satisfactory",
        "category": "sandbox",
        "professions": ["Разработчик систем автоматизации", "3D программист", "Специалист по оптимизации"]
    },
    "stardewvalley": {
        "name": "Stardew Valley",
        "category": "sandbox",
        "professions": ["2D художник", "Разработчик игровых механик", "Гейм-дизайнер"]
    },

    # Сложные игры
    "darksouls3": {
        "name": "Dark Souls III",
        "category": "souls",
        "professions": ["Разработчик боевых систем", "3D аниматор", "Специалист по балансу"]
    },
    "sekiro": {
        "name": "Sekiro: Shadows Die Twice",
        "category": "souls",
        "professions": ["Разработчик боевых систем", "3D аниматор", "Технический художник"]
    },
    "bloodborne": {
        "name": "Bloodborne",
        "category": "souls",
        "professions": ["Разработчик боевых систем", "3D художник", "Специалист по балансу"]
    },
    "cuphead": {
        "name": "Cuphead",
        "category": "souls",
        "professions": ["2D аниматор", "Разработчик боевых систем", "Композитор"]
    },

    # Симуляторы управления
    "citiessl": {
        "name": "Cities: Skylines",
        "category": "management",
        "professions": ["Разработчик AI", "Специалист по оптимизации", "Разработчик симуляций"]
    },
    "prisonarch": {
        "name": "Prison Architect",
        "category": "management",
        "professions": ["AI программист", "Разработчик симуляций", "UI/UX дизайнер"]
    },
    "twopointhosp": {
        "name": "Two Point Hospital",
        "category": "management",
        "professions": ["AI программист", "Разработчик симуляций", "Гейм-дизайнер"]
    },
    "planetzoo": {
        "name": "Planet Zoo",
        "category": "management",
        "professions": ["AI программист", "3D художник", "Разработчик симуляций"]
    },

    # Сюжетные игры
    "lifeisstrange": {
        "name": "Life is Strange: True Colors",
        "category": "narrative",
        "professions": ["Сценарист игр", "Дизайнер диалогов", "Нарративный дизайнер"]
    },
    "detroit": {
        "name": "Detroit: Become Human",
        "category": "narrative",
        "professions": ["Сценарист игр", "Технический художник", "Motion Capture специалист"]
    },
    "plaguetale": {
        "name": "A Plague Tale: Innocence",
        "category": "narrative",
        "professions": ["Сценарист игр", "3D художник", "Технический художник"]
    },
    "hellblade": {
        "name": "Hellblade: Senua's Sacrifice",
        "category": "narrative",
        "professions": ["3D художник", "Sound дизайнер", "Motion Capture специалист"]
    },

    # MMO и онлайн игры
    "wow": {
        "name": "World of Warcraft",
        "category": "mmo",
        "professions": ["Backend разработчик", "Разработчик сетевого кода", "Специалист по базам данных"]
    },
    "fortnite": {
        "name": "Fortnite",
        "category": "mmo",
        "professions": ["Разработчик сетевого кода", "Специалист по античиту", "Разработчик игровых механик"]
    },
    "gtaonline": {
        "name": "GTA Online",
        "category": "mmo",
        "professions": ["Backend разработчик", "Разработчик сетевого кода", "Специалист по безопасности"]
    },
    "seaofthieves": {
        "name": "Sea of Thieves",
        "category": "mmo",
        "professions": ["Разработчик сетевого кода", "3D художник", "Разработчик физического движка"]
    },

    # Космос
    "nms": {
        "name": "No Man's Sky",
        "category": "space",
        "professions": ["Специалист по процедурной генерации", "3D программист", "Разработчик шейдеров"]
    },
    "outerwilds": {
        "name": "Outer Wilds",
        "category": "space",
        "professions": ["Физический программист", "Дизайнер головоломок", "Разработчик игровых механик"]
    },
    "ksp": {
        "name": "Kerbal Space Program",
        "category": "space",
        "professions": ["Физический программист", "Разработчик симуляций", "UI/UX дизайнер"]
    },
    "destiny2": {
        "name": "Destiny 2",
        "category": "space",
        "professions": ["Разработчик сетевого кода", "3D художник", "Разработчик боевых систем"]
    },
    "starfield": {
        "name": "Starfield",
        "category": "space",
        "professions": ["3D Моделлер", "Разработчик процедурной генерации", "Технический художник"]
    },
    "elitedangerous": {
        "name": "Elite Dangerous",
        "category": "space",
        "professions": ["Разработчик физического движка", "Специалист по процедурной генерации", "Backend разработчик"]
    },
    "evochron": {
        "name": "Evochron Legacy",
        "category": "space",
        "professions": ["Разработчик физического движка", "3D программист", "Разработчик игровых механик"]
    },
    "empyrion": {
        "name": "Empyrion - Galactic Survival",
        "category": "space",
        "professions": ["Разработчик процедурной генерации", "3D художник", "Разработчик игровых механик"]
    },
    "everspace": {
        "name": "EVERSPACE",
        "category": "space",
        "professions": ["3D художник", "Разработчик боевых систем", "Технический художник"]
    },
    "rebelgalaxy": {
        "name": "Rebel Galaxy",
        "category": "space",
        "professions": ["2D художник", "Разработчик боевых систем", "Композитор"]
    },
    "Portal 2": {
        "name": "Portal 2",
        "category": "🧩 Головоломки",
        "professions": [
            "Физический программист",
            "Дизайнер головоломок",
            "Разработчик игровых механик",
            "3D программист",
            "Сценарист игр"
        ]
    },
    "The Witness": {
        "name": "The Witness",
        "category": "🧩 Головоломки",
        "professions": [
            "Дизайнер головоломок",
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "3D художник",
            "Гейм-дизайнер"
        ]
    },
    "Baba Is You": {
        "name": "Baba Is You",
        "category": "🧩 Головоломки",
        "professions": [
            "Разработчик игровых механик",
            "Дизайнер головоломок",
            "2D художник",
            "Гейм-дизайнер",
            "UI/UX дизайнер"
        ]
    },
    "The Talos Principle": {
        "name": "The Talos Principle",
        "category": "🧩 Головоломки",
        "professions": [
            "Физический программист",
            "Дизайнер головоломок",
            "3D художник",
            "Сценарист игр",
            "Разработчик игровых механик"
        ]
    },
    "Return of the Obra Dinn": {
        "name": "Return of the Obra Dinn",
        "category": "🧩 Головоломки",
        "professions": [
            "2D художник",
            "Сценарист игр",
            "UI/UX дизайнер",
            "Гейм-дизайнер",
            "Разработчик игровых механик"
        ]
    },
    "Opus Magnum": {
        "name": "Opus Magnum",
        "category": "🧩 Головоломки",
        "professions": [
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "2D художник",
            "Гейм-дизайнер",
            "Разработчик симуляций"
        ]
    },
    "Antichamber": {
        "name": "Antichamber",
        "category": "🧩 Головоломки",
        "professions": [
            "3D программист",
            "Дизайнер головоломок",
            "UI/UX дизайнер",
            "Гейм-дизайнер",
            "Разработчик игровых механик"
        ]
    },
    "The Room": {
        "name": "The Room",
        "category": "🧩 Головоломки",
        "professions": [
            "3D художник",
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "Гейм-дизайнер",
            "Sound дизайнер"
        ]
    },
    "Monument Valley": {
        "name": "Monument Valley",
        "category": "🧩 Головоломки",
        "professions": [
            "2D художник",
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "Гейм-дизайнер",
            "Композитор"
        ]
    },
    "Stephen's Sausage Roll": {
        "name": "Stephen's Sausage Roll",
        "category": "🧩 Головоломки",
        "professions": [
            "Разработчик игровых механик",
            "Дизайнер головоломок",
            "2D художник",
            "Гейм-дизайнер",
            "UI/UX дизайнер"
        ]
    },
    "World of Goo": {
        "name": "World of Goo",
        "category": "🧩 Головоломки",
        "professions": [
            "Физический программист",
            "2D художник",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Sound дизайнер"
        ]
    },
    "Braid": {
        "name": "Braid",
        "category": "🧩 Головоломки",
        "professions": [
            "2D художник",
            "Разработчик игровых механик",
            "Композитор",
            "Гейм-дизайнер",
            "UI/UX дизайнер"
        ]
    },
    "FEZ": {
        "name": "FEZ",
        "category": "🧩 Головоломки",
        "professions": [
            "2D художник",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Композитор",
            "Гейм-дизайнер"
        ]
    },
    "The Swapper": {
        "name": "The Swapper",
        "category": "🧩 Головоломки",
        "professions": [
            "2D художник",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Сценарист игр",
            "Sound дизайнер"
        ]
    },
    "Limbo": {
        "name": "Limbo",
        "category": "🧩 Головоломки",
        "professions": [
            "2D художник",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Гейм-дизайнер"
        ]
    },
    # Выживание
    "subnautica": {
        "name": "Subnautica",
        "category": "survival",
        "professions": [
            "3D художник",
            "Разработчик процедурной генерации",
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "Sound дизайнер"
        ]
    },
    "projectzomboid": {
        "name": "Project Zomboid",
        "category": "survival",
        "professions": [
            "2D художник",
            "Разработчик AI",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Специалист по оптимизации"
        ]
    },
    "valheim": {
        "name": "Valheim",
        "category": "survival",
        "professions": [
            "3D художник",
            "Разработчик физического движка",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Специалист по оптимизации"
        ]
    },
    "rust": {
        "name": "Rust",
        "category": "survival",
        "professions": [
            "Разработчик сетевого кода",
            "3D художник",
            "Разработчик игровых механик",
            "Специалист по античиту",
            "Backend разработчик"
        ]
    },
    "ark": {
        "name": "ARK: Survival Evolved",
        "category": "survival",
        "professions": [
            "3D художник",
            "Разработчик физического движка",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Специалист по оптимизации"
        ]
    },
    "theforest": {
        "name": "The Forest",
        "category": "survival",
        "professions": [
            "3D художник",
            "Разработчик AI",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Sound дизайнер"
        ]
    },
    "dontstarve": {
        "name": "Don't Starve",
        "category": "survival",
        "professions": [
            "2D художник",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Гейм-дизайнер",
            "Композитор"
        ]
    },
    "greenhell": {
        "name": "Green Hell",
        "category": "survival",
        "professions": [
            "3D художник",
            "Разработчик игровых механик",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Специалист по оптимизации"
        ]
    },

    # Головоломки
    "tetris": {
        "name": "Tetris Effect",
        "category": "puzzle",
        "professions": [
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "Композитор",
            "Гейм-дизайнер",
            "2D художник"
        ]
    },
    "lumines": {
        "name": "Lumines Remastered",
        "category": "puzzle",
        "professions": [
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "Композитор",
            "Гейм-дизайнер",
            "2D художник"
        ]
    },
    "hexcells": {
        "name": "Hexcells",
        "category": "puzzle",
        "professions": [
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "2D художник",
            "Гейм-дизайнер",
            "Композитор"
        ]
    },
    "snakebird": {
        "name": "Snakebird",
        "category": "puzzle",
        "professions": [
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "2D художник",
            "Гейм-дизайнер",
            "Композитор"
        ]
    },
    "hexcells": {
        "name": "Hexcells",
        "category": "puzzle",
        "professions": [
            "UI/UX дизайнер",
            "Разработчик игровых механик",
            "2D художник",
            "Гейм-дизайнер",
            "Композитор"
        ]
    },

    # Экшен игры
    "doom": {
        "name": "DOOM Eternal",
        "category": "action",
        "professions": [
            "Разработчик боевых систем",
            "3D художник",
            "Разработчик физического движка",
            "UI/UX дизайнер",
            "Sound дизайнер"
        ]
    },
    "devilmaycry": {
        "name": "Devil May Cry 5",
        "category": "action",
        "professions": [
            "Разработчик боевых систем",
            "3D аниматор",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Технический художник"
        ]
    },
    "bayonetta": {
        "name": "Bayonetta 3",
        "category": "action",
        "professions": [
            "Разработчик боевых систем",
            "3D аниматор",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Технический художник"
        ]
    },
    "metalgear": {
        "name": "Metal Gear Rising: Revengeance",
        "category": "action",
        "professions": [
            "Разработчик боевых систем",
            "3D аниматор",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Технический художник"
        ]
    },
    "ninjagaiden": {
        "name": "Ninja Gaiden: Master Collection",
        "category": "action",
        "professions": [
            "Разработчик боевых систем",
            "3D аниматор",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Технический художник"
        ]
    },
    "hades": {
        "name": "Hades",
        "category": "action",
        "professions": [
            "2D художник",
            "Разработчик боевых систем",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Гейм-дизайнер"
        ]
    },
    "deadcells": {
        "name": "Dead Cells",
        "category": "action",
        "professions": [
            "2D художник",
            "Разработчик боевых систем",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Гейм-дизайнер"
        ]
    },
    "hollowknight": {
        "name": "Hollow Knight",
        "category": "action",
        "professions": [
            "2D художник",
            "Разработчик боевых систем",
            "UI/UX дизайнер",
            "Sound дизайнер",
            "Гейм-дизайнер"
        ]
    }
} 