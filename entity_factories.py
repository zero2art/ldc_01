from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item
import tcod

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=40, base_defense=1, base_power=3),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)
dragon = Actor(
    char="*DRAGON*,
    color=(0x0, 0x0, 0x0),
    name="I'm a dragon mother fucker!!! You are so toast",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=100, base_defense=50, base_power=25),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=10000),
)

kobold = Actor(
    char="K",
    color=(63, 127, 63), 
    name="Kobold",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)

orc = Actor(
    char="O",
    color=(63, 127, 63), 
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=12, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=20, base_defense=3, base_power=6), 
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

wyvern = Actor(
    char="W", 
    color=(0x0, 0x0, 0x0),
    name="Wyvern",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=28, base_defense=5, base_power=6),
    inventory=Inventory(capacity=0), 
    level=Level(xp_given=100),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=5),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0), 
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger(),
)

sword = Item(
    char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword(),
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail(),
)