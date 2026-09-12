# aclilearner

This is a command line tool that gives us quick tldr examples on the commands which are categorized.
It also includes a download organizer that organizes the files in the download directory to appropriate folders.
The goal of this project was to learn package distribution.

## Installation

aclilearner is available in pypi

```bash
pip install aclilearner
```

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZLaTaN003/aclilearner.git
   ```

2. **Set up a virtual environment (recommended):**

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install .
   ```

4. **Run the program:**
   ```bash
   cd src/
   python -m acli.main fd  # -h for help
   ```

### Preview

![demo](https://raw.githubusercontent.com/ZLaTaN003/aclilearner/4f7592f0e9c07e103869dd179da16854c98a3a2d/images/demo.gif)

#### Command TLDR from [tldr.inbrowser.app](https://tldr.inbrowser.app/)