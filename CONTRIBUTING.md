## Adding a Resource

Adding a resource to the docs is as simple as inserting a link. Fork this repository and add the link locally following the steps below. When you're done, open a PR with your addition.

1. **Determine which category the resource best fits.** Each resource is assigned to a single category, with a few exceptions for particularly sprawling documentation (e.g. WikiTI).
2. **Write a short description of the resource.** A good description fits in one line, and provides an objective, utilitarian summary of the resource.
3. **Determine which calculator(s) the resource supports.** The table of models and their corresponding emoji is at the top of the README.
4. **Add the link, description, and supported models to `README.md`.** The entries in the `All Resources` section are sorted alphabetically. Here's a template:

```
- [name here](link here) - ◒ 🎨 🌈 🎈  
description here
```

Note the extra two spaces after the last emoji; this prevents the description from being put on the same line as the link.

Please ensure your suggestion is of general interest and documentation value; this is not a place to promote personal projects. We will not include anything that is not explicitly documentation or tooling. If you have any questions about the suitability of your resource, feel free to open an issue before making your pull request.

Links added to the `I want to...` section follow the same format as above but are specifically targeted at people starting a new project. Be sure to add your link and description to **both** the `I want to...` section *and* the `All Resources` section. We try to keep the number of links in the `I want to...` section limited to prevent overwhelming users; open an issue if you have any doubts, or mention it in your pull request.

## Adding a Static Resource

If your resource is old, volatile, or currently offline, *please* add a static copy to the `docs` branch of this repository with a separate pull request. Upload the file in whatever format is best suited for it (preferably `.txt`, `.md`, or `.pdf`), then follow the steps above to add a link, where instead your link will be of the form `https://github.com/TI-Toolkit/awesome-ti-docs/blob/docs/<filename here>`.

## Corrections and Edits

Please do not hesitate to correct any dead links, incorrect descriptions, or outdated information in the docs. That being said, take care when editing static resources in the `docs` branch if you aren't the author. Furthermore, *do not* remove any links unless they are irrecoverable; try to find a mirror, web archive, or static copy instead.

If you have suggestions for reorganizing or reformating the docs, please open an issue or PR to discuss them.
