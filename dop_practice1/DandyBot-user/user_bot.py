def script(check, x, y):
    if check("level") == 1:
        if check('gold', x, y):
            return 'take'

        if not check('wall', x + 2, y):
            return 'right'
        return 'down'

    elif check("level") == 2:
        if check('gold', x, y):
            return 'take'

        if check('gold', x + 1, y):
            return 'right'

        if check('gold', x, y - 1):
            return 'up'

        if check('gold', x, y + 1):
            return 'down'

        if check('wall', x + 2, y):
            return 'up'
        return 'right'

    elif check("level") == 3:
        if check('gold', x, y):
            return 'take'

        if not check('wall', x + 1, y) and (check('wall', x, y + 1) or check('wall', x + 1, y + 1)):
            return 'right'

        if not check('wall', x, y - 1) and (check('wall', x + 1, y) or check('wall', x + 1, y - 1)):
            return 'up'

        if not check('wall', x, y + 1) and (check('wall', x - 1, y) or check('wall', x - 1, y + 1)):
            return 'down'

        if not check('wall', x - 1, y) and (check('wall', x, y - 1) or check('wall', x - 1, y - 1)):
            return 'left'

    elif check("level") == 4:
        if check('gold', x, y):
            return 'take'

        if check("wall", x, y - 1) and check("wall", x - 2, y + 2) and check("wall", x - 1, y + 2) and check("wall", x, y + 2):
            return "down"

        if check("wall", x, y + 1) and check("wall", x + 2, y - 2) and check("wall", x + 1, y - 2) and check("wall", x, y - 2):
            return "up"

        if not check('wall', x + 1, y) and (check('wall', x, y + 1) or check('wall', x + 1, y + 1)):
            return 'right'

        if not check('wall', x, y - 1) and (check('wall', x + 1, y) or check('wall', x + 1, y - 1)):
            return 'up'

        if not check('wall', x, y + 1) and (check('wall', x - 1, y) or check('wall', x - 1, y + 1)):
            return 'down'

        if not check('wall', x - 1, y) and (check('wall', x, y - 1) or check('wall', x - 1, y - 1)):
            return 'left'