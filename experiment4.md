# 实验四 Python字典和while循环

班级： 21计科2

学号： B20210302216

姓名： 曾令翔

Github地址：<https://github.com/xiang003/ouubai>

CodeWars地址：<https://www.codewars.com/users/ouubai>

---

## 实验目的

1. 学习Python字典
2. 学习Python用户输入和while循环

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

Python列表操作

完成教材《Python编程从入门到实践》下列章节的练习：

- 第6章 字典
- 第7章 用户输入和while循环

---

### 第二部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：淘气还是乖孩子（Naughty or Nice）

难度： 7kyu

圣诞老人要来镇上了，他需要你帮助找出谁是淘气的或善良的。你将会得到一整年的JSON数据，按照这个格式：

```python
{
    January: {
        '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
    },
    February: {
        '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
    },
    ...
    December: {
        '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
    }
}
```

你的函数应该返回 "Naughty!"或 "Nice!"，这取决于在某一年发生的总次数（以较大者为准）。如果两者相等，则返回 "Nice！"。
代码提交地址：
<https://www.codewars.com/kata/5662b14e0a1fb8320a00005c>

---

#### 第二题： 观察到的PIN（The observed PIN）

难度：4kyu

好了，侦探，我们的一个同事成功地观察到了我们的目标人物，抢劫犯罗比。我们跟踪他到了一个秘密仓库，我们认为在那里可以找到所有被盗的东西。这个仓库的门被一个电子密码锁所保护。不幸的是，我们的间谍不确定他看到的密码，当罗比进入它时。

键盘的布局如下：

```python
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```

他注意到密码1357，但他也说，他看到的每个数字都有可能是另一个相邻的数字（水平或垂直，但不是对角线）。例如，代替1的也可能是2或4。而不是5，也可能是2、4、6或8。

他还提到，他知道这种锁。你可以无限制地输入错误的密码，但它们最终不会锁定系统或发出警报。这就是为什么我们可以尝试所有可能的（*）变化。

*可能的意义是：观察到的PIN码本身和考虑到相邻数字的所有变化。

你能帮助我们找到所有这些变化吗？如果有一个函数，能够返回一个列表，其中包含一个长度为1到8位的观察到的PIN的所有变化，那就更好了。我们可以把这个函数命名为getPINs（在python中为get_pins，在C#中为GetPINs）。

但请注意，所有的PINs，包括观察到的PINs和结果，都必须是字符串，因为有可能会有领先的 "0"。我们已经为你准备了一些测试案例。
侦探，我们就靠你了!
代码提交地址：
<https://www.codewars.com/kata/5263c6999e0f40dee200059d>

---

#### 第三题： RNA到蛋白质序列的翻译（RNA to Protein Sequence Translation）

难度：6kyu

蛋白质是由DNA转录成RNA，然后转译成蛋白质的中心法则。RNA和DNA一样，是由糖骨架（在这种情况下是核糖）连接在一起的长链核酸。每个由三个碱基组成的片段被称为密码子。称为核糖体的分子机器将RNA密码子转译成氨基酸链，称为多肽链，然后将其折叠成蛋白质。

蛋白质序列可以像DNA和RNA一样很容易地可视化，作为大字符串。重要的是要注意，“停止”密码子不编码特定的氨基酸。它们的唯一功能是停止蛋白质的转译，因此它们不会被纳入多肽链中。“停止”密码子不应出现在最终的蛋白质序列中。为了节省您许多不必要（和乏味）的键入，已为您的氨基酸字典提供了键和值。

给定一个RNA字符串，创建一个将RNA转译为蛋白质序列的函数。注意：测试用例将始终生成有效的字符串。

```python
protein（'UGCGAUGAAUGGGCUCGCUCC'）
```

将返回`CDEWARS`

作为测试用例的一部分是一个真实世界的例子！最后一个示例测试用例对应着一种叫做绿色荧光蛋白的蛋白质，一旦被剪切到另一个生物体的基因组中，像GFP这样的蛋白质可以让生物学家可视化细胞过程！

Amino Acid Dictionary

