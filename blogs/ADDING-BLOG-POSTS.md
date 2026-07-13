# Adding a New Blog Post

These instructions are for a person (or AI assistant) publishing a new post on the Anderson Law Firm static website. No build tools are required—only HTML files.

## What you will change

| File | Action |
|------|--------|
| `blogs/_template.html` | Copy this file; do **not** edit the template itself |
| `blogs/YOUR-SLUG.html` | New post page (created from the template) |
| `blog.html` | Add a listing entry at the **top** of the post list |
| `sitemap.xml` | Add the new post URL |

Optional (nice for SEO): add the new post to the `blogPost` array inside the Blog schema JSON-LD in `blog.html`.

## Step-by-step

### 1. Choose a slug (filename)

Use lowercase words separated by hyphens. Example: `trusts-for-blended-families`.

Final path: `blogs/trusts-for-blended-families.html`  
Public URL: `https://andersonplc.com/blogs/trusts-for-blended-families.html`

Do not use spaces, underscores, or special characters.

### 2. Copy the template

Copy `blogs/_template.html` to `blogs/YOUR-SLUG.html`.

### 3. Fill every placeholder in the new file

Search the new file for these tokens and replace **all** occurrences of each:

| Placeholder | Meaning | Example |
|-------------|---------|---------|
| `POST_TITLE` | Full headline | `Trusts for Blended Families` |
| `META_DESCRIPTION` | ~150–160 character summary for search/social | `How a trust can protect children from a prior marriage while providing for a surviving spouse.` |
| `META_KEYWORDS` | Comma-separated topics | `trusts, blended families, estate planning, Michigan` |
| `SLUG` | Filename without `.html` | `trusts-for-blended-families` |
| `ARTICLE_SECTION` | Short category | `Estate Planning` |
| `BREADCRUMB_NAME` | Short breadcrumb label (can match section or a short title) | `Trusts for Blended Families` |
| `DATE_PUBLISHED_ISO` | ISO datetime with timezone | `2026-07-13T12:00:00-04:00` |
| `DATE_DISPLAY` | Human-readable date | `July 13, 2026` |

Also replace the sample paragraphs inside `<article class="article-body">` with the real post content.

**Allowed body HTML:** `<p>`, `<h2>`, `<ul>`, `<ol>`, `<li>`, `<strong>`, `<em>`, `<a href="...">`. Avoid custom styles or inline CSS.

**Asset paths:** Posts live in `/blogs/`, so site assets already use `../` (for example `../main.css`, `../images/logo.png`). Keep those as-is.

### 4. Add the post to `blog.html`

In `blog.html`, find `<div class="blog-list">` and insert a **new** item as the **first** child (newest first):

```html
<article class="blog-list__item">
    <h2 class="blog-list__title">
        <a href="blogs/YOUR-SLUG.html">POST_TITLE</a>
    </h2>
    <p class="blog-list__meta"><time datetime="DATE_PUBLISHED_ISO">DATE_DISPLAY</time> · ARTICLE_SECTION</p>
    <p class="blog-list__excerpt">One or two sentences that tease the article (often the same as META_DESCRIPTION, or slightly shorter).</p>
    <a class="blog-list__more" href="blogs/YOUR-SLUG.html">Read more</a>
</article>
```

Optionally add a matching object to the `blogPost` array in the Blog schema near the top of `blog.html`.

### 5. Update `sitemap.xml`

Add a new `<url>` block (use today’s date for `lastmod`):

```xml
<url>
    <loc>https://andersonplc.com/blogs/YOUR-SLUG.html</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
</url>
```

Also update the `lastmod` on `https://andersonplc.com/blog.html` when you add a post.

### 6. Quick checklist before publishing

- [ ] Filename is `blogs/lowercase-hyphen-slug.html`
- [ ] No leftover placeholders (`POST_TITLE`, `SLUG`, `META_DESCRIPTION`, etc.)
- [ ] Title, description, dates, and body look correct in a browser
- [ ] Listing appears at the top of `blog.html`
- [ ] `sitemap.xml` includes the new URL
- [ ] HubSpot script is still present just before `</body>` (it is already in the template)

## Suggested categories (`ARTICLE_SECTION`)

Use one short label, for example:

- Estate Planning
- Trusts
- Probate
- Business Planning
- Elder Law
- Legal Insights

## AI assistant prompt (copy/paste)

```
Add a new blog post to this static site.

1. Copy blogs/_template.html to blogs/{slug}.html
2. Replace every placeholder listed in blogs/ADDING-BLOG-POSTS.md
3. Write the article body in HTML inside .article-body
4. Add a newest-first listing entry in blog.html
5. Add the URL to sitemap.xml and bump blog.html lastmod

Do not modify blogs/_template.html.
Keep the existing header, footer, fonts, and HubSpot embed from the template.
```

## Do not

- Edit `blogs/_template.html` for a single post (only update it when the shared layout changes)
- Put new posts outside the `blogs/` folder
- Link to posts with a leading slash inconsistently—prefer relative links like `blogs/slug.html` from `blog.html`, and `../blog.html` from inside a post
- Remove the HubSpot tracking script at the bottom of the page
