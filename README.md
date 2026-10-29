# 🤖 Reddit Public Data Harvester & Guest Session OAuth Bearer Token API SDK

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Active%20Listing-orange.svg?logo=rapidapi)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/reddit-data-harvester-guest-session-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Latency](https://img.shields.io/badge/Latency-Sub--40ms-brightgreen.svg)]()
[![Free Tier](https://img.shields.io/badge/Free%20Plan-50%20Calls%2Fmo-green.svg)]()

> **High-throughput Reddit Guest Session API. Dynamically acquires anonymous OAuth bearer tokens and device session state to harvest subreddit posts, comments, media, and user profiles without user credentials or strict rate-limiting penalties.**

---

## 🚀 Instant Free Access (50 Free Calls/Month)

Subscribe and get your live API key in 5 seconds:  
👉 **[Subscribe on RapidAPI Hub (Free Plan Available)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/reddit-data-harvester-guest-session-api)**

- **RapidAPI Host:** `reddit-data-harvester-guest-session-api.p.rapidapi.com`
- **Base Gateway:** `https://reddit-data-harvester-guest-session-api.p.rapidapi.com`

---

## ⚡ Why Use Reddit Guest Session API?

* **No Official Reddit Developer App Needed:** Ingest public Reddit discussions without API approval bureaucracy or costly enterprise tier fees.
* **Anonymous OAuth 2.0 Pool:** Fresh Bearer tokens issued on demand with authentic client credentials.
* **High Concurrency Throughput:** Scale your data pipeline across hundreds of concurrent threads without IP bans.
* **Full Subreddit & Post Coverage:** Harvest JSON payloads for posts, nested comment trees, and search results.

---

## 💻 Quickstart Examples

### 1. cURL (Instant Terminal Test)
```bash
curl --request POST \
  --url https://reddit-data-harvester-guest-session-api.p.rapidapi.com/api/v1/reddit/guest-session \
  --header 'x-rapidapi-host: reddit-data-harvester-guest-session-api.p.rapidapi.com' \
  --header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### 2. Python (`requests`)
```python
import requests

API_KEY = "YOUR_RAPIDAPI_KEY"

# Step 1: Acquire Guest Session OAuth Bearer Token
url = "https://reddit-data-harvester-guest-session-api.p.rapidapi.com/api/v1/reddit/guest-session"
headers = {
    "x-rapidapi-host": "reddit-data-harvester-guest-session-api.p.rapidapi.com",
    "x-rapidapi-key": API_KEY,
    "Content-Type": "application/json"
}

session = requests.post(url, headers=headers).json()
access_token = session.get("access_token")
print("Acquired Reddit Bearer Token:", access_token)

# Step 2: Fetch Subreddit Hot Posts
sub_url = "https://reddit-data-harvester-guest-session-api.p.rapidapi.com/api/v1/reddit/subreddit/technology/hot"
posts = requests.get(sub_url, headers=headers).json()
print("Top Post:", posts.get("data", {}).get("children", [{}])[0])
```

### 3. Node.js / TypeScript (`axios`)
```typescript
import axios from "axios";

async function harvestSubreddit(subreddit: string) {
  const headers = {
    "x-rapidapi-host": "reddit-data-harvester-guest-session-api.p.rapidapi.com",
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY"
  };

  const res = await axios.get(
    `https://reddit-data-harvester-guest-session-api.p.rapidapi.com/api/v1/reddit/subreddit/${subreddit}/hot`,
    { headers }
  );
  console.log("Subreddit Data:", res.data);
}

harvestSubreddit("technology");
```

---

## 🎯 Endpoints Available

1. `POST /api/v1/reddit/guest-session` — Generate valid guest OAuth 2.0 bearer token and session cookies.
2. `GET /api/v1/reddit/subreddit/{name}/hot` — Scrape trending hot threads with author info and vote ratios.
3. `GET /api/v1/reddit/comments/{article_id}` — Retrieve entire recursive comment hierarchy.

---

## 🔍 SEO & Use Cases
- **Sentiment & Brand Reputation:** Live monitoring of product mentions on niche subreddits.
- **AI & NLP Training Pipelines:** Ingest conversational datasets at scale without rate limits.
- **Market Intelligence:** Detect emerging trends and customer pain points in real-time.

---

## 📄 License
MIT © [Aether Protocol Labs](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default)