```python
   # Your dictionary is provided as PROTEIN_DICT
   PROTEIN_DICT = {
    # Phenylalanine
    'UUC': 'F', 'UUU': 'F',
    # Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Methionine
    'AUG': 'M',
    # Valine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine
    'UAU': 'Y', 'UAC': 'Y',
    # Histidine
    'CAU': 'H', 'CAC': 'H',
    # Glutamine
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine
    'AAU': 'N', 'AAC': 'N',
    # Lysine
    'AAA': 'K', 'AAG': 'K',
    # Aspartic Acid
    'GAU': 'D', 'GAC': 'D',
    # Glutamic Acid
    'GAA': 'E', 'GAG': 'E',
    # Cystine
    'UGU': 'C', 'UGC': 'C',
    # Tryptophan
    'UGG': 'W',
    # Arginine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # Stop codon
    'UAA': 'Stop', 'UGA': 'Stop', 'UAG': 'Stop'
}
```

代码提交地址：
<https://www.codewars.com/kata/555a03f259e2d1788c000077>

---

#### 第四题： 填写订单（Thinkful - Dictionary drills: Order filler）

难度：8kyu

您正在经营一家在线业务，您的一天中很大一部分时间都在处理订单。随着您的销量增加，这项工作占用了更多的时间，不幸的是最近您遇到了一个情况，您接受了一个订单，但无法履行。

您决定写一个名为`fillable()`的函数，它接受三个参数：一个表示您库存的字典`stock`，一个表示客户想要购买的商品的字符串`merch`，以及一个表示他们想购买的商品数量的整数n。如果您有足够的商品库存来完成销售，则函数应返回`True`，否则应返回`False`。

有效的数据将始终被传入，并且n将始终大于等于1。

代码提交地址：
<https://www.codewars.com/kata/586ee462d0982081bf001f07/python>

---

#### 第五题： 莫尔斯码解码器（Decode the Morse code, advanced）

难度： 4kyu

在这个作业中，你需要为有线电报编写一个莫尔斯码解码器。
有线电报通过一个有按键的双线路运行，当按下按键时，会连接线路，可以在远程站点上检测到。莫尔斯码将每个字符的传输编码为"点"（按下按键的短按）和"划"（按下按键的长按）的序列。

在传输莫尔斯码时，国际标准规定：

- "点" - 1个时间单位长。
- "划" - 3个时间单位长。
- 字符内点和划之间的暂停 - 1个时间单位长。
- 单词内字符之间的暂停 - 3个时间单位长。
- 单词间的暂停 - 7个时间单位长。

但是，该标准没有规定"时间单位"有多长。实际上，不同的操作员会以不同的速度进行传输。一个业余人士可能需要几秒钟才能传输一个字符，一位熟练的专业人士可以每分钟传输60个单词，而机器人发射器可能会快得多。

在这个作业中，我们假设消息的接收是由硬件自动执行的，硬件会定期检查线路，如果线路连接（远程站点的按键按下），则记录为1，如果线路未连接（远程按键弹起），则记录为0。消息完全接收后，它会以一个只包含0和1的字符串的形式传递给你进行解码。

例如，消息`HEYJUDE`，即`·····−·−−··−−−··−−··`可以如下接收：

```python
1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
```

如您所见，根据标准，这个传输完全准确，硬件每个"点"采样了两次。

因此，你的任务是实现两个函数：

函数decodeBits(bits)，应该找出消息的传输速率，正确解码消息为点（.）、划（-）和空格（字符之间有一个空格，单词之间有三个空格），并将它们作为一个字符串返回。请注意，在消息的开头和结尾可能会出现一些额外的0，确保忽略它们。另外，如果你无法分辨特定的1序列是点还是划，请假设它是一个点。

函数decodeMorse(morseCode)，它将接收上一个函数的输出，并返回一个可读的字符串。

注意：出于编码目的，你必须使用ASCII字符.和-，而不是Unicode字符。

莫尔斯码表已经预加载给你了（请查看解决方案设置，以获取在你的语言中使用它的标识符）。

```python
morseCodes(".--")  #to access the morse translation of ".--"
```

下面是Morse码支持的完整字符列表：

