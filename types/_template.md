# Minting a new page type

Copy this shape. Fill every field — a type without Signals can't be proposed
by evidence, and one without an ask-for checklist produces vague pages.
Save the finished definition to `<wiki>/setup/custom-types/<type>.md` and
inline it into the wiki schema's type table and required-sections list.

**Mint vs stretch:** mint only when pages of the new kind need *different
required sections* or a *different ask-for checklist* than every existing
type. A different topic with the same shape is a tag, not a type. When in
doubt, stretch an existing type and let `audit` reveal whether it strains.

---

# <type-name> — <one-line what it captures>

- **Tier**: minted (user: <name>, date, reason in one line)
- **Prefix**: `<type-name>-`
- **Purpose**: <two or three sentences: what one page of this type represents,
  and what question it answers when consulted.>

## Signals
- <observable evidence — files, directory shapes, tools, phrases in
  conversation — that suggests this type belongs in a schema>

## Required sections
- `## <Section>` — <what belongs in it>
- `## Facts` — dated, provenance-tagged bullets for everything that fits no
  other section (most types want this)

## Ask the user for
- <the details the agent must obtain to make a page complete — the things it
  must never guess: paths, owners, dates, states>

## Naming
- `<type-name>-<kebab-case-slug>.md`; slug rule + an example.

## Typical relations
- <which other types its pages usually link to, in which direction>
