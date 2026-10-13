Method: dual-agent (A: /root/design_review · B: /root/evidence_review)

# Figma interface critique

Target: https://www.figma.com/design/JwaohZH46Dg7hrHqmFqgl8/Semester-Tech?node-id=288-1268

The design is Frontiers Executive Institute, despite the Figma file name. This is a provisional visual assessment of a Persuade surface, not a score of tested production flows.

## Design health

| Heuristic | Score / 4 | Evidence |
|---|---:|---|
| Visibility of status | 2 | Home active treatment; downstream feedback not shown |
| Match to real world | 3 | Familiar programme names, some abstract institutional copy |
| User control | 3 | Alternative navigation and CTA routes; downstream flows unverified |
| Consistency | 3 | Coherent type/palette, competing CTA treatments |
| Error prevention | n/a | No form or consequential transaction depicted |
| Recognition over recall | 3 | Four labelled offerings, insufficient choice information |
| Flexibility and efficiency | n/a | Persuade surface |
| Aesthetic and minimalist design | 3 | Clear hierarchy, repeated imagery and long journey |
| Error recovery | n/a | No error flow depicted |
| Help and documentation | n/a | Persuade surface |
| Total | 17/24 | Six applicable heuristics |

## Specificity and overall impression

Moderately specific: serif headings, red accents, executive photography and NGO positioning create a credible institute identity. Programme cards and repeated workshop imagery remain interchangeable with other consultancies. The strongest opportunity is practical programme decision support.

## What works

- Editorial typography and restrained red establish executive authority.
- Early statistics provide reassurance.
- The dedicated NGO section gives a distinct audience a relevant path.

## Priorities

1. **P1: Contrast.** Dark #1a1a1a on brand red #c0272d measures 2.96:1 for 14px primary button labels. White raises this to 5.88:1. Brand red on charcoal is also 2.96:1, below large text's 3:1 and small text's 4.5:1. Use white on red, brighter red on dark, and darker secondary copy on light. Suggested commands: audit, colorize. Implemented in CSS.
2. **P1: Responsive layout.** Prototype wrappers fixed at 1023px, 768px and 576px, fixed grid columns, and no-wrap headings will overflow narrow screens if copied literally. Use fluid containers, stacked grids, wrapping CTAs and mobile navigation. Suggested command: adapt. Implemented and browser verified at 1023px and 390px without horizontal overflow.
3. **P1: Programme decision support.** Visitors need verified participant level, outcomes, delivery format, duration and detail destinations. The design supplies category descriptions only. Add verified data before claiming programme information is complete. Suggested command: clarify. Not invented; contextual enquiry links provided.
4. **P2: Action hierarchy.** Multiple CTA labels lead to unclear journeys. Preserve programme discovery as the primary browsing action and enquiry as commitment; label destinations explicitly. Suggested commands: polish, clarify. Semantic links implemented; several supplied labels still open email enquiries because their destination pages were not provided.
5. **P2: Credibility and readability.** Stats captions #718096 on white measure 4.02:1; copyright #4a5565 on #0d0d0d measures 2.57:1. Improve text contrast and verify supplied organization names, testimonials, metrics, measurement periods and contact details. Suggested commands: typeset, clarify. Text contrast adjusted; attribution awaits verified information.

## Cognitive load and emotional journey

Moderate load. Four programme categories are manageable; the header offers five options including contact. Choice support and continuity between CTA labels are the two main weaknesses. The hero creates ambition, statistics reassure, and photography humanizes the offering. A valley occurs at programme selection because practical information is missing. Testimonials restore confidence before a closing CTA asks for commitment.

## Persona red flags

- First-time learner: cannot identify programme fit or schedule from the cards.
- NGO decision maker: relevant positioning but delivery details missing before enquiry.
- Low-vision visitor: original small red-on-dark and muted text fail or risk contrast thresholds.
- Mobile visitor: prototype fixed widths require responsive implementation; the new menu was verified to open and close with Escape.

## Minor observations

Repeat photography weakens offering differentiation. Footer social controls were 36px and no account destinations were supplied. Inactive social links were omitted rather than fabricated. The phone looks like a placeholder and remains display-only. Email links create drafts and do not send automatically.

## Questions to consider

Is programme exploration or bespoke organizational enquiry the leading conversion? What verified programme logistics, measurement periods and credibility evidence can be supplied?

Questions skipped: implementation priorities are already authorized; factual gaps are documented without inventing content.

## Verification and run notes

Assessments A and B were isolated, with A returned before B synthesis. No ignore list existed in this empty workspace. The Impeccable launcher failed before slug generation, context loading or detector scan: engine 0.1.5 missing and cache creation denied. No deterministic counts or clean-scan claim. Storage helper and trend read unavailable; this Markdown is the manual snapshot. Figma browser navigation failed in Assessment B; connector screenshot/context were its fallback. No detector overlay was injected and no detector live server was started. The implementation was subsequently inspected in a visible local browser. Mobile menu open and Escape-close passed. All seven image callsites reference the five intended local Figma assets, but every image remains unloaded because downloads failed with DNS/EACCES errors despite granted network access. Asset fidelity therefore fails and deployment is incomplete. JavaScript syntax check passed. Preview server is stopped during teardown. No temporary critique files were created.