```javascript
A    ·–
B    –···
C    –·–·
D    –··
E    ·
F    ··–·
G    ––·
H    ····
I    ··
J    ·–––
K    –·–
L    ·–··
M    ––
N    –·
O    –––
P    ·––·
Q    ––·–
R    ·–·
S    ···
T    –
U    ··–
V    ···–
W    ·––
X    –··–
Y    –·––
Z    ––··
0    –––––
1    ·––––
2    ··–––
3    ···––
4    ····–
5    ·····
6    –····
7    ––···
8    –––··
9    ––––·
.    ·–·–·–
,    ––··––
?    ··––··
'    ·––––·
!    –·–·––
/    –··–·
(    –·––·
)    –·––·–
&    ·–···
:    –––···
;    –·–·–·
=    –···–
+    ·–·–·
-    –····–
_    ··––·–
"    ·–··–·
$    ···–··–
@    ·––·–·
```

代码提交地址：
<https://www.codewars.com/kata/decode-the-morse-code-advanced>

---

### 第三部分

使用Mermaid绘制程序流程图

安装VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序流程图（至少一个），Markdown代码如下：

![程序流程图](/Experiments/img/2023-08-05-22-00-00.png)

显示效果如下：

```mermaid
flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

查看Mermaid流程图语法-->[点击这里](https://mermaid.js.org/syntax/flowchart.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

请将实验过程与结果放在这里，包括：

- [第一部分 Python列表操作和if语句](#第一部分)
- [第二部分 Codewars Kata挑战](#第二部分)
  
  第一题
  ```
  cnt1 = 0
  cnt2 = 0
    for month in data:
        for day in data[month]:
            if data[month][day] == 'Naughty':
                cnt1 += 1
            if data[month][day] == 'Nice':
                cnt2 += 1

    if cnt1 > cnt2:
        return "Naughty!"
    if cnt1 < cnt2:
        return "Nice!"
    else:
        return "Nice!"
  ```
  第二题
  ```
  def get_pins(observed):
    adj = {
        "1": "124",
        "2": "2135",
        "3": "326",
        "4": "4157",
        "5": "52468",
        "6": "6359",
        "7": "748",
        "8": "85790",
        "9": "968",
        "0": "08",
    }
    result = ['']
    for d in observed:
        result = [prefix+c for prefix in result for c in adj[d]]
    return result
  ```
  第三题
  ```
    sq = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if PROTEIN_DICT[codon] == 'Stop':
            break
        sq += PROTEIN_DICT[codon]
    return sq
  ```
    第四题
  ```
  def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False
  ```  
  第五题
 ```
   def decodeBits(bits):
    bits = bits.strip('0')
    time_unit = min(map(len, bits.replace('1', ' ').split() + bits.replace('0', ' ').split()))
    word_sep = '0' * 7 * time_unit
    char_sep = '0' * 3 * time_unit
    ones_sep = '0' * 1 * time_unit
    dash = '1' * 3 * time_unit
    dot = '1' * 1 * time_unit
    return bits.replace(dash, '-').replace(dot, '.') \
               .replace(word_sep, '   ').replace(char_sep, ' ').replace(ones_sep, '')

def decodeMorse(morse_code):
    return ' '.join(''.join(map(MORSE_CODE.get, word.split()))
                    for word in morse_code.split('   ')).strip()
 ```
- [第三部分 使用Mermaid绘制程序流程图](#第三部分)
- 第一题
```mermaid
flowchart LR
    A[Start] --> B[cnt1 = 0, cnt2 = 0]
    B --> C{"for month in data: for day in data[month]:"}
    C ---> |Yes| D{"data[month][day] == 'Naughty'"}
    D --> |Yes| E[cnt1 += 1]
    D --> |No| F[cnt2 += 1]
    E --> D
    F --> D
    C ---> |No| G{cnt1 > cnt2:}
    G --> |Yes| H["return "Naughty!""]
    G --> |No| I["return "Nice!""]
    H --> J[end]
    I --> J
```
第四题
```mermaid
flowchart LR
    A[Start] --> B{"merch in stock and stock[merch] >= n"}
    B --> |Yes| C[return True]
    B --> |No| D[return False]
    C --> J[end]
    D --> J
```
注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

![Git命令](/Experiments/img/2023-07-26-22-48.png)

显示效果如下：

```bash
git init
git add .
git status
git commit -m "first commit"
```

如果是Python代码，应该使用下面代码块格式，例如：

![Python代码](/Experiments/img/2023-07-26-22-52-20.png)

显示效果如下：

```python
def add_binary(a,b):
    return bin(a+b)[2:]
