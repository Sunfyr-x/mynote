"""
读取指定的 Markdown 文件，按顺序提取所有符合 **[A-Z]** 格式的字母，
并将字母按出现顺序组成数组输出。

用法:
    python extract_letters.py <markdown文件路径>
示例:
    python extract_letters.py example.md
"""

import sys
import re


def extract_letters_from_markdown(file_path: str) -> list[str]:
    """读取 Markdown 文件，提取所有 **X**（X 为大写字母）中的字母，按出现顺序返回列表。"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # \*\*  匹配两个星号
    # ([A-Z])  捕获一个大写字母（仅字母本身进入结果列表）
    # \*\*  匹配两个星号
    pattern = r"\*\*([A-Z])\*\*"
    letters = re.findall(pattern, text)
    return letters

def main():
    letters_num = 45
    file_path = sys.argv[1]
    # file_path = "2023.md"
    try:
        letters = extract_letters_from_markdown(file_path)
        if len(letters)!= letters_num :
            print(f"答卷格式有问题")
            sys.exit(1)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{file_path}'")
        sys.exit(1)
    except OSError as e:
        print(f"读取文件时出错: {e}")
        sys.exit(1)

    print("提取到的字母数组:")
    print(letters)


if __name__ == "__main__":
    main()
