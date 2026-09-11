# Monetization Ethics

Rubric for evaluating monetization flows against professional ethics standards
and regulatory requirements. Use this file when reviewing a purchase flow,
designing a new revenue stream, or preparing for a public launch that will face
regulatory scrutiny. The goal is not zero monetization — it is defensible
monetization that survives player pushback, media investigation, and regulatory
audit.

## 1. Dark Pattern Checklist

A purchase interface may contain a dark pattern if it triggers any of the
following. Score each purchase flow against every item before launch.

**Obfuscated pricing.** The real-world cost of a purchase is hidden behind
currency conversion with no clear exchange rate displayed at the point of
purchase. *Remedy:* always show the base-value equivalent in the player's
local currency next to the premium-currency price.

**False urgency.** A countdown timer, limited-stock indicator, or flashing
"last chance" label on a purchase that will return or is not actually scarce.
*Remedy:* only use timers on purchases that genuinely expire and will not
return in the same form.

**Pay-to-skip-fun.** The primary monetization flow asks the player to pay to
skip the only engaging content in the game (e.g., paying to skip a fun
minigame, paying to avoid a well-designed encounter). *Remedy:* monetize
optional content, not mandatory fun.

**Gacha opacity.** Random-reward mechanics with undisclosed probabilities or
no pity timer. *Remedy:* publish all probabilities; implement a hard pity at
N pulls; display a clear probability table before any random purchase.

**Bury the free path.** The free alternative to a premium purchase is hidden
behind multiple menus, requires scrolling, or is not mentioned at the point of
purchase. *Remedy:* every premium item page must show the free acquisition path
as the default-view option.

**Exploit vulnerability.** Mechanics that specifically target known cognitive
vulnerabilities: loss aversion (you will lose this if you do not buy now),
sunk cost (you have already spent, so spend more), or social comparison
(others have this and you do not). *Remedy:* audit messaging against the
principle that every purchase must be an informed, unpressured choice.

## 2. Premium Purity Rule

Premium currency may accelerate time, unlock cosmetics, or skip grind. It may
not increase any performance stat permanently. This is the dividing line
between acceptable monetization and pay-to-win.

Test every premium purchase against three categories:
- **Direct power boost:** does this permanently increase a combat stat?
- **Indirect advantage:** does this premium item provide a persistent edge in
  competitive contexts (more vision, faster resource generation, better
  matchmaking priority)?
- **Stacking loophole:** do multiple premium items combine to produce an effect
  that crosses the power boundary even though each individual item is clean?

A purchase that passes all three is premium-pure. If it fails any, redesign.

## 3. F2P Path Guarantee

Every item available through premium currency must have an alternative free
path costing at most 2x the paid method in play time. The free path must be
visible to the player at the point of purchase without scrolling or entering
a submenu.

Rationale: the F2P path is not charity — it protects the premium economy. A
premium-only item that does not exist for non-spenders creates two games: one
for spenders and one for everyone else. The second group either converts
(which the business wants) or quits (which the business does not want).
The visible free path gives them a reason to stay and engage.

## 4. Regulatory Considerations

| Jurisdiction | Key Constraint |
|-------------|----------------|
| EU (GDPR) | Consent requirements, data retention, minor protections |
| UK Gambling Commission | Loot boxes may constitute gambling; probability disclosure |
| Belgium / Netherlands | Probabilistic purchases effectively banned |
| China (2021) | Weekly spending caps for minors; daily time limits; probability disclosure |
| US (FTC) | Deceptive marketing enforcement; refund requirements |
| Apple / Google stores | Store-specific review guidelines on monetization disclosure |

These are minimums, not targets. A design that barely complies with the strictest
jurisdiction is a design that will fail a player trust test even where it is
legal.