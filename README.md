### README in English

# ArchiveConverter

**ArchiveConverter** is a utility for converting archives between different formats, such as ZIP, RAR, 7z, TAR, GZ, and others. The program allows users to easily change the archive format for convenience.

## Installation

Ensure you have Microsoft Visual C++ 14 or greater, if not get it with Microsoft Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/

You need to install components:

Desktop development with C++

MSVC v142 - VS 2019 C++ x64/x86 build tools (All analog for your visual studio version)

Windows 10 SDK

If you haveproblems with installing libraries try to use in cmd pip install --upgrade setuptools wheel

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

---

### README на русском

# ArchiveConverter

**ArchiveConverter** — это утилита для конвертации архивов между различными форматами, такими как ZIP, RAR, 7z, TAR, GZ и другими. Программа позволяет пользователям легко изменять формат архивов для удобства работы с ними.

## Установка

1. Клонируйте репозиторий или скачайте его.
2. Установите зависимости с помощью pip:

```bash
pip install -r requirements.txt
```

3. Убедитесь, что у вас установлены библиотеки для работы с архивами, такие как `py7zr`, `rarfile` и другие.

## Использование

Запустите программу, указав исходный и целевой архивные форматы. Пример:

```bash
python archive_converter.py input.zip output.7z
```

Поддерживаемые форматы:
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

## Пример конвертации

1. Конвертация из ZIP в 7z:

```bash
python archive_converter.py archive.zip archive.7z
```

2. Конвертация из RAR в ZIP:

```bash
python archive_converter.py archive.rar archive.zip
```

## Зависимости

- `py7zr`
- `rarfile`
- `zipfile`
- `pyunpack`
- `patoolib`

Для их установки используйте команду:

```bash
pip install -r requirements.txt
```
