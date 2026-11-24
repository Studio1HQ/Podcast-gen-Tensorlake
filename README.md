<div align="center">

<img src="https://raw.githubusercontent.com/Studio1HQ/Studio1HQ/main/assets/banners/Podcast-gen-Tensorlake.webp" alt="Hacker News Podcast Generator on Tensorlake: Turn the top Hacker News articles into short podcast episodes" width="100%" />

<br />
<br />

# Hacker News Podcast Generator on Tensorlake

### Turn the top Hacker News articles into short podcast episodes

A Tensorlake application that fetches the top three Hacker News articles, crawls them with a headless browser, summarises each with Gemini and voices it with ElevenLabs. A Streamlit app wraps it.

<br />

[![Built by Studio1](https://img.shields.io/badge/Built_by_Studio1-f97316?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNjAgMTYwIiBmaWxsPSJub25lIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTAgMzVDMCAxNi42ODA3IDE0LjA3NDQgMS42NDg0NCAzMiAwLjEyNjk1M1YxNDFINTEuMDUyM0M1Mi40MzA4IDEzNy4zNDQgNTQuNzQ0NiAxMzMuNjg5IDU3Ljk5MzggMTMwLjAzM0M2MS4xNDQ2IDEyNi41MDggNjQuNjg5MiAxMjMuNDQgNjguNjI3NyAxMjAuODI5QzcyLjU2NjIgMTE4LjM0OSA3Ni4zNTY5IDExNi43ODIgODAgMTE2LjEyOVY4Ni43NTQ0Qzc1LjQ3MDggODcuOTI5MiA3MS4zODQ2IDg5LjY5MTkgNjcuNzQxNSA5Mi4wNDE1QzY0IDk0LjUyMjUgNjAuNzUwOCA5Ny40NiA1Ny45OTM4IDEwMC44NTRDNTYuNTM0NSAxMDIuNzIgNTUuMjU0NSAxMDQuNjU5IDU0LjE1MzkgMTA2LjY3MVYwSDEyNUMxNDQuMzMgMCAxNjAgMTUuNjY5OSAxNjAgMzVWMTI1QzE2MCAxNDQuMzMgMTQ0LjMzIDE2MCAxMjUgMTYwSDEyNFYxOEgxMDQuOTQ4QzEwMy41NjkgMjEuNjgxNiAxMDEuMjU1IDI1LjM2MjggOTguMDA2MiAyOS4wNDQ0Qzk0Ljg1NTQgMzIuNTk0MiA5MS4zMTA4IDM1LjY4NDEgODcuMzcyMyAzOC4zMTRDODMuNDMzOCA0MC44MTIgNzkuNjQzMSA0Mi4zODk2IDc2IDQzLjA0NzRWNzIuNjMwNEM4MC41MjkyIDcxLjQ0NzMgODQuNjE1NCA2OS42NzI0IDg4LjI1ODUgNjcuMzA1N0M5MiA2NC44MDc2IDk1LjI0OTIgNjEuODQ5MSA5OC4wMDYyIDU4LjQzMDdDOTkuNDY1NSA1Ni41NTEzIDEwMC43NDUgNTQuNTk4NiAxMDEuODQ2IDUyLjU3MjNWMTYwSDM1QzE1LjY3IDE2MCAwIDE0NC4zMyAwIDEyNVYzNVoiIGZpbGw9IiNmZmZmZmYiLz48L3N2Zz4K)](https://studio1hq.com)
[![Built with Tensorlake](https://img.shields.io/badge/Built_with_Tensorlake-141414?style=for-the-badge)](https://tensorlake.ai)

[Tensorlake docs](https://docs.tensorlake.ai) &nbsp;·&nbsp; [Tensorlake](https://tensorlake.ai) &nbsp;·&nbsp; [More examples](https://github.com/Studio1HQ) &nbsp;·&nbsp; [studio1hq.com](https://studio1hq.com)

</div>

<br />

## Overview

This example turns the current top three Hacker News stories into short podcast clips. It is a [Tensorlake](https://tensorlake.ai) application, `podcast_agent`, that runs a small pipeline: fetch the front page, crawl each article with a headless Chromium browser, summarise it with Gemini, and read the summary aloud with ElevenLabs.

A Streamlit app, `app.py`, lists the top three stories, takes your API keys in the sidebar and shows the generated audio.

## Features

- **Hacker News intake**: A Tensorlake function scrapes `news.ycombinator.com` and returns the top three article links.
- **Headless crawling**: `fetch_content` runs in a custom container image with Chromium and [PyDoll](https://github.com/autoscrape-labs/pydoll). It extracts page text and links, and base64-encodes binary files.
- **Depth-first crawl**: `crawl` follows same-domain links up to `max_depth` and `max_links`.
- **Gemini summaries**: Each article, trimmed to its first 6,000 characters, is summarised into five short lines with `gemini-2.5-flash`.
- **ElevenLabs audio**: The summary is voiced with the `eleven_v3` model and returned as MP3.
- **Streamlit UI**: Shows the stories, a crawl-depth slider and a download button per podcast.
- **Retries and sizing**: Fetch steps use Tensorlake `Retries` and explicit CPU and memory settings.

## Tech stack

| Layer | Tool |
| --- | --- |
| Runtime | [Tensorlake](https://tensorlake.ai) applications and custom images |
| Crawling | [PyDoll](https://github.com/autoscrape-labs/pydoll) with Chromium, BeautifulSoup |
| Summarisation | [Google Gemini](https://ai.google.dev/) (`google-genai`) |
| Text to speech | [ElevenLabs](https://elevenlabs.io/) |
| UI | [Streamlit](https://streamlit.io) |

## Getting started

### Prerequisites

- Python 3.10 or later (the scraper image uses Python 3.11)
- A [Gemini API key](https://aistudio.google.com/app/apikey)
- An [ElevenLabs API key](https://elevenlabs.io/)
- A [Tensorlake](https://tensorlake.ai) account if you deploy the application

### Installation

```bash
git clone https://github.com/Studio1HQ/Podcast-gen-Tensorlake.git
cd Podcast-gen-Tensorlake
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the project root. The repo already contains one with placeholder values; replace them and do not commit real keys.

| Variable | Description |
| --- | --- |
| `GEMINI_API_KEY` | Google Gemini key, from [Google AI Studio](https://aistudio.google.com/app/apikey). Declared as a Tensorlake secret. |
| `ELEVENLABS_API_KEY` | ElevenLabs key, from the [ElevenLabs dashboard](https://elevenlabs.io/). Declared as a Tensorlake secret. |

You can also paste both keys into the Streamlit sidebar.

### Run

Streamlit UI at [http://localhost:8501](http://localhost:8501):

```bash
streamlit run app.py
```

Or run the agent directly. It writes `podcasts.zip` containing `podcast_1.mp3` to `podcast_3.mp3`:

```bash
python podcast_agent.py
```

## How it works

1. `fetch_hackernews_top_article` parses the Hacker News front page and returns the first three `span.titleline > a` links.
2. For each link, `crawl` calls `fetch_content` on the scraper image. PyDoll opens the page in headless Chromium and returns `innerText` and the page links.
3. `extract_clean_text` joins the page text.
4. `summarize_with_gemini` produces a five-line, podcast-friendly summary.
5. `generate_audio` posts the summary to the ElevenLabs text-to-speech API (voice ID `21m00Tcm4TlvDq8ikWAM`).
6. `podcast_agent` zips the three MP3 files and returns them as a Tensorlake `File`.

```text
.
├── podcast_agent.py   # Tensorlake application and all pipeline functions
├── app.py             # Streamlit front end
├── requirements.txt
└── podcast_audio.mp3  # Sample output
```

## Resources

- [Tensorlake docs](https://docs.tensorlake.ai): applications, functions and images.
- [Tensorlake](https://tensorlake.ai): the platform used here.
- [Gemini API docs](https://ai.google.dev/gemini-api/docs): models and the `google-genai` SDK.
- [ElevenLabs docs](https://elevenlabs.io/docs): text-to-speech API.
- [PyDoll](https://github.com/autoscrape-labs/pydoll): the headless browser library.

<br />

---

<div align="center">

<a href="https://studio1hq.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Studio1HQ/website/main/brand/studio1-logo-on-dark.svg" />
    <img src="https://raw.githubusercontent.com/Studio1HQ/website/main/brand/studio1-logo-on-light.svg" alt="Studio1" width="160" />
  </picture>
</a>

Built by **[Studio1](https://studio1hq.com)**, the technical content and DevRel partner for devtool teams. Made with [Tensorlake](https://tensorlake.ai).<br />
Browse more open-source examples at [github.com/Studio1HQ](https://github.com/Studio1HQ).

[![Website](https://img.shields.io/badge/studio1hq.com-0b0807?style=for-the-badge&logo=googlechrome&logoColor=white)](https://studio1hq.com)
[![Book a call](https://img.shields.io/badge/Book_a_strategy_call-f97316?style=for-the-badge&logo=googlecalendar&logoColor=white)](https://cal.com/studio1/collab)
[![X](https://img.shields.io/badge/%40Studio1HQ-141414?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Studio1HQ)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/studio1hq/)

<sub><a href="https://studio1hq.com">studio1hq.com</a> · Technical content, docs, video and DevRel for devtools</sub>

</div>
