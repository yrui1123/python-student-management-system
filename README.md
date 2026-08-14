# StudentCMS - Python 学生信息管理系统

这是我在自学 Python 过程中完成的一个命令行学生信息管理系统。

项目最初来自黑马程序员 Python 公开课中面向对象部分的课程练习。完成课程原有功能后，我尝试对数据存储部分进行修改：将原本使用纯文本文件保存学生信息的方式，改为了使用 `pandas` 读写 Excel 文件。

这个项目主要用于练习 Python 面向对象编程、模块组织以及简单的数据持久化。

## 主要功能

程序提供一个命令行菜单，可以完成基本的学生信息管理操作：

* 添加学生信息
* 删除学生信息
* 修改学生信息
* 查询单个学生信息
* 查看全部学生信息
* 保存学生信息
* 退出程序时自动保存数据

每个学生目前包含以下信息：

```text
name
gender
age
phone
desc
```

## 项目结构

```text
python-student-management-system/
├── main.py
├── Student.py
├── StudentCMS.py
├── stu_information.xlsx
├── README.md
└── .gitignore
```

各文件主要作用：

```text
main.py
└── 程序入口，创建 StudentCMS 对象并启动程序

Student.py
└── 定义 Student 类，用于保存单个学生的信息

StudentCMS.py
└── 实现学生信息的增删改查、菜单逻辑以及数据的读取与保存

stu_information.xlsx
└── 保存学生数据
```

## 程序结构

程序入口位于 `main.py`：

```text
main.py
   ↓
StudentCMS
   ↓
加载 Excel 中已有数据
   ↓
显示命令行菜单
   ↓
增 / 删 / 改 / 查 / 保存
   ↓
退出程序时保存数据
```

`Student` 类用于表示一个学生对象，`StudentCMS` 类负责管理学生对象列表以及程序的主要操作逻辑。

## 数据存储

课程原项目使用纯文本文件保存学生数据。

在完成原项目后，我尝试使用 `pandas` 将数据存储方式改为 Excel。

保存时，程序首先将学生对象转换为字典：

```python
std_dict = [stu.__dict__ for stu in self.stu_list]
```

之后将这些数据转换成 `DataFrame`：

```python
df = pd.DataFrame(std_dict)
```

最后写入 Excel 文件：

```python
df.to_excel(
    './stu_information.xlsx',
    index=False,
    engine='openpyxl'
)
```

程序启动时则读取 Excel：

```python
df = pd.read_excel('./stu_information.xlsx')
```

再将数据转换为字典列表，并重新创建 `Student` 对象，从而恢复之前保存的学生信息。

## 使用的技术

* Python
* Python 面向对象编程
* `pandas`
* `openpyxl`
* Excel 数据读写
* 命令行交互
* 简单的数据持久化

## 运行方式

项目需要安装：

```bash
pip install pandas openpyxl
```

进入项目目录后运行：

```bash
python main.py
```

程序启动后会显示操作菜单：

```text
***********************
StudentCMS
    1.add student information
    2.delete student information
    3.update student information
    4.search single student information
    5.print all students information
    6.save students information
    0.quit CMS
***********************
```

输入对应数字即可执行相应操作。

## 学习收获

这是我学习 Python 早期完成的一个练习项目。

通过这个项目，我主要练习了：

* 使用类和对象组织程序
* 将不同职责拆分到多个 Python 文件中
* 使用一个列表管理多个对象
* 完成基本的增、删、改、查逻辑
* 将程序运行过程中的数据保存到文件
* 使用 `pandas` 的 `DataFrame` 处理结构化数据
* 使用 `read_excel()` 和 `to_excel()` 完成 Excel 数据读写
* 在课程项目基础上，根据自己的想法修改已有实现

其中，我在完成课程原本的纯文本存储方案后，又尝试使用 `pandas + Excel` 重新实现了数据的保存和加载。这也是我第一次尝试在完成课程要求后，自己修改一个已有项目的实现方式。

## 项目局限

这是一个用于学习 Python 的小型练习项目，并不是实际使用的学生管理系统。

目前主要存在以下局限：

* 只有命令行界面，没有 GUI 或 Web 前端
* 使用 Excel 文件而不是数据库进行数据持久化
* 学生信息结构比较简单
* 输入校验和异常处理比较基础
* 没有用户登录和权限管理
* 查询方式只支持简单的姓名匹配
* 不适合多人同时使用或管理大量数据

项目的主要目的，是通过一个完整的小程序练习 Python 面向对象编程，并尝试将所学内容应用到数据存储方式的修改中。
