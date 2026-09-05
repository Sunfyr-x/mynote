#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 markdown 文件中挤在一行的选择题选项拆开，每个选项占一行。

规则：遇到 "A."、"B."、……（含 **A**. 这种加粗形式）这类选项标签，
就在它前面插入换行符。题干（或题号）保留在第一行。

- 不会误伤 "U.S."、"e.g."、题号 "1." 等（选项标签前后必须紧跟空白）；
- 行首是纯题号时（如完形填空 "1. A. ..."），题号与第一个选项保持同一行。

用法：
    python3 split_options.py 文件1.md [文件2.md ...]
"""

import re
import sys

# 选项标签 = 可选加粗 ** + 大写字母 A-Z + 可选加粗 ** + 句点，后跟空白。
# 用「空白 + 前瞻」来定位，从而避开 "U.S." 里的 "S." 这类不是选项的情况。
OPTION_SPLIT = re.compile(r"\s+(?=\*{0,2}[A-Z]\*{0,2}\.\s)")

# 纯题号，如 "1."、"21."
BARE_NUMBER = re.compile(r"\d+\.\s*")


def split_line(line: str) -> str:
    """把一行里的选项拆成多行。"""
    line = line.rstrip()
    parts = OPTION_SPLIT.split(line)
    if len(parts) == 1:
        # 没有选项标签，原样返回
        return line
    head, options = parts[0], parts[1:]
    if BARE_NUMBER.fullmatch(head):
        # 行首是纯题号（如 "1."），让题号与第一个选项保持同一行
        return f"{head.strip()} {options[0]}" + "".join(f"\n{o}" for o in options[1:])
    # 行首是题干（或第一个选项），题干单独一行，其余选项各占一行
    return "\n".join(parts)


def split_options(text: str) -> str:
    """对整个文件内容做选项拆分。"""
    return "\n".join(split_line(line) for line in text.split("\n"))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    for path in argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        with open(path, "w", encoding="utf-8") as f:
            f.write(split_options(text))
        print(f"已处理: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
