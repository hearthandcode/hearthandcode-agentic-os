# Marketing Metrics

A pragmatic guide to the numbers that matter for a solo-founder product. The default instinct is to measure everything — this file exists to narrow you to the 5–7 numbers that inform decisions. Everything else is noise.

## The funnel is a heuristic, not a law

Classic marketing funnels (AIDA, awareness-interest-desire-action, topline) are useful for structuring thought but dangerous for accounting. The number of people who "hear about the brand" is not a meaningful metric if it does not affect revenue. Prefer behavior-based proxy questions to awareness.

## The five metrics that matter early

### 1. Customer Acquisition Cost (CAC)

```
Total cost (spend + hours of work ~ $ value) / customers acquired
```

For a solo founder of a \$15 product: CAC is your existential number. If it exceeds $12, you are losing money on every customer and cannot grow. If it is below \$5, your channel is efficient but might be too small.

A **paid-market CAC** count includes: ad spend + creative production cost + hour of ad management. A **free/tactical CAC** measures hours only: month spent in forums, emailing, writing content, priced at \$25—50/hour in hypothetical cost. Most small campaigns ignore the time component; you should not.

### 2. Conversion rate (CVR)

Number of leads that become paying customers, per channel or per step:

- Visitor to email signup: 2–5% baseline for a landing page
- Email signup to purchase: 3–8% for a release launch
- Trial to paid: 15–30% for a single-try paid
- Ad click to purchase: 1–3% in B2C software

### 3. Lifetime Value (LTV)

How much a single customer generates over their life. For a $15 one-time purchase, LTV is not just money but:

- Upgrade (if you add a second product)
- App store in-app upgrade
- Word-of-mouth referral (1 average referral = +$7 to LTV)
- Everything above: \~$25 per customer

If average superb = 5, LTV = 5* 15 = $75. But each — actually first year zero upgrades: LTV stays flat.

### 4. Channel attribution (simple version)

Which activity drove the sale? At launch, a simple three-column survey: new customer during the first month writes "where did you hear of us?" with top options: Hacker News, Product Hunt, Reddit, blog, referral, x. This is sufficient because complex attribution is wasteful with fewer than 100 customers.

### 5. Return on Investment (ROI)

Total Revenue minus Total Marketing Spend divided by Total Marketing Spend.

For Focus Forge: 1,000 units sold is \$15,000. Spend total of \$1,200. ROI: (15k — $1,200) / $1,200 = 11.5x. Good.

---

## Funnel metrics for the small team

### Initial (awareness)

- **Reach:** Total impressions of content (blog, social, ad platform)
- **Share ratio:** Social shares / total impressions. High share ratio (>5%) indicates encoding/responding.
- **Escaped rate:** Email newsletter growth (N/ week = low? Running out the signal of interest)

### Mid-funnel (interest/desire)

| Metric | Value for | Use | Target | 
|---------|----------|-----|--------|
| Email optional + email open rate | Content quality | At launch, 2024-30% for a non-social list |
| Landing-to-signup / info download | Hook match | Waitlist: 5—8% conversion is a first scenario |
| Blog read time | Engagement | Average >2:30 min means audience is reading |

### Bottom-funnel

| Metric | Value | Target |
|--------|-------|--------|
| Purchase conversion rate | % of visitors purchase | 1–3% for app landing page |
| Average order value — AoV | For identifying up/cross sells | Straightforward purchase: $15 |
| Churn but one-time | → (less) if teaser upgrade | — |

---

## Attribution humility

Perfect attribution is not worth the time cost for a solo founder.

- First-touch (the channel they saw before conversion) is good enough for channel prioritization;
- Last-touch is better for converting touchpoints (landing page, email) decisions.
- Multi-touch attribution requires a tracking and costing system that costs more than \$5,000.

Recommendation: Ask each new customer one question: "What was the first thing that made you (pay) attention to Focus Forge?" Tabulate manual for first 100.

---

## Dashboard minimum

A launch dashboard needs these reports:

1. **Daily revenue:** Online sales (from payment processor) vs. target run rate
2. **Daily new visitors:** (landing page or app)
3. **Email conversion funnel:** Visitors → signups → email to purchase
4. **Channels breakdown:** Revenue per acquisition source (for first 100 customers — natural)
5. **Budget remaining:** vs. elapsed time
6. **Ad spend vs ROI** (paid channels only)

Check every three days during the launch. After 4 weeks, check weekly.

---

## Benchmarks for a \$15 product

| Metric | Good | Okay | At-Risk |
|--------|------|------|---------|
| LTV: CAC ratio | > 3:1 | 1.5–3:1 | < 1.5:1 |
| Month one conversion (email → purchase) | 5% | 2.5% | <1% |
| Landing page CVR (ad → purchase) | >3% | 0.5–2% | <0.5% |
| Email signup cost | Free (organic) is best | <$2/signup Paid | >$5 |
| Payback period (CAC after unit price) | <2 months | <6 months | >6 months |

## Things not to measure (for a solo launch)

- **Brand sentiment**: sample size too small, actionable.
- **Social follower growth:** vanity. Followers who do not buy are a retention number, not a growth number.
- **Impressions:** raw volume without meaningful metrics (like click or conversion) is the worst noise.
- **NPS with 12 customers:** statistically meaningless. Use customer calls instead.

## Recovery rules

If a quarterly analysis shows * CAC > \$15 * (unit price), pause all paid channels until further. Run an organic campaign only until the channels lose the problem. The fastest most effective change your targeting and testing at twice the CPC is unchanged for three weeks. Fix on radically by improving the offer or the landing page.

If the email → purchase less than 2%, test both the landing page and the email copy. Change one variable per email, then test.