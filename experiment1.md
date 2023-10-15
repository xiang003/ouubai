# 实验一 Git和Markdown基础

班级： 21计科2

学号： B20210302216

姓名： 曾令翔

Github地址：<https://github.com/yourusername/python_course>

---

## 实验目的

1. Git基础，使用Git进行版本控制
2. Markdown基础，使用Markdown进行文档编辑

## 实验环境

1. Git
2. VSCode
3. VSCode插件

## 实验内容和步骤

### 第一部分 实验环境的安装

1. 安装git，从git官网下载后直接点击可以安装：[git官网地址](https://git-scm.com/)
2. 从Github克隆课程的仓库：[课程的仓库地址](https://github.com/zhoujing204/python_course)，运行git bash应用（该应用包含在git安装包内），在命令行输入下面的命令（命令运行成功后，课程仓库会默认存放在Windows的用户文件夹下）

```bash
git clone https://github.com/zhoujing204/python_course.git
```

如果你在使用`git clone`命令时遇到SSL错误，请运行下面的git命令(这里假设你的Git使用了默认安装目录)：

```bash
git config --global http.sslCAInfo C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
```

该仓库的课程材料后续会有更新，如果需要更新课程材料，可以在本地课程仓库的目录下运行下面的命令：

```bash
git pull
```

3. 注册Github账号，创建一个新的仓库，用于存放实验报告和实验代码。
4. 安装VScode，下载地址：[Visual Studio Code](https://code.visualstudio.com/)
5. 安装下列VScode插件
   - GitLens
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

### 第二部分 Git基础

教材《Python编程从入门到实践》P440附录D：使用Git进行版本控制，按照教材的步骤，完成Git基础的学习。

### 第三部分 learngitbranching.js.org

访问[learngitbranching.js.org](https://learngitbranching.js.org)，如下图所示完成Main部分的Introduction Sequence和Ramping Up两个小节的学习。

![Learngitbranching.js.org](/Experiments/img/2023-07-28-21-07-40.png)

上面你学习到的git命令基本上可以应付百分之九十以上的日常使用，如果你想继续深入学习git，可以：

- 继续学习[learngitbranching.js.org](https://learngitbranching.js.org)后面的几个小节（包括Main和Remote）
- 在日常的开发中使用git来管理你的代码和文档，用得越多，记得越牢
- 在git使用过程中，如果遇到任何问题，例如：错误删除了某个分支、从错误的分支拉取了内容等等，请查询[git-flight-rules](https://github.com/k88hudson/git-flight-rules)

### 第四部分 Markdown基础

查看[Markdown cheat-sheet](http://www.markdownguide.org/cheat-sheet)，学习Markdown的基础语法

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果




# 1.git commit

```
 git commit
 git commit
```

# 2.git branch

```
git brach bugFix //创建了⼀个bugFix分⽀
git checkout bugFix //切换分⽀
```

# 3. git merge
 ```
 git branch bugFix //创建了⼀个bugFix分⽀
git checkout bugFix //切换分⽀
git commit 
git checkout main 
git commit
git merge bugFix //将bugFix分⽀合并到main分⽀
```
# 4. git reset
```
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```
# 5. 分离head
```
git checkout C4
```
# 6.相对引用（^）
```
git checkout C4
git checkout HEAD^
```
# 7.相对引用2（~）
```
git branch -f main C6
git checkout C1
git branch -f bugFix C0
```
# 8.撤销变更
```
git reset C3^
git checkout pushed
git revert C2
```
**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## 实验考查

请使用自己的语言回答下面的问题，这些问题将在实验检查时用于提问和答辩，并要求进行实际的操作。

1. 什么是版本控制？使用Git作为版本控制软件有什么优点？
```
版本控制是一种管理和跟踪文件变化的系统。它记录了文件的每一次修改，可以帮助团队成员协同工作、追踪变更历史、恢复到之前的版本等。

Git是一种分布式版本控制系统，它具有以下几个优点：

分布式：每个开发者都可以拥有完整的代码仓库，可以在本地进行版本控制和修改，不需要依赖网络连接。这样可以提高开发效率，并且在没有网络的情况下仍然可以进行版本控制。

高效性能：Git的设计简洁高效，它使用了一种称为"快照"的方式来记录文件的变化，而不是直接记录文件的差异。这种方式使得Git在处理大型项目和大量文件时表现出色，速度快且占用空间少。

强大的分支管理：Git的分支管理功能非常强大，可以轻松创建、合并和切换分支。这使得团队成员可以并行开发不同的功能，而不会相互干扰。同时，Git的分支管理也使得项目的版本控制更加灵活和可靠。

安全性和完整性：Git使用了一种称为"哈希值"的机制来标识每个文件的内容，这保证了文件的完整性和安全性。一旦文件内容发生变化，Git会自动计算并更新哈希值，从而确保每个文件的版本都是唯一的。

```
   
2. 如何使用Git撤销还没有Commit的修改？如何使用Git检出（Checkout）已经以前的Commit？（实际操作）
 ```
 使⽤ git rm--cached-r 或者 git reset 可以撤销修改。
使⽤ git checkout [-q] [＜commit＞] [--]＜paths＞ 或者 git checkout [＜branch＞]来检测
```
3. Git中的HEAD是什么？如何让HEAD处于detached HEAD状态？（实际操作）
```
在Git中，HEAD是指向当前所在分支的指针。要将HEAD置于detached HEAD状态，可以使用以下命
令：
git checkout <commit的哈希值>：将HEAD指向指定的提交，不再指向任何分支。
```
4. 什么是分支（Branch）？如何创建分支？如何切换分支？（实际操作）
 ```
# 分支是主线某个状态的一个复制, 在不影响主线情况下, 可以有新的变化
# 创建分支<name>
git branch <name>
# 切换到分支<name>
git checkout <name>
# 创建并切换到分支<name>
git checkout -b <name>
```
5. 如何合并分支？git merge和git rebase的区别在哪里？（实际操作）
 ```
#将分支<name>合并到当前分支
git merge <name>
#将当前分支合并到<name>
git rebase <name>
```
6. 如何在Markdown格式的文本中使用标题、数字列表、无序列表和超链接？（实际操作）
```
在Markdown格式的文本中使用标题、数字列表、无序列表和超链接可以按照以下方式进行：
标题：使用#符号，#后面加空格和标题内容，#越多表示标题级别越低。
数字列表：使用数字和句点，例如"1. "，后面加上列表项内容。
无序列表：使用星号、加号或减号，后面加上列表项内容。
超链接：使用方括号和圆括号，方括号中是链接的显示文本，圆括号中是链接的URL。
```

## 实验总结

```
1. Git基础操作：学习了Git的基本命令，包括初始化仓库、添加文件、提交修改、撤销修改、查看提交历史、切换分支、合并分支等操作。
2. 分支管理：了解了分支的概念和作用，学习了创建、切换、合并和删除分支的方法。
3. 学会了使用markdown语法来做笔记以及转码为pdf格式
4. 版本控制：学习了版本控制的概念，了解了Git作为一种强大的版本控制系统的优点和使用方法。
```
