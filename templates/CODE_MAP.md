# 代码接口地图

> **本文件 = 代码的"圣经"**。记录每个关键文件、函数的职责、输入输出、修改时的注意事项。
> 改完代码后立即更新本文件。

---

## 文件结构速查

```
project/
├── models/
│   ├── model_a.py       (主模型 A，改这个要通知 Engineer + Architect)
│   └── model_b.py       (辅助模型，改这个影响 model_a 的输入)
├── data/
│   ├── dataset.py       (数据加载，改这个要检查训练脚本)
│   └── preprocess.py
├── scripts/
│   ├── run_train.sh     (训练脚本，超参定义在这里)
│   └── run_eval.sh      (评估脚本)
├── configs/
│   └── base.py          (配置中枢，所有超参都通过这里)
└── utils/
    └── metrics.py       (度量计算)
```

---

## 关键文件详解

### models/model_a.py

**职责**: [做什么]

**关键类**:

#### class ModelA(nn.Module)

**初始化参数**:
- `param1` (type, default): [说明]
- `param2` (type, default): [说明]

**关键方法**:

##### forward(input_a, input_b) → output

**输入**:
- `input_a`: shape (B, seq_len), dtype float32, 范围 [0, 1]
- `input_b`: shape (B, hidden_dim), dtype float32

**输出**:
- shape (B, num_classes), dtype float32, logits

**注意**:
- ⚠️ 不要改 forward 的输入签名（eval.py 依赖这个接口）
- ⚠️ 改了隐藏层维度后要同步 CODE_MAP.md 和 configs/base.py

**调用关系**:
```
train.py:forward() → model_a.forward()
eval.py:forward() → model_a.forward()
```

---

### data/dataset.py

**职责**: 数据加载和预处理

**关键类**:

#### class MyDataset(torch.utils.data.Dataset)

**初始化参数**:
- `data_path`: 数据文件路径
- `max_seq_len`: 序列最大长度（修改这个会改数据形状，要 smoke test）

**__getitem__ 返回**:
```python
{
  'input_ids': shape (seq_len,),
  'label': int,
  'metadata': {...}
}
```

**注意**:
- ⚠️ 改了 __getitem__ 的返回 key 要同步 train.py 的 batch unpacking
- ⚠️ 改了数据预处理逻辑要重新生成数据缓存（删除旧的，重新生成）

---

### configs/base.py

**职责**: 参数中枢

**关键参数**:

```python
class Config:
  model_name: str = "model_a"  # 改这个会切换模型
  hidden_dim: int = 768        # 改这个会改模型大小，要调学习率
  learning_rate: float = 1e-4  # 改这个要调 warmup_steps
  ...
```

**修改约定**:
- 新增参数要有默认值
- 改参数默认值要通知 Engineer（可能影响历史结果复现）
- 参数的"依赖关系"要在注释里说清

---

### scripts/run_train.sh

**职责**: 训练执行脚本

**关键变量**:

```bash
EXPERIMENT="exp_name"     # 改这个改实验名
BATCH_SIZE=16             # 改这个要考虑显存
EPOCHS=10                 # 改这个改训练时长
SEEDS="41 73 2026"        # 改这个改种子数
```

**修改约定**:
- 新增消融要加新的 if/elif 分支
- 改默认超参要在注释里说"为什么改"

---

## 修改风险速查表

| 文件 | 修改内容 | 风险 | 需要同步 |
|---|---|---|---|
| models/model_a.py | forward 签名 | 高 ⚠️ | eval.py, train.py |
| models/model_a.py | 隐藏层维度 | 中 | configs/base.py, CODE_MAP.md |
| data/dataset.py | 返回 key | 高 | train.py unpacking |
| data/dataset.py | 预处理逻辑 | 中 | 数据缓存（需重生成） |
| configs/base.py | 参数默认值 | 低 | 通知 Engineer（可能影响复现） |
| scripts/run_train.sh | 消融定义 | 低 | RESULTS.md / STATUS.md |

---

## 代码改动记录

### [日期] [改动]

**改了什么**: [具体文件和行号]

**为什么改**: [背景和原因]

**影响范围**: [哪些模块受影响]

**需要重新验证**: [需要 smoke test 什么]

---

## 已知的技术债

- [技术债 1]: [什么时候引入的，优先级，修复方案]
- [技术债 2]: [...]

---

## 参考

- 详细的实现日志见 `docs/roles/engineer.md`
- 踩过的坑见 `docs/roles/engineer.md` 的「踩过的坑」部分
