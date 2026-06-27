# 🚦 STATUS — [项目名称] 跨窗口状态板

> **每个对话窗口先读本文件**，再读你角色的主场文档（见下「文档地图」）。
> 本板是 4 个角色窗口（🧭设计师 / 🔧工程师 / ✍️论文 / 🔬复现师）之间唯一的实时通信渠道——窗口之间不共享上下文，只靠文档互相了解。
> **改完任何工作，务必回来更新本板的「角色看板」+「Handoff 消息」**。最后更新 **[日期]** by 【窗口】。

---

## 一句话现状

[项目现在的状态是什么？最关键的进展/瓶颈是什么？用 1-2 句话说清楚]

**例子**：
- RGI 仍为当前最优架构 (85.34±0.27)。两个补洞实验已出数，论文暂不启动，多图结构继续改进。
- 核心模型已实现，当前焦点是优化推理速度和鲁棒性。

---

## 当前主线 & 下一步

### 主线
- [✅/🚧] **[主线名称]** — [简要说明]
- [✅/🚧] **[支线 1]** — [说明，已验证/已归档/进行中]
- [❌/📋] **[失败线]** — [为什么失败，何时停止的]

### 优先级
1. [最高] — [为什么优先，什么时候做]
2. [次高] — [...]
3. [可并行] — [哪些工作互不阻塞]

**例子**：
- ✅ **RGI 架构** — full 85.34，OCR 注入贡献 +0.68，rationale 中性，q 中性
- 🚧 **多图创新** — RGI-MIR pair reasoning 暂停（v1.0 +1.09 vs v1.1 -0.74），但多图方向未归档
- ❌ **GDC 差异融合** — v1/v2 都未超 RGI，信噪比低，归档为 negative result
- **下一步优先级**：① RGI-MIR 新方向设计（不沿 pair residual）② Paper 等架构定 ③ 补 A@512 对照

---

## 📁 文档地图 & 读写协议

| 角色 | 主场文档（你写这里） | 上手先读（orient） |
|---|---|---|
| 🧭 总设计师 Architect | `docs/roles/architect.md`（live 策略/决策）+ `method.md`（架构 spec） | STATUS → method.md → docs/roles/architect.md |
| 🔧 代码工程师 Engineer | `docs/roles/engineer.md` + `CODE_MAP.md`（接口，改完代码就要更新）+ 代码 | STATUS → CODE_MAP.md → docs/roles/engineer.md |
| ✍️ 论文写作 Paper | `docs/roles/paper.md`（故事/大纲/草稿） | STATUS → RESULTS.md → method.md → docs/roles/paper.md |
| 🔬 复现师 Repro | `docs/roles/repro.md`（参考论文代码分析） | STATUS → method.md → docs/roles/repro.md |
| — 共享结果数据 | `RESULTS.md`（结果表，谁出数谁更新） | 所有角色按需查 |
| — 历史日志 | `WORK_PLAN.md`（按时间追加的 Changelog，**不是状态板**） | 需要历史细节时查 |

> 深度文档（method/CODE_MAP/RESULTS/WORK_PLAN）保留在根目录原位（被大量引用）；角色主场文档在 `docs/roles/`。

---

## 👥 角色看板（在做 / 待办 / 最近产出）

### 🧭 Architect
- 在做：[当前任务]
- 待办：[接下来的优先级任务]
- 最近产出（日期）：[完成了什么]

**例子**：
- 在做：重新思考多图结构创新，旧 pair residual 路线暂停。
- 待办：提出下一版多图结构 spec；保留 RGI full / A512 / no_incongruity 作为已验证结论。
- 最近产出（06-27）：补洞实验结论已读入，多图继续设计。

### 🔧 Engineer
- 在做：[...]
- 待办：[...]
- 最近产出（日期）：[...]

### ✍️ Paper
- 在做：[...]
- 待办：[...]
- 最近产出（日期）：[...]

### 🔬 Repro
- 在做：[...]
- 待办：[...]
- 最近产出（日期）：[...]

---

## 🔁 Handoff 消息（时间倒序，跨窗口对话发这里）

> 格式：`- **【日期】 【发送者】 → 【接收者】**: 【简要标题】`
> 然后缩进子bullet 放详细信息。这是 4 个窗口的**唯一通信渠道**。

**例子**：
```
- **2026-06-27 🧭Architect → 🔧Engineer**:
  **修正当前策略：补洞结论写入，但不要启动论文窗口；多图结构仍需继续改进尝试。**
  - **A512 结论保留**：A512=84.13±0.42，较 A@160-cap +0.61，但仍低 RGI 1.21。
  - **no_incongruity 结论保留**：no_incongruity=84.92±0.87，低于 full 0.42。
  - **策略修正**：工程窗口"可交 Paper"判断过早。当前不让 ✍️Paper 起草；多图结构继续设计。

- **2026-06-27 🔧Engineer → 🧭Architect / ✍️Paper**:
  **两个补洞实验出数，全部消融终版锁定。**
  - **A512=84.13±0.42**
  - **no_incongruity=84.92±0.87**
  - **字段消融终版**: relation +0.76 >> per_image +0.54 > incongruity +0.42 > text_summary +0.23 >> entities +0.05
  - **代码改动**: run_rgi.sh / run_uracr_ablation.sh / train.py

- **2026-06-25 🧭Architect → 🔧Engineer**:
  **请先补两个论文前关键实验。**
  - **实验 1：`RGI no_incongruity`**
    - 目的：确认 incongruity 是否是字段线中疑似噪声源。
    - 代码改动：run_rgi.sh 新增 no_incongruity 消融；train.py 新增 --rgi_drop_fields argparse。
    - 跑法：ABLATIONS="no_incongruity" SEEDS="41 73 2026" CUDA_VISIBLE_DEVICES=N bash scripts/run_rgi.sh
  
  - **实验 2：`A@512-cap@v3`**
    - 目的：堵 reviewer 问题——A@v3 的 83.52 是否只因为 160 cap。
    - 代码改动：run_uracr_ablation.sh 增加 A512 ablation。
    - 跑法：LLM=v3.json SUFFIX=_v3cap512 ABLATIONS="A512" SEEDS="41 73 2026" CUDA_VISIBLE_DEVICES=N bash scripts/run_uracr_ablation.sh
```

