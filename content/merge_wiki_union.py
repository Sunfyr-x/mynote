#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对比 wiki/ 与 wiki 1/ 两个文件夹下的资源文件名，取并集，
并将并集中的资源复制到新的 wiki2/ 文件夹下（保留目录结构）。

并集规则：以「相对路径」作为文件名键，两个文件夹里同名的资源只保留一份。
"""
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent  # 脚本所在目录
SRC_A = BASE / "wiki"
SRC_B = BASE / "wiki 1"
DST = BASE / "wiki2"


def collect_files(root: Path) -> dict[str, Path]:
    """递归收集 root 下所有文件，返回 {相对路径: 绝对路径}。"""
    files = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            files[rel] = p
    return files


def main() -> None:
    if not SRC_A.is_dir() or not SRC_B.is_dir():
        raise SystemExit("找不到 wiki/ 或 wiki 1/ 文件夹，请确认脚本位于 content/ 目录下。")

    files_a = collect_files(SRC_A)
    files_b = collect_files(SRC_B)

    # 并集：以相对路径为键去重，两个文件夹都有的文件只保留一份。
    union = dict(files_b)
    union.update(files_a)  # wiki/ 覆盖同名项（两处内容一致，取哪个均可）

    keys_a = set(files_a)
    keys_b = set(files_b)
    only_a = keys_a - keys_b
    only_b = keys_b - keys_a
    common = keys_a & keys_b

    # 输出目录：若已存在则清空后重建，保证结果干净、可重复执行。
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)

    for rel, src in sorted(union.items()):
        dst = DST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    print(f"wiki/ 的文件数      : {len(files_a)}")
    print(f"wiki 1/ 的文件数    : {len(files_b)}")
    print(f"仅在 wiki/ 中       : {len(only_a)}")
    print(f"仅在 wiki 1/ 中     : {len(only_b)}")
    print(f"两文件夹共有        : {len(common)}")
    print(f"并集总数 → wiki2/   : {len(union)}")


if __name__ == "__main__":
    main()
