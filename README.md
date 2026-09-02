# bee

The holy scripture downloader.

`bee` downloads a pinned plain-text copy of the Bee Movie dialogue transcript,
converts work-related words to leetspeak, and writes the result to a file.

## Requirements

The standalone script and native Linux packages require:

- A POSIX-compatible shell
- `curl`
- GNU `sed`

The PyPI package uses Python 3.9 or newer and works natively on Linux, macOS,
and Windows.

## Usage

```sh
./bee
```

This creates `the_holy_scripture.txt` in the current directory. To choose a
different destination, pass it as the first argument:

```sh
./bee output.txt
```

## Install

```sh
install -m 755 bee /usr/local/bin/bee
```

## Packages

Release builds provide packages for Debian/Ubuntu (`.deb`), Fedora/RHEL/openSUSE
(`.rpm`), and Alpine (`.apk`), plus a portable archive. Packaging definitions
for Arch/AUR, Homebrew on Linux, Nix, and Snap are in [`packaging`](packaging).

The package is named `bee` where that name is available. Registries where it is
already owned by another project use `bee-holy-scripture`. Every package installs
the command as `bee`.

### npm

```sh
npm install --global bee-holy-scripture
```

### PyPI

```sh
pipx install bee-holy-scripture
bee --version
```

### Nix

```sh
nix profile install github:redpanas/bee
```

On installations where flakes are not enabled globally:

```sh
nix --extra-experimental-features "nix-command flakes" \
  profile install github:redpanas/bee
```

## License

The source code in this repository is available under the [MIT License](LICENSE).
Bee Movie and its screenplay belong to their respective copyright holders and
are not included in this repository.
