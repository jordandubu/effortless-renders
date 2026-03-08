# Effortless Renders

[![Blender Compatibility](https://github.com/jordandubu/effortless-renders/actions/workflows/blender-compat.yml/badge.svg)](https://github.com/jordandubu/effortless-renders/actions/workflows/blender-compat.yml)
[![Release](https://github.com/jordandubu/effortless-renders/actions/workflows/release.yml/badge.svg)](https://github.com/jordandubu/effortless-renders/releases)

A Blender addon for automating 3D marketplace renders — turntables, product shots, wireframes, and search images in one click.

## Features

- 🎬 **One-click rendering** — Batch render multiple scene types (product shots, turntable, wireframe, search image)
- 🔄 **Turntable video** — Automatically generates MP4 turntable animations via Blender's built-in video encoder
- 📦 **Scene library** — Load render scenes from `.blend` files
- 🧊 **Helper box** — Import helper box collection for framing
- 🔌 **TurboSquid integration** — API connection for marketplace publishing

## Requirements

- **Blender** 4.0+

## Installation

1. Download the latest release from [Releases](https://github.com/jordandubu/effortless-renders/releases)
2. In Blender: **Edit → Preferences → Add-ons → Install**
3. Select the downloaded `.zip` file
4. Enable "3D Market Exporter" in the addon list

## Usage

1. Open the **Tool** sidebar in the 3D Viewport (`T` key)
2. Find the **3D Market Exporter** panel
3. Select a collection to render
4. Set an export path
5. Choose a render scene from your library
6. Toggle which renders you want (Rendering, Turntable, Search Image, Wire)
7. Hit **RENDER**

## Configuration

In **Edit → Preferences → Add-ons → 3D Market Exporter**:

- **Library Path** — Set the path to your folder of `.blend` render scene files

## 🌍 Community Render Scenes

Want more lighting setups and studio environments? You can create your own `.blend` render scenes and contribute them to the **Community Pack**! 

All contributed scenes are included in future releases, making them free for the entire community. Check out the [Contributing Guidelines](CONTRIBUTING.md) to learn how to add your own setups.

## Development

```bash
git clone https://github.com/jordandubu/effortless-renders.git
```

### CI/CD

This repo is self-maintaining:

- **Blender compatibility** is automatically tested every 2 weeks against the latest Blender release
- **Breaking changes** are auto-fixed via AI and submitted as PRs, which are **automatically merged** if the fix passes the tests.
- **Releases** are created automatically when you push a version tag (`git tag v1.2 && git push --tags`)

## License

[GPL-2.0](LICENSE) — Free software. See individual source files for full license headers.