```

代码运行结果的文本可以直接粘贴在这里。

**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. 字典的键和值有什么区别？
        在Python中，字典是一种键-值（key-value）存储结构。键（key）是字典中用于索引值的标识符，而值（value）则是与该键相关联的数据。

        简单来说，键是字典中用于区分不同数据的唯一标识符，而值则是与该键相关联的实际数据。例如，你可以使用人名作为键，把每个人的电话号码作为与之对应的值，这样你就可以通过人名查找到对应的电话号码。

        在字典中，键必须是唯一的，因为如果你使用相同的键来存储不同的值，后来存储的值会覆盖之前的值。而值则可以重复，因为不同的键可以对应相同的值。
2. 在读取和写入字典时，需要使用默认值可以使用什么方法？
```
        在读取和写入字典时，可以使用字典的get()方法来获取指定键的值，并设置默认值。get()方法接受两个参数，第一个参数是要获取值的键，第二个参数是默认值，当键不存在时返回默认值。如果不设置默认值，则在键不存在时返回None。
```
3. Python中的while循环和for循环有什么区别？
        循环是一种重复执行特定代码块的结构，可以在编程中用于处理重复的任务或迭代遍历数据。在Python中，有两种常见的循环结构：while循环和for循环。

        while循环：while循环在满足指定条件时重复执行代码块，直到条件不再满足为止。循环开始前会先判断条件是否满足，如果满足则执行代码块，然后再次判断条件，直到条件不满足时循环结束。while循环适用于在未知条件下循环执行代码，可以根据条件动态控制循环的次数和终止条件。

        for循环：for循环用于遍历可迭代对象中的元素，执行相应的代码块。可迭代对象可以是列表、元组、字符串、字典等。for循环会自动遍历可迭代对象中的每个元素，并依次执行代码块。for循环适用于已知条件下循环遍历可迭代对象中的元素，循环次数是固定的。

        总的来说，while循环适用于需要根据条件灵活控制循环的情况，而for循环适用于已知条件下的遍历操作。根据具体的需求和场景，选择合适的循环结构可以提高代码的效率和可读性。
4. 阅读[PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/), 总结Python 3.10中新出现的match语句的使用方法。
``````
1.基本语法：
match expression:
    pattern1:
        # code block
    pattern2:
        # code block
    ...
    patternN:
        # code block
匹配模式（patterns）：
常量模式（Constant pattern）：匹配特定的常量值。
变量模式（Variable pattern）：将匹配的值绑定到一个变量。
通配符模式（Wildcard pattern）：使用_匹配任意值。
结构模式（Structure pattern）：匹配复杂的数据结构，如元组、列表、字典等。
类型模式（Type pattern）：匹配特定的类型。
条件模式（Guard pattern）：在模式中添加条件，用于进一步筛选匹配。
匹配模式的优先级：

匹配模式按照从上到下的顺序进行匹配，一旦找到匹配的模式，就执行对应的代码块，然后退出match语句。
如果没有找到匹配的模式，会引发MatchError异常。
使用as关键字绑定匹配的值：

在模式中使用as关键字可以将匹配的值绑定到一个变量，以便在代码块中使用。
使用|操作符进行多个模式的匹配：

可以使用|操作符将多个模式组合起来，表示匹配其中任意一个模式。
使用...表示省略部分：

可以使用...表示省略部分，用于匹配任意数量的元素。
使用_忽略不关心的部分：

可以使用_匹配任意值，表示不关心该部分的具体值。
使用case关键字：

可以使用case关键字替代match关键字，使代码更具可读性。
``````
## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

&emsp;&emsp;在Python中，字典是一种无序的键值对集合，可以用于存储和检索数据。通过使用花括号或dict()函数创建字典，可以添加、删除和访问键值对。而while循环是一种基本的循环结构，可以重复执行一段代码块，直到满足某个条件。通过设置循环条件和循环体，可以控制循环的执行流程。在实验中，我们通过一个例子学习了如何使用字典和while循环实现一个简单的单词计数器。这个实验使我们更加熟悉了Python中字典和while循环的使用方法，同时也加深了对Python基本语法和编程思想的理解。