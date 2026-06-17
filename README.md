# python-security-essentials

> Validate password strength and generate cryptographically secure passwords from the command line.

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-[DO%20UZUPEŁNIENIA]-lightgrey.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

---

## Description

**python-security-essentials** is a lightweight CLI utility that checks whether a password meets a defined strength policy and, if it does not, automatically generates a cryptographically secure replacement. It relies on Python's built-in `secrets` module — the standard library's recommended source of randomness for security-sensitive use cases — rather than the weaker `random` module. The tool is aimed at developers learning secure coding practices and at end users who need a quick password audit or generation tool without installing a full password manager.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- **Instant strength check** — validates a password against a four-class policy (lowercase, uppercase, digits, special characters) plus a minimum length of 8 characters.
- **Cryptographically secure generation** — uses `secrets.choice` and `secrets.SystemRandom` (backed by the OS CSPRNG) to produce 12-character passwords that are safe for security-critical contexts.
- **Guaranteed policy compliance** — generated passwords always satisfy all four character-class requirements before any additional random characters are appended.
- **Color-coded feedback** — green for valid passwords, red for failures, cyan for the generated replacement; works on Windows, macOS, and Linux via `colorama`.
- **Zero external dependencies beyond colorama** — no heavy frameworks, no network calls.

---

## Tech Stack

| Component | Detail |
|---|---|
| Language | Python 3.6+ |
| Randomness | `secrets` (stdlib) |
| Character sets | `string` (stdlib) |
| Colored output | `colorama` 0.4+ |

---

## Requirements

- **Python 3.6 or higher** — the `secrets` module was introduced in Python 3.6.
- **pip** — to install the single third-party dependency.

Check your Python version:

```bash
python --version
# or
python3 --version
```

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/eryks23/python-security-essentials.git
cd python-security-essentials
```

2. **Create and activate a virtual environment (recommended):**

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install the single dependency directly:

```bash
pip install colorama
```

---

## Usage

Run the script and enter the password you want to evaluate when prompted:

```bash
python [DO UZUPEŁNIENIA: script filename, e.g. password_checker.py]
```

**Example — weak password:**

```
Enter password to check: hello
Password too weak. Generating new one...
Your new password: aB3$rKp#X7mQ
```

**Example — strong password:**

```
Enter password to check: Tr0ub4dor&3
Password is correct!
```

A password passes validation when it meets **all** of the following criteria:

| Rule | Requirement |
|---|---|
| Length | At least 8 characters |
| Lowercase letters | At least 1 (`a–z`) |
| Uppercase letters | At least 1 (`A–Z`) |
| Digits | At least 1 (`0–9`) |
| Special characters | At least 1 (any `string.punctuation` character) |

---

## API Reference

Both functions can be imported into your own scripts.

### `check_password(password)`

Validates whether a password satisfies the strength policy.

```python
from [DO UZUPEŁNIENIA: module name] import check_password

check_password("Weak1")         # False — too short
check_password("alllowercase1!") # False — no uppercase
check_password("Str0ng!Pass")   # True
```

| Parameter | Type | Description |
|---|---|---|
| `password` | `str` | The password string to evaluate. |

**Returns:** `bool` — `True` if the password meets all requirements, `False` otherwise.

---

### `generate_password()`

Generates a 12-character cryptographically secure password that satisfies all four character-class requirements.

```python
from [DO UZUPEŁNIENIA: module name] import generate_password

pwd = generate_password()
print(pwd)  # e.g. "xB7#mKq!2pLr"
```

**Returns:** `str` — a 12-character password composed of at least one lowercase letter, one uppercase letter, one digit, and one special character; remaining characters are drawn randomly from the full pool (`string.ascii_letters + string.digits + string.punctuation`).

> **Security note:** `generate_password` uses `secrets.choice` and `secrets.SystemRandom().shuffle`, which draw entropy from the operating system's cryptographically secure pseudorandom number generator (CSPRNG). This is appropriate for generating passwords, tokens, and other security-critical values.

---

## Project Structure

```
python-security-essentials/
├── [DO UZUPEŁNIENIA: script filename]   # Main CLI script
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

> **Note:** If the project grows to include multiple utilities, this section should be updated to reflect the expanded structure.

---

## Testing

No automated tests are included at this time. To verify behaviour manually:

```bash
# Test weak password (no uppercase, too short)
echo "weak" | python [DO UZUPEŁNIENIA: script filename]

# Test strong password
echo "Str0ng!Pass" | python [DO UZUPEŁNIENIA: script filename]
```

To add unit tests using `pytest`:

```bash
pip install pytest
```

Example test file (`test_password.py`):

```python
from password_checker import check_password, generate_password

def test_short_password_fails():
    assert check_password("Ab1!") is False

def test_missing_uppercase_fails():
    assert check_password("weakpass1!") is False

def test_strong_password_passes():
    assert check_password("Str0ng!Pass") is True

def test_generated_password_passes_policy():
    pwd = generate_password()
    assert check_password(pwd) is True

def test_generated_password_length():
    pwd = generate_password()
    assert len(pwd) == 12
```

Run tests:

```bash
pytest test_password.py -v
```

---

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes with a clear message: `git commit -m "Add: brief description"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request against `main`.

Please ensure any new functions are covered by tests and that existing tests continue to pass before submitting a PR.

---

## Author

**eryks23** — [github.com/eryks23](https://github.com/eryks23)

Project repository: [https://github.com/eryks23/python-security-essentials](https://github.com/eryks23/python-security-essentials)
