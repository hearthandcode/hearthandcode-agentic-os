# A/B Testing Copy

## Hypothesis-Driven Testing

A/B testing copy without a hypothesis is random noise. Every test must name: what you expect to find, how that thing manifests in the metric, and what your success threshold is.

**Hypothesis formula:** "If we [specific change], then [specific metric] will [sign and magnitude], because [reason]. We will call the test conclusive when [confidence threshold]."

**Bad hypothesis:** "We want to test the headline."
**Good hypothesis:** "If we change the headline from 'The best invoicing app' to 'Invoice in 30 seconds flat, every time,' we expect click-through rate to increase by 10%+, because the benefit is specific and time-conscious vs. a generic claim. We will call the test at 95% confidence with a minimum of 5,000 visitors per variant."

**Before writing test copy:**
1. Define the metric (click rate, conversion rate, bounce rate, time on page)
2. Estimate how long the test will take (baseline conversion × minimum detectable effect × number of variants)
3. Identify one change per variant

---

## One-Change Rule

Test one change at a time. A variant that changes headline, CTA, and image gives no insight into which change drove the result.

| Good single-variable tests | Bad multi-variable tests |
|----------------------------|--------------------------|
| Headline: A vs B | Headline, CTA, image all changed |
| CTA text: "Try free" vs "Get started" | Layout, headline, and copy all changed |
| Button color: blue vs green | Page design changed wholesale |

**Why multi-variable tests fail:** They cannot attribute the delta. The test may show +5%, but if the headline helped and the CTA hurt, you have no way to separate the signals. Run multivariate tests with a model — not an A/B.

---

## Sample Size Discipline

Most tests end too early. The runner sees 300 visits of the B variant at 12% conversion and stops to call it conclusive. That is noise.

**Table of sample sizes per variant (baseline 5% conversion, significance 95%):**

| Effect size you need to detect | Visitors per variant |
|--------|----|
| 20% relative (5% → 6%) | ~15,000 |
| 30% relative (5% → 6.5%) | ~6,800 |
| 50% relative (5% → 7.5%) | ~2,800 |
| 100+% relative (5% → 10+) | ~800 |

**Sample-size formula install:** [(Z α/2 + Z β)² × (p1(1-p1) + p2(1-p2))] / (p2 - p1)²

Or use a calculator: site • https://www.evanmiller.org/ab-testing/sample-size.html

---

## Duration Discipline

Split sample evenly over time. The goal is to cover an engagement cycle — 7 days minimum, 14 days is better. Never make decisions in the same day or the same day of week.

**Day-of-week effect:** Monday morning vs Friday afternoon traffic is different. Run through a full week to capture the full angle of at least one business cycle.

---

## Reading the Results

**Three-step reading:**

1. **Direction:** Is the met compared metric direction consistent across the tested period? If week 1 shows B beating and week 2 shows A beating, the effect is not steady — may be external factors.
2. **Confidence:** Is p < 0.05? If not, the test needs more data.
3. **Segment:** Does the variation beat the baseline in every segment? If mobile is -5% but desktop is +15%, the variant is a segment — work on that.

---

## After the test

- **Winner:** Implement the winning variant. Schedule a follow-up test to micro-optimise.
- **Inconclusive:** A result that does not reach significance does not mean "the copy is at least the same." Restructure the hypothesis — src and retest with a stronger assumption.
- **No measurable difference:** The change is not effective enough to matter. Use runner-down on test that is not moving the KPI.

---

## Copy-specific A/B test ideas

| Area | What to test | Metric |
|--------|------------|--------|
| Headline | Direct promise vs Number vs Question | CTR, bounce |
| CTA text | Verb-first vs Benefit-first | Conversion |
| Social proof | "x users trust us" vs a specific testimonial quote | conversion |
| Offer phrasing | "Free trial" vs "30-day access" vs "Starts free" | Signup rate |
| Price display | $19/mo vs $228/yr vs $19/mo (announced yearly) | Avg rev / conversion rate |
| Length | short page (top only) vs full scroll | Conversion rate