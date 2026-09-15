<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : prd-builder.skill  →  references/prd-best-practices.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# PRD Best Practices — Synthesis

Distilled from the sources the team studies: Atlassian Agile Coach (PRD in agile), ProductPlan (PRD components), Product School, Miro (visual PRDs), Lenny's Newsletter (real PRDs from Stripe/Airbnb/Netflix-class companies), Mind the Product, and r/ProductManagement practitioner threads. Use this to shape judgment during brainstorms — it's the "why" behind the quality bars.

## 1. The PRD is an alignment tool, not a contract (Atlassian)

The document's job is shared understanding between PM/PO, Design, and Engineering — not to specify implementation. Requirements say **what and why**; the team owns **how**. When the PO drifts into API shapes or screen-by-screen prescriptions:
- Move it to a linked doc (Important Links) and keep the PRD at outcome level.
- Over-specification is the #1 practitioner complaint on MTP/r/PM: engineers either ignore bloated PRDs or follow them off a cliff. Either way the document failed.

Corollary: **shorter beats longer**. A "Lite PRD" (this template's default mode) that everyone reads outperforms a 40-page spec nobody does. If a section balloons, extract to an appendix or linked doc.

## 2. Living document (Atlassian, Lenny's)

A PRD frozen at kickoff is fiction by week 4. Practices that keep it alive:
- Version History rows for every substantive change — cheap, and it's the diff log stakeholders actually read.
- Open questions stay **visible** in the doc (`[RESEARCH]`, `⚠ Giả định`) instead of being resolved by silent optimism.
- Meeting Notes section captures decisions with dates; the PRD body reflects them; history links the two.
- Revisit the Executive Summary after S3/S4/S5 solidify — it's written iteratively, read first.

## 3. Problem before solution (ProductPlan, Lenny's)

The strongest real-world PRDs Lenny publishes share one trait: the problem/opportunity section is the best-written part, and the feature list is almost boring by the time you reach it — because it follows inevitably. Enforcement moves:
- Don't let the solution paragraph exist before the problem paragraph survives challenge.
- The "5 whys" on the pain point: keep asking why it hurts until you hit money, time, identity, or fear.
- If a feature can't name the persona-need it serves, it's decoration.

## 4. Evidence over opinion, honestly labeled

- Real review quotes beat invented pain points. Store reviews, Reddit, support tickets are primary sources.
- Estimates carry their basis. A PRD that says "ước tính, dựa trên số rating × tỉ lệ chuyển đổi điển hình" earns trust; one that states invented DAU as fact loses the room the first time an engineer checks.
- Relative comparison ("competitor A monetizes harder than B, gap at the simple end") is usually all a product decision needs — precision theater wastes time.

## 5. Ruthless scope, explicit non-scope (Product School, r/PM)

- MVP = the smallest thing that **proves the one statement** (retention thesis, conversion thesis...). Write that statement first; scope answers to it.
- The out-of-scope list should sting a little. Its second job: pre-answering "tại sao không có X?" so the debate happens once, in the doc, not every sprint.
- Practitioner heuristic from r/PM: if stakeholders read the scope section and nobody is disappointed, it wasn't scoped — it was collected.

## 6. Success criteria you can lose against (Lenny's, MTP)

- A goal you can't fail isn't a goal. "Tăng engagement" → unfalsifiable. "D7 ≥ 12% trước khi mở rộng tính năng" → the team can be wrong, which is the point.
- Pair every growth metric with a quality metric (downloads × retention; conversion × refund/complaint rate) to block vanity optimization.
- Set the review date at target-setting time ("hiệu chỉnh sau 4 tuần") — targets are calibration devices, not prophecy.

## 7. Visualize flows, link don't embed (Miro)

- User flows, journey maps, wireframes communicate faster than prose — but they live in Figma/Miro where they stay current. The PRD carries the numbered text sequence (source of truth for logic) + a link (source of truth for visuals).
- The Important Links table is the PRD's API to the rest of the project. A healthy Lite PRD links out a lot.

## 8. Anti-patterns catalog (MTP, r/ProductManagement — the "kinh nghiệm xương máu" list)

Watch for these during brainstorms and name them when they appear:

| Anti-pattern | Smell | Countermove |
|---|---|---|
| Solution in search of a problem | Problem statement written after the feature list | Rewrite problem from persona's day, re-derive features |
| Persona cosplay | 3 personas = 1 persona in 3 age costumes | Merge; differentiate by need/context or not at all |
| Everything is P0 | Priority column is decoration | Force-rank: "if we cut the bottom 30%, what breaks?" |
| Vanity market sizing | "$X billion TAM by 2030" from a report nobody read | Category-download framing with named apps |
| Copy-the-leader | Feature table mirrors competitor #1 | Return to review mining: win on the complaints, match the loves |
| Silent assumptions | Load-bearing claims with no flag | `⚠ Giả định cần kiểm chứng` + a validation plan |
| PRD as novel | 30 pages, zero readers | Lite mode; extract appendices; exec summary carries the narrative |
| Spec creep into how | API/DB/UI prescriptions in requirements | Outcome language; move detail to linked engineering docs |
| Frozen PRD | Doc contradicts reality by mid-project | Version history discipline; scheduled review checkpoints |
| Metrics without owners | KPI table exists, nobody measures | Each KPI names its measurement method; DA stakeholder signs the table |

## 9. Facilitation craft (Product School, MTP)

- Draft-first collaboration: after 2-4 answers, write the section yourself and ask "sửa gì?" — people edit 5× faster than they compose.
- One devil's-advocate pass per section, aimed at the load-bearing assumption, delivered as a question not a verdict.
- Timebox divergence: brainstorm wide for a bounded stretch, then explicitly converge and commit to the working file. Unwritten agreement decays overnight.
- End every session with the status board + the single recommended next section — momentum is a feature of the process, not the doc.