---

## 红线要求

**所有窗口必须遵守**：

1. **STATUS.md 是唯一的跨窗口通信渠道** — 不要用 Slack / 邮件 / notes，一切都写在这里
2. **完成任务立即回写** — 不要等到项目结束，每个 checkpoint 都更新一遍
3. **每次进窗口先读 STATUS.md** — 了解全局状态和是否有给你的 Handoff
4. **严格遵守角色边界** — Architect 只改 method.md，Engineer 只改代码 + CODE_MAP.md，等等
5. **深度文档保留在根目录** — 不要把 method.md/CODE_MAP.md/RESULTS.md 移到 docs/roles/

---

## 快速导航

| 需求 | 去哪里 |
|---|---|
| 我是新进度来的，想了解全局 | 读本板「一句话现状」+ 「当前主线」 |
| 我是 Architect，想继续设计 | 读本板「Handoff 消息」找是否有给我的任务 → 进 docs/roles/architect.md |
| 我是 Engineer，想跑实验 | 读本板「Handoff 消息」找 Architect 的指令 → 参考 CODE_MAP.md 改代码 |
| 我是 Paper，想继续写论文 | 读 RESULTS.md 最新数据 → 读 method.md 架构 → 改 docs/roles/paper.md 草稿 |
| 我想看详细设计 | 读 method.md（当前 spec）+ docs/roles/architect.md（设计历程） |
| 我想看代码怎么改 | 读 CODE_MAP.md + docs/roles/engineer.md（踩过的坑） |
| 我想看实验结果 | 读 RESULTS.md（结果表）+ STATUS.md（Handoff 中的数字总结） |
| 我想看工作日志 | 读 WORK_PLAN.md（按时间倒序） |

---

## 例子：一个完整的工作流

假设你是 Architect，今天进来：

1. **读本文件**的「一句话现状」
   ```
   一句话现状：RGI 仍为当前最优架构 (85.34±0.27)。两个补洞实验已出数，论文暂不启动。
   ```

2. **读本文件**的「Handoff 消息」找给你的消息
   ```
   - **2026-06-27 🔧Engineer → 🧭Architect**: 两个补洞实验出数...
   ```

3. **跳到** `docs/roles/architect.md`
   ```
   读「最近产出」看你上次做了什么
   读「待设计项目」看下一步该做什么
   ```

4. **完成工作后**（比如设计了新的多图结构）
   ```
   1. 更新 method.md 新增 §1.8 RGI-MIR 结构
   2. 更新 docs/roles/architect.md 追加新设计
   3. 回来 STATUS.md，写一条 Handoff 给 Engineer：
      - **2026-06-28 🧭Architect → 🔧Engineer**:
        **RGI-MIR 结构设计完成，请实现。**
        - method.md §1.8 定义 RGI-MIR
        - 需要新建 models/rgi_multi.py
        - 4 个消融：mir_rel_full / mir_rel_no_pair / ...
   4. 更新本板「角色看板」Architect 行的「最近产出」
   ```

5. **下个窗口的 Engineer 进来**
   ```
   1. 读 STATUS.md「一句话现状」+ 「Handoff 消息」
   2. 看到 Architect 给的任务
   3. 进 docs/roles/engineer.md 开始实现
   4. 跑完实验后，回 STATUS.md 写 Handoff 给 Architect：已完成
   ```

---

**[保留以下内容供参考，但删除这行]**

---

## 为什么这个系统有效

### 1. 上下文分离
每个窗口只关心自己的角色和该角色相关的信息。4 个窗口 = 4 倍的总上下文。

### 2. 异步协作
不需要"在线会议"，每个人按自己节奏工作，通过 STATUS.md 同步。

### 3. 决策可追踪
Handoff 消息形成了一个完整的"决策历史"。6 个月后可以查"为什么当时弃用了 X"。

### 4. 降低认知负载
一个窗口 = 一个角色 = 一种认知模式。不需要频繁切换。

---

## 常见问题

**Q: 一个人分身成 4 个角色窗口是不是过度设计？**

A: 不是。即使一个人，也可以：
- 今天上午是 Architect（改 method.md）
- 今天下午是 Engineer（改代码）
- 明天是 Paper（写论文）
- 每个窗口都保持清爽上下文

**Q: 紧急插队任务怎么处理？**

A: 在 STATUS.md 的 Handoff 里标 🚨，该角色的下个窗口进入时会立即看到。

**Q: 项目中途可以加新角色吗？**

A: 可以。新建 `docs/roles/new_role.md`，在本板加新行即可。
