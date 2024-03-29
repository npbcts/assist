
### 子模块git使用教程(此处是常用方法演示)  
相关的学习资源:  
- git官网关于git submoudle 命令的讲解:  [7.11 Git 工具 - 子模块](https://git-scm.com/book/zh/v2/-Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97)  
- 知乎网友 Hanley Lee发布的文章: [Git Submodule 使用](https://zhuanlan.zhihu.com/p/374662328)

***
#### 已有项目添加子模块

我们首先将一个已存在的 Git 仓库添加为正在工作的仓库的子模块assist。 你可以通过在 git submodule add 命令后面加上想要跟踪的项目的相对或绝对 URL 来添加新的子模块。

`git submodule add https://github.com/npbcts/assist.git`

私有模块使用以下命令:

`git submodule add git@github.com:npbcts/installer.git`

默认情况下，子模块会将子项目放到一个与仓库同名的目录中,即assist文件夹中。

虽然 assist 是工作目录中的一个子目录，但 Git 还是会将它视作一个子模块。当你不在那个目录中时，Git 并不会跟踪它的内容， 而是将它看作子模块仓库中的某个具体的提交。

#### 克隆含有子模块的项目

当你在克隆(使用普通的`git clone`)这样的项目时，默认会包含该子模块目录，但其中还没有任何文件。  
克隆含有子模块的项目并包含子项目所有文件的命令:  
`git clone --recurse-submodules https://github.com/chaconinc/xxxProject`

如果给 git clone 命令传递 --recurse-submodules 选项，它就会自动初始化并更新仓库中的每一个子模块， 包括可能存在的嵌套子模块。  
如果你已经克隆了项目但忘记了 --recurse-submodules，可以使用下述两种命令，下载子模块的内容:  
1. 直接初始化并更新
`git submodule update --init --recursive`

2. 先初始化后更新  
初始化子库: `git submodule init `  
更新子库: `git submodule update --remote`  

#### 在包含子模块的项目上工作
现在我们有一份包含子模块的项目副本，我们将会同时在主项目和子模块项目上与队员协作。  
git 的 submodule 作为一个独立的 repo, 其拥有普通 repo 全部的功能, 我们可以完全按照普通的 repo 管理命令来进入 submodule 中进行手动管理. 不过如果存在多个 submodule 位于同一 superproject 下时, 掌握一些 git submodule ... 命令就变得尤为重要了.

1. 从*子模块*的远端拉取上游修改

在项目中使用子模块的最简模型，就是只使用子项目并不时地获取更新，而并不在你的检出中进行任何更改。

如果想要在子模块中查看新工作，可以**进入到目录中**运行 `git pull`，合并上游分支来更新本地代码。

如果你现在返回到主项目，就会看到子模块被更新的同时获得了一个包含新添加提交的列表。

1.1 已有项目新建子项目的拉取，主项目下执行下面的命令，更新全部子项目:

`git pull --recurse-submodules`

2. 从*项目远端***更新**上游更改

在 主项目 仓库的本地克隆， 只是执行 git pull 获取你新提交的更改还不够，它不会 更新 子模块。  

在 主项目 仓库中更新子模块文件内容使用的命令:

`git submodule update --remote`

如果我们想让 Git 总是以 --recurse-submodules 拉取, 可以将配置选项 submodule.recurse 设置为 true. 具体命令为:
` git config --global submodule.recurse true`
此选项会让 Git 为所有支持 --recurse-submodules 的命令使用该选项 (除 clone 以外).

3. 在子模块上工作

在子模块中编写代码的同时，还想在主项目上编写代码

我们在主项目中提交并推送但并不推送子模块上的改动，其他尝试检出我们修改的人会遇到麻烦， 因为他们无法得到依赖的子模块改动。那些改动只存在于我们本地的拷贝中。

push主模块时，检查子模块是否推送的命令:
`git push --recurse-submodules=check`

可以通过设置 `git config push.recurseSubmodules check` 让它成为默认行为


#### 从当前项目移除 submodule

```python
git submodule deinit -f <submodule_path>  
rm -rf .git/modules/<submodule_path>  
git rm -f <submodule_path>  
```

#### 总结

1. 主模块的操作一般不影响子模块的文件,如pull, push

2. 进入子模块的目录中对相关内容进行修改, 然后通过常用的 git 命令进行操作，git命令和单独模块一致

3. 注意主模块pull,push过程中的针对所有子模块命令

4. 注意子模块先提交，主模块后提交

5. vscode的git管理工具，针对不同子模块的git单独管理

6. 在 `repo Test` 作为 `submodule` 被 `superproject` 管理后:在 `superproject` 下可以通过 `git submodule ***` 命令来管理其下的所有子仓库, 使其与远程库保持同步或推送到远程库.