# User specific environment and startup programs

FLO_HOME=/Users/flo
DOTNET_HOME=/opt/dotnet6
JAVA_HOME=/opt/jdk11
PHP_HOME=/opt/homebrew/opt/php
BUN_HOME=$FLO_HOME/.bun
DENO_HOME=$FLO_HOME/.deno
HOMEBREW_HOME=/opt/homebrew
GO_HOME=/usr/local/go
LUA_HOME=/usr/local/lua
VLANG_HOME=/usr/local/vlang
RUST_HOME=$FLO_HOME/.cargo
NIM_HOME=$FLO_HOME/.nimble
NODE_HOME=/opt/homebrew/opt/node
# the following lines will interfere with the original
# python path if you used the native python installer
#PYTHON_HOME=/opt/homebrew/opt/python\@3.9
#PYTHON_HOME=/opt/homebrew/opt/python\@3.10
#PYTHON_HOME=/opt/homebrew/opt/python\@3.11

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/flo/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/flo/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/flo/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/flo/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
conda deactivate
# <<< conda initialize <<<
# . "$HOME/.cargo/env"

export JAVA_HOME

PATH=$PATH:/usr/local/bin:/usr/local/sbin:

export PATH=$HOMEBREW_HOME/bin:$HOMEBREW_HOME/sbin:$JAVA_HOME/bin:$PHP_HOME/bin:$BUN_HOME/bin:$DENO_HOME/bin:$GO_HOME/bin:$LUA_HOME/bin:$RUST_HOME/bin:$NIM_HOME/bin:$DOTNET_HOME:$VLANG_HOME:$NODE_HOME/bin:$PATH
