# bee

[![Test packages](https://github.com/redpanas/bee/actions/workflows/test.yml/badge.svg)](https://github.com/redpanas/bee/actions/workflows/test.yml)

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

Options:

```text
bee [OUTPUT_FILE]
bee --help
bee --version
```

## Installation

Every distribution installs the command as `bee`. The package is named `bee`
where that name is available; registries where another project already owns
the name use `bee-holy-scripture`.

### Standalone script

```sh
git clone https://github.com/redpanas/bee.git
cd bee
sudo install -m 755 bee /usr/local/bin/bee
```

### Linux release packages

The [v1.0.0 GitHub release](https://github.com/redpanas/bee/releases/tag/v1.0.0)
provides `.deb`, `.rpm`, `.apk`, and portable `.tar.gz` files.

### Homebrew

```sh
brew install redpanas/tap/bee-holy-scripture
```

### Ubuntu PPA

The initial package for Ubuntu 24.04 LTS is currently in the
[Launchpad build queue](https://launchpad.net/~redpanas/+archive/ubuntu/bee/+build/33563177).
Once published, install it with:

```sh
sudo add-apt-repository ppa:redpanas/bee
sudo apt update
sudo apt install bee-holy-scripture
```

### Snap

The Snap Store package is published. Its short `bee` alias is awaiting store
approval, so use the fully qualified command until that approval is granted:

```sh
sudo snap install bee-holy-scripture
snap run bee-holy-scripture.bee
```

### npm

```sh
npm install --global bee-holy-scripture
bee --version
```

### PyPI

```sh
pipx install bee-holy-scripture
bee --version
```

### RubyGems

```sh
gem install bee-holy-scripture
bee --version
```

### Cargo

```sh
cargo install bee-holy-scripture
bee --version
```

### Nix

```sh
nix --extra-experimental-features "nix-command flakes" \
  profile install github:redpanas/bee
```

If `nix-command` and flakes are enabled globally, the shorter form works:

```sh
nix profile install github:redpanas/bee
```

## License

The source code in this repository is available under the [MIT License](LICENSE).
Bee Movie and its screenplay belong to their respective copyright holders and
are not included in this repository.
