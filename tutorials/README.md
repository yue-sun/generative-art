# Introduction to Generative Art and Scientific Visualization (January@GSAS 2023)

## Python tutorial

`python_tutorial.ipynb`

This tutorial walks through the basics of Python programming and plotting.

`vscode_tutorial.py`

This Python script contains examples of the interactive and debugging modes in Visual Studio Code.

## Run code (locally)

We store all code examples on GitHub, which allows us to version control the code. To have your own local updated copy of the course git repo:
1. Open your terminal and navigate to target directory
    ```
    cd your_target_directory_generative_art
    ```

2. Clone the Git repo
    ```
    git clone https://github.com/yue-sun/generative-art.git
    ```

3. To access updates to the code examples use
    ```
    git pull
    ```
You can also use the GitHub Desktop app to keep a local copy of the repo. If you use VS Code, its source control should automatically have the options to pull the changes.

## Python installation

You may have different preferences in terms of how to use Python. Google Colab is an ideal choice to run your code without having to install Python on your machine. However, if you prefer to work on the code locally, you need to (properly) install your Python environment. In addition, you need to install Jupyter notebook because it allows interactive editing.

### The easy way

The most straightforward way is to install using `Anaconda` and `conda`. This approach will point your Python and modules to the `conda` environment. If you do not point your Python path correctly, you will likely end up in a [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell). However, it requires very few installation steps and is suitable for new users. Follow this [official documentation](https://docs.jupyter.org/en/latest/install/notebook-classic.html) to download `Anaconda`.

### The "proper" way

If you do not want to deal with the Python dependency hell in the near future, I highly recommend installing Python and Jupyter **NOT** using `conda`. This will require some more steps, but it will make your path much cleaner.

> Note that the following commands are only tested on Mac OS Monterey (in January 2022). For Linux users, it should also work (but requires some changes to default Python paths and `Homebrew` installation). For Windows users, you can check out this [link](https://www.python.org/downloads/). **`Homebrew` approach does not work for Windows.** If you run into any issues, you can contact the teaching staff for help. 

1. Check whether your machine already has Python 3 installed in your terminal (and its version)
    ```
    $ which python3
    /usr/bin/python3

    $ python3 --version
    Python 3.8.9
    ```
    We need to upgrade the Python version to 3.9, which can either be done via directly [downloading Python](https://www.python.org/downloads/) (this option your Python path will remain the same), or use `Homebrew` to install Python 3.9 (this option your Python path will change). The following steps are based on installing using `Homebrew`.

2. Install `Homebrew`
    ```
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    (No need to install/download Xcode, command line tools will automatically download.)

3. Set Homebrew path
    ```
    $ echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/$USER/.zprofile
    $ eval $(/opt/homebrew/bin/brew shellenv)
    $ brew help
    ```
    (The last command to check whether `Homebrew` is successfully installed.)

4. Install git (for GitHub)
    ```
    brew install git
    ```

5. Install Python 3.9
    ```
    brew install python@3.9
    ```

6. Reset default Python and set `Homebrew` Python path
    ```
    nano ~/.bash
    alias python=python3.9
    ```
    (Edit the file and save.)
    ```
    source ~/.bash
    export PATH="/usr/local/opt/python/libexec/bin:$PATH"
    which python3
    python3 --version
    ```
    (Should give 3.9 instead of the default 3.8, and the path is `/opt/homebrew/bin/python3`.)

7. Install `pip` and Jupyter notebook
    ```
    pip3 install --upgrade pip
    pip3 install jupyter
    export PATH=~/.local/bin:$PATH
    jupyter notebook
    ```
    (Check if the browser launches the notebook window.)

8. Install Python packages

    You can directly install all the modules by default:
    ```
    pip3 install numpy scipy matplotlib sklearn pandas opencv-python torch
    ```
    >But I would recommend creating a [virtual environment](https://docs.python.org/3/library/venv.html) for the course and installing all the modules there. This will give you a clean Python environment. Note that all the modules will only exist in the virtual environment. If you do not activate that environment, you will find the module is missing.
    >
    >Step 1: Create a virtual environment
    >```
    >python3 -m pip install --user virtualenv
    >python3 -m venv /path/to/new/virtual/environment/am111
    >```
    >
    >Step 2: Activate the virtual environment
    >```
    >source /path/to/new/virtual/environment/am111/bin/activate
    >```
    >
    >Step 3: Install Python packages in the virtual environment
    >
    >Step 4: Leave the virtual environment
    >```
    >deactivate
    >```


## Recommended Python editor

You can use your favorite editor to code in Python, e.g., `Sublime Text` or `vim`. My personal recommendation for writing Python is [`Visual Studio Code`](https://code.visualstudio.com/), where you can code Python interactively, write and preview Jupyter notebooks and Markdown files, and debug your code easily.

You can follow this [official documentation](https://code.visualstudio.com/docs/python/python-tutorial) to install VS Code and the Python extension.
> The most important step is to select the right Python interpreter. Usually, VS Code is smart enough to detect the proper Python path. For example, on a Mac:
> - If you directly download Python 3.9 to install, the Python interpreter path should be the default `/usr/bin/python`.
> - If you install Python 3.9 using `Homebrew`, then the interpreter path is `/opt/homebrew/bin/python3`.
> - If you use `virtualenv` to install packages, then you should select the appropriate virtual environment Python path.

You can also edit Jupyter notebooks in VS Code. Follow this [official documentation](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) for details. You will likely need to install additional extensions in VS Code, but there should be an automatic pop window to suggest the installation.
> If you run `python_tutorial.ipynb` in VS Code, you can view/inspect/filter variables using the Variable Explorer and Data Viewer, which will greatly simplify debugging. This functionality does not exist if you open a Jupyter notebook through a browser.