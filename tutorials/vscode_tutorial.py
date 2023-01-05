# %%[markdown]
# # Run Python interactively in VS Code

# In VS Code, we can interactively run a `.py` file as if it is a Jupyter
# notebook. This means we can write Markdown, make our code into cell blocks,
# run cells separately, and debug cells.

# You can run this file interactively by stepping through each cell. Or you
# can just run the file via terminal (inside VS Code, "View -> Terminal")
# ```
# python3 /your/git/folder/00_python_tutorial/vscode_tutorial.py
# ```

# %%
# Import modules
import numpy as np


# %%
# Define a function (with a bug)
# Add a breakpoint at Line 25 by clicking in front of the line number
# (you should see a red dot)
def dot_error(a, b):
    # Modify shape of b to trigger an error
    b = np.reshape(b, newshape=(1, b.shape[0]))
    dot = np.dot(a, b)
    return dot


# %%
# Create two arrays and dot
# Note that this cell will return an error
a = np.ones(4)
b = np.ones(4) * 4
dot_error(a, b)


# %%[markdown]
# ## Debugging in VS Code

# If you run the cell above, it will return a ValueError.
# We can use the debug mode in VS Code to find the bug.
# Before we start debugging, click on the fourth icon of the most-left column
# to switch to "Run and Debug". While we step through the code, the variables
# will show up under the "VARIABLES".


# ### Approach 1: Locally using "Debug Cell"

# Above the cell (Line 30-35), there is a "Debug Cell" option.
# Click on it, and you can step over (F10) or into (F11) each line of the cell:
# - For example, you would want to step into Line 35 so that we can inspect
# `dot_error`, which is the problematic function.
# - You can hover your mouse over each variable and see its value/type/etc.
# - Once you are stepped into `dot_error`, open "Debug Console" (usually in
# the bottom panel, but you can also open it in "View -> Debug Console").
# - In the debug console, you can write small code snippets to test/verify
# your ideas or to check if a line has a bug. For example, you can type
# `np.dot(a, b)` in the debug console before stepping through
# `b = np.reshape(b, newshape=(1, b.shape[0]))`. It is clear that
# `np.dot(a, b)` works but the reshape function is causing problem.
# - We have located which line the bug is. Then we just need to fix it
# (by deleting that line).


# ### Approach 2: Run the entire file with breakpoints

# Breakpoints are probably the most useful thing when it comes to debugging.
# They allow us to pause the code at specific lines (typically at or before
# the bugs), step through the code line by line, and inspect variables.
# In VS Code, when we are in "Run and Debug", we need to initialize debugging
# configurations (usually "Debug the currently active Python file" will do).
# Follow this link https://code.visualstudio.com/docs/python/debugging:
# - Click on the green play button to start debugging the current Python file
# - The code will stop before Line 25.
# - Similarly, you can hover over variables (like `a` or `b`) to inspect them.
# - You can also test/verify code in the debug console.

# > Both approaches work when debugging. You can also select certain lines and
# > only run them by right-clicking and selecting "Run Selection/Line in
# > Interactive Window". However, using breakpoints may be more suitable for
# > longer Python files. (You can add as breakpoints as you like.)


# ### Exit debug mode
# Make sure to exit the debug mode after you are done debugging. Otherwise your
# actual Python program will run very slow if the debug mode is on.
