# Contributing to Effortless Renders

First off, thank you for considering contributing to Effortless Renders! People like you make this tool better for everyone.

While code contributions are always welcome, **the biggest way you can help is by contributing to the Community Render Scenes Pack!**

## 🌍 The Community Render Scenes Pack

We are building a free, open-source library of high-quality render scenes (lighting setups, backdrops, studio environments) that anyone can use to showcase their 3D models. 

By contributing your custom `.blend` render scenes, you help other 3D artists present their work professionally with zero effort.

### How to Contribute a Render Scene

1. **Create your scene:**
   - Create a new `.blend` file.
   - Set up your lighting, cameras, backdrop, and any necessary environment nodes.
   - Organize your scene clearly so it works seamlessly with the addon (e.g., proper lighting for product shots, turntables, or wireframes).
   - **Important:** Ensure you have the rights to share all assets in the `.blend` file (no paid HDRIs or copyrighted models unless you have permission to distribute them freely).

2. **Prepare the file for the addon:**
   - Name the scenes inside your `.blend` file according to the renders they are meant for if applicable (e.g., `rendering`, `turntable`, `searchimage`, `wire`).
   - If your scene requires a specific framing object, include a `helperbox` collection.

3. **Submit your scene:**
   - **Fork** this repository.
   - Place your `.blend` file into the `render_scenes/` directory.
   - Commit your changes: `git commit -m "Add [Description of your scene] to community pack"`
   - Open a **Pull Request** (PR) against this repository.

### What happens next?

Once your PR is reviewed and merged, your scene will be included in the next release of the addon, making it instantly available for free to the entire Effortless Renders community!

---

## 💻 Code Contributions

If you want to contribute code to the addon itself:

1. Fork the repo and create your branch from `main`.
2. Write clear, documented Python code matching the existing style.
3. Ensure your code passes the automated tests (the repo will automatically run `ruff` and test Blender compatibility on your PR).
4. Update the `README.md` if you are adding new features.
5. Open a Pull Request!

If you find a bug or have a feature request, please [open an issue](https://github.com/jordandubu/effortless-renders/issues).
