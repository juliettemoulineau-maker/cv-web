import re

with open('index.css', 'r') as f:
    css = f.read()

# We will find all blocks containing :hover.
# A block is roughly `selector { rules }`.
# But wait, we just want to replace `:hover` with `@media (hover: hover) { \n selector:hover { rules } \n }`

# Actually, doing it via a robust parser is better, but since it's a simple CSS file, we can do it manually for the important ones.
