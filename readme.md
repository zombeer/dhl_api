### Here we go...

#### Approaches tested
- Requests session. Failed at live code session.
- Headless browser. Somewhat succeeded at getting data, but I'm not satisfied with quality of this solution since it can't be put into production and be scaled reasonably.
- The final one: Turned out that DHL is having bunch of APIs for different purposes. Just googled "dhl api" (:

#### Root of all evil
 [AKAMAI antibot](https://www.akamai.com/) one of the toughest to bypass in fact. I was able to get data using puppeteer, even dockerized, but it's quite unstable solution. Very slow and expensive.
 [Here's some info](https://www.zenrows.com/blog/bypass-akamai#what-is-a-bot-detection-software) on bypassing AKAMAI protection. Which is quite tricky and involving deobfuscation of JS code and researching on dozens parameters this code collects. Interesting, but time consuming (: Not worth it when API is available.

#### Final product
