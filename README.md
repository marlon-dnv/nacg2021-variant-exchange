# NACG / VariantExchange API Workshop

## Setup

### Installing Python

There are several different ways to install python, if it's not installed already.

#### **Conda**

1. Download an installer
   - Windows - <https://docs.conda.io/en/latest/miniconda.html#windows-installers>
     - Use the 64-bit installer unless you are absolutely certain you're running 32-bit Windows
   - MacOS - <https://docs.conda.io/en/latest/miniconda.html#macos-installers>
     - `bash`: installs via command-line
     - `pkg`: GUI installation (I think?)
     - `Apple M1 ARM`: Use if you have a new MacBookPro that uses the M1/ARM64 CPU
   - Linux - <https://docs.conda.io/en/latest/miniconda.html#linux-installers>
     - Use the standard 64-bit installer unless you know you have a different CPU architecture
2. Run the installer
   - Windows exe / MacOS pkg
     - Double-click the downloaded file
   - MacOS / Linux
     - In a terminal: `bash Miniconda3-py39_4.10.3-Linux-x86_64.sh`
     - _NB:_ the exact filename of the script will vary depending on the version downloaded
3. Follow the installer prompts
   - If you are unsure about any of the options, use the default settings
4. Open a new terminal window and run `conda list` to test that everything was installed correctly

#### **Homebrew** _(MacOS only)_

- `brew install python`

#### **Package Managers** _(Linux only, requires root/sudo privileges)_

- Debian/Ubuntu-based distros
  - `sudo apt-get update && sudo apt-get install python3 python3-pip python3-venv`
- CentOS/RedHat/Fedora
  - `sudo dnf install python3`

### Create a virtual environment

#### Windows

```sh
python -m venv venv
venv\Scripts\activate
```

#### MacOS / Linux

```bash
python -m venv venv
source venv/bin/activate
# your prompt should now start with (venv) to show that the virtualenv is active
```

### Install dependencies

Make sure the virtualenv you created in the previous step is active. If it is, your command prompt should start with `(venv)`.

```sh
pip install -r requirements.txt
```

### Install an IDE

You can use any basic text editor to write python code, but specialized applications called IDEs
(Integrated Development Environment) make it a lot easier and using them is highly recommended. All
three of the IDEs listed below support Windows, MacOS and Linux operating systems.

- VS Code
  - <https://code.visualstudio.com/#alt-downloads>
- Atom
  - <https://flight-manual.atom.io/getting-started/sections/installing-atom/>
- Notepad++
  - <https://notepad-plus-plus.org/downloads/>
