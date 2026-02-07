# Design System Documentation

This document provides a comprehensive reference for the shadcn/ui-based design system implemented in this application. All theming follows the official shadcn default theme with black (#000000) as the primary accent color.

---

## Table of Contents

1. [Color System](#color-system)
2. [Typography](#typography)
3. [Spacing & Layout](#spacing--layout)
4. [Border Radius](#border-radius)
5. [Shadows](#shadows)
6. [Theme Provider](#theme-provider)
7. [UI Components](#ui-components)
8. [Usage Guidelines](#usage-guidelines)

---

## Color System

All colors are defined as HSL values in CSS custom properties. The system supports both light and dark modes with automatic switching.

### Core Color Tokens

| Token | Light Mode | Dark Mode | Usage |
|-------|-----------|-----------|-------|
| `--background` | `0 0% 100%` (white) | `0 0% 3.5%` (near-black) | Page background |
| `--foreground` | `210 25% 7.8%` (dark gray) | `0 0% 98%` (off-white) | Primary text |
| `--card` | `180 6.7% 97%` (light gray) | `0 0% 7%` (dark gray) | Card backgrounds |
| `--card-foreground` | `210 25% 7.8%` | `0 0% 98%` | Card text |
| `--popover` | `0 0% 100%` | `0 0% 8%` | Popover/dropdown backgrounds |
| `--popover-foreground` | `210 25% 7.8%` | `0 0% 98%` | Popover text |

### Primary & Accent Colors

| Token | Light Mode | Dark Mode | Usage |
|-------|-----------|-----------|-------|
| `--primary` | `0 0% 9%` (black) | `0 0% 98%` (white) | Primary buttons, links |
| `--primary-foreground` | `0 0% 98%` | `0 0% 9%` | Text on primary |
| `--secondary` | `210 40% 96.1%` | `0 0% 15%` | Secondary buttons |
| `--secondary-foreground` | `222.2 47.4% 11.2%` | `0 0% 98%` | Text on secondary |
| `--muted` | `210 40% 96.1%` | `0 0% 15%` | Muted backgrounds |
| `--muted-foreground` | `215.4 16.3% 46.9%` | `0 0% 65%` | Muted text |
| `--accent` | `210 40% 96.1%` | `0 0% 15%` | Accent highlights |
| `--accent-foreground` | `222.2 47.4% 11.2%` | `0 0% 98%` | Text on accent |

### Status Colors

| Token | Light Mode | Dark Mode | Usage |
|-------|-----------|-----------|-------|
| `--destructive` | `0 84.2% 60.2%` (red) | `0 62.8% 30.6%` | Error states, delete actions |
| `--destructive-foreground` | `0 0% 98%` | `0 0% 98%` | Text on destructive |
| `--success` | `142 76% 36%` (green) | `142 71% 45%` | Success states |
| `--success-foreground` | `0 0% 98%` | `0 0% 9%` | Text on success |
| `--warning` | `38 92% 50%` (orange) | `38 92% 60%` | Warning states |
| `--warning-foreground` | `0 0% 98%` | `0 0% 9%` | Text on warning |
| `--info` | `217 91% 60%` (blue) | `217 91% 70%` | Info states |
| `--info-foreground` | `0 0% 98%` | `0 0% 9%` | Text on info |

### Form & Border Colors

| Token | Light Mode | Dark Mode | Usage |
|-------|-----------|-----------|-------|
| `--border` | `214.3 31.8% 91.4%` | `0 0% 28%` | Border color |
| `--input` | `214.3 31.8% 91.4%` | `0 0% 28%` | Input borders |
| `--ring` | `0 0% 9%` | `0 0% 83.9%` | Focus ring color |

### Chart Colors (Grayscale Palette)

| Token | Light Mode | Dark Mode |
|-------|-----------|-----------|
| `--chart-1` | `0 0% 30%` | `0 0% 75%` |
| `--chart-2` | `0 0% 42%` | `0 0% 65%` |
| `--chart-3` | `0 0% 54%` | `0 0% 55%` |
| `--chart-4` | `0 0% 66%` | `0 0% 45%` |
| `--chart-5` | `0 0% 78%` | `0 0% 35%` |

### Sidebar Colors

| Token | Light Mode | Dark Mode |
|-------|-----------|-----------|
| `--sidebar` | `0 0% 98%` | `0 0% 7%` |
| `--sidebar-foreground` | `0 0% 20%` | `0 0% 95%` |
| `--sidebar-primary` | `0 0% 90%` | `0 0% 75%` |
| `--sidebar-primary-foreground` | `0 0% 10%` | `0 0% 7%` |
| `--sidebar-accent` | `0 0% 85%` | `0 0% 15%` |
| `--sidebar-accent-foreground` | `0 0% 10%` | `0 0% 95%` |
| `--sidebar-border` | `0 0% 90%` | `0 0% 28%` |
| `--sidebar-ring` | `0 0% 20%` | `0 0% 80%` |

### Gradient Colors

| Token | Light Mode | Dark Mode |
|-------|-----------|-----------|
| `--gradient-from` | `0 0% 9%` | `0 0% 98%` |
| `--gradient-via` | `280 100% 70%` | `0 0% 70%` |
| `--gradient-to` | `340 100% 70%` | `0 0% 60%` |

---

## Typography

### Font Families

```css
--font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-serif: Georgia, serif;
--font-mono: "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
```

### Usage in Tailwind

```tsx
<p className="font-sans">Body text</p>
<code className="font-mono">Code snippet</code>
<blockquote className="font-serif">Quote text</blockquote>
```

### Heading Styles

All headings use:
- `font-weight: 600` (semi-bold)
- `letter-spacing: -0.025em` (tight tracking)

### Text Balance

The utility class `.text-balance` applies `text-wrap: balance` for improved line wrapping in headings.

---

## Spacing & Layout

### Base Spacing Unit

```css
--spacing: 0.25rem; /* 4px */
```

Tailwind's spacing scale multiplies this base unit:
- `p-1` = 0.25rem (4px)
- `p-2` = 0.5rem (8px)
- `p-4` = 1rem (16px)
- `p-6` = 1.5rem (24px)
- `p-8` = 2rem (32px)

### Letter Spacing

```css
--tracking-normal: 0em;
```

---

## Border Radius

```css
--radius: 0.5rem; /* 8px base radius */
```

### Tailwind Border Radius Classes

| Class | Value |
|-------|-------|
| `rounded-lg` | `var(--radius)` (8px) |
| `rounded-md` | `calc(var(--radius) - 2px)` (6px) |
| `rounded-sm` | `calc(var(--radius) - 4px)` (4px) |

---

## Shadows

### Light Mode Shadows

| Token | Value |
|-------|-------|
| `--shadow-2xs` | `0px 1px 2px 0px hsl(0, 0%, 0%, 0.05)` |
| `--shadow-xs` | `0px 1px 2px 0px hsl(0, 0%, 0%, 0.05), 0px 1px 3px 0px hsl(0, 0%, 0%, 0.1)` |
| `--shadow-sm` | `0px 1px 2px 0px hsl(0, 0%, 0%, 0.05), 0px 1px 3px 0px hsl(0, 0%, 0%, 0.1)` |
| `--shadow` | `0px 1px 3px 0px hsl(0, 0%, 0%, 0.1), 0px 1px 2px -1px hsl(0, 0%, 0%, 0.1)` |
| `--shadow-md` | `0px 4px 6px -1px hsl(0, 0%, 0%, 0.1), 0px 2px 4px -2px hsl(0, 0%, 0%, 0.1)` |
| `--shadow-lg` | `0px 10px 15px -3px hsl(0, 0%, 0%, 0.1), 0px 4px 6px -4px hsl(0, 0%, 0%, 0.1)` |
| `--shadow-xl` | `0px 20px 25px -5px hsl(0, 0%, 0%, 0.1), 0px 8px 10px -6px hsl(0, 0%, 0%, 0.1)` |
| `--shadow-2xl` | `0px 25px 50px -12px hsl(0, 0%, 0%, 0.25)` |

### Dark Mode Shadows

Dark mode uses increased opacity for better depth perception on dark backgrounds:
- Base opacity: 0.3-0.6 (vs 0.05-0.25 in light mode)

---

## Theme Provider

### Setup

The theme provider is located at `client/src/components/theme-provider.tsx` and wraps the entire application.

```tsx
import { ThemeProvider } from "@/components/theme-provider";

function App() {
  return (
    <ThemeProvider>
      {/* Your app content */}
    </ThemeProvider>
  );
}
```

### Usage

```tsx
import { useTheme } from "@/hooks/use-theme";

function MyComponent() {
  const { theme, setTheme, toggleTheme, setPrimaryColor } = useTheme();

  return (
    <button onClick={toggleTheme}>
      Current theme: {theme}
    </button>
  );
}
```

### API

| Method | Type | Description |
|--------|------|-------------|
| `theme` | `"light" \| "dark"` | Current theme value |
| `setTheme` | `(theme: Theme) => void` | Set theme explicitly |
| `toggleTheme` | `() => void` | Toggle between light/dark |
| `setPrimaryColor` | `(hex: string) => void` | Change primary accent color |

### Dynamic Primary Color

The `setPrimaryColor` function accepts a hex color and automatically:
1. Converts to HSL
2. Calculates appropriate foreground color for contrast
3. Adjusts lightness for dark mode visibility
4. Persists to localStorage

```tsx
const { setPrimaryColor } = useTheme();
setPrimaryColor("#3B82F6"); // Blue primary
```

### Dark Mode Implementation

The theme is applied via the `.dark` class on `<html>`:

```tsx
// Tailwind config
darkMode: ["class"]

// Usage
<div className="bg-white dark:bg-black text-black dark:text-white">
  Content
</div>
```

---

## UI Components

All 49+ components are sourced from shadcn/ui v4 and located in `client/src/components/ui/`.

### Layout Components

| Component | File | Description |
|-----------|------|-------------|
| Card | `card.tsx` | Container with header, content, footer |
| Separator | `separator.tsx` | Horizontal/vertical divider |
| Aspect Ratio | `aspect-ratio.tsx` | Maintain aspect ratios |
| Resizable | `resizable.tsx` | Resizable panels |
| Scroll Area | `scroll-area.tsx` | Custom scrollbars |

### Form Components

| Component | File | Variants |
|-----------|------|----------|
| Button | `button.tsx` | default, destructive, outline, secondary, ghost, link |
| Input | `input.tsx` | - |
| Textarea | `textarea.tsx` | - |
| Checkbox | `checkbox.tsx` | - |
| Radio Group | `radio-group.tsx` | - |
| Switch | `switch.tsx` | - |
| Slider | `slider.tsx` | - |
| Select | `select.tsx` | - |
| Calendar | `calendar.tsx` | - |
| Form | `form.tsx` | React Hook Form integration |
| Label | `label.tsx` | - |
| Input OTP | `input-otp.tsx` | One-time password input |

### Button Variants

```tsx
<Button variant="default">Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="destructive">Delete</Button>
<Button variant="outline">Outline</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="link">Link</Button>
```

### Button Sizes

```tsx
<Button size="default">Default</Button>
<Button size="sm">Small</Button>
<Button size="lg">Large</Button>
<Button size="icon"><Icon /></Button>
```

### Feedback Components

| Component | File | Variants |
|-----------|------|----------|
| Alert | `alert.tsx` | default, destructive |
| Badge | `badge.tsx` | default, secondary, destructive, outline |
| Progress | `progress.tsx` | - |
| Skeleton | `skeleton.tsx` | - |
| Toast | `toast.tsx` | - |
| Toaster | `toaster.tsx` | - |

### Badge Variants

```tsx
<Badge variant="default">Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="destructive">Destructive</Badge>
<Badge variant="outline">Outline</Badge>
```

### Navigation Components

| Component | File | Description |
|-----------|------|-------------|
| Navigation Menu | `navigation-menu.tsx` | Desktop navigation with dropdowns |
| Menubar | `menubar.tsx` | Application menubar |
| Breadcrumb | `breadcrumb.tsx` | Breadcrumb navigation |
| Tabs | `tabs.tsx` | Tabbed content |
| Pagination | `pagination.tsx` | Page navigation |

### Overlay Components

| Component | File | Description |
|-----------|------|-------------|
| Dialog | `dialog.tsx` | Modal dialogs |
| Alert Dialog | `alert-dialog.tsx` | Confirmation dialogs |
| Sheet | `sheet.tsx` | Slide-out panels |
| Drawer | `drawer.tsx` | Bottom/side drawers |
| Popover | `popover.tsx` | Floating content |
| Tooltip | `tooltip.tsx` | Hover tooltips |
| Hover Card | `hover-card.tsx` | Rich hover content |
| Context Menu | `context-menu.tsx` | Right-click menus |
| Dropdown Menu | `dropdown-menu.tsx` | Dropdown menus |
| Command | `command.tsx` | Command palette (⌘K) |

### Data Display Components

| Component | File | Description |
|-----------|------|-------------|
| Table | `table.tsx` | Data tables |
| Avatar | `avatar.tsx` | User avatars |
| Accordion | `accordion.tsx` | Expandable sections |
| Collapsible | `collapsible.tsx` | Toggle visibility |
| Carousel | `carousel.tsx` | Image/content carousel |
| Chart | `chart.tsx` | Recharts integration |

### Sidebar Components

| Component | File | Description |
|-----------|------|-------------|
| Sidebar | `sidebar.tsx` | Full sidebar system |

---

## Usage Guidelines

### Color Usage Best Practices

1. **Use semantic tokens**: Always use `bg-primary` instead of hardcoded colors
2. **Pair foreground colors**: When using `bg-primary`, use `text-primary-foreground`
3. **Status consistency**: Use `destructive` for errors, `success` for confirmations

### Dark Mode Best Practices

1. **Always specify both modes**:
   ```tsx
   <div className="bg-white dark:bg-gray-900">
   ```

2. **Use CSS variables for custom styles**:
   ```css
   .custom {
     background: hsl(var(--background));
     color: hsl(var(--foreground));
   }
   ```

3. **Test both modes** before shipping

### Component Composition

```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

function FeatureCard() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Feature Name</CardTitle>
        <CardDescription>Feature description</CardDescription>
      </CardHeader>
      <CardContent>
        <p>Content here</p>
      </CardContent>
      <CardFooter>
        <Button>Action</Button>
      </CardFooter>
    </Card>
  );
}
```

### Accessibility

All components are built on Radix UI primitives which provide:
- Keyboard navigation
- Focus management
- ARIA attributes
- Screen reader support

### File Structure

```
client/src/
├── components/
│   ├── ui/                 # shadcn/ui components
│   ├── layout/             # Layout wrappers
│   ├── design-system/      # Design system views
│   └── landing/            # Landing page sections
├── hooks/
│   └── use-theme.ts        # Theme hook
├── lib/
│   └── utils.ts            # cn() utility
└── index.css               # CSS custom properties
```

---

## Configuration Files

### tailwind.config.ts

The Tailwind configuration extends the default theme with:
- Custom color tokens from CSS variables
- Font family references
- Border radius scale
- Accordion animations

### index.css

Contains:
- `:root` light mode variables
- `.dark` dark mode variables
- Base layer typography styles
- Component layer utilities
- Utility layer helpers

---

## Version Information

- **shadcn/ui version**: v4
- **Tailwind CSS**: v3.x
- **Radix UI**: Latest
- **React**: 18.x

---

## Quick Reference

### Import Paths

```tsx
// Components
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

// Hooks
import { useTheme } from "@/hooks/use-theme";
import { useToast } from "@/hooks/use-toast";

// Utilities
import { cn } from "@/lib/utils";
```

### The `cn()` Utility

Combines clsx and tailwind-merge for conditional classes:

```tsx
import { cn } from "@/lib/utils";

<div className={cn(
  "base-styles",
  isActive && "active-styles",
  className
)} />
```
