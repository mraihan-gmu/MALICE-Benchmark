# MALICE — Dataset Card

**MALICE** (Malicious Adversarial LLM Input for Code Evaluation) is an adversarial benchmark for
evaluating Code LLM safety guardrails under code-mixed and transliterated inputs.

- **Paper:** *On the Robustness of Code LLM Guardrails to Code-mixed and Transliterated Inputs*,
  Findings of the ACL: EMNLP 2026.
- **Authors / curators:** Nishat Raihan, Dipak Meher, Bhuwan Dhingra, Marcos Zampieri
  (George Mason University; Duke University).
- **Point of contact:** `mraihan2@gmu.edu`
- **License:** Restricted-use, research-only (see [`LICENSE`](LICENSE)).
- **Languages:** 18 (see below).

## Composition

| Field | Value |
| --- | --- |
| Instances | ~249,890 adversarial prompts |
| Code-mixed partition | 124,945 |
| Transliterated partition | 124,945 |
| Unique English seeds | 24,989 (after dedup) |
| Candidates per seed (*k*) | 5 |
| Raw aggregated seeds (pre-dedup) | 25,303 |

Each instance is a natural-language prompt (no executable code). Fields: `seed_prompt`,
`malice_prompt`, `type` (`code-mixed` | `transliteration`), `languages`.

### Languages

- **Code-mixed (10, Latin-script, Joshi class 0–2):** Swahili, Yoruba, Tagalog, Somali, Hausa,
  Igbo, Cebuano, Malagasy, Sundanese, Javanese.
- **Transliterated (8):** Chinese (romanized to Pinyin, ISO 7098), Hindi (Devanagari),
  Russian (Cyrillic), Arabic (Arabic), Japanese (Kana/Kanji), Korean (Hangul), Greek (Greek),
  Bengali (Bengali). Only Chinese is romanized; the other seven retain native script.

## Provenance

Seeds are aggregated from nine public malicious-code / jailbreak benchmarks:

| # | Source | Size | Notes |
|---|--------|-----:|-------|
| 1 | SecurityEval | 121 | CWE-mapped vulnerability prompts |
| 2 | LLMSecEval | 150 | NL prompts for CWE scenarios |
| 3 | CodeLMSec | 280 | Non-secure code completion prompts |
| 4 | AdvBench | 520 | Harmful-behavior instructions |
| 5 | CodeGuard | 2,000 | Unsafe prompts only |
| 6 | DiSCo | 2,000 | Vulnerable Python code pairs |
| 7 | MalwareBench | 3,520 | Malware-generation jailbreak prompts |
| 8 | RedCode | 4,050 | Risky code-execution prompts |
| 9 | CySecBench | 12,662 | Cybersecurity jailbreak prompts |

Please also cite the relevant source datasets when using MALICE.

## Construction pipeline

1. **Aggregate & dedup** the nine seed sets (exact-match + Jaccard > 0.85) → 24,989 English seeds.
2. **Tag programming keywords** with a three-layer detector (reserved words from 8 languages;
   Tree-sitter AST extraction; a 1,243-term security/technical dictionary) so they are preserved
   verbatim during translation.
3. **Generate variants** — code-mixed (sentence-level NLLB-200 translation into randomly sampled
   low-resource languages) and transliterated (translation into a target language; Chinese
   additionally romanized to Pinyin via GPT-5.2).
4. **Quality-filter** by BERTScore back-translation fidelity (τ = 0.80).
5. **Select** the top *k* = 5 accepted candidates per seed.

## Recommended splits

Experiments in the paper report the mean over five bootstrap resamples of a fixed 3,000-prompt
evaluation split, stratified by source dataset.

## Known limitations

- Prompts are machine-translated (NLLB-200), not produced by native speakers; BERTScore filtering
  mitigates but does not eliminate translation artifacts.
- The benchmark measures whether a model *generates* code, not whether that code executes.
- 18 languages are a representative subset, not exhaustive linguistic coverage.

## Ethical considerations

Released for defensive research only. No executable malicious code is included. The full corpus is
gated (institutional verification + stated research purpose). See [`ACCESS.md`](ACCESS.md) and
[`LICENSE`](LICENSE).
