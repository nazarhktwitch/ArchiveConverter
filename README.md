# ArchiveConverter

**ArchiveConverter** is a utility for converting archives between different formats, such as ZIP, RAR, 7z, TAR, GZ, and others. The program allows users to easily change the archive format for convenience.

## Installation

Ensure you have Microsoft Visual C++ 14 or greater, if not get it with Microsoft Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/

You need to install components:

Desktop development with C++

MSVC v142 - VS 2019 C++ x64/x86 build tools (Or analog for your visual studio version)

Windows 10 SDK

And restart your pc

1. Clone or download the repository.
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Ensure you have libraries for working with archives, such as `py7zr`, `rarfile`, and others.

## Usage

Run the program by specifying the source and target archive formats. Example:

```bash
python archive_converter.py input.zip output.7z
```

Supported formats:
- ZIP
- RAR
- 7z
- TAR
- GZ
- BZ2
- XZ
- LZMA
- ARJ
- LZH

## Example Conversion

1. Converting from ZIP to 7z:

```bash
python archive_converter.py archive.zip archive.7z
```

2. Converting from RAR to ZIP:

```bash
python archive_converter.py archive.rar archive.zip
```

## Dependencies

- `py7zr`
- `rarfile`
- `zipfile`
- `pyunpack`
- `patoolib`

To install them, use the command:

```bash
pip install -r requirements.txt
```

---

### `requirements.txt`

```
py7zr
rarfile
pyunpack
patoolib
```
