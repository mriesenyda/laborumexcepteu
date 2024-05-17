from selenium.webdriver.support.color import Color

def cprint(text, color):
    """
    Prints text in color to the console.

    Args:
        text (str): The text to print.
        color (str): The color to print the text in.
    """
    colors = {
        "black": Color.BLACK,
        "red": Color.RED,
        "green": Color.GREEN,
        "yellow": Color.YELLOW,
        "blue": Color.BLUE,
        "magenta": Color.MAGENTA,
        "cyan": Color.CYAN,
        "white": Color.WHITE,
    }
    if color not in colors:
        raise ValueError("Invalid color: {}".format(color))

    print(colors[color].decorate(text))
