# Deck design system

Use this reference after the story map exists.

## Typography

Use a neutral sans-serif stack that works without downloads:

```css
font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,
  "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
```

For a 1920 × 1080 logical canvas:

- display: 96–144 px;
- slide title: 54–76 px;
- body: 28–38 px;
- labels and metadata: at least 20 px.

Use weight and scale for hierarchy. Do not use condensed, decorative, serif, or monospace faces for ordinary body text.

## Color

Start with one of two systems:

- dark: near-black background, warm-white text, one vivid accent;
- light: warm-white background, near-black text, one vivid accent.

The accent should guide attention, not decorate every object. Keep ordinary text at readable contrast. Never communicate a state by color alone.

## Layout

Use a 12-column mental grid with a generous safe zone. Prefer:

- one strong statement;
- statement plus one proof object;
- two-column comparison;
- one framework with three to five parts;
- one visual sequence.

Avoid:

- six equal cards with equal emphasis;
- text touching the stage edge;
- long paragraphs centered on screen;
- titles competing with diagrams;
- decoration that creates a second focal point.

## Motion

Use motion only to explain order, causality, continuity, or change.

- one entrance grammar per deck;
- 180–500 ms for ordinary UI transitions;
- up to 900 ms for a deliberate scene change;
- no auto-advancing slides by default;
- reduced-motion must remain fully usable.

## Visual review

The deterministic verifier cannot see aesthetics. Render every slide and check:

1. the intended focal point is obvious in one second;
2. no text is smaller than the viewing context permits;
3. no line, label, or visual overlaps;
4. the slide works without narration when it contains a decision;
5. the deck still works without animation.
