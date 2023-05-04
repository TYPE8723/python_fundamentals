import enum

class Season(enum.Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print(Season.SPRING)

print(Season.SPRING.name)

print(Season.SPRING.value)

print(type(Season.SPRING))

print(repr(Season.SPRING))## printing enum member as repr

print(list(Season))

for season in Season:
    print(season.name)