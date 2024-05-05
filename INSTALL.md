# Install (tested on Ubuntu 24 LTS)

```
apt install -y pkg-config cmake libssl-dev pipenv make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git
```

## Manually install Rust Compiler with flags enabled (works with version 1.69)

Rust compiler is needed for tokenizer and transformers library compilation. 

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

export PATH="$HOME/.cargo/bin:$PATH"

rustup install 1.69
rustup default 1.69
export RUSTFLAGS="-A invalid_reference_casting"
source ~/.bashrc
```

Check to see if correct rust version is installed 

`rustc --version`


## Install python (v3.10) 

```
curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

source ~/.bashrc

pyenv install 3.10.14

pyenv global 3.10

```

## Install missing dependencies 

This works with specific versions of tokenizers and transformers library

```
cd promting_hate_speech
pip install -r requirements.txt
```

## RUN 

`python run_encoder.py`

