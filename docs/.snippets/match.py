import textcase

textcase.kebab.match("css-class-name")  # True
textcase.snake.match("css-class-name")  # False
textcase.snake.match("CSS_CLASS_NAME")  # False
