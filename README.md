# CodeSage

CodeSage 是一个基于 AI 的自动代码评审系统，专门设计用于日常编程练习的评估和反馈。系统能够自动检测新提交的代码，进行多维度分析，并提供详细的评审报告。

## 📝 如何提交每日代码
**参与之前，你需要联系仓库所有者，添加你的邮箱到合作者列表中，方便你能直接对主仓库进行提交操作，但注意，请不要随意破坏仓库！**
### 1. 进入对应日期的文件夹
每一天的编程练习都会有一个独立的文件夹，格式为 `YYYYMMDD`，例如 `20250121`。请进入该日期对应的文件夹。

```bash
cd 20250121
```

### 2. 阅读题目说明
在该日期文件夹中，有一个 `README.md` 文件，其中包含了当天的编程题目和要求。请先仔细阅读此文件，理解题目的需求和解题目标。
![49a373fabe6e5c3340a11ebed988bfc2](https://github.com/user-attachments/assets/52a28e20-9e0e-4950-b271-5bbfcc9f3eaa)

```bash
cat README.md
```

### 3. 将代码提交到 `codes` 文件夹
在 `codes` 文件夹中，按照自己的名字缩写（拼音首字母）命名你的代码文件。例如，如果你的名字是张三，可以将 C 语言代码命名为 `zs.c`，Python 代码命名为 `zs.py`，Java 代码命名为 `zs.java` 等。
![image](https://github.com/user-attachments/assets/dfd0df72-819f-4d8d-877f-4ed12593bad1)

点击这个按钮后，你可以选择文件上传，或者直接在github里面编辑，例如zzy.cpp,zzy.py,zzy.java全是有效文件

![image](https://github.com/user-attachments/assets/173fbb92-e753-4669-84f2-7e4383dac9f7)


确保代码可以顺利运行并解决题目要求，然后将其提交到 `codes` 文件夹中。

### 4. 生成评审报告
提交代码后，系统会自动进行评审。评审结果会生成在 `reviews` 文件夹下，文件名与提交的代码文件名对应，例如 `zs_review.md`。

你可以在评审报告中看到关于代码风格、解题思路、正确性等方面的反馈和建议。


## 📋 功能特点

- 🤖 自动代码评审和评分
- 📊 多维度代码分析（代码风格、解题思路、正确性）
- ⏰ 每小时自动检查新提交
- 📝 独立的评审报告
- 🔄 支持多种编程语言 (C，C++, Python, Java)

## 📁 仓库结构

```
├── YYYYMMDD/              # 每日题目文件夹
│   ├── README.md         # 题目说明
│   ├── codes/           # 代码文件夹
│   │   ├── xxx.c
│   │   ├── xxx.cpp     
│   │   ├── xxx.py      
│   │   └── xxx.java    
│   └── reviews/        # 评审文件夹
│       ├── xxx_review.md
│       └── ...
├── bot/                 # 评审机器人代码（comming soon...）
│   └── code_review_bot.py
└── README.md           # 本文件
```

## 📝 提交规范

### 代码文件命名
- 使用作者姓名拼音缩写
- 例如：`zs.cpp`, `ls.py`, `ww.java`

### 评审文件格式
每个代码文件的评审结果将生成对应的 `xxx_review.md`，包含：
- 评分（1-10分）
- 代码风格评价
- 解题思路分析
- 正确性评估
- 总体评价
- 改进建议

## 🔄 自动评审流程

1. 系统每小时自动检查新提交的代码
2. 对于新代码或更新的代码进行评审
3. 生成评审报告并自动提交
4. 可在对应日期文件夹的 reviews 目录下查看结果


## 📊 评分标准

评分采用 1-10 分制，基于以下几个维度：

1. 代码风格 (30%)
   - 变量命名规范
   - 代码格式化
   - 注释完整性

2. 解题思路 (40%)
   - 算法选择
   - 实现方式
   - 代码效率

3. 代码正确性 (30%)
   - 功能实现
   - 边界处理
   - 异常处理

## 🤝 参与贡献

1. Fork 本仓库
2. 创建新的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📄 开源协议

本项目采用 MIT 协议 - 查看 [LICENSE](LICENSE) 文件了解详情

## 👥 维护者

- [@Pi-zzy](https://github.com/Pi-zzy)

## ⭐ 致谢

感谢所有为此项目做出贡献的参与者！
