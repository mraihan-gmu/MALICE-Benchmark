# MALICE Benchmark

**M**alicious **A**dversarial **L**LM **I**nput for **C**ode **E**valuation

> 📢 **Accepted to Findings of the Association for Computational Linguistics: EMNLP 2026.**

MALICE is a large-scale adversarial benchmark for probing the robustness of **Code LLM safety
guardrails** under linguistically diverse inputs. It converts malicious English coding prompts into
**code-mixed** and **transliterated** variants — translating sentence-by-sentence into low-resource
languages (or into non-Latin scripts) while preserving programming keywords verbatim — and measures
how much this degrades detection and increases malicious code generation across nine models and
safety tools (including Claude 4.6 and GPT-5.2).

> ⚠️ **Content warning.** This dataset contains prompts engineered to elicit malicious code
> (malware, exploits, phishing, etc.). It is released **strictly for defensive security and safety
> research**. See [Intended Use & Ethics](#-intended-use--ethics) and [`LICENSE`](LICENSE) before
> requesting access.

---

## 📄 Paper

**On the Robustness of Code LLM Guardrails to Code-mixed and Transliterated Inputs**
Nishat Raihan, Dipak Meher, Bhuwan Dhingra, Marcos Zampieri.
*Findings of the ACL: EMNLP 2026.*

If you use MALICE, please [cite the paper](#-citation).

---

## 🔎 What the benchmark shows

- Code-mixed malicious prompts drop the **best classifier's accuracy from 0.93 → 0.21**.
- Even the most safety-aligned model raises its malicious-code generation rate **~3×**
  (e.g., Claude 4.6: 0.09 → 0.28).
- Transliteration into native non-Latin scripts is **almost as damaging** as code-mixing.
- The effect is **Code-LLM-specific**: an ablation shows that removing programming-keyword
  preservation drops attack success *below* the English baseline.

Current safety alignment works for English but fails to generalize across languages and scripts.

---

## 📊 Dataset overview

| Property | Value |
| --- | --- |
| Total adversarial prompts | ~249,890 (~250K) |
| Code-mixed partition | 124,945 |
| Transliterated partition | 124,945 |
| Deduplicated English seed prompts | 24,989 |
| Candidates per seed (*k*) | 5 |
| Languages | 18 (10 code-mixed + 8 transliterated) |
| Source benchmarks aggregated | 9 |
| Quality filter | BERTScore back-translation, τ = 0.80 |

Seeds are aggregated from nine public malicious-code benchmarks (SecurityEval, LLMSecEval,
CodeLMSec, AdvBench, CodeGuard, DiSCo, MalwareBench, RedCode, CySecBench) and deduplicated with
exact-match + Jaccard (> 0.85) filtering. Full construction details are in the paper and
[`DATA_CARD.md`](DATA_CARD.md).

### Schema

Each row is one adversarial prompt:

| Column | Description |
| --- | --- |
| `seed_prompt` | Original English malicious prompt (from a source benchmark). |
| `malice_prompt` | The code-mixed / transliterated adversarial variant (keywords preserved). |
| `type` | `code-mixed` or `transliteration`. |
| `languages` | Language assignment, e.g. `Sentence 1: Swahili \| Sentence 2: Yoruba`, or `Chinese (Pinyin)`. |

### Languages

| Track | Languages |
| --- | --- |
| **Code-mixed** (Latin script, low-resource) | Swahili, Yoruba, Tagalog, Somali, Hausa, Igbo, Cebuano, Malagasy, Sundanese, Javanese |
| **Transliterated** (non-Latin scripts) | Chinese (Pinyin), Hindi, Russian, Arabic, Japanese, Korean, Greek, Bengali |

---

## 🔐 Access to the full dataset

Consistent with the paper's ethics commitment (and with the release practice of AdvBench, RedCode,
and CySecBench), the **full MALICE corpus is gated** and released only for defensive research.

➡️ **See [`ACCESS.md`](ACCESS.md) to request access.** Requests require institutional affiliation
and a short statement of research purpose. Approved researchers receive the full `malice.csv`
(code-mixed), the transliterated partition, and `malice-full.csv`.

A **small illustrative sample** ([`data/sample/malice_sample.csv`](data/sample/malice_sample.csv),
30 rows) is included in this repository so you can inspect the schema and try the tooling without
requesting access.

---

## 🚀 Quick start

```bash
git clone https://github.com/mraihan-gmu/MALICE-Benchmark.git
cd MALICE-Benchmark
pip install -r requirements.txt

# Inspect the bundled 30-row sample
python scripts/load_malice.py --path data/sample/malice_sample.csv --stats

# Filter to a track / language
python scripts/load_malice.py --path data/sample/malice_sample.csv --type code-mixed
python scripts/load_malice.py --path data/sample/malice_sample.csv --language Yoruba --limit 5
```

Once you have been granted the full corpus, point `--path` at the file you received:

```bash
python scripts/load_malice.py --path /path/to/malice-full.csv --stats
```

In Python:

```python
from scripts.load_malice import load_malice

df = load_malice("data/sample/malice_sample.csv")      # returns a pandas DataFrame
code_mixed = df[df["type"] == "code-mixed"]
```

---

## 🗂️ Repository structure

```
MALICE-Benchmark/
├── README.md                     # this file
├── DATA_CARD.md                  # dataset card (provenance, stats, construction)
├── ACCESS.md                     # how to request the full gated corpus
├── LICENSE                       # restricted-use, research-only terms
├── CITATION.cff                  # machine-readable citation
├── requirements.txt
├── data/
│   └── sample/
│       ├── malice_sample.csv     # 30-row illustrative sample (schema demo)
│       └── README.md
└── scripts/
    └── load_malice.py            # loader / filter / stats CLI
```

---

## 🛡️ Intended use & ethics

MALICE exists to **expose and help fix** multilingual safety blind spots in Code LLMs.

**Permitted:** evaluating and hardening safety classifiers and guardrails; red-teaming your own
models; safety-alignment and data-augmentation research; reproducing the paper.

**Not permitted:** using the prompts to generate, deploy, or distribute actual malware or to attack
systems you do not own or have explicit authorization to test; redistributing the gated corpus.

No executable malicious code is included in this dataset — only prompts. Use is governed by
[`LICENSE`](LICENSE).

---

## 📚 Citation

```bibtex
@inproceedings{raihan2026malice,
  title     = {On the Robustness of Code {LLM} Guardrails to Code-mixed and Transliterated Inputs},
  author    = {Raihan, Nishat and Meher, Dipak and Dhingra, Bhuwan and Zampieri, Marcos},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2026},
  year      = {2026}
}
```

## ✉️ Contact

Nishat Raihan — `mraihan@nd.edu` (George Mason University).
For data access, follow [`ACCESS.md`](ACCESS.md).
