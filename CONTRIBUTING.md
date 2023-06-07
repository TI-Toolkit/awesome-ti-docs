## Adding a Resource

Adding a resource to the docs is as simple as inserting a link. Fork this repository and add the link locally following the steps below. When you're done, open a PR with your addition.

1. **Determine which category the resource best fits.** Each resource is assigned to a single category, with a few exceptions for particularly sprawling documentation (e.g. WikiTI).
2. **Write a short description of the resource.** A good description fits in one line, and provides an objective, utilitarian summary of the resource.
3. **Determine which calculator(s) the resource supports.** The table of models and their corresponding emoji is at the top of the README.
4. **Add the link, description, and supported models to `README.md`.** The entries are (currently) sorted alphabetically. Here's a template:

```
- [name here](link here) - ◒ 🎨 🌈 🎈  
description here
```

Note the extra whitespace after the last emoji; this prevents the description from being put on the same line as the link.

Please ensure your suggestion is of general interest and documentation value. We will not accept personal projects or programs, or anything that is not explicitly documentation or tooling.

## Adding a Static Resource

If your resource is old, volatile, or currently offline, you can add a static copy to the `docs` branch of this repository. Upload the file in whatever format is best suited for it (preferably `.txt`, `.md`, or `.pdf`), then follow the steps above to add a link, where instead your link will be of the form `https://github.com/TI-Toolkit/awesome-ti-docs/blob/docs/<filename here>`.

## Corrections and Edits

Please do not hesitate to correct any dead links, incorrect descriptions, or outdated information in the docs. That being said, take care when editing static resources in the `docs` branch if you aren't the author. Furthermore, *do not* remove any links unless they are irrecoverable; try to find a mirror, web archive, or static copy instead.

If you have suggestions for reorganizing or reformating the docs, please open an issue or PR to discuss them.
