# 🔧 Engineer — 工程师窗口

> 本文件是 🔧 Engineer 角色的主场。记录代码改动、实验运行、踩过的坑、技术决策。
> 与 `CODE_MAP.md` 不同：CODE_MAP.md 是接口圣经（当前状态）；本文件是实现日志（演变过程）。

---

## 代码实现日志

### [日期] [功能/模块名]

**任务**：[来自 Architect 的指令 + 背景]

**实现**：
- [改了哪个文件]
- [新增了什么]
- [删除了什么]
- [为什么这样实现]

**验证**：
- [CPU smoke 测试]
- [GPU 小规模测试]
- [最终的 3-seed 结果]

**遇到的问题**：
- [问题 1 + 解决方案]
- [问题 2 + 解决方案]

**代码质量**：
- [性能如何]
- [显存占用如何]
- [是否有技术债]

---

## 实验运行日志

### [日期] [实验名称]

**实验目的**：[Architect 想验证什么？]

**配置**：
- 模型：[...]
- 超参数：[...]
- 数据集：[...]
- Seeds：[41, 73, 2026]

**运行状态**：
- 卡 A (seed 41): [状态]
- 卡 B (seed 73): [状态]
- 卡 C (seed 2026): [状态]

**结果**：
- [数字]
- [vs baseline 的对比]
- [结论]

**代码改动**：
- [修改了哪些脚本]
- [新增了哪些超参]

---

## 踩过的坑 (TL;DR)

[这一部分是给未来的自己和团队的"防踩坑指南"。每当发现一个重要坑，立即记录。]

### 坑 1：[坑名]

**表现**：[什么时候会掉进这个坑]

**根因**：[为什么会这样]

**解决方案**：[怎么修复]

**预防**：[以后怎么避免]

---

## 性能优化笔记

[如果做过任何性能相关的优化，记录在这里]

- [优化 1]: 原来 [X] ms，优化后 [Y] ms，通过 [什么方法]
- [优化 2]: ...

---

## 显存优化笔记

- [优化 1]: 原来 [X] GB，优化后 [Y] GB，通过 [什么方法]
- [优化 2]: ...

---

## 给其他窗口的反馈

[如果在实现过程中发现设计问题，写在这里。需要改设计时，通过 STATUS.md 的 Handoff 通知 Architect。]

### [日期] 设计反馈 → Architect

**问题**：[具体遇到了什么问题]

**建议**：[有什么改进建议]

**影响**：[如果不改，会怎样]

---

## 例子（来自真实项目）

```
代码实现日志

### 2026-06-15 RGI (残差门控 rationale 注入) 实现

任务：Architect 拍板转向 RGI 架构，需要实现 _GatedCrossInject 模块，支持 rationale 残差门控注入。

实现：
- 新建 models/rgi.py，定义 RGIModel + _GatedCrossInject
- _GatedCrossInject: 
  - 输入 T1 (OCR 增强后的文本) / R (rationale) / q (intensity gate)
  - 输出 LN(T1 + (q·g)⊙CrossAttn(T1,R))
  - 其中 g = sigmoid(MLP(rationale_embed))
- train.py 新增 --rgi_use_rationale / --rgi_use_rqe 等开关
- run_rgi.sh 定义 4 个消融：full / no_rqe / no_ocr / no_rationale

验证：
- CPU 5 样本 smoke：forward / backward / eval / test 全通
- 待 GPU 真训练

遇到的问题：
1. Q 网络的初始化——用了 Kaiming 初始化但 loss 不稳定
   → 改成从"无 rationale"态开始预测，用 L1 loss: |L_no_rat - L_with_rat|
   → 现在稳定了，q 的直方图符合预期
2. rationale 在 DeBERTa tokenizer 中的截断问题
   → 改用 max_rationale_len=512 而不是 160
   → 实测全 10833 样本零截断

代码质量：
- 参数量：新增 3.2M（relative 5% 相对较小）
- 显存：batch=16 时 ~18GB（可接受）
- 推理速度：vs baseline +3%（可接受）

性能优化笔记：
- _GatedCrossInject 中的 CrossAttn 显存开销最大（3 次 matmul）
  → 后续如果显存紧张，可考虑用 flash-attention

---

踩过的坑

### 坑：DeBERTa tokenizer 的隐式截断

表现：模型输出不稳定，rationale 的贡献预期应该是 +0.3 但实际 +0.0。

根因：
  DeBERTa 默认输入限制 512，我们把 rationale concat 到原文后超了 512，
  被静默截断。但截断的是 incongruity（附在最后），导致数据污染。

解决：
  改成 max_rationale_len=512 参数，在 dataset 层面就做长度约束，
  确保 token 装得下。

预防：
  - 一定要在 dataset 层面验证"数据长度"
  - 不要相信 tokenizer 的默认行为，要手动 check max length
  - 务必在 smoke test 中检查一些样本的真实 token 长度

坑的影响等级：⚠️ 中等（导致数据污染，模型学不到信号）
```

---

## 快速参考

| 需求 | 位置 |
|---|---|
| 我想知道某个模块怎么实现的 | 读「代码实现日志」 |
| 我想知道最近的实验结果 | 读「实验运行日志」 |
| 我想知道某个 bug 怎么避免 | 读「踩过的坑」 |
| 我想知道代码性能 | 读「性能优化笔记」 |
| 我发现了设计问题 | 写在「给其他窗口的反馈」 |
