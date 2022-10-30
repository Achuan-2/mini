> 为什么要用zsh不用bash
>
> 1. 可以配置主题，[powerlevel10k](https://github.com/romkatv/powerlevel10k)，省心美观好用。
> 2. 可以加插件，自动补全很好用
>

# 安装git zsh
## 2
## h3

‍

1. 链接[Package: zsh - MSYS2 Packages](https://packages.msys2.org/package/zsh?repo=msys&variant=x86_64)

    ![image](https://assets.b3logfile.com/siyuan/1610205759005/assets/image-20221023111504-d8ewb0f.png)​
2. 这里推荐使用 https://peazip.github.io/ 进行解压。当然如果你有其他的解压工具能解压也行。

    ![Snipaste_2022-10-23_11-16-00](https://assets.b3logfile.com/siyuan/1610205759005/assets/Snipaste_2022-10-23_11-16-00-20221023111603-bl2idvo.png)​
3. 在移动到Git目录前，我们需要先修改zsh的文件，点开usr/bin，删除0kb的zsh，把zsh-5.9.exe重命名为zsh.exe

    ![Snipaste_2022-10-23_11-17-05](https://assets.b3logfile.com/siyuan/1610205759005/assets/Snipaste_2022-10-23_11-17-05-20221023111707-e7oboem.png)​
4. 打开Git的安装目录根目录

    ![Snipaste_2022-10-23_11-17-39](https://assets.b3logfile.com/siyuan/1610205759005/assets/Snipaste_2022-10-23_11-17-39-20221023111808-vfo1wj2.png)​
5. 把zsh所有文件粘贴过去

    ![Snipaste_2022-10-23_11-18-50](https://assets.b3logfile.com/siyuan/1610205759005/assets/Snipaste_2022-10-23_11-18-50-20221023111852-odd61cm.png)​

# 配置Git-zsh

1. vim ~/.bash_profile

    ```bash
    if [ -t 1 ]; then
      exec zsh
    fi
    ```
2. 安装 oh-my-zsh

    ```bash
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```
3. 配置conda

    不能直接conda init

    ```bash
    conda init zsh
    ```

    编辑conda.sh

    ```bash
    export CONDA_EXE='/d/Environment/miniconda/Scripts/conda.exe'
    export _CE_M=''
    export _CE_CONDA=''
    export CONDA_PYTHON_EXE='D:\Environment\miniconda\python.exe'

    # Copyright (C) 2012 Anaconda, Inc
    # SPDX-License-Identifier: BSD-3-Clause
    __add_sys_prefix_to_path() {
        # In dev-mode CONDA_EXE is python.exe and on Windows
        # it is in a different relative location to condabin.
        if [ -n "${_CE_CONDA}" ] && [ -n "${WINDIR+x}" ]; then
            SYSP=$(\dirname "${CONDA_EXE}")
            SYSP=$(echo ${SYSP} | tr -d '\r')
        else
            SYSP=$(\dirname "${CONDA_EXE}")
            SYSP=$(\dirname "${SYSP}")
            SYSP=$(echo ${SYSP} | tr -d '\r')
        fi

        if [ -n "${WINDIR+x}" ]; then
            PATH="${SYSP}/bin:${PATH}"
            PATH="${SYSP}/Scripts:${PATH}"
            PATH="${SYSP}/Library/bin:${PATH}"
            PATH="${SYSP}/Library/usr/bin:${PATH}"
            PATH="${SYSP}/Library/mingw-w64/bin:${PATH}"
            PATH="${SYSP}:${PATH}"
            PATH=$(echo ${PATH} | tr -d '\r')
        else
            PATH="${SYSP}/bin:${PATH}"
            PATH=$(echo ${PATH} | tr -d '\r')
        fi
        \export PATH
    }

    __conda_exe() (
        __add_sys_prefix_to_path
        $(echo "$CONDA_EXE" | tr -d '\r') $_CE_M $_CE_CONDA $(echo "$@" | tr -d '\r')
    )

    __conda_hashr() {
        if [ -n "${ZSH_VERSION:+x}" ]; then
            \rehash
        elif [ -n "${POSH_VERSION:+x}" ]; then
            :  # pass
        else
            \hash -r
        fi
    }

    __conda_activate() {
        if [ -n "${CONDA_PS1_BACKUP:+x}" ]; then
            # Handle transition from shell activated with conda <= 4.3 to a subsequent activation
            # after conda updated to >= 4.4. See issue #6173.
            PS1="$CONDA_PS1_BACKUP"
            PS1=$(echo ${PS1} | tr -d '\r')
            \unset CONDA_PS1_BACKUP
        fi
        \local ask_conda
        ask_conda="$(PS1="${PS1:-}" __conda_exe shell.posix "$@")" || \return
        ask_conda=$(echo ${ask_conda:gs/\\/\/} | tr -d '\r')
        \eval "$ask_conda"
        __conda_hashr
    }

    __conda_reactivate() {
        \local ask_conda
        ask_conda="$(PS1="${PS1:-}" __conda_exe shell.posix reactivate)" || \return
        ask_conda=$(echo ${ask_conda} | tr -d '\r')
        \eval "$ask_conda"
        __conda_hashr
    }

    conda() {
        \local cmd="${1-__missing__}"
        case "$cmd" in
            activate|deactivate)
                __conda_activate $(echo "$@" | tr -d '\r')
                ;;
            install|update|upgrade|remove|uninstall)
                __conda_exe $(echo "$@" | tr -d '\r') || \return
                __conda_reactivate
                ;;
            *)
                __conda_exe $(echo "$@" | tr -d '\r')
                ;;
        esac
    }

    if [ -z "${CONDA_SHLVL+x}" ]; then
        \export CONDA_SHLVL=0
        # In dev-mode CONDA_EXE is python.exe and on Windows
        # it is in a different relative location to condabin.
        if [ -n "${_CE_CONDA:+x}" ] && [ -n "${WINDIR+x}" ]; then
            PATH="$(\dirname "$CONDA_EXE")/condabin${PATH:+":${PATH}"}"
        else
            PATH="$(\dirname "$(\dirname "$CONDA_EXE")")/condabin${PATH:+":${PATH}"}"
        fi
        \export PATH

        # We're not allowing PS1 to be unbound. It must at least be set.
        # However, we're not exporting it, which can cause problems when starting a second shell
        # via a first shell (i.e. starting zsh from bash).
        if [ -z "${PS1+x}" ]; then
            PS1=
        fi
    fi
    ```

    然后编辑~/.zshrc  

    ```bash
    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    export PYTHONIOENCODING=UTF-8
    . /d/Environment/miniconda/etc/profile.d/conda.sh
    conda activate ai
    # <<< conda initialize <<<

    ```
4. 安装插件

    ```Bash
    #插件存放于 ~/.oh-my-zsh/custom/plugins
    # git下载 zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    # git下载 zsh-autosuggestions
    # git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```

    下载完成后，我们修改一下zsh的配置文件，使插件生效。

    ```Bash
    # 首先用vim进入.zshrc配置文件
    vim ~/.zshrc

    # 之后利用vim编辑文件为
    plugins=(
            git
            zsh-syntax-highlighting
            # zsh-autosuggestions #不建议开启
            )

    source $ZSH/oh-my-zsh.sh
    source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    ```
5. 配置[powerlevel10k](https://github.com/romkatv/powerlevel10k)

    ```bash
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
    ```

    换主题`vim ~/.zshrc`​​​

    ```bash
    ZSH_THEME="powerlevel10k/powerlevel10k"
    ```

    ​`source ~/.zshrc`​​​

    配置主题`p10k configure`​

    > 注意：选择Unicode而不是ASCII，就可以选择显示icon模式
    >
6. 安装neofetch

    ```powershell
    # 安装scoop
    iwr -useb get.scoop.sh | iex
    # 安装neofetch
    scoop install neofetch
    ```

![Snipaste_2022-10-23_12-19-04](https://assets.b3logfile.com/siyuan/1610205759005/assets/Snipaste_2022-10-23_12-19-04-20221023121912-v64277c.png)​

![Snipaste_2022-10-23_12-21-21](https://assets.b3logfile.com/siyuan/1610205759005/assets/Snipaste_2022-10-23_12-21-21-20221023122127-2rm2i1r.png)​

完结撒花

> Linux安装zsh见
>
> * root用户
>
>   * [linux 安装并配置zsh - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1702635)
> * 非root用户：
>
>   * [Linux 以非root用户安装zsh&amp;配置on my zsh - Xi-iX - 博客园 ](https://www.cnblogs.com/XiiX/p/14618799.html)
>

# 注意

* 不建议开启`zsh-syntax-highlighting`​：会导致vscode 运行代码，终端显示命令是一个字一个字蹦出来的，很烦，建议关闭！
* ​`zsh-autosuggestions`​可能会导致粘贴卡顿，建议在`~.zshrc`​粘贴下面一句

  ```bash
  pasteinit() {
    OLD_SELF_INSERT=${${(s.:.)widgets[self-insert]}[2,3]}
    zle -N self-insert url-quote-magic # I wonder if you'd need `.url-quote-magic`?
  }

  pastefinish() {
    zle -N self-insert $OLD_SELF_INSERT
  }
  zstyle :bracketed-paste-magic paste-init pasteinit
  zstyle :bracketed-paste-magic paste-finish pastefinish
  ```