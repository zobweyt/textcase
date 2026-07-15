import textcase

textcase.snake("scale2D")  # scale_2_d

textcase.snake("scale2D", boundaries=[textcase.LOWER_DIGIT])  # scale_2d
textcase.snake("scale2D", boundaries=[])  # scale2d
