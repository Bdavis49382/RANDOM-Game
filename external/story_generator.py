attributes = {
    "Player Look": [
        "Rogue",
        "Blob",
        "Fighter",
        "Frog",
        "Elf",
        "Dwarf"
    ],
    "Player abilities": [
        "Pistol",
        "Stabby Sword",
        "Slashy Sword",
        "Bow and Arrow",
        "Laser Gun",
        "Punch",
        "Kick"
    ],
    "Enemy Look": [
        "Angry Blobs",
        "Grunts",
        "Goblins",
        "Zombies",
        "Guards",
    ],
    "Scenario": [
        "Survive as long as you can",
        "Steal the artifact",
        "Destroy the enemy base",
        "Explore the area",
        "Find the heart of the dungeon",
        "Defeat your enemy",
    ],
    "Co-op": [
        "With a friend",
        "By yourself"
    ],
    "Level Appearance": [
        "Outer space: the final frontier",
        "The forest floor",
        "The Dark dungeons",
        "A tropical island",
        "A spaceship"
    ]
}
import random

parts = [random.choice(attribute_list).lower() for attribute_list in attributes.values()]
story = 'You, a(n) {0} with your handy {1}, set out to fight {2} in order to {3} {4} in {5}'.format(*parts)
print(story)
