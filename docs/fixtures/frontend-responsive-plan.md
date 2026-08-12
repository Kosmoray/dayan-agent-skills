# Responsive UI acceptance plan

Skill: `dayan-frontend-responsive-ui`

## Input

A dashboard page works on a laptop but the cards collapse badly on phones and the primary action disappears below unrelated status panels.

## Output artifact

### Target states

- phone: 360 px wide;
- tablet: 768 px wide;
- desktop: 1280 px wide.

### Acceptance rules

1. The primary action is visible without horizontal scroll.
2. Metric cards wrap to one column on phone and two columns on tablet.
3. Empty states remain readable at 360 px.
4. Focus order follows visual order.
5. Tap targets are at least 44 px high.

### Test fixture

Use a synthetic dashboard with:

- one title;
- one primary action;
- four metric cards;
- one empty activity list;
- one warning banner.

### Review checklist

- no horizontal scroll at 360 px;
- no overlapping text;
- primary action remains before secondary panels;
- keyboard focus is visible;
- reduced-motion preference does not hide state changes.

## Verification

- Capture one screenshot or viewport report for each target state.
- Record any remaining visual issue as a blocker, concern, or accepted tradeoff.

## Boundary

This fixture does not prove product usability, accessibility conformance, or browser coverage beyond the tested viewports.
