# Requesting access to the full MALICE corpus

The full MALICE dataset (~250K adversarial prompts) is **gated** and released only for defensive
security and safety research, in line with the paper's Ethical Considerations and the release
practice of AdvBench, RedCode, and CySecBench.

The public [`data/sample/malice_sample.csv`](data/sample/malice_sample.csv) (30 rows) is provided so
you can evaluate the schema and tooling before requesting the full data.

## Who can request

Researchers with a verifiable institutional affiliation (university, research lab, or a security
team acting in a defensive capacity) and a concrete, defensive research purpose.

## How to request

Email **`md.nishat.008@gmail.com`** with the subject line **`MALICE dataset access request`** and include:

1. **Name** and **institutional affiliation** (with an institutional email address).
2. A link to a **web page verifying your affiliation** (faculty/lab/staff page, or similar).
3. A short (2–4 sentence) **statement of research purpose** describing the intended defensive use.
4. Your acknowledgment that you have read and agree to the [`LICENSE`](LICENSE), specifically:
   - use is limited to defensive security / safety research;
   - you will **not** use the prompts to generate, deploy, or distribute actual malware, or to
     attack systems without authorization;
   - you will **not** redistribute the corpus; you will refer others to this request process.

## Request template

```
To: md.nishat.008@gmail.com
Subject: MALICE dataset access request

Name:
Institution:
Institutional email:
Affiliation verification URL:

Intended research use (2-4 sentences):

I have read the MALICE LICENSE and agree to its terms, including defensive-research-only
use and no redistribution.
```

Approved requesters receive the code-mixed partition, the transliterated partition, and the combined
`malice-full.csv`. Because the full corpus exceeds typical Git hosting limits, it is distributed via
a gated host (e.g., a Hugging Face gated dataset or an institutional file link) rather than committed
to this repository.
