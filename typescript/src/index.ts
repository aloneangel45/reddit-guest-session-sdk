export class RedditSessionClient {
  private rapidApiKey: string;
  private host: string;

  constructor(apiKey: string, host = "reddit-data-harvester-guest-session-api.p.rapidapi.com") {
    this.rapidApiKey = apiKey;
    this.host = host;
  }

  async getGuestSession() {
    const res = await fetch(`https://${this.host}/api/v1/reddit/guest-session`, {
      method: "POST",
      headers: {
        "x-rapidapi-host": this.host,
        "x-rapidapi-key": this.rapidApiKey,
        "Content-Type": "application/json"
      }
    });

    if (!res.ok) {
      throw new Error(`Reddit API error: ${res.status} ${res.statusText}`);
    }
    return await res.json();
  }
}
